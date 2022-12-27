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
import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Radiobutton
from tkinter import messagebox

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
    print(list(table))
    id = 1
    for person in table:
        #tree.insert("",END ,values=id)
        ins = list(str(id))
        for i in person:
            ins.append(i)
        print(ins)
        tree.insert("", END, values=ins)
        id += 1

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
    nik = Nikname_Entry.get()
    return controller.delete_contact(nik)

# Извлекаем ник нэйм из поля ввода и передаём в controller
def Search_date_of_contact():
    nik = Nikname_os_Entry.get()
    return controller.Give_nik_to_controller(nik)

#Принемаем отфильтрованные номера телефонов контакта из файла Controlle и выводим их в таблицу
def Show_phone_numbers(data):
    # Чистим данныев таблице
    for i in tree_phone.get_children():
        tree_phone.delete(i)
    # Добавляем данные в таблицу
    print(list(data))
    id = 1
    for person in data:
        #tree.insert("",END ,values=id)
        ins = list(str(id))
        for i in person:
            ins.append(i)
        print(ins)
        tree_phone.insert("", END, values=ins)
        id += 1

# Передаю данные контакта на вывод
def Show_data_contact(result):
    list = result
    Soname_Entry.insert(0,list[0])
    Name_Entry.insert(0, list[1])
    Patronymic_Entry.insert(0, list[2])
    Nikname_Entry.insert(0, list[3])
    Age_Entry.insert(0, list[4])
    Gender_Entry.insert(0, list[5])
    Nationality_Entry.insert(0, list[6])
    return result
 
#messagebox.showinfo('Заголовок', 'Текст')

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
View_filter_lable_soname.grid(column=0, row=1)
View_filter_soname.grid(column=0, row=2)
View_filter_lable_name.grid(column=1, row=1)
View_filter_name.grid(column=1, row=2)
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
change_text = Label(change_data, text='Изменение данных телефонной книги', padx=1, pady=2)
change_text.grid(column=0, row=0, columnspan=10)

# Задаём общие виджеты для вывода данных контакта
Lable_os_nikname = Label(change_data, text='Никнэйм')
Nikname_os_Entry = Entry(change_data, width=15)
Os_button = Button(change_data, text='Поиск', command=Search_date_of_contact)
Empty_lable = Label(change_data, text='')

# Задаём виджеты для обновление данных контакта пользователя
Lable_soname = Label(change_data, text='Фамилия')
Soname_Entry = Entry(change_data, width=15)
Lable_name = Label(change_data, text='Имя')
Name_Entry = Entry(change_data, width=15)
Lable_patronymic = Label(change_data, text='Отчество')
Patronymic_Entry = Entry(change_data, width=15)
Lable_nikname = Label(change_data, text='Никнэйм')
Nikname_Entry = Entry(change_data, width=15)
Lable_age = Label(change_data, text='Возраст')
Age_Entry = Entry(change_data, width=15)
Lable_gender = Label(change_data, text='Пол')
Gender_Entry = Entry(change_data, width=15)
Lable_nationality = Label(change_data, text='Национальность')
Nationality_Entry = Entry(change_data, width=15)
Update_button = Button(change_data, text='Обновить контакт',command=delet_user_contact)
Del_button = Button(change_data, text='Удалить контакт',command=delet_user_contact)
Lable_result = Label(change_data, text='Тут будет результат')

# Размечаем общие виджеты для вывода данных контакта
Lable_os_nikname.grid(row=1, column=0, padx=2)
Nikname_os_Entry.grid(row=2, column=0, padx=2)
Os_button.grid(row=2, column=1, padx=2)
Empty_lable.grid(row=3, column=0, padx=2, pady=10)

# Размечаем виджеты для обновление данных контакта пользователя
Lable_soname.grid(row = 4, column=0, padx=2, pady=2)
Soname_Entry.grid(row = 4, column=1, padx=2, pady=2)
Lable_name.grid(row = 5, column=0, padx=2, pady=2)
Name_Entry.grid(row = 5, column=1, padx=2, pady=2)
Lable_patronymic.grid(row = 6, column=0, padx=2, pady=2)
Patronymic_Entry.grid(row = 6, column=1, padx=2, pady=2)
Lable_nikname.grid(row = 7, column=0, padx=2, pady=2)
Nikname_Entry.grid(row = 7, column=1, padx=2, pady=2)
Lable_age.grid(row = 8, column=0, padx=2, pady=2)
Age_Entry.grid(row = 8, column=1, padx=2, pady=2)
Lable_gender.grid(row = 9, column=0, padx=2, pady=2)
Gender_Entry.grid(row = 9, column=1, padx=2, pady=2)
Lable_nationality.grid(row = 10, column=0, padx=2, pady=2)
Nationality_Entry.grid(row = 10, column=1, padx=2, pady=2)
Update_button.grid(row = 11, column=0, padx=2, pady=2)
Del_button.grid(row = 11, column=1, padx=2, pady=2)
Lable_result.grid(row = 12, column=0, columnspan=2, padx=2, pady=2)

# Задаём виджеты для просмотра и обновления телефонов контакта
Lable_phone = Label(change_data, text='Телефон')
Phone_Entry = Entry(change_data, width=15)
Lable_comment = Label(change_data, text='Комментарий')
Comment_Entry = Entry(change_data, width=15)
Update_phone_button = Button(change_data, text='Обновить телефон', command=delet_user_contact)
Del_phone_button = Button(change_data, text='Удалить телефон', command=delet_user_contact)

columns_phone = ("№", "phone", "comment")
tree_phone = ttk.Treeview(change_data, columns=columns_phone, show="headings")

# определяем заголовки с выпавниваем по левому краю
tree_phone.heading("№", text="№", anchor=W)
tree_phone.heading("phone", text="Телефон", anchor=W)
tree_phone.heading("comment", text="Комментарий", anchor=W)

# настраиваем столбцы
tree_phone.column("#1", stretch=NO, width=30)
tree_phone.column("#2", stretch=NO, width=100)
tree_phone.column("#3", stretch=NO, width=100)

# добавляем вертикальную прокрутку
scrollbar = ttk.Scrollbar(change_data, orient=VERTICAL,command=tree_phone.yview)
tree_phone.configure(yscroll=scrollbar.set)

# Размечаем виджеты для обновление данных контакта пользователя
Lable_phone.grid(row = 4, column=2, padx=25, pady=2)
Phone_Entry.grid(row = 4, column=3, padx=2, pady=2)
Lable_comment.grid(row = 5, column=2, padx=25, pady=2)
Comment_Entry.grid(row = 5, column=3, padx=2, pady=2)
Update_phone_button.grid(row = 4, column=4, padx=2, pady=2)
Del_phone_button.grid(row = 5, column=4, padx=2, pady=2)

tree_phone.grid(column=2, row = 6, rowspan=16, columnspan=3, padx=20, pady=2)
scrollbar.grid(column=4, row=6,  sticky="ns", pady=2, rowspan=16)

tab_control.grid(column=0, row=0)

root.mainloop()