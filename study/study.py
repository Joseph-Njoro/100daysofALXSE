import random

# Define flashcards (questions and answers)
flashcards = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
    "What is the chemical symbol for water?": "H2O",
    "What year did the Titanic sink?": "1912"
}

# Function to display flashcards and prompt user for answers
def study_flashcards():
    print("Welcome to the Flashcard Study App!")
    print("Enter your answer for each question. Type 'exit' to quit.")
    
    # Shuffle flashcards
    flashcard_items = list(flashcards.items())
    random.shuffle(flashcard_items)
    
    # Iterate through flashcards
    for question, answer in flashcard_items:
        user_answer = input(f"\nQuestion: {question}\nYour Answer: ").strip().lower()
        
        # Check user's answer
        if user_answer == 'exit':
            print("Exiting the Flashcard Study App. Goodbye!")
            return
        elif user_answer == flashcards[question].lower() or user_answer == flashcards[question].lower().replace("0", "o"):
            print("Correct!")
        else:
            print(f"Sorry, the correct answer is: {flashcards[question]}")
    
    print("You have completed all the flashcards!")

# Main function
def main():
    study_flashcards()

if __name__ == "__main__":
    main()