THEME_COLOR = "#ffd58c"
TEXT_COLOR="#FF5733"
from tkinter import *
from quiz_brain import QuizBrain
class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("KBC")
        self.window.config(padx=20,pady=40,bg=THEME_COLOR)

        self.label=Label(text="Score:0",fg="white",bg=THEME_COLOR)
        self.label.grid(row=0,column=1)

        self.canvas=Canvas(width=500,height=250, bg="white")
        self.question_text=self.canvas.create_text(250,125,text="some Question text",fill=TEXT_COLOR,font=("Arial",20,"italic"),width=400)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        tru_img=PhotoImage(file="images/true.png")
        self.tru_button=Button(image=tru_img,highlightthickness=0,command=self.true_pressed)
        self.tru_button.grid(row=2,column=0)
        f_img=PhotoImage(file="images/false.png")
        self.false_button=Button(image=f_img,highlightthickness=0,command=self.false_pressef)
        self.false_button.grid(row=2,column=1)
        self.get_question()

        self.window.mainloop()
    global score
    score=0

    def update_score(self):
        global score
        score+=1
        self.label.config(text="Score:{}".format(score))
    def get_question(self):
        self.canvas.config(bg="white")
        q_text=self.quiz.next_question()
        self.canvas.itemconfig(self.question_text,text=q_text)
    def true_pressed(self):
        self.check_ans(self.quiz.check_answer("true"))
    def false_pressef(self):
        self.check_ans(self.quiz.check_answer("false"))
    def check_ans(self, is_right):
        if is_right:
            self.update_score()
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_question)





