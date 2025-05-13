from tkinter import *
root = Tk()

def Palindrome():
    text = ent.get()
    processed_text = ''.join(char.lower() for char in text if char.isalnum())
    if text == processed_text:
        lab["text"] = "Даний рядок є паліндромом"
    else:
        lab["text"] = "Даний рядок НЕ є паліндромом"

ent = Entry(root, font="Arial 12")
lab = Label(root, font="Arial 12")
btn = Button(root, text = "Обчислити", font="Arial 12", command=Palindrome)

ent.pack()
lab.pack()
btn.pack()

root.mainloop()