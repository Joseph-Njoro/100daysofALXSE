import nltk
from nltk.tokenize import sent_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random

# Function to get user input (from file or manual typing)
def get_user_text():
    print("Do you want to enter text manually or provide a file path?")
    print("1. Manually")
    print("2. File Path")
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == '1':
        print("Please enter the text information:")
        user_text = input()
        return user_text
    elif choice == '2':
        file_path = input("Please enter the file path: ").strip()
        with open(file_path, 'r') as file:
            user_text = file.read()
        return user_text
    else:
        print("Invalid choice. Please try again.")
        return get_user_text()

# Remaining code stays the same...

# Main function
def main():
    # User Input
    text = get_user_text()

    # Text Analysis
    sentences, lemmatized_words = analyze_text(text)

    # Question Generation
    questions = generate_questions(sentences)

    # Answer Extraction
    answers = extract_answers(lemmatized_words)

    # Quiz Interaction
    quiz_interaction(questions, answers)

if __name__ == "__main__":
    main()