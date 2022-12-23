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

def insert_contact():
    if ins_soname.get() != '' and ins_name.get() != '' and ins_nikname.get() !='' and ins_phone.get() !='':
        name = ins_name.get()
        soname = ins_soname.get()
        name = ins_name.get()
        patr = ins_patr.get()
        nik = ins_nikname.get()
        age = ins_age.get()
        gender = ins_gender.get()
        nationality = ins_nationality.get()
        phone = ins_phone.get()
        return controller.ins_con_in_db(soname, name, patr, nik, age, gender, nationality,phone)
    else:
        return contact_ins_result_lable.configure(text=f'Контакт не добавлен. Заполните все обязательные поля (*) и повторите попытку')

def view_ins_cont_result(result):
    return contact_ins_result_lable.configure(text=f'{result}')

def delet_user_contact():
    nik = Del_nikname.get()
    return controller.delete_contact(nik)


def delet_user_result(result):
    return Del_user_result_label.configure(text=result)
 
import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Radiobutton

root = Tk()
root.title("Телефонная книга")
root.geometry("1000x500+50+50")
#root.resizable(width = False, height = False)

# =====================================================================================================
# Создаём вкладку для добавления данных
# =====================================================================================================
#Создаём вкладку для добавление данных в БД
tab_control = ttk.Notebook(root)
addition_data = ttk.Frame(tab_control) 
tab_control.add(addition_data, text='Добавлеине')
addition_text = Label(addition_data, text='Добавление данных в телефонную книгу') 
addition_text.grid(column=0, row=0, columnspan=8)

#Заполняем поля ввода для данных контакта
ins_contact_lable = Label(addition_data, text='Заполните поля для добавления нового контакта(поля помеченные звёздочкой (*) обязательны для заполнения)')

ins_name_lable = Label(addition_data, text='(*) Имя')
ins_name = Entry(addition_data, width=10)

ins_soname_lable = Label(addition_data, text='(*) Фамилия')
ins_soname = Entry(addition_data, width=10)

ins_patr_lable = Label(addition_data, text='Отчество')
ins_patr = Entry(addition_data, width=10)

ins_nikname_lable = Label(addition_data, text='(*) Никнэйм')
ins_nikname = Entry(addition_data, width=10)

ins_age_lable = Label(addition_data, text='Возраст')
ins_age = Entry(addition_data, width=3)

ins_gender_lable = Label(addition_data, text='Пол')
ins_gender = Entry(addition_data, width=3)

ins_nationality_lable = Label(addition_data, text='Национальность')
ins_nationality = Entry(addition_data, width=8)

ins_phone_lable = Label(addition_data, text='(*) Телефон')
ins_phone = Entry(addition_data, width=15)

ins_button = Button(addition_data, text='Добавить', command=insert_contact)

contact_ins_result_lable = Label(addition_data, text='')

# Теперь размечаем поля ввода для данных контакта
ins_contact_lable.grid(column=0, row=2, columnspan=8, padx=1, pady=25)
ins_soname_lable.grid(column=0, row=3,padx=1, pady=1)
ins_soname.grid(column=0, row=4, padx=1, pady=1)
ins_name_lable.grid(column=1, row=3, padx=1, pady=1)
ins_name.grid(column=1, row=4, padx=1, pady=1)
ins_patr_lable.grid(column=2, row=3, padx=1, pady=1)
ins_patr.grid(column=2, row=4, padx=1, pady=1)
ins_nikname_lable.grid(column=3, row=3, padx=1, pady=1)
ins_nikname.grid(column=3, row=4, padx=1, pady=1)
ins_age_lable.grid(column=4, row=3, padx=1, pady=1)
ins_age.grid(column=4, row=4, padx=1, pady=1)
ins_gender_lable.grid(column=5, row=3, padx=1, pady=1)
ins_gender.grid(column=5, row=4, padx=1, pady=1)
ins_nationality_lable.grid(column=6, row=3, padx=1, pady=1)
ins_nationality.grid(column=6, row=4, padx=1, pady=1)
ins_phone_lable.grid(column=7, row=3, padx=1, pady=1)
ins_phone.grid(column=7, row=4, padx=1, pady=1)
ins_button.grid(column=3, row=5, padx=1, pady=25)
contact_ins_result_lable.grid(column=0, row=6, columnspan=8, padx=1, pady=25)

addition_data.columnconfigure(index=0, weight=1)
addition_data.columnconfigure(index=1, weight=1)
addition_data.columnconfigure(index=2, weight=1)
addition_data.columnconfigure(index=3, weight=1)
addition_data.columnconfigure(index=4, weight=1)
addition_data.columnconfigure(index=5, weight=1)
addition_data.columnconfigure(index=6, weight=1)

# ======================================================================================================
#Создаём вкладку с просмотра данных
# ======================================================================================================
#Создаём саму вкладку "Просмотр контактных телефонов"
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

# ======================================================================================================
# Создаём вкладку для редактирования данных
# ======================================================================================================
change_data = ttk.Frame(tab_control)
tab_control.add(change_data, text='Изменение') 
change_text = Label(change_data, text='Изменение данных телефонной книги', padx=1, pady=25)
change_text.grid(column=0, row=0, columnspan=7)

# # Выбор между введением пользователя или телефона
# selected = IntVar()
# r_b1 = Radiobutton(change_data, text="Редактировать контактное лицо", value=1, variable=selected)
# r_b2 = Radiobutton(change_data, text="Редактировать данные телефонов контакта", value=2, variable=selected)

# r_b1.grid(column=0, row=1, columnspan=4)
# r_b2.grid(column=4, row=1, columnspan=4)

# Задаём виджеты для удаления пользователя
Del_lable_nikname = Label(change_data, text='Никнэйм')
Del_nikname = Entry(change_data, width=10)
Del_button = Button(change_data, text='Удалить контакт', command=delet_user_contact)
Del_user_result_label = Label(change_data, text='')

#Размечаем виджеты для удаления пользователя
Del_lable_nikname.grid(column=0, row=1, columnspan=2)
Del_nikname.grid(column=0, row=2)
Del_button.grid(column=1, row=2)
Del_user_result_label.grid(column=0, row=3, columnspan=2)


tab_control.grid(column=0, row=0)

root.mainloop()