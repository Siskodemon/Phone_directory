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
import controller

def clicked():
    nik = View_filter_nikname.get()
    soname = View_filter_soname.get()
    name = View_filter_name.get()
    phone = View_filter_phone_number.get()
    print(f'soname = {soname}, name = {name}, nik = {nik}, phone = {phone}')
    return controller.nik_filter(soname, name, nik, phone)

def view_table(table:list):
    #Чистим данныев таблице
    for i in tree.get_children():
        tree.delete(i)
    #Добавляем данные в таблицу
    for person in table:
        tree.insert("", END, values=person)


import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Radiobutton

root = Tk()
root.title("Телефонная книга")
root.geometry("660x500+50+50")
root.resizable(width = False, height = False)

#Создаём вкладку для добавление данных в БД
tab_control = ttk.Notebook(root)
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

#Создаём вкладку "Просмотр контактных телефонов"
View_data = ttk.Frame(tab_control)
tab_control.add(View_data, text='Просмотр')

View_text = Label(View_data, text='Просморт данных телефонной книги') 

##Задаём поля для фильтрования данных в таблице просмотра контактных телефонов
#Задём поле фильтра по имени
View_filter_lable_name = Label(View_data, text='Имя')
View_filter_name = Entry(View_data,width=15)

#Задём поле фильтра по фамилии
View_filter_lable_soname = Label(View_data, text='Фамилия')
View_filter_soname = Entry(View_data, width=15)

# Задём поле фильтра по никнэйму
View_filter_lable_nikname = Label(View_data, text='Никнэйм')
View_filter_nikname = Entry(View_data, width=10)

# Задём поле фильтра по номеру телефона
View_filter_lable_phone_number = Label(View_data, text='Номер телефона')
View_filter_phone_number = Entry(View_data, width=10)

# Задём кнопку исполнения фильтра
View_filter_button = Button(View_data, text='Фильтр', width= 5, command=clicked)

#Определяем данные для отображения
with sqlite3.connect('direkt.db') as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    people = (row for row in cursor.fetchall())

# определяем столбцы
columns = ("№", "soname", "name", "nikname", "phone", "comment")

tree = ttk.Treeview(View_data,columns=columns, show="headings")


# определяем заголовки с выпавниваем по левому краю
tree.heading("№", text="№", anchor=W)
tree.heading("soname", text="Фамилия", anchor=W)
tree.heading("name", text="Имя", anchor=W)
tree.heading("nikname", text="Никнэйм", anchor=W)
tree.heading("phone", text="Телефон", anchor=W)
tree.heading("comment", text="Комментарий", anchor=W)


# настраиваем столбцы
tree.column("#1", stretch=NO, width=30)
tree.column("#2", stretch=NO, width=80)
tree.column("#3", stretch=NO, width=80)
tree.column("#4", stretch=NO, width=80)
tree.column("#5", stretch=NO, width=80)
tree.column("#6", stretch=NO, width=80)

# добавляем данные
controller.nik_filter('', '', '', '')

# добавляем вертикальную прокрутку
scrollbar = ttk.Scrollbar(View_data, orient=VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)

#Размещаем виджеты на сетке вкладки
View_text.grid(column=0, row=0,columnspan=5)
View_filter_lable_name.grid(column=0, row=1)
View_filter_name.grid(column=0, row=2)
View_filter_lable_soname.grid(column=1, row=1)
View_filter_soname.grid(column=1, row=2)
View_filter_lable_nikname.grid(column=2, row=1)
View_filter_nikname.grid(column=2, row=2)
View_filter_lable_phone_number.grid(column=3, row=1)
View_filter_phone_number.grid(column=3, row=2)
View_filter_button.grid(column=4, row=2)
tree.grid(column=0, row=3,columnspan=5)
scrollbar.grid(column=5, row=3,  sticky="ns")


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