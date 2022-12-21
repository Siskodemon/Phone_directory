# labal(text = "бла бла бла") - выводит текст в окне
# button() - создает кнопку
# entry() - создает поле ввода
# bind() - отвечает за обработку событий
# pack() grid() plase() - распологают виджеты в окне
# mainloop() - запускает цикл обработки событий
# text = "бла бла бла"
# command =   - выполняет команду
# padx = 10, pady = 10  - создание отступов
# textvariable = v   -

# import tkinter.ttk as ttk
import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Radiobutton

root = Tk()
root.title("Телефонная книга")
root.geometry("1000x500+50+50")
root.resizable(width = False, height = False)

tab_control = ttk.Notebook(root)  # 
addition_data = ttk.Frame(tab_control) 
tab_control.add(addition_data, text='Добавлеине')
addition_text = Label(addition_data, text='Добавление данных в телефонную книгу') 
addition_text.grid(column=0, row=0)

# Выбор между введением пользователя или телефона
selected = IntVar()
r_b1 = Radiobutton(addition_data, text="Добавить контактное лицо", value=1, variable=selected)
r_b1.grid(column=0, row=1)
r_b1 = Radiobutton(addition_data, text="Добавить номер телефона", value=2, variable=selected)
r_b1.grid(column=0, row=2)

#Ввод имени пользователя
ins_name = Entry(addition_data, width=8)
ins_name.grid(column=0, row=3)

View_data = ttk.Frame(tab_control)
tab_control.add(View_data, text='Просмотр')
View_text = Label(View_data, text='Просморт данных телефонной книги') 
View_text.grid(column=0, row=0)

# определяем данные для отображения
with sqlite3.connect('direkt.db') as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    people = (row for row in cursor.fetchall())


# определяем столбцы
columns = ("№", "name", "soname", "patronimik","nikname","age", "gender", "nationality")

tree = ttk.Treeview(View_data,columns=columns, show="headings")
tree.grid(column=0, row=1)

# определяем заголовки с выпавниваем по левому краю
tree.heading("№", text="№", anchor=W)
tree.heading("name", text="Имя", anchor=W)
tree.heading("soname", text="Фамилия", anchor=W)
tree.heading("patronimik", text="Отчество", anchor=W)
tree.heading("nikname", text="Никнэйм", anchor=W)
tree.heading("age", text="Возраст", anchor=W)
tree.heading("gender", text="Пол", anchor=W)
tree.heading("nationality", text="Национальность", anchor=W)

# настраиваем столбцы
tree.column("#1", stretch=NO, width=30)
tree.column("#2", stretch=NO, width=80)
tree.column("#3", stretch=NO, width=80)
tree.column("#4", stretch=NO, width=80)
tree.column("#5", stretch=NO, width=80)
tree.column("#6", stretch=NO, width=80)
tree.column("#7", stretch=NO, width=80)
tree.column("#8", stretch=NO, width=100)

# добавляем данные
for person in people:
    tree.insert("", END, values=person)

# добавляем вертикальную прокрутку
scrollbar = ttk.Scrollbar(View_data, orient=VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=1, column=2, sticky="ns")


# class Table(tk.Frame):
#     def __init__(self, parent=None, headings=tuple(), rows=tuple()):
#         super().__init__(parent)

#         table = ttk.Treeview(self, show="headings", selectmode="browse")
#         table["columns"] = headings
#         table["displaycolumns"] = headings

#         for head in headings:
#             table.heading(head, text=head, anchor=tk.CENTER)
#             table.column(head, anchor=tk.CENTER)

#         for row in rows:
#             table.insert('', tk.END, values=tuple(row))

#         scrolltable = tk.Scrollbar(self, command=table.yview)
#         table.configure(yscrollcommand=scrolltable.set)
#         scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
#         table.pack(expand=tk.YES, fill=tk.BOTH)


# data = list()
# with sqlite3.connect('direkt.db') as connection:
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM users")
#     data = (row for row in cursor.fetchall())

# root = tk.Tk()
# table = Table(root, headings=('Фамилия', 'Имя', 'Отчество'), rows=data)
# table.pack(expand=tk.YES, fill=tk.BOTH)
# root.mainloop()

change_data = ttk.Frame(tab_control)
tab_control.add(change_data, text='Изменение') 
change_text = Label(change_data, text='Изменение данных телефонной книги') 
change_text.grid(column=0, row=0)

tab_control.grid(column=0, row=0)

root.mainloop()