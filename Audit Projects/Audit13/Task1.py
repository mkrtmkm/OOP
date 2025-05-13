import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename


class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Конвертер Валют")

        self.rates = {}
        self.selected_rate = None

        self.build_interface()
        self.build_menu()

    def build_interface(self):
        list_frame = tk.LabelFrame(self.root, text="Курси валют", padx=10, pady=10)
        list_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.listbox = tk.Listbox(list_frame, height=10, width=40)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(list_frame, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox.config(yscrollcommand=scrollbar.set)
        self.listbox.bind('<<ListboxSelect>>', self.on_listbox)

        tk.Label(self.root, text="Сума:").grid(row=4, column=0, pady=(10, 0), sticky='e')
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.grid(row=4, column=1, pady=(10, 0), padx=10, sticky='w')

        # Кнопки
        tk.Button(self.root, text="Конвертувати", command=self.convert)\
            .grid(row=5, column=0, pady=15, padx=10)
        tk.Button(self.root, text="Вийти", command=self.root.quit)\
            .grid(row=5, column=1, pady=15, padx=10)


        self.result_label = tk.Label(self.root, text="Результат: ")
        self.result_label.grid(row=6, column=0, columnspan=2, pady=10)

    def build_menu(self):
        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label = "Відкрити", command = self.LoadFile)
        filemenu.add_separator()
        filemenu.add_command(label = "Вихід", command = self.root.quit)

        menubar.add_cascade(label = "Файл", menu=filemenu)

        root.config(menu=menubar)

    def LoadFile(self):
        filename = askopenfilename(title="Виберіть файл з курсами", filetypes=[("Text files", "*.txt")])
        if not filename:
            return

        self.rates.clear()
        self.listbox.delete(0, tk.END)

        try:
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    parts = line.strip().split()
                    if len(parts) != 3:
                        continue
                    from_cur, to_cur, rate = parts
                    try:
                        rate = float(rate)
                        self.rates[(from_cur, to_cur)] = rate
                        self.listbox.insert(tk.END, f"{from_cur} {to_cur} {rate}")
                    except ValueError:
                        continue
        except Exception as e:
            messagebox.showerror("Помилка, не вдалося відкрити файл")

    def on_listbox(self, event):
        cur = self.listbox.curselection()
        if not cur:
            self.selected_rate = None
            return
        text = self.listbox.get(cur[0])
        try:
            parts = text.split()
            self.from_cur = parts[0]
            self.to_cur = parts[1]
            self.selected_rate = float(parts[2])
        except:
            self.selected_rate = None



    def convert(self):
        if self.selected_rate is None:
            messagebox.showwarning("Увага", "Оберіть курс з списку.")
            return

        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("Помилка", "Введіть коректну суму.")
            return

        converted = amount * self.selected_rate
        self.result_label.config(text=f"Результат: {amount:.2f} {self.from_cur} = {converted:.2f} {self.to_cur}")



if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()