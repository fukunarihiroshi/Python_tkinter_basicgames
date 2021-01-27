import tkinter
import random

def click_btn():
    label_01["text"]=random.choice(["大吉", "中吉", "小吉", " 凶 "])
    label_01.update()


# window の作成
root = tkinter.Tk()
root.title("おみくじ")
root.resizable(False,False)

#canvas の作成
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()

#画像読み込み
gazou = tkinter.PhotoImage(file="miko.png")
canvas.create_image(400,300,image=gazou)


#ラベルの作成
label_01 = tkinter.Label(root, text="運勢？", font=("Times New Roman", 60) )
label_01.place(x=380, y=20)

#ボタンの作成
button = tkinter.Button(root, text="おみくじを引く", font=("Times New Roman", 20), command=click_btn )
button.place(x=360, y=400)

root.mainloop()


