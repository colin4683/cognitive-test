"""
Decision Tree Engine & Scoring System
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal, Optional

from questions import MEMORY_STIMULUS, QUESTIONS

# Types
Category = Literal["language", "reasoning", "memory"]
Difficulty = Literal["easy", "medium", "hard"]
DIFFICULTY_ORDER: list[Difficulty] = ["easy", "medium", "hard"]
# Points awarded per difficulty level
POINTS: dict[Difficulty, int] = {"easy": 1, "medium": 2, "hard": 3}
TOTAL_QUESTIONS = 15  # per adaptive category


# Data Classes
@dataclass
class QuestionResult:
    """Record of a single answered question."""

    category: Category
    q_number: int
    difficulty: Difficulty
    question: str
    choices: list[str]
    correct: str
    user_answer: str
    is_correct: bool
    points_earned: int


@dataclass
class CategoryState:
    """Mutable state for one adaptive category session (Language or Reasoning)."""

    category: Category
    q_number: int = 1
    difficulty: Difficulty = "medium"
    score: int = 0
    results: list[QuestionResult] = field(default_factory=list)
    finished: bool = False

    def current_question(self) -> dict:
        return QUESTIONS[self.category][self.q_number][self.difficulty]

    def submit_answer(self, user_answer: str) -> QuestionResult:
        """
        Core decision-tree step:
          • evaluate correctness
          • adjust difficulty up/down
          • accumulate score
          • advance question counter
        Returns a QuestionResult for the frontend to display feedback.
        """
        q_data = self.current_question()
        is_correct = user_answer.strip().lower() == q_data["answer"].strip().lower()
        pts = POINTS[self.difficulty] if is_correct else 0

        result = QuestionResult(
            category=self.category,
            q_number=self.q_number,
            difficulty=self.difficulty,
            question=q_data["q"],
            choices=q_data["choices"],
            correct=q_data["answer"],
            user_answer=user_answer,
            is_correct=is_correct,
            points_earned=pts,
        )
        self.results.append(result)
        self.score += pts

        # Decision Tree: adjust difficulty based on correctness
        idx = DIFFICULTY_ORDER.index(
            self.difficulty
        )  # get the current difficulty index
        if is_correct:
            # move up one level if not already at Hard
            self.difficulty = DIFFICULTY_ORDER[min(idx + 1, 2)]
        else:
            # move down one level if not already at Easy
            self.difficulty = DIFFICULTY_ORDER[max(idx - 1, 0)]

        # Advance or finish
        if self.q_number >= TOTAL_QUESTIONS:
            self.finished = True
        else:
            self.q_number += 1

        return result


@dataclass
class MemoryState:
    """
    Memory category state.
    Phase 1 — stimulus shown
    Phase 2 — distraction
    Phase 3 — recall questions answered here.
    Score = number of correct recalls
    """

    stimulus: list[str] = field(default_factory=list)
    q_number: int = 1
    score: int = 0
    results: list[QuestionResult] = field(default_factory=list)
    finished: bool = False

    def __post_init__(self):
        pass

    def current_question(self) -> dict:
        return QUESTIONS["memory"][self.q_number]["medium"]  # memory qs don't adapt

    def submit_answer(self, user_answer: str) -> QuestionResult:
        q_data = self.current_question()
        is_correct = user_answer.strip().lower() == q_data["answer"].strip().lower()
        pts = 1 if is_correct else 0

        result = QuestionResult(
            category="memory",
            q_number=self.q_number,
            difficulty="medium",
            question=q_data["q"],
            choices=q_data["choices"],
            correct=q_data["answer"],
            user_answer=user_answer,
            is_correct=is_correct,
            points_earned=pts,
        )
        self.results.append(result)
        self.score += pts

        if self.q_number >= TOTAL_QUESTIONS:
            self.finished = True
        else:
            self.q_number += 1

        return result


# Maximum possible raw scores
MAX_ADAPTIVE_SCORE = sum(POINTS["hard"] for _ in range(TOTAL_QUESTIONS))  # 30
MAX_MEMORY_SCORE = TOTAL_QUESTIONS  # 10
MAX_TOTAL_SCORE = MAX_ADAPTIVE_SCORE * 2 + MAX_MEMORY_SCORE  # 70


@dataclass
class FinalReport:
    language_score: int
    reasoning_score: int
    memory_score: int
    total_score: int
    max_score: int
    percentage: float
    cognitive_level: str
    feedback: str
    language_results: list[QuestionResult]
    reasoning_results: list[QuestionResult]
    memory_results: list[QuestionResult]


def compute_cognitive_level(percentage: float) -> tuple[str, str]:
    """Map overall percentage to a cognitive ability label + feedback string."""
    if percentage >= 90:
        return (
            "Exceptional",
            "",
        )
    elif percentage >= 75:
        return (
            "Advanced",
            "",
        )
    elif percentage >= 60:
        return (
            "Proficient",
            "",
        )
    elif percentage >= 45:
        return (
            "Developing",
            "",
        )
    else:
        return (
            "Foundational",
            "",
        )


def build_final_report(
    lang: CategoryState,
    reason: CategoryState,
    mem: MemoryState,
) -> FinalReport:
    total = lang.score + reason.score + mem.score
    percentage = round((total / MAX_TOTAL_SCORE) * 100, 1)
    level, feedback = compute_cognitive_level(percentage)

    return FinalReport(
        language_score=lang.score,
        reasoning_score=reason.score,
        memory_score=mem.score,
        total_score=total,
        max_score=MAX_TOTAL_SCORE,
        percentage=percentage,
        cognitive_level=level,
        feedback=feedback,
        language_results=lang.results,
        reasoning_results=reason.results,
        memory_results=mem.results,
    )


def get_stimulus(difficulty: Difficulty = "medium") -> list[str]:
    """Return the memory stimulus list for a given difficulty tier."""
    return MEMORY_STIMULUS[difficulty]
