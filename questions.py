"""
All question data for Language, Reasoning, and Memory categories.
"""

# Memory Stimulus
MEMORY_STIMULUS = {
    "easy": ["Apple", "Car", "Blue"],
    "medium": ["Dog", "Red", "Chair", "Book"],
    "hard": ["3", "7", "2", "9", "5"],
}

# Question Banks
# Structure: QUESTIONS[category][question_number][difficulty]
#   → {"q": str, "choices": [str, str, str, str], "answer": str}

QUESTIONS = {
    "language": {
        1: {
            "easy": {
                "q": "Which word is a noun?",
                "choices": ["run", "happy", "dog", "quickly"],
                "answer": "dog",
            },
            "medium": {
                "q": "Choose the correct sentence:",
                "choices": [
                    "She don't like apples",
                    "She doesn't like apples",
                    "She not like apples",
                    "She no like apples",
                ],
                "answer": "She doesn't like apples",
            },
            "hard": {
                "q": "Identify the grammatical error: 'Each of the players have a jersey.'",
                "choices": ["Each", "players", "have", "jersey"],
                "answer": "have",
            },
        },
        2: {
            "easy": {
                "q": "Synonym of 'big'?",
                "choices": ["small", "large", "tiny", "thin"],
                "answer": "large",
            },
            "medium": {
                "q": "Antonym of 'increase'?",
                "choices": ["grow", "expand", "decrease", "raise"],
                "answer": "decrease",
            },
            "hard": {
                "q": "Meaning of 'ambiguous'?",
                "choices": ["clear", "uncertain", "loud", "simple"],
                "answer": "uncertain",
            },
        },
        3: {
            "easy": {
                "q": "Which is a verb?",
                "choices": ["chair", "run", "blue", "tall"],
                "answer": "run",
            },
            "medium": {
                "q": "Identify the tense: 'She is running.'",
                "choices": ["past", "present continuous", "future", "past perfect"],
                "answer": "present continuous",
            },
            "hard": {
                "q": "Identify the voice: 'The ball was thrown by John.'",
                "choices": ["active", "passive", "future", "imperative"],
                "answer": "passive",
            },
        },
        4: {
            "easy": {
                "q": "Plural of 'child'?",
                "choices": ["childs", "children", "childes", "child"],
                "answer": "children",
            },
            "medium": {
                "q": "Choose the correct spelling:",
                "choices": ["recieve", "receive", "receeve", "receve"],
                "answer": "receive",
            },
            "hard": {
                "q": "Choose the correct sentence:",
                "choices": [
                    "Neither of them are ready",
                    "Neither of them is ready",
                    "Neither them is ready",
                    "Neither are them ready",
                ],
                "answer": "Neither of them is ready",
            },
        },
        5: {
            "easy": {
                "q": "Opposite of 'hot'?",
                "choices": ["cold", "warm", "heat", "burn"],
                "answer": "cold",
            },
            "medium": {
                "q": "Meaning of 'fragile'?",
                "choices": ["strong", "delicate", "heavy", "loud"],
                "answer": "delicate",
            },
            "hard": {
                "q": "Synonym of 'meticulous'?",
                "choices": ["careless", "precise", "messy", "fast"],
                "answer": "precise",
            },
        },
        6: {
            "easy": {
                "q": "Which is an adjective?",
                "choices": ["run", "happy", "jump", "quickly"],
                "answer": "happy",
            },
            "medium": {
                "q": "Identify the adverb: 'She runs quickly.'",
                "choices": ["She", "runs", "quickly", "none"],
                "answer": "quickly",
            },
            "hard": {
                "q": "Identify clause type: 'Because it was raining...'",
                "choices": ["independent", "dependent", "noun", "verb"],
                "answer": "dependent",
            },
        },
        7: {
            "easy": {
                "q": "Which is correct?",
                "choices": [
                    "He go to school",
                    "He goes to school",
                    "He going school",
                    "He gone school",
                ],
                "answer": "He goes to school",
            },
            "medium": {
                "q": "Identify the subject: 'The dog barked loudly.'",
                "choices": ["dog", "barked", "loudly", "The"],
                "answer": "dog",
            },
            "hard": {
                "q": "Identify the predicate:",
                "choices": ["The dog", "dog", "barked loudly", "loudly"],
                "answer": "barked loudly",
            },
        },
        8: {
            "easy": {
                "q": "Fill in: She ___ happy.",
                "choices": ["is", "are", "am", "be"],
                "answer": "is",
            },
            "medium": {
                "q": "Choose correct tense: 'They ___ dinner yesterday.'",
                "choices": ["eat", "ate", "eats", "eating"],
                "answer": "ate",
            },
            "hard": {
                "q": "Identify tense: 'She had finished before he arrived.'",
                "choices": ["past", "present", "past perfect", "future"],
                "answer": "past perfect",
            },
        },
        9: {
            "easy": {
                "q": "Which is spelled correctly?",
                "choices": ["becuase", "because", "becase", "becaus"],
                "answer": "because",
            },
            "medium": {
                "q": "Choose correct pronoun: 'This is ___ book.'",
                "choices": ["me", "my", "I", "mine"],
                "answer": "my",
            },
            "hard": {
                "q": "Identify the error: 'Me and him went to the store.'",
                "choices": ["Me", "him", "went", "store"],
                "answer": "Me",
            },
        },
        10: {
            "easy": {
                "q": "Which is a complete sentence?",
                "choices": ["running fast", "The dog runs", "fast running", "dog the"],
                "answer": "The dog runs",
            },
            "medium": {
                "q": "Identify the conjunction:",
                "choices": ["I", "stayed", "because", "rained"],
                "answer": "because",
            },
            "hard": {
                "q": "Identify sentence type: 'Close the door.'",
                "choices": [
                    "declarative",
                    "interrogative",
                    "imperative",
                    "exclamatory",
                ],
                "answer": "imperative",
            },
        },
        11: {
            "easy": {
                "q": "Which word is a pronoun?",
                "choices": ["run", "she", "blue", "jump"],
                "answer": "she",
            },
            "medium": {
                "q": "Choose the correct spelling:",
                "choices": ["definately", "definitly", "definitely", "definatly"],
                "answer": "definitely",
            },
            "hard": {
                "q": "Identify the figure of speech: 'The wind whispered through the trees.'",
                "choices": ["simile", "metaphor", "personification", "alliteration"],
                "answer": "personification",
            },
        },
        12: {
            "easy": {
                "q": "Which word is a preposition?",
                "choices": ["run", "on", "big", "fast"],
                "answer": "on",
            },
            "medium": {
                "q": "Choose the correct article: '___ umbrella was found.'",
                "choices": ["A", "An", "The", "No article"],
                "answer": "An",
            },
            "hard": {
                "q": "What type of clause is this? 'Whoever arrives first should open the door.'",
                "choices": [
                    "adjective clause",
                    "adverb clause",
                    "noun clause",
                    "independent clause",
                ],
                "answer": "noun clause",
            },
        },
        13: {
            "easy": {
                "q": "Opposite of 'dark'?",
                "choices": ["bright", "dim", "black", "night"],
                "answer": "bright",
            },
            "medium": {
                "q": "Which sentence uses the subjunctive correctly?",
                "choices": [
                    "I wish I was taller",
                    "I wish I were taller",
                    "I wish I am taller",
                    "I wish I be taller",
                ],
                "answer": "I wish I were taller",
            },
            "hard": {
                "q": "Identify the rhetorical device: 'Peter Piper picked a peck of pickled peppers.'",
                "choices": ["assonance", "alliteration", "onomatopoeia", "hyperbole"],
                "answer": "alliteration",
            },
        },
        14: {
            "easy": {
                "q": "What is the past tense of 'go'?",
                "choices": ["goed", "goes", "went", "gone"],
                "answer": "went",
            },
            "medium": {
                "q": "Which word is an adverb?",
                "choices": ["quick", "quickly", "quickness", "quicker"],
                "answer": "quickly",
            },
            "hard": {
                "q": "What mood is this verb? 'If I were the president, I would change the law.'",
                "choices": ["indicative", "imperative", "conditional", "subjunctive"],
                "answer": "subjunctive",
            },
        },
        15: {
            "easy": {
                "q": "Which sentence is a question?",
                "choices": [
                    "She is happy.",
                    "Are you ready?",
                    "Come here.",
                    "How nice!",
                ],
                "answer": "Are you ready?",
            },
            "medium": {
                "q": "Meaning of 'benevolent'?",
                "choices": ["cruel", "kind", "lazy", "jealous"],
                "answer": "kind",
            },
            "hard": {
                "q": "Identify the error: 'Between you and I, this is wrong.'",
                "choices": ["Between", "you", "I", "wrong"],
                "answer": "I",
            },
        },
    },
    "reasoning": {
        1: {
            "easy": {"q": "2 + 2 = ?", "choices": ["3", "4", "5", "6"], "answer": "4"},
            "medium": {
                "q": "5 × 3 = ?",
                "choices": ["10", "15", "20", "25"],
                "answer": "15",
            },
            "hard": {
                "q": "12 ÷ 4 + 3 = ?",
                "choices": ["5", "6", "7", "8"],
                "answer": "6",
            },
        },
        2: {
            "easy": {
                "q": "Next: 1, 2, 3, ?",
                "choices": ["4", "5", "6", "7"],
                "answer": "4",
            },
            "medium": {
                "q": "2, 4, 6, ?",
                "choices": ["7", "8", "9", "10"],
                "answer": "8",
            },
            "hard": {
                "q": "3, 6, 12, ?",
                "choices": ["18", "20", "24", "30"],
                "answer": "24",
            },
        },
        3: {
            "easy": {
                "q": "Odd one out:",
                "choices": ["Apple", "Banana", "Car", "Orange"],
                "answer": "Car",
            },
            "medium": {
                "q": "Odd one out:",
                "choices": ["Dog", "Cat", "Tiger", "Table"],
                "answer": "Table",
            },
            "hard": {
                "q": "Odd one out:",
                "choices": ["Circle", "Square", "Triangle", "Blue"],
                "answer": "Blue",
            },
        },
        4: {
            "easy": {
                "q": "If A=1, B=2, C=3, then D=?",
                "choices": ["2", "3", "4", "5"],
                "answer": "4",
            },
            "medium": {
                "q": "If A=1, then Z=?",
                "choices": ["24", "25", "26", "27"],
                "answer": "26",
            },
            "hard": {
                "q": "If B=2, then E=?",
                "choices": ["3", "4", "5", "6"],
                "answer": "5",
            },
        },
        5: {
            "easy": {
                "q": "Which is larger?",
                "choices": ["5", "3", "equal", "none"],
                "answer": "5",
            },
            "medium": {
                "q": "Which is larger?",
                "choices": ["12", "21", "equal", "none"],
                "answer": "21",
            },
            "hard": {
                "q": "Which is larger?",
                "choices": ["3²", "2³", "equal", "none"],
                "answer": "3²",
            },
        },
        6: {
            "easy": {
                "q": "Mirror of 6?",
                "choices": ["6", "9", "0", "8"],
                "answer": "9",
            },
            "medium": {
                "q": "Rotate 'b' 180°",
                "choices": ["b", "d", "p", "q"],
                "answer": "q",
            },
            "hard": {
                "q": "Which shape has 6 faces?",
                "choices": ["cube", "sphere", "cone", "cylinder"],
                "answer": "cube",
            },
        },
        7: {
            "easy": {
                "q": "All cats are animals. True or False?",
                "choices": ["True", "False", "Sometimes", "Unknown"],
                "answer": "True",
            },
            "medium": {
                "q": "Some dogs are pets.",
                "choices": ["True", "False", "Always false", "Unknown"],
                "answer": "True",
            },
            "hard": {
                "q": "All A are B. All B are C. Therefore A are C?",
                "choices": ["True", "False", "Sometimes", "Unknown"],
                "answer": "True",
            },
        },
        8: {
            "easy": {
                "q": "Pattern: ● ○ ● ○ ?",
                "choices": ["●", "○", "both", "none"],
                "answer": "●",
            },
            "medium": {
                "q": "Pattern: ▲ ■ ▲ ■ ?",
                "choices": ["▲", "■", "both", "none"],
                "answer": "▲",
            },
            "hard": {
                "q": "Pattern: 1, 4, 9, 16, ?",
                "choices": ["20", "25", "30", "36"],
                "answer": "25",
            },
        },
        9: {
            "easy": {"q": "10 − 3 = ?", "choices": ["6", "7", "8", "9"], "answer": "7"},
            "medium": {
                "q": "15 − 7 = ?",
                "choices": ["6", "7", "8", "9"],
                "answer": "8",
            },
            "hard": {
                "q": "100 − (25 × 2) = ?",
                "choices": ["25", "50", "75", "100"],
                "answer": "50",
            },
        },
        10: {
            "easy": {
                "q": "Which comes first alphabetically?",
                "choices": ["Apple", "Ball", "Same", "None"],
                "answer": "Apple",
            },
            "medium": {
                "q": "Which comes first?",
                "choices": ["Car", "Cat", "Same", "None"],
                "answer": "Car",
            },
            "hard": {
                "q": "Which comes first?",
                "choices": ["Alphabet", "Alphanumeric", "Same", "None"],
                "answer": "Alphabet",
            },
        },
        11: {
            "easy": {
                "q": "How many sides does a triangle have?",
                "choices": ["2", "3", "4", "5"],
                "answer": "3",
            },
            "medium": {
                "q": "If a train travels 60 km/h for 2 hours, how far does it go?",
                "choices": ["60 km", "90 km", "120 km", "150 km"],
                "answer": "120 km",
            },
            "hard": {
                "q": "What is 15% of 200?",
                "choices": ["20", "25", "30", "35"],
                "answer": "30",
            },
        },
        12: {
            "easy": {
                "q": "Odd one out:",
                "choices": ["Rose", "Tulip", "Oak", "Daisy"],
                "answer": "Oak",
            },
            "medium": {
                "q": "Next in sequence: 2, 5, 10, 17, ?",
                "choices": ["24", "25", "26", "27"],
                "answer": "26",
            },
            "hard": {
                "q": "If all Bloops are Razzles and all Razzles are Lazzles, are all Bloops Lazzles?",
                "choices": ["Yes", "No", "Sometimes", "Cannot determine"],
                "answer": "Yes",
            },
        },
        13: {
            "easy": {
                "q": "What is 50% of 80?",
                "choices": ["20", "30", "40", "50"],
                "answer": "40",
            },
            "medium": {
                "q": "A rectangle has length 8 and width 5. What is its area?",
                "choices": ["35", "40", "45", "30"],
                "answer": "40",
            },
            "hard": {
                "q": "If x + y = 10 and x - y = 4, what is x?",
                "choices": ["5", "6", "7", "8"],
                "answer": "7",
            },
        },
        14: {
            "easy": {
                "q": "Which shape has no corners?",
                "choices": ["square", "triangle", "circle", "rectangle"],
                "answer": "circle",
            },
            "medium": {
                "q": "Pattern: 100, 90, 81, 73, ?",
                "choices": ["65", "66", "67", "68"],
                "answer": "66",
            },
            "hard": {
                "q": "How many prime numbers are between 10 and 30?",
                "choices": ["3", "4", "5", "6"],
                "answer": "4",
            },
        },
        15: {
            "easy": {
                "q": "What is 7 x 8?",
                "choices": ["54", "56", "58", "60"],
                "answer": "56",
            },
            "medium": {
                "q": "Which is NOT a multiple of 6?",
                "choices": ["18", "24", "32", "36"],
                "answer": "32",
            },
            "hard": {
                "q": "A car depreciates 20% per year. Value after 2 years if it started at $10,000?",
                "choices": ["$6,000", "$6,400", "$7,200", "$8,000"],
                "answer": "$6,400",
            },
        },
    },
    "memory": {
        1: {
            "easy": {
                "q": "Which item was shown earlier?",
                "choices": ["Apple", "Tree", "House", "Dog"],
                "answer": "Apple",
            },
            "medium": {
                "q": "Which item was shown earlier?",
                "choices": ["Dog", "Lamp", "Phone", "Table"],
                "answer": "Dog",
            },
            "hard": {
                "q": "What was the third number shown earlier?",
                "choices": ["2", "7", "9", "5"],
                "answer": "2",
            },
        },
        2: {
            "easy": {
                "q": "Which item was shown earlier?",
                "choices": ["Car", "Plane", "Boat", "Bike"],
                "answer": "Car",
            },
            "medium": {
                "q": "Which item was NOT shown earlier?",
                "choices": ["Dog", "Chair", "Book", "Bottle"],
                "answer": "Bottle",
            },
            "hard": {
                "q": "What was the last number shown earlier?",
                "choices": ["5", "9", "2", "7"],
                "answer": "5",
            },
        },
        3: {
            "easy": {
                "q": "Which color was shown?",
                "choices": ["Blue", "Green", "Yellow", "Purple"],
                "answer": "Blue",
            },
            "medium": {
                "q": "Which item came second?",
                "choices": ["Dog", "Red", "Chair", "Book"],
                "answer": "Red",
            },
            "hard": {
                "q": "Which number came before 9?",
                "choices": ["2", "7", "3", "5"],
                "answer": "2",
            },
        },
        4: {
            "easy": {
                "q": "Which item was shown earlier?",
                "choices": ["Apple", "Pen", "Cup", "Desk"],
                "answer": "Apple",
            },
            "medium": {
                "q": "Which item came last?",
                "choices": ["Dog", "Red", "Chair", "Book"],
                "answer": "Book",
            },
            "hard": {
                "q": "Which number was first?",
                "choices": ["3", "7", "2", "9"],
                "answer": "3",
            },
        },
        5: {
            "easy": {
                "q": "Which item was shown earlier?",
                "choices": ["Car", "Train", "Plane", "Boat"],
                "answer": "Car",
            },
            "medium": {
                "q": "Which item came third?",
                "choices": ["Dog", "Red", "Chair", "Book"],
                "answer": "Chair",
            },
            "hard": {
                "q": "Which number came after 7?",
                "choices": ["2", "9", "5", "3"],
                "answer": "2",
            },
        },
        6: {
            "easy": {
                "q": "Which color was shown?",
                "choices": ["Blue", "Pink", "Black", "White"],
                "answer": "Blue",
            },
            "medium": {
                "q": "Which item was NOT shown?",
                "choices": ["Dog", "Chair", "Book", "Lamp"],
                "answer": "Lamp",
            },
            "hard": {
                "q": "Which number came before 5?",
                "choices": ["9", "2", "7", "3"],
                "answer": "9",
            },
        },
        7: {
            "easy": {
                "q": "Which item was shown earlier?",
                "choices": ["Apple", "Orange", "Banana", "Grape"],
                "answer": "Apple",
            },
            "medium": {
                "q": "Which item came first?",
                "choices": ["Dog", "Red", "Chair", "Book"],
                "answer": "Dog",
            },
            "hard": {
                "q": "Which number came after 2?",
                "choices": ["9", "5", "7", "3"],
                "answer": "9",
            },
        },
        8: {
            "easy": {
                "q": "Which item was shown earlier?",
                "choices": ["Car", "Bike", "Scooter", "Bus"],
                "answer": "Car",
            },
            "medium": {
                "q": "Which item came second?",
                "choices": ["Dog", "Red", "Chair", "Book"],
                "answer": "Red",
            },
            "hard": {
                "q": "Which number was last?",
                "choices": ["5", "2", "7", "9"],
                "answer": "5",
            },
        },
        9: {
            "easy": {
                "q": "Which color was shown?",
                "choices": ["Blue", "Green", "Orange", "Purple"],
                "answer": "Blue",
            },
            "medium": {
                "q": "Which item came before Book?",
                "choices": ["Dog", "Red", "Chair", "Book"],
                "answer": "Chair",
            },
            "hard": {
                "q": "Which number came before 9?",
                "choices": ["2", "7", "3", "5"],
                "answer": "2",
            },
        },
        10: {
            "easy": {
                "q": "Which item was shown earlier?",
                "choices": ["Apple", "Chair", "Desk", "Lamp"],
                "answer": "Apple",
            },
            "medium": {
                "q": "Which item was last?",
                "choices": ["Dog", "Red", "Chair", "Book"],
                "answer": "Book",
            },
            "hard": {
                "q": "Which number was second?",
                "choices": ["7", "3", "2", "9"],
                "answer": "7",
            },
        },
        11: {
            "easy": {
                "q": "Which item was shown earlier?",
                "choices": ["Apple", "Shoe", "Lamp", "Clock"],
                "answer": "Apple",
            },
            "medium": {
                "q": "Which item appeared in the list?",
                "choices": ["Dog", "Cat", "Bird", "Fish"],
                "answer": "Dog",
            },
            "hard": {
                "q": "What was the fourth number in the sequence?",
                "choices": ["9", "3", "5", "2"],
                "answer": "9",
            },
        },
        12: {
            "easy": {
                "q": "Which color was in the stimulus?",
                "choices": ["Blue", "Red", "Green", "Yellow"],
                "answer": "Blue",
            },
            "medium": {
                "q": "Which item was NOT in the list?",
                "choices": ["Red", "Dog", "Pencil", "Chair"],
                "answer": "Pencil",
            },
            "hard": {
                "q": "How many numbers were in the Hard stimulus set?",
                "choices": ["3", "4", "5", "6"],
                "answer": "5",
            },
        },
        13: {
            "easy": {
                "q": "Which item was shown?",
                "choices": ["Car", "Bus", "Bike", "Plane"],
                "answer": "Car",
            },
            "medium": {
                "q": "What came right after 'Dog' in the list?",
                "choices": ["Chair", "Book", "Red", "Dog"],
                "answer": "Red",
            },
            "hard": {
                "q": "What is the sum of all numbers in the Hard stimulus?",
                "choices": ["24", "26", "27", "28"],
                "answer": "26",
            },
        },
        14: {
            "easy": {
                "q": "Was 'Apple' in the stimulus?",
                "choices": ["Yes", "No", "Maybe", "Not sure"],
                "answer": "Yes",
            },
            "medium": {
                "q": "What was the first item shown?",
                "choices": ["Red", "Chair", "Dog", "Book"],
                "answer": "Dog",
            },
            "hard": {
                "q": "Which two numbers in the sequence are next to each other?",
                "choices": ["3 and 9", "7 and 2", "2 and 9", "9 and 5"],
                "answer": "7 and 2",
            },
        },
        15: {
            "easy": {
                "q": "Which item was shown earlier?",
                "choices": ["Apple", "Pen", "Cup", "Plate"],
                "answer": "Apple",
            },
            "medium": {
                "q": "How many items were in the Medium stimulus?",
                "choices": ["2", "3", "4", "5"],
                "answer": "4",
            },
            "hard": {
                "q": "Which number appeared in the sequence and is greater than 5?",
                "choices": ["3", "7", "2", "5"],
                "answer": "7",
            },
        },
    },
}
