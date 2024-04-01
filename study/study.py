import tkinter as tk
from tkinter import ttk
import spacy
import random

# Load the spaCy English language model
nlp = spacy.load("en_core_web_sm")

class StudyApp:
    def __init__(self, master):
        self.master = master
        master.title("Study App")
        master.geometry("600x400")

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

        self.quit_button = ttk.Button(self.frame, text="Quit", command=self.quit_app)
        self.quit_button.pack(side=tk.BOTTOM)

        self.progress_label = ttk.Label(self.frame, text="Progress:")
        self.progress_label.pack(side=tk.LEFT, padx=20)

        self.progress_bar = ttk.Progressbar(self.frame, orient=tk.HORIZONTAL, length=200, mode='determinate')
        self.progress_bar.pack(side=tk.LEFT)

        self.questions = []
        self.answer_vars = []

    def analyze_text(self):
        text = self.text_entry.get("1.0", tk.END)
        sentences, lemmatized_words = self.analyze_text_core(text)

        # Question Generation
        self.generate_questions(sentences)

        # Display questions
        self.display_questions()

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

        # Formulate questions and options
        self.questions = []
        self.answer_vars = []
        for sentence in key_sentences:
            self.questions.append(sentence)
            doc = nlp(sentence)
            nouns = [token.text for token in doc if token.pos_ == "NOUN"]
            options = random.sample(nouns, min(len(nouns), 4))
            self.answer_vars.append(tk.StringVar(value=options[0]))
            question_frame = ttk.Frame(self.frame)
            question_frame.pack(pady=(10, 0), padx=20, fill=tk.X)
            question_label = ttk.Label(question_frame, text=f"{sentence}?")
            question_label.pack(side=tk.LEFT)
            for option in options:
                option_checkbox = ttk.Checkbutton(question_frame, text=option, variable=self.answer_vars[-1], onvalue=option)
                option_checkbox.pack(side=tk.LEFT)

    def display_questions(self):
        self.analyze_button.configure(state="disabled")
        self.quit_button.configure(state="disabled")

        # Submit button
        submit_button = ttk.Button(self.frame, text="Submit", command=self.submit_answers)
        submit_button.pack(pady=10)

    def submit_answers(self):
        # Quiz Interaction
        score = 0
        total_questions = len(self.questions)

        for i, question in enumerate(self.questions):
            correct_answer = question.split("?")[0].strip()
            user_answer = self.answer_vars[i].get()
            if user_answer == correct_answer:
                score += 1

            # Update progress bar
            progress_value = int(((i + 1) / total_questions) * 100)
            self.progress_bar["value"] = progress_value
            self.progress_bar.update()

        print(f"\nQuiz Complete! You scored {score}/{total_questions}")
        self.analyze_button.configure(state="normal")
        self.quit_button.configure(state="normal")

    def quit_app(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = StudyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()