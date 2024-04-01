import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random

# spaCy English language model
nlp = spacy.load("en_core_web_sm")

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
            user_text = file.read()s
        return user_text
    else:
        print("Invalid choice. Please try again.")
        return get_user_text()

# Text Analysis
def analyze_text(text):
    # Tokenization and sentence splitting
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]

    # Lemmatization
    lemmatized_words = [token.lemma_ for token in doc]

    return sentences, lemmatized_words

# Question Generation
def generate_questions(sentences):
    # Identify key sentences
    key_sentences = random.sample(sentences, min(len(sentences), 5))

    # Formulate questions
    questions = [sentence + "?" for sentence in key_sentences]

    # Randomizing question order
    random.shuffle(questions)

    return questions

# Answer Extraction
def extract_answers(lemmatized_words):
    # For simplicity, we'll just extract nouns as answers for demonstration
    nouns = [token.text for token in nlp(" ".join(lemmatized_words)) if token.pos_ == "NOUN"]
    answers = random.sample(nouns, min(len(nouns), 5))
    return answers

# Quiz Interaction
def quiz_interaction(questions, answers):
    print("Let's start the quiz!")
    score = 0
    total_questions = len(questions)

    for i, question in enumerate(questions):
        print(f"\nQuestion {i+1}: {question}")
        user_answer = input("Your Answer: ").strip().lower()
        
        # Compare user's answer to correct answer
        correct_answer = answers[i]
        if user_answer == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is: {correct_answer}")

    print(f"\nQuiz Complete! You scored {score}/{total_questions}")

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