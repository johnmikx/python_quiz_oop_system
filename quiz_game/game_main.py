from quiz_loader import QuizLoader
from quiz_runner import QuizRunner

def main():
    loader = QuizLoader()
    questions = loader.load_questions_from_file()

    game = QuizRunner(questions)
    game.run_quiz()

if __name__ == "__main__":
    main()