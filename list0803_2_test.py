# 入力キーを調べるプログラム

import tkinter

key = "" # null を代入
def key_down(e):
    global key
    key = e.keysym

def main_proc():
    if key == "a":
        label["text"] = "apple"
    elif key == "b":
        label["text"] = "bee"
    elif key == "c":
        label["text"] = "cash"
    else:
        label["text"] = key
    root.after(100, main_proc)

root = tkinter.Tk()
root.title("リアルタイムキー入力")

root.bind("<KeyPress>", key_down)

label = tkinter.Label(font=("Times New Roman", 80))
label.pack()

main_proc()
root.mainloop()


