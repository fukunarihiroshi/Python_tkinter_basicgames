# カウントアッププログラム　改良版

import tkinter
tmr = 0

def count_up():
    global tmr
    tmr = tmr + 1
    label["text"] = tmr

# 改良版　10秒数え終わったら、ウィンドウを閉じる
    if tmr < 10:
        root.after(1000, count_up)
    else:
        root.destroy()

root = tkinter.Tk()
label = tkinter.Label(font=("Times New Roman", 80))
label.pack()

root.after(1000, count_up)
root.mainloop()
