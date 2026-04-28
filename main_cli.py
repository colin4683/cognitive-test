from cli import (
    ask_question,
    clear,
    pause,
    show_answer_feedback,
    show_category_banner,
    show_category_summary,
    show_final_report,
    show_memory_stimulus,
)
from engine import (
    MAX_ADAPTIVE_SCORE,
    MAX_MEMORY_SCORE,
    TOTAL_QUESTIONS,
    CategoryState,
    MemoryState,
    build_final_report,
    get_stimulus,
)

# Re-export so engine doesn't import cli
_LETTERS = ["A", "B", "C", "D"]


# Adaptive Category Runner (Language / Reasoning)
def run_adaptive_category(state: CategoryState) -> None:
    """
    Run a full 10-question adaptive session for Language or Reasoning.
    `distraction=True` labels the banner as a memory distraction phase.
    """
    show_category_banner(state.category)

    while not state.finished:
        q_data = state.current_question()

        # Map letter → actual choice text for the engine
        letter = ask_question(
            q_number=state.q_number,
            total=TOTAL_QUESTIONS,
            difficulty=state.difficulty,
            question_text=q_data["q"],
            choices=q_data["choices"],
        )

        # Convert A/B/C/D → the actual answer text
        idx = _LETTERS.index(letter)
        chosen_text = q_data["choices"][idx]

        result = state.submit_answer(chosen_text)
        show_answer_feedback(result.is_correct, result.correct, result.points_earned)

    show_category_summary(
        state.category,
        state.score,
        MAX_ADAPTIVE_SCORE,
        state.results,
    )


# Memory Recall Runner
def run_memory_recall(mem_state: MemoryState) -> None:
    """Run all 10 memory recall questions."""
    show_category_banner("memory")

    while not mem_state.finished:
        q_data = mem_state.current_question()

        letter = ask_question(
            q_number=mem_state.q_number,
            total=TOTAL_QUESTIONS,
            difficulty="medium",
            question_text=q_data["q"],
            choices=q_data["choices"],
        )

        idx = _LETTERS.index(letter)
        chosen_text = q_data["choices"][idx]

        result = mem_state.submit_answer(chosen_text)
        show_answer_feedback(result.is_correct, result.correct, result.points_earned)

    show_category_summary(
        "memory",
        mem_state.score,
        MAX_MEMORY_SCORE,
        mem_state.results,
    )


def main():
    # 1. Welcome
    clear()
    pause("  Press [Enter] to start the test…")

    # 2. Memory Stimulus (shown FIRST, before distraction)
    stimulus = get_stimulus("medium")
    mem_state = MemoryState(stimulus=stimulus)
    show_memory_stimulus(stimulus, seconds=6)

    # 3. Language (also serves as distraction phase for memory)
    lang_state = CategoryState(category="language")
    run_adaptive_category(lang_state)

    # 4. Reasoning (second distraction phase)
    reason_state = CategoryState(category="reasoning")
    run_adaptive_category(reason_state)

    # 5. Memory Recall
    run_memory_recall(mem_state)

    # 6. Final Report
    report = build_final_report(lang_state, reason_state, mem_state)
    show_final_report(report)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear()
        print("\n  Test interrupted. Goodbye!\n")
