"""
TODO: Replace with PySimpleGUI
"""

import os
import sys
import time

# ANSI colour helpers
_USE_COLOUR = sys.stdout.isatty()  # disable in pipes / redirected output


def _c(code: str, text: str) -> str:
    return f"\033[{code}m{text}\033[0m" if _USE_COLOUR else text


def green(t):
    return _c("92", t)


def red(t):
    return _c("91", t)


def yellow(t):
    return _c("93", t)


def cyan(t):
    return _c("96", t)


def bold(t):
    return _c("1", t)


def dim(t):
    return _c("2", t)


def magenta(t):
    return _c("95", t)


# Layout helpers

WIDTH = 68


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def rule(char="─"):
    print(dim(char * WIDTH))


def header(title: str):
    rule("═")
    pad = (WIDTH - len(title)) // 2
    print(bold(" " * pad + title))
    rule("═")


def section(title: str):
    print()
    rule()
    print(bold(f"  {title}"))
    rule()


def pause(msg: str = "  Press [Enter] to continue…"):
    input(dim(msg))


# Stimulus display
def show_memory_stimulus(items: list[str], seconds: int = 5):
    clear()
    section("MEMORY")
    print()
    print(f"  Memorise the following items. You will be asked about them later.\n")
    for i, item in enumerate(items, 1):
        print(f"    {bold(str(i) + '.')}  {yellow(item)}")
    print()
    for remaining in range(seconds, 0, -1):
        sys.stdout.write(f"\r  {dim(f'Items hidden in {remaining}s…  ')}")
        sys.stdout.flush()
        time.sleep(1)
    time.sleep(0.8)


# Category banner

CATEGORY_LABELS = {
    "language": "LANGUAGE",
    "reasoning": "REASONING",
    "memory": "MEMORY RECALL",
}


def show_category_banner(category: str):
    clear()
    label = CATEGORY_LABELS.get(category, category.upper())
    header(f"  {label}  ")
    print()


# Question presenter

OPTION_LETTERS = ["A", "B", "C", "D"]


def ask_question(
    q_number: int,
    total: int,
    difficulty: str,
    question_text: str,
    choices: list[str],
) -> str:
    """
    Display a single multiple-choice question and return the validated
    letter choice (uppercase A–D).
    Pure I/O — no scoring logic.
    """
    diff_colour = {"easy": green, "medium": yellow, "hard": red}[difficulty]
    print(
        f"  Question {bold(str(q_number))}/{total}   "
        f"Difficulty: {diff_colour(difficulty.capitalize())}"
    )
    print()
    print(f"  {bold(question_text)}")
    print()

    for letter, choice in zip(OPTION_LETTERS, choices):
        print(f"    {bold(letter)})  {choice}")
    print()

    while True:
        raw = input("  Your answer (A/B/C/D): ").strip().upper()
        if raw in OPTION_LETTERS[: len(choices)]:
            return raw
        print(red("  ✗  Please enter A, B, C, or D."))


def show_answer_feedback(is_correct: bool, correct_answer: str, points: int):
    if is_correct:
        print(
            f"\n  {green('✓  Correct!')}  +{points} point{'s' if points != 1 else ''}"
        )
    else:
        print(
            f"\n  {red('✗  Incorrect.')}  The correct answer was: {bold(correct_answer)}"
        )
    time.sleep(0.8)
    print()


# Category summary
def show_category_summary(category: str, score: int, max_score: int, results):
    section(f"{CATEGORY_LABELS.get(category, category.upper())} — Summary")
    correct = sum(1 for r in results if r.is_correct)
    print(f"  Correct answers : {bold(str(correct))}/{len(results)}")
    print(f"  Points earned   : {bold(str(score))}/{max_score}")
    pct = round((score / max_score) * 100) if max_score else 0
    colour = green if pct >= 70 else (yellow if pct >= 40 else red)
    pct_string = f"{pct}%"
    print(f"  Category score  : {bold(colour(pct_string))}")
    print()
    pause()


# Final report
def show_final_report(report):
    clear()
    header("  FINAL RESULTS  ")
    print()

    rows = [
        ("Language", report.language_score, 30),
        ("Reasoning", report.reasoning_score, 30),
        ("Memory", report.memory_score, 10),
    ]

    for label, score, max_s in rows:
        pct = round((score / max_s) * 100)
        fill = int(pct / 100 * 30)
        bar = "█" * fill + "░" * (30 - fill)
        colour = green if pct >= 70 else (yellow if pct >= 40 else red)
        score_string = f"{score:2}/{max_s}"
        pct_string = f"{pct}%"
        print(f"  {bold(label):12}  {colour(score_string)} ({colour(pct_string)})")

    rule()
    pct_total = report.percentage
    fill = int(pct_total / 100 * 30)
    bar = "█" * fill + "░" * (30 - fill)
    colour = green if pct_total >= 70 else (yellow if pct_total >= 40 else red)
    print(
        f"  {bold('TOTAL'):12}  [{colour(bar)}]  "
        f"{report.total_score:2}/{report.max_score}  ({pct_total}%)"
    )
    rule()
    print()

    level_colour = {
        "Exceptional": green,
        "Advanced": cyan,
        "Proficient": yellow,
        "Developing": magenta,
        "Foundational": red,
    }.get(report.cognitive_level, bold)

    print(
        f"  Cognitive Ability Level:  "
        f"{bold(level_colour(report.cognitive_level.upper()))}"
    )
    print()
    print(f"  {report.feedback}")
    print()
    rule("═")

    view_detail = input("\n  View per-question breakdown? (y/n): ").strip().lower()
    if view_detail == "y":
        _show_detailed_breakdown(report)

    print()
    rule("═")
    print(bold("  Thank you for completing the Cognitive Ability Test."))
    rule("═")
    print()


def _show_detailed_breakdown(report):
    """Print a per-question table for every category."""
    for category, results in [
        ("Language", report.language_results),
        ("Reasoning", report.reasoning_results),
        ("Memory", report.memory_results),
    ]:
        section(f"{category} — Detailed Breakdown")
        for r in results:
            tick = green("✓") if r.is_correct else red("✗")
            print(
                f"  Q{r.q_number:2}  [{r.difficulty[0].upper()}]  {tick}  "
                f"{dim(r.question[:50])}"
            )
        print()
