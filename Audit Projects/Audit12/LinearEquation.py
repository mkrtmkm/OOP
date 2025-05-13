from tkinter import *


def Solve_Sys():
    try:
        a1 = float(ent_a1.get())
        b1 = float(ent_b1.get())
        c1 = float(ent_c1.get())
        a2 = float(ent_a2.get())
        b2 = float(ent_b2.get())
        c2 = float(ent_c2.get())

        det = a1 * b2 - a2 * b1
        det_x = c1 * b2 - c2 * b1
        det_y = a1 * c2 - a2 * c1

        if det != 0:
            x = det_x / det
            y = det_y / det
        else:
            if det_x == 0 and det_y == 0:
                result_label["text"] = "Неск кількість розв"
            else:
                result_label["text"] = "Немає розв"
    except ValueError:
        result_label["text"] = "Виникла помилка"

root = Tk()

#=====РІВНЯННЯ 1=====

frame_eq1 = LabelFrame(root, text="Рівняння 1")
frame_eq1.pack(pady=5, fill="x", padx=10)

ent_a1 = Entry(frame_eq1)
ent_a1.pack(side = BOTTOM)
lab_a1 = Label(ent_a1, text = "* x")
lab_a1.pack(side = RIGHT)
ent_b1 = Entry(lab_a1)
ent_b1.pack(side = RIGHT)
lab_b1 = Label(ent_b1, text = "* y")
lab_b1.pack(side = RIGHT)
lab_c1 = Label(lab_b1, text = " = ")
lab_c1.pack(side = RIGHT)
ent_c1 = Entry(lab_c1)
ent_c1.pack(side = RIGHT)


#=====РІВНЯННЯ 2=====
frame_eq2 = LabelFrame(ent_a1, text="Рівняння 2")
frame_eq1.pack(side = BOTTOM)

ent_a2 = Entry(frame_eq2)
ent_a2.pack(side = BOTTOM)
lab_a2 = Label(ent_a2, text = "* x")
lab_a2.pack(side = RIGHT)
ent_b2 = Entry(lab_a2)
ent_b2.pack(side = RIGHT)
lab_b2 = Label(ent_b2, text = "* y")
lab_b2.pack(side = RIGHT)
lab_c2 = Label(lab_b2, text = " = ")
lab_c2.pack(side = RIGHT)
ent_c2 = Entry(lab_c2)
ent_c2.pack(side = RIGHT)

solve_button = Button(ent_a2, text="Розв'язати", command=Solve_Sys)
solve_button.pack(side = BOTTOM)

result_label = Label(solve_button, text="", font=("Arial", 12))
result_label.pack(side = BOTTOM)

root.mainloop()
