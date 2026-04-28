import time

import PySimpleGUI as sg

from engine import (
    MAX_ADAPTIVE_SCORE,
    MAX_MEMORY_SCORE,
    TOTAL_QUESTIONS,
    CategoryState,
    MemoryState,
    build_final_report,
    get_stimulus,
)
from questions import QUESTIONS

# Configuration
sg.theme("DarkGrey8")
FONT_MAIN = ("Helvetica", 12)
FONT_BOLD = ("Helvetica", 12, "bold")
FONT_HEADER = ("Helvetica", 16, "bold")


class CognitiveTestGUI:
    def __init__(self):
        self.window = None
        self.state = None  # Holds CategoryState or MemoryState
        self.mem_state = None
        self.lang_state = None
        self.reason_state = None

    def create_welcome_layout(self):
        return [
            [sg.VPush()],
            [
                sg.Text(
                    "Cognitive Ability Test",
                    font=FONT_HEADER,
                    justification="center",
                    expand_x=True,
                )
            ],
            [
                sg.Text(
                    "This test will assess Language, Reasoning, and Memory.",
                    justification="center",
                    expand_x=True,
                )
            ],
            [sg.Button("Start Test", size=(15, 2), pad=(0, 20), key="-START-")],
            [sg.VPush()],
        ]

    def create_stimulus_layout(self, items):
        layout = [[sg.Text("MEMORY STIMULUS", font=FONT_HEADER, text_color="#FFD700")]]
        layout.append(
            [
                sg.Text(
                    "Memorize the following items. You will be asked about them later.",
                    pad=(0, 10),
                )
            ]
        )
        for i, item in enumerate(items, 1):
            layout.append(
                [sg.Text(f"{i}. {item}", font=FONT_BOLD, text_color="#FFA500")]
            )
        layout.append(
            [
                sg.ProgressBar(
                    6, orientation="h", size=(20, 20), key="-PROG-", pad=(0, 20)
                )
            ]
        )
        layout.append([sg.Text("Items hidden in 6s...", key="-TIMER-")])
        return layout

    def create_question_layout(self):
        return [
            [
                sg.Text("", key="-CAT-", font=FONT_HEADER),
                sg.Push(),
                sg.Text("", key="-PROG-TEXT-"),
            ],
            [sg.Text("", key="-DIFF-", font=FONT_BOLD)],
            [sg.HSeparator()],
            [sg.Text("", key="-QUESTION-", font=FONT_BOLD, size=(50, 3), pad=(0, 10))],
            # Removed circle_color here to fix the "fake filled" look
            [sg.Radio("", "RADIO1", key="-OPT0-", font=FONT_MAIN)],
            [sg.Radio("", "RADIO1", key="-OPT1-", font=FONT_MAIN)],
            [sg.Radio("", "RADIO1", key="-OPT2-", font=FONT_MAIN)],
            [sg.Radio("", "RADIO1", key="-OPT3-", font=FONT_MAIN)],
            [sg.Text("", key="-FEEDBACK-", font=FONT_BOLD, pad=(0, 10))],
            [
                sg.Button("Submit", key="-SUBMIT-"),
                sg.Button("Next", key="-NEXT-", visible=False),
            ],
        ]

    def create_report_layout(self, report):
        return [
            [sg.Text("FINAL RESULTS", font=FONT_HEADER)],
            [
                sg.Text(f"Language: {report.language_score}/30"),
                sg.ProgressBar(100, orientation="h", size=(20, 20), key="-BAR-LANG-"),
            ],
            [
                sg.Text(f"Reasoning: {report.reasoning_score}/30"),
                sg.ProgressBar(100, orientation="h", size=(20, 20), key="-BAR-REASON-"),
            ],
            [
                sg.Text(f"Memory: {report.memory_score}/15"),
                sg.ProgressBar(100, orientation="h", size=(20, 20), key="-BAR-MEM-"),
            ],
            [sg.HSeparator()],
            [
                sg.Text(
                    f"TOTAL SCORE: {report.total_score}/{report.max_score} ({report.percentage}%)",
                    font=FONT_BOLD,
                )
            ],
            [
                sg.Text(
                    f"Level: {report.cognitive_level.upper()}",
                    font=FONT_HEADER,
                    text_color="#00FF00",
                )
            ],
            [sg.Button("Exit", key="-EXIT-")],
        ]

    def update_question_ui(self, q_data):
        self.window["-QUESTION-"].update(q_data["q"])
        self.window["-CAT-"].update(self.state.category.upper())
        self.window["-PROG-TEXT-"].update(f"Q: {self.state.q_number}/{TOTAL_QUESTIONS}")

        diff_colors = {"easy": "#00FF00", "medium": "#FFFF00", "hard": "#FF4500"}
        self.window["-DIFF-"].update(
            f"Difficulty: {self.state.difficulty.capitalize()}",
            text_color=diff_colors.get(self.state.difficulty, "white"),
        )

        for i in range(4):
            if i < len(q_data["choices"]):
                self.window[f"-OPT{i}-"].update(
                    text=q_data["choices"][i], visible=True, value=False
                )
            else:
                self.window[f"-OPT{i}-"].update(visible=False)

        self.window["-FEEDBACK-"].update("")
        self.window["-SUBMIT-"].update(visible=True)
        self.window["-NEXT-"].update(visible=False)

    def run(self):
        # Initial Window
        self.window = sg.Window(
            "Cognitive Ability Test",
            self.create_welcome_layout(),
            size=(600, 450),
            element_justification="c",
        )

        # Bind the Enter key to a special event string
        self.window.finalize()
        self.window.bind("<Return>", "_ENTER_")

        auto_next = False  # Track if we are in the 1-second "waiting" phase

        while True:
            # If auto_next is True, we wait 1000ms (1s), otherwise wait indefinitely
            timeout = 1000 if auto_next else None
            event, values = self.window.read(timeout=timeout)

            # --- HANDLE AUTO-NEXT TIMEOUT ---
            if event == sg.TIMEOUT_KEY and auto_next:
                event = "-NEXT-"  # Force the "Next" event to happen
                auto_next = False

            if event in (sg.WIN_CLOSED, "-EXIT-"):
                break

            # --- HANDLE ENTER KEY ---
            if event == "_ENTER_":
                if self.window["-SUBMIT-"].visible:
                    event = "-SUBMIT-"
                elif self.window["-NEXT-"].visible:
                    event = "-NEXT-"

            if event == "-START-":
                # 1. Prepare Memory Data
                stimulus = get_stimulus("medium")
                self.mem_state = MemoryState(stimulus=stimulus)

                # 2. Show Stimulus Window FIRST
                self.window.close()
                self.window = sg.Window(
                    "Memory Stimulus",
                    self.create_stimulus_layout(stimulus),
                    size=(600, 450),
                    finalize=True,
                )

                # Stimulus countdown loop
                for i in range(6, -1, -1):
                    self.window["-PROG-"].update(6 - i)
                    self.window["-TIMER-"].update(f"Items hidden in {i}s...")
                    self.window.refresh()
                    time.sleep(1)

                # 3. Setup All Test States
                self.lang_state = CategoryState(category="language")
                self.reason_state = CategoryState(category="reasoning")
                # Order: Language -> Reasoning -> Memory Recall
                self.states_to_run = [
                    self.lang_state,
                    self.reason_state,
                    self.mem_state,
                ]
                self.current_state_idx = 0
                self.state = self.states_to_run[self.current_state_idx]

                # 4. Show Question Window SECOND
                self.window.close()
                self.window = sg.Window(
                    "Cognitive Test",
                    self.create_question_layout(),
                    size=(600, 450),
                    finalize=True,
                )

                # 5. Bind keys and load the first question
                self.window.bind("<Return>", "_ENTER_")
                self.update_question_ui(self.state.current_question())

            if event == "-SUBMIT-":
                q_data = self.state.current_question()
                # Find which radio is selected
                selected_text = None
                for i in range(len(q_data["choices"])):
                    if values[f"-OPT{i}-"]:
                        selected_text = q_data["choices"][i]
                        break

                if selected_text is None:
                    sg.popup_error("Please select an answer!")
                    continue

                result = self.state.submit_answer(selected_text)

                if result.is_correct:
                    self.window["-FEEDBACK-"].update(
                        f"✓ Correct! (+{result.points_earned})", text_color="#00FF00"
                    )
                else:
                    self.window["-FEEDBACK-"].update(
                        f"✗ Incorrect. Correct: {result.correct}", text_color="#FF4500"
                    )

                auto_next = True
                self.window["-SUBMIT-"].update(visible=False)
                self.window["-NEXT-"].update(visible=True)

            if event == "-NEXT-":
                auto_next = False
                if not self.state.finished:
                    self.update_question_ui(self.state.current_question())
                else:
                    self.current_state_idx += 1
                    if self.current_state_idx < len(self.states_to_run):
                        self.state = self.states_to_run[self.current_state_idx]
                        self.update_question_ui(self.state.current_question())
                    else:
                        # --- PHASE 3: FINAL REPORT ---
                        report = build_final_report(
                            self.lang_state, self.reason_state, self.mem_state
                        )
                        self.window.close()

                        # Use finalize=True to allow immediate updates
                        self.window = sg.Window(
                            "Test Report",
                            self.create_report_layout(report),
                            size=(600, 500),
                            finalize=True,
                        )

                        # Manually update the bars now that the window is finalized
                        self.window["-BAR-LANG-"].update(
                            current_count=int((report.language_score / 30) * 100)
                        )
                        self.window["-BAR-REASON-"].update(
                            current_count=int((report.reasoning_score / 30) * 100)
                        )
                        self.window["-BAR-MEM-"].update(
                            current_count=int((report.memory_score / 15) * 100)
                        )

        self.window.close()


if __name__ == "__main__":
    test_gui = CognitiveTestGUI()
    test_gui.run()
