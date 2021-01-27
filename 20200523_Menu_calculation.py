import tkinter

#-- まずは部品を用意
def click_btn():
    total=0
    pts = 0
    for i in range(7):
        if bvar[i].get() == True:
            total = total + price[i]
    text.delete("1.0", tkinter.END)
    text.insert("1.0", "＜合計金額＞\nお会計は" + str(total) + " €。\n")


#-- ここからメインプログラム
root = tkinter.Tk()
root.title("ネコに餌を買ってあげましょう")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="sumire.png")
canvas.create_image(400, 300, image=gazou)
button = tkinter.Button(text="支払い", font=("Times New Roman", 32), bg="lightgreen", command=click_btn)
button.place(x=400, y=480)
text = tkinter.Text(width=40, height=5, font=("Times New Roman", 16))
text.place(x=320, y=30)

#-- メニューを準備
bvar = [None]*7
cbtn = [None]*7
price = [1,2,4,8,16,32,64]

#-- 入力欄フォームを準備
for i in range(7):
    bvar[i] = tkinter.BooleanVar()
    bvar[i].set(False)
    cbtn[i] = tkinter.Checkbutton(text=str(price[i])+" €", font=("Times New Roman", 12), variable=bvar[i], bg="#dfe")
    cbtn[i].place(x=400, y=160+40*i)

#-- メインループ
root.mainloop()
