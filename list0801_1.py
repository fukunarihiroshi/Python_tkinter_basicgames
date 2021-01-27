# カウントアップのプログラム

import tkinter

tmr = 0
def count_up():
    global tmr
    tmr = tmr + 1
    label["text"] = tmr
    if tmr < 10:
        root.after(500, count_up)


root = tkinter.Tk()
label = tkinter.Label(font=("Times New Roman", 80))
label.pack()
root.after(500, count_up)
root.mainloop()

# 再帰プログラム -> loop 


