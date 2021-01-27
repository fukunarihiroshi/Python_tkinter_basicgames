import tkinter
root = tkinter.Tk()
root.title("おみくじ")
#root.resizable(False,False)

canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()

gazou = tkinter.PhotoImage(file="jinja.png")
canvas.create_image(400, 300, image=gazou)
#root.mainloop()







'''
Pnohtyg

'''

