from questions import QUESTIONS, MEMORY_STIMULUS
from dataclasses import dataclass

# Constants used by the GUI
TOTAL_QUESTIONS = 15
MAX_ADAPTIVE_SCORE = 30 # (e.g., 2 points for hard)
MAX_MEMORY_SCORE = 15

@dataclass
class AnswerResult:
    is_correct: bool
    correct: str
    points_earned: int

class CategoryState:
    def __init__(self, category):
        self.category = category
        self.q_number = 1
        self.difficulty = "easy"
        self.score = 0
        self.finished = False
        self.correct_streak = 0

    def current_question(self):
        # Access: QUESTIONS['language'][1]['easy']
        return QUESTIONS[self.category][self.q_number][self.difficulty]

    def submit_answer(self, user_choice):
        q_data = self.current_question()
        is_correct = user_choice == q_data["answer"]
        
        points = {"easy": 1, "medium": 2, "hard": 3}.get(self.difficulty, 1)
        
        if is_correct:
            self.score += points
            self.correct_streak += 1
            # Adaptive logic: Level up difficulty after 2 correct answers
            if self.correct_streak >= 2:
                if self.difficulty == "easy": self.difficulty = "medium"
                elif self.difficulty == "medium": self.difficulty = "hard"
                self.correct_streak = 0
        else:
            self.correct_streak = 0
            # Optional: Level down if incorrect
            if self.difficulty == "hard": self.difficulty = "medium"
            elif self.difficulty == "medium": self.difficulty = "easy"

        if self.q_number >= TOTAL_QUESTIONS:
            self.finished = True
        else:
            self.q_number += 1
            
        return AnswerResult(is_correct, q_data["answer"], points if is_correct else 0)

class MemoryState(CategoryState):
    def __init__(self, stimulus):
        super().__init__("memory")
        self.stimulus_list = stimulus
        # Memory is usually scored 1pt per question, no adaptive jump logic needed usually
    
    def submit_answer(self, user_choice):
        # Simplest version: 1 point per memory question
        q_data = self.current_question()
        is_correct = user_choice == q_data["answer"]
        if is_correct: self.score += 1
        
        if self.q_number >= TOTAL_QUESTIONS:
            self.finished = True
        else:
            self.q_number += 1
        return AnswerResult(is_correct, q_data["answer"], 1 if is_correct else 0)

def get_stimulus(difficulty):
    return MEMORY_STIMULUS.get(difficulty, MEMORY_STIMULUS["easy"])

@dataclass
class Report:
    language_score: int
    reasoning_score: int
    memory_score: int
    total_score: int
    max_score: int
    percentage: float
    cognitive_level: str

def build_final_report(lang, reason, mem):
    total = lang.score + reason.score + mem.score
    max_s = 75 # (15 questions * max 3 pts for adaptive, plus 15 for memory)
    pct = round((total / max_s) * 100, 1)
    
    level = "Average"
    if pct > 85: level = "Superior"
    elif pct > 70: level = "High Average"
    elif pct < 50: level = "Impaired"
    
    return Report(lang.score, reason.score, mem.score, total, max_s, pct, level)