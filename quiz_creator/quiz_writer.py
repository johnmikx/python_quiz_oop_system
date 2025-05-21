class QuizWriter:
    def write_to_file(self, formatted_quiz, filename="quiz_output.txt"):
        with open(filename, "a", encoding="utf-8") as file:
            file.write(formatted_quiz)