class QuizLoader:
    def load_questions_from_file(self, filename="quiz_output.txt"):
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        blocks = content.strip().split("--------------------------------------------------")
        questions = []

        for block in blocks:
            lines = block.strip().splitlines()
            if len(lines) < 6:
                continue

            question_text = lines[0][len("Question: "):]
            options = {
                'a': lines[1][3:],
                'b': lines[2][3:],
                'c': lines[3][3:],
                'd': lines[4][3:]
            }
            correct = lines[5][len("Correct Answer: "):].strip().lower()

            questions.append({
                'question': question_text,
                'options': options,
                'answer': correct
            })

        return questions