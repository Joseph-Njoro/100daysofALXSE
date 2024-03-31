import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random

# User Input
def get_user_text():
    print("Please enter the text information:")
    user_text = input()
    return user_text

# Text Analysis
def analyze_text(text):
    # Tokenization
    sentences = sent_tokenize(text)

    # Part-of-Speech Tagging and Named Entity Recognition (optional)
    words = []
    for sentence in sentences:
        words.extend(nltk.word_tokenize(sentence))
    pos_tags = nltk.pos_tag(words)
    named_entities = nltk.chunk.ne_chunk(pos_tags)

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

    return sentences, lemmatized_words

# Question Generation
def generate_questions(sentences):
    # Identify key sentences
    key_sentences = random.sample(sentences, min(len(sentences), 5))

    # Formulate questions
    questions = []
    for sentence in key_sentences:
        questions.append(sentence + "?")

    return questions

# Answer Extraction
def extract_answers(lemmatized_words):
    # Factual questions: extract specific information
    # Concept-based questions: derive answers based on context
    # For simplicity, we'll just extract nouns as answers for demonstration
    nouns = [word for (word, pos) in nltk.pos_tag(lemmatized_words) if pos.startswith('N')]
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