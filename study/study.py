import tkinter as tk
from tkinter import messagebox, ttk
import spacy
import random

# Load the spaCy English language model
nlp = spacy.load("en_core_web_sm")

class StudyApp:
    def __init__(self, master):
        self.master = master
        master.title("Study App")
        master.geometry("600x400")  # Set the initial size of the window

        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0", font=("Arial", 12))
        self.style.configure("TButton", background="#007bff", foreground="#ffffff", font=("Arial", 12))

        self.frame = ttk.Frame(master)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.text_label = ttk.Label(self.frame, text="Enter the text information:")
        self.text_label.pack(pady=(20, 10))

        self.text_entry = tk.Text(self.frame, height=8, width=50, font=("Arial", 12))
        self.text_entry.pack()

        self.analyze_button = ttk.Button(self.frame, text="Analyze Text", command=self.analyze_text)
        self.analyze_button.pack(pady=10)

        self.quit_button = ttk.Button(self.frame, text="Quit", command=master.quit)
        self.quit_button.pack()

    def analyze_text(self):
        text = self.text_entry.get("1.0", tk.END)
        sentences, lemmatized_words = self.analyze_text_core(text)

        # Question Generation
        questions = self.generate_questions(sentences)

        # Answer Extraction
        answers = self.extract_answers(lemmatized_words)

        # Quiz Interaction
        self.quiz_interaction(questions, answers)

    def analyze_text_core(self, text):
        # Tokenization and sentence splitting
        doc = nlp(text)
        sentences = [sent.text for sent in doc.sents]

        # Lemmatization
        lemmatized_words = [token.lemma_ for token in doc]

        return sentences, lemmatized_words

    def generate_questions(self, sentences):
        # Identify key sentences
        key_sentences = random.sample(sentences, min(len(sentences), 5))

        # Formulate questions
        questions = [sentence + "?" for sentence in key_sentences]

        return questions

    def extract_answers(self, lemmatized_words):
        # For simplicity, we'll just extract nouns as answers for demonstration
        nouns = [token.text for token in nlp(" ".join(lemmatized_words)) if token.pos_ == "NOUN"]
        answers = random.sample(nouns, min(len(nouns), 5))
        return answers

    def quiz_interaction(self, questions, answers):
        messagebox.showinfo("Quiz", "Let's start the quiz!")
        score = 0
        total_questions = len(questions)

        for i, question in enumerate(questions):
            user_answer = messagebox.askquestion(f"Question {i+1}", question)

            # Compare user's answer to correct answer
            correct_answer = answers[i]
            if user_answer.lower() == "yes":
                messagebox.showinfo("Result", "Correct!")
                score += 1
            else:
                messagebox.showinfo("Result", f"Sorry, the correct answer is: {correct_answer}")

        messagebox.showinfo("Quiz Complete", f"You scored {score}/{total_questions}")

def main():
    root = tk.Tk()
    app = StudyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()