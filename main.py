from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
ARROW = " "
timerr = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timerr)
    canvas.itemconfig(timer_text, text="00:00")
    timer["text"] = "Timer"
    check_mark["text"] = ARROW
    global reps
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if (reps % 2 != 0):
        count_down(work_sec)
        timer.config(text="Work", fg= GREEN)
    if (reps % 2 == 0):
        count_down(short_break_sec)
        timer.config(text="5MinBreak", fg= PINK)
        check_mark["text"] += "✓"
    if (reps % 8 == 0):
        count_down(long_break_sec)
        timer.config(text="20Minbreak", fg=RED)
        check_mark["text"] += "✓"
    reps += 1

# ----------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = "0" + str(seconds)

    canvas.itemconfig(timer_text,text=f"{minutes}:{seconds}")
    if count > 0:
        global timerr
        timerr = window.after(1000,count_down,count -1)
    else:
        start_timer()
# -----------00----------------- UI SETUP -------------------------------=-=
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


canvas = Canvas(width=200,height=223,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,105,image=tomato_img)
timer_text = canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)



timer = Label(text="Timer",font=(FONT_NAME,55,"bold"),bg=YELLOW,fg=GREEN)
timer.grid(column=1,row=0)

start = Button(text="Start",highlightbackground=YELLOW,command=start_timer)
start.grid(column=0,row=2)

end = Button(text="Reset",highlightbackground=YELLOW,command=reset_timer)
end.grid(column=2,row=2)

check_mark = Label(text=ARROW,bg=YELLOW,fg=GREEN,font=(FONT_NAME,30))
check_mark.grid(column=1,row=2)

window.mainloop()

