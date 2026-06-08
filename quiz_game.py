import random

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which language is used for AI/ML?",
        "options": ["A. Java", "B. C++", "C. Python", "D. PHP"],
        "answer": "C"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Core Processing Unit"],
        "answer": "B"
    },
    {
        "question": "Which company made Python?",
        "options": ["A. Google", "B. Microsoft", "C. Apple", "D. Guido van Rossum"],
        "answer": "D"
    },
    {
        "question": "What is 2 * 8 in Python?",
        "options": ["A. 16", "B. 64", "C. 256", "D. 512"],
        "answer": "A"
    },
    {
        "question": "What does RAM stand for?",
        "options": ["A. Random Access Memory", "B. Read Access Memory", "C. Run Access Memory", "D. Random Active Memory"],
        "answer": "A"
    },
    {
        "question": "Which of these is a Python data type?",
        "options": ["A. int", "B. integer", "C. number", "D. digit"],
        "answer": "A"
    },
    {
        "question": "What symbol is used for comments in Python?",
        "options": ["A. //", "B. /*", "C. #", "D. --"],
        "answer": "C"
},
]

def run_quiz():
    score = 0
    random.shuffle(questions)   # shuffles question order every time

    print("Welcome to the Quiz!")
    print("----------------------")

    for i, q in enumerate(questions):
        print(f"\nQ{i+1}. {q['question']}")
        for option in q["options"]:
            print(option)

        answer = input("Your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("Correct! ✓")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}")

    print("\n----------------------")
    print(f"Your score: {score}/{len(questions)}")

    if score == len(questions):
        print("Perfect score! Excellent!")
    elif score >= 3:
        print("Good job! Keep learning.")
    else:
        print("Keep practicing. You'll get better!")

play_again = "yes"
while play_again == "yes":
    run_quiz()
    play_again = input("Do you want to play again? (yes/no): ").lower()

print("Thanks for playing!")