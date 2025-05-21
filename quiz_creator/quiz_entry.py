class QuizEntry:
    def collect_quiz_data(self):
        question = input("Enter the quiz question: ").strip()
        answer_a = input("Enter answer option (a): ").strip()
        answer_b = input("Enter answer option (b): ").strip()
        answer_c = input("Enter answer option (c): ").strip()
        answer_d = input("Enter answer option (d): ").strip()
        correct_answer = input("Enter the correct answer (a/b/c/d): ").strip().lower()

        return {
            "question": question,
            "a": answer_a,
            "b": answer_b,
            "c": answer_c,
            "d": answer_d,
            "correct": correct_answer
        }

    def format_quiz_data(self, quiz):
        return (
            f"Question: {quiz['question']}\n"
            f"a) {quiz['a']}\n"
            f"b) {quiz['b']}\n"
            f"c) {quiz['c']}\n"
            f"d) {quiz['d']}\n"
            f"Correct Answer: {quiz['correct']}\n"
            + "-" * 50 + "\n"
        )