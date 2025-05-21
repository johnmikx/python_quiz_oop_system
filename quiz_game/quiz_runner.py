import random

class QuizRunner:
    def __init__(self, questions):
        self.questions = questions
        random.shuffle(self.questions)

    def run_quiz(self):
        print("\nWelcome to the Quiz Game! 🤗")
        print("Answer the following questions. Type a, b, c, or d.\n")

        for q in self.questions:
            print("\n" + "=" * 100)
            print(f"Question: {q['question']}")
            for key, value in q['options'].items():
                print(f"  {key}) {value}")
            print("=" * 100)

            user_answer = input("Your Answer: ").strip().lower()
            while user_answer not in ['a', 'b', 'c', 'd']:
                user_answer = input("Invalid. Please enter a, b, c, or d: ").strip().lower()

            if user_answer == q['answer']:
                print("✅ Correct!\n")
            else:
                correct_text = q['options'][q['answer']]
                print(f"❌ Incorrect! The correct answer is ({q['answer']}) {correct_text}\n")

        print("🎉 You've completed the quiz. Well done! :)")
