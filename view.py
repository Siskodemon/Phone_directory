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

import sqlite3
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Телефонная книга")
root.geometry("1000x500+50+50")
root.resizable(width = False, height = False)

tab_control = ttk.Notebook(root)  # 
addition_data = ttk.Frame(tab_control) 
tab_control.add(addition_data, text='Добавлеине')
addition_text = Label(addition_data, text='Добавление данных в телефонную книгу') 
addition_text.grid(column=0, row=0)

View_data = ttk.Frame(tab_control)
tab_control.add(View_data, text='Просмотр')
View_text = Label(View_data, text='Просморт данных телефонной книги') 
View_text.grid(column=0, row=0)

change_data = ttk.Frame(tab_control)
tab_control.add(change_data, text='Изменение') 
change_text = Label(change_data, text='Изменение данных телефонной книги') 
change_text.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both') 

root.mainloop()