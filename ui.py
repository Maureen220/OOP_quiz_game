from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Labels
        self.score_label = Label(text="Score: 0", font=("Ariel", 10, "normal"), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1, pady=5, sticky="E")

        # Quote
        self.canvas = Canvas(width=400, height=300, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            200,
            150,
            text="",
            fill="black",
            font=("Arial", 20, "italic"),
            width=380
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        # Buttons
        self.right_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_img, highlightthickness=0, command=self.true_answer)
        self.right_button.grid(row=2, column=0)

        self.wrong_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_img, highlightthickness=0, command=self.false_answer)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've finished the game.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer(user_answer="True"))

    def false_answer(self):
        is_right = self.quiz.check_answer(user_answer="False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg='green')
        else:
            self.canvas.configure(bg='red')
        self.window.after(1000, self.get_next_question)



