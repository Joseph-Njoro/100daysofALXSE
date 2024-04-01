import tkinter as tk
from tkinter import messagebox
import study

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz App")
        self.geometry("400x300")
        
        self.text_label = tk.Label(self, text="Enter text or file path:")
        self.text_label.pack()
        
        self.text_entry = tk.Entry(self, width=50)
        self.text_entry.pack()
        
        self.submit_button = tk.Button(self, text="Start Quiz", command=self.start_quiz)
        self.submit_button.pack()
    
    def start_quiz(self):
        user_text = self.text_entry.get()
        if not user_text:
            messagebox.showerror("Error", "Please enter text or file path.")
            return
        
        sentences, lemmatized_words = study.analyze_text(user_text)
        questions = study.generate_questions(sentences)
        answers = study.extract_answers(lemmatized_words)
        
        self.destroy()
        QuizInterface(questions, answers)

class QuizInterface(tk.Toplevel):
    def __init__(self, questions, answers):
        super().__init__()
        self.title("Quiz")
        self.geometry("400x300")
        
        self.questions = questions
        self.answers = answers
        self.score = 0
        self.current_question_index = 0
        
        self.question_label = tk.Label(self, text=self.questions[self.current_question_index])
        self.question_label.pack()
        
        self.answer_entry = tk.Entry(self, width=50)
        self.answer_entry.pack()
        
        self.submit_button = tk.Button(self, text="Submit Answer", command=self.check_answer)
        self.submit_button.pack()
    
    def check_answer(self):
        user_answer = self.answer_entry.get().lower()
        correct_answer = self.answers[self.current_question_index].lower()
        
        if user_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showinfo("Incorrect", f"Sorry, the correct answer is: {correct_answer}")
        
        self.current_question_index += 1
        
        if self.current_question_index < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question_index])
            self.answer_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Quiz Complete", f"Quiz complete! You scored {self.score}/{len(self.questions)}")
            self.destroy()

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()