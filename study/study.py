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
        self.current_question_index = 0

    def analyze_text(self):
        text = self.text_entry.get("1.0", tk.END)
        sentences, lemmatized_words = self.analyze_text_core(text)

        # Question Generation
        self.generate_questions(sentences)

        # Display questions
        self.display_current_question()

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
            correct_answer = random.choice(nouns)
            options = random.sample(nouns, min(len(nouns), 4))
            options.remove(correct_answer)
            options.insert(random.randint(0, len(options)), correct_answer)
            self.answer_vars.append(tk.StringVar(value=correct_answer))
            question_frame = ttk.Frame(self.frame)
            question_frame.pack(pady=(10, 0), padx=20, fill=tk.X)
            question_label = ttk.Label(question_frame, text=f"{sentence}?", wraplength=400)
            question_label.pack(side=tk.TOP)
            for i, option in enumerate(options, start=65):
                option_checkbox = ttk.Radiobutton(question_frame, text=f"{chr(i)}. {option}", variable=self.answer_vars[-1], value=option)
                option_checkbox.pack(side=tk.TOP)

    def display_current_question(self):
        # Hide previous question
        if hasattr(self, 'current_question_frame'):
            self.current_question_frame.pack_forget()

        self.current_question_frame = ttk.Frame(self.frame)
        self.current_question_frame.pack(pady=20)

        question_text = self.questions[self.current_question_index]
        question_label = ttk.Label(self.current_question_frame, text=question_text)
        question_label.pack()

        options_frame = ttk.Frame(self.current_question_frame)
        options_frame.pack(pady=10)

        answer_options = ['A', 'B', 'C', 'D']
        for i, option in enumerate(answer_options):
            option_label = ttk.Label(options_frame, text=f"{option}. {self.answer_vars[self.current_question_index].get()}")
            option_label.grid(row=0, column=i, padx=10)

        if self.current_question_index > 0:
            prev_button = ttk.Button(self.current_question_frame, text="Previous", command=self.show_previous_question)
            prev_button.pack(side=tk.LEFT)

        if self.current_question_index < len(self.questions) - 1:
            next_button = ttk.Button(self.current_question_frame, text="Next", command=self.show_next_question)
            next_button.pack(side=tk.RIGHT)

    def show_previous_question(self):
        if self.current_question_index > 0:
            self.current_question_index -= 1
            self.display_current_question()

    def show_next_question(self):
        if self.current_question_index < len(self.questions) - 1:
            self.current_question_index += 1
            self.display_current_question()

    def quit_app(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    app = StudyApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()