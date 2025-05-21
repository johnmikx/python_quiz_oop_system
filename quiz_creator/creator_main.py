from quiz_entry import QuizEntry
from quiz_writer import QuizWriter

def main():
    print("=" * 50)
    print("        Welcome to the Quiz Creator System        ")
    print("=" * 50)

    entry = QuizEntry()
    writer = QuizWriter()

    while True:
        quiz_data = entry.collect_quiz_data()
        formatted = entry.format_quiz_data(quiz_data)
        writer.write_to_file(formatted)
        print("\nQuiz question saved successfully!")

        another = ("\nDo you want to add another question (yes/no): ").strip().lower()
        if another != "yes":
            break
    
    print("\n" + "=" * 55)
    print("All quiz questions have been saved to `quiz_output.txt`")
    print("=" * 55)

if __name__ == "__main__":
    main()