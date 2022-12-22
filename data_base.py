import sqlite3
from sqlite3 import Error


def view_phone_numbers(soname, name, nik, phone):
    connection = create_connection('direkt.db')
    cursor = connection.cursor()
    #nik = nik_output(cursor, 'users')
    print(f' Выводим все телефоны контакта {nik}')
    request = f"""
            SELECT
                users.id, users.soname, users.name, users.nikname, phone.phone, phone.comment
            FROM
                users
            JOIN
                phone
            ON
                users.id = phone.user_id"""
    if nik != '' or soname !='' or name !='' or phone !='':
        count = 0
        request = request + f"""
            WHERE"""
        if nik != '':
            if count == 0:
                count = 1
                request = request + f"""
                nikname = '{nik}'
                """
            else:
                request = request + " AND " + f"""
                nikname = '{nik}'
                """
        if soname != '':
            if count == 0:
                count = 1
                request = request + f"""
                soname = '{soname}'
                """
            else:
                request = request + " AND " + f"""
                soname = '{soname}'
                """
        if name != '':
            if count == 0:
                count = 1
                request = request + f"""
                name = '{name}'
                """
            else:
                request = request + " AND " + f"""
                name = '{name}'
                """
        if phone != '':
            if count == 0:
                count = 1
                request = request + f"""
                phone = '{phone}'
                """
            else:
                request = request + " AND " + f"""
                phone = '{phone}'
                """
        print(f'request = {request}')
    try:
        cursor.execute(request)
        id = cursor.fetchall()
        for i in id:
            print(f'{i}')
        connection.commit()
        print(f"Телефоны контакта {nik} успешно выведены")
    except Error as e:
        print(f"The error '{e}' occurred")
    return id

# Соединение с БД
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Соединение с бд установлено")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

# #Вывод списка значений из поля nikname
def nik_output(focus,table):
    print(f'=================================')
    focus.execute(f"SELECT nikname FROM {table}")
    id = focus.fetchall()
    for i in id:
        print(f'{i}', end='')
    print()
    nikname= input(f'Введите ник контакта из списка выше: -->')
    print(f'=================================')
    return nikname

# # Работа с таблицей в инициализированной бд
# def work_for_table(connection, name_table):
#     cursor = connection.cursor()
#     if name_table == 'users':
#         print(f'Выберите действие: ')
#         print(f'1 - добавление контакта, 2 - просмотр списка контактов, 3 - обновление контакта, 4 - удаление контакта')
#         chois = int(input(f'--> '))
#         if chois == 1:
#             insert = []
#             insert.append(input('Введите фамилию - '))
#             insert.append(input('Введите имя - '))
#             insert.append(input('Введите ник - '))
#             print(f' Добавляем следующие данные в БД - {insert}')
#             try:
#                 cursor.execute(f"""
#                 INSERT INTO
#                 {name_table}
#                     (soname, name, nikname)
#                 VALUES
#                     ('{insert[0]}', '{insert[1]}', '{insert[2]}')""")
#                 connection.commit()
#                 print(f"Данные успешно добавлены")
#             except Error as e:
#                 print(f"The error '{e}' occurred")
#         elif chois == 2:
#             cursor.execute(f"SELECT * FROM {name_table}")
#             id = cursor.fetchall()
#             for i in id:
#                 print(i)
#         elif chois == 3:
#             nik = nik_output(cursor,'users')
#             print(f'Имя - 1, Фамилию - 2, Отчество - 3, Ник - 4, Возраст - 5, Пол - 6, Национальность - 7')
#             param = int(input(f'Выберите что будем обновлять? --> '))
#             print(f'=================================')
#             if param == 1:
#                 param = 'name'
#             elif param == 2:
#                 param = 'soname'
#             elif param == 3:
#                 param = 'patronymic'
#             elif param == 4:
#                 param = 'nikname'
#             elif param == 5:
#                 param = 'age'
#             elif param == 6:
#                 param = 'gender'
#             elif param == 7:
#                 param = 'nationality'
#             else:
#                 print(f'Введёт неверный параметр. Повторите ввод')
#             if param == 'age':
#                 update = int(input(f'Введите новые данные: '))
#             else:
#                 update = input(f'Введите новые данные: ')
#             try:
#                 cursor.execute(f"""
#                 UPDATE
#                     {name_table}
#                 SET
#                     {param} = '{update}'
#                 WHERE
#                     nikname = '{nik}'
#                 """)
#                 connection.commit()
#                 print(f"Данные успешно изменены")
#             except Error as e:
#                 print(f"The error '{e}' occurred")
#         elif chois == 4:
#             nik = nik_output(cursor, 'users')
#             try:
#                 cursor.execute(f"""
#                 DELETE FROM
#                     {name_table}
#                 WHERE
#                     nikname = '{nik}'
#                 """)
#                 connection.commit()
#                 print(f"Контакт {nik} успешно удалён.")
#             except Error as e:
#                 print(f"The error '{e}' occurred")
#         else:
#             print(f'Вводе не верен, повторите')
#     elif name_table == 'phone':
#         print(f'Выберите действие: ')
#         print(f'1 - добавить телефон, 2 - просмотр список телефонов контакта, 3 - обновление номера телефона, 4 - удаление телефона')
#         chois = int(input(f'--> '))
#         if chois == 1:
#             nik = nik_output(cursor, 'users')
#             insert = []
#             insert.append(input('Введите номер телефона - '))
#             insert.append(input('Введите комментарий - '))
#             print(f' Добавляем следующие данные в БД номеров телефонов контакта {nik} - {insert}')
#             try:
#                 cursor.execute(f"SELECT id FROM users WHERE nikname = '{nik}'")
#                 id = cursor.fetchall()
#                 print(f'Тип id - {type(id[0])}')
#                 print(f'Найденый id - {id[0]}')
#                 connection.commit()
#                 print(f"Id успешно найден")
#             except Error as e:
#                 print(f"The error '{e}' occurred")
#             count = list(id[0])
#             try:
#                 cursor.execute(f"""
#                 INSERT INTO
#                 {name_table}
#                     (phone, comment, user_id)
#                 VALUES
#                     ({int(insert[0])}, '{insert[1]}', {count[0]})""")
#                 connection.commit()
#                 print(f"Телефон успешно добавлен контакту {nik}")
#             except Error as e:
#                 print(f"The error '{e}' occurred")
#         elif chois == 2:
#             nik = nik_output(cursor, 'users')
#             print(f' Выводим все телефоны контакта {nik}')
#             try:
#                 cursor.execute(f"""
#                 SELECT 
#                     users.soname, users.name, users.nikname, phone.phone, phone.comment 
#                 FROM 
#                     users
#                 JOIN 
#                     phone 
#                 ON 
#                     users.id = phone.user_id
#                 WHERE 
#                     nikname = '{nik}'
#                 ;""")
#                 id = cursor.fetchall()
#                 for i in id:
#                     print(f'{i}')
#                 connection.commit()
#                 print(f"Телефоны контакта {nik} успешно выведены")
#             except Error as e:
#                 print(f"The error '{e}' occurred")
#         elif chois == 3:
#             nik = nik_output(cursor, 'users')
#             cursor.execute(f"""
#                 SELECT 
#                     phone.id, phone.phone, phone.comment 
#                 FROM 
#                     users
#                 JOIN 
#                     phone 
#                 ON 
#                     users.id = phone.user_id
#                 WHERE 
#                     nikname = '{nik}'
#                 ;""")
#             id = cursor.fetchall()
#             for i in id:
#                 print(f'{i}')
#             print()
#             chois = int(input(f'Введите id, по которому будем менять данные: --> '))
#             print(f'=================================')
#             print(f'Введите что будем менять?')
#             print(f'1 - номер телефона, 2 - комментарий')
#             param = int(input(f'--> '))
#             if param == 1:
#                 param = 'phone'
#                 buf = int(input('Введите новый номер телефона: '))
#             elif param == 2:
#                 param = 'comment'
#                 buf = input('Введите новый комментарий: ')
            
#             print(f'=================================')
#             print(f' Перезаписываем поле {param} контакта {nik}, по полю id={chois} ')
#             try:
#                 cursor.execute(f"""
#                 UPDATE
#                     {name_table}
#                 SET
#                     {param} = '{buf}'
#                 WHERE
#                     id = {chois}
#                 """)
#                 id = cursor.fetchall()
#                 for i in id:
#                     print(f'{i}')
#                 connection.commit()
#                 print(f"Телефон контакт {nik} c id={chois} успешно обновлён")
#             except Error as e:
#                 print(f"The error '{e}' occurred")
#         elif chois == 4:
#             nik = nik_output(cursor, 'users')
#             cursor.execute(f"""
#                 SELECT 
#                     phone.id, phone.phone, phone.comment 
#                 FROM 
#                     users
#                 JOIN 
#                     phone 
#                 ON 
#                     users.id = phone.user_id
#                 WHERE 
#                     nikname = '{nik}'
#                 ;""")
#             id = cursor.fetchall()
#             for i in id:
#                 print(f'{i}')
#             print()
#             chois = int(input(f'Введите id, по которому будем удалять данные: --> '))
#             try:
#                 cursor.execute(f"""
#                 DELETE FROM
#                     {name_table}
#                 WHERE
#                     id = {chois}
#                 """)
#                 connection.commit()
#                 print(f"Данные контакта {nik} по id={chois} успешно удалены.")
#             except Error as e:
#                 print(f"The error '{e}' occurred")
#         # try:
#         #     cursor.execute(query)
#         #     connection.commit()
#         #     print(f"Таблица {name_table} успешно создана")
#         # except Error as e:
#         #     print(f"The error '{e}' occurred")

# bd = create_connection('direkt.db')

# # Добавление данных в таблицу в инициализированной бд
# def create_table(connection, query, name_table):
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         connection.commit()
#         print(f"Таблица {name_table} успешно подключена")
#     except Error as e:
#         print(f"The error '{e}' occurred")

# # команда для создания таблицы user в базе данных
# user_table ="""
#       CREATE TABLE IF NOT EXISTS users(
#       id INTEGER PRIMARY KEY AUTOINCREMENT,
#       soname TEXT NOT NULL,
#       name TEXT NOT NULL,
#       patronymic TEXT,
#       nikname TEXT NOT NULL,
#       age INTEGER,
#       gender TEXT,
#       nationality TEXT
#       );"""

# # команда для создания таблицы phone в базе данных
# phone_table = """
#       CREATE TABLE IF NOT EXISTS phone(
#       id INTEGER PRIMARY KEY AUTOINCREMENT,
#       phone INTEGER NOT NULL,
#       comment TEXT,
#       user_id INTEGER NOT NULL, 
#       FOREIGN KEY (user_id) REFERENCES users(id)
#       );"""

# create_table(bd, user_table, 'users')
# create_table(bd, phone_table, 'phone')

# print(f'Работаем с контактами или с телефонами?')
# print(f'С контактами - 1, с телефонами - 2')
# if int(input(f'--> ')) == 1:
#     work_for_table(bd,'users')
# else:
#     work_for_table(bd, 'phone')

# #Внесение данных пользователя
# # insert=[]
# # soname = input('Введите фамилию - ')
# # insert.append(soname)
# # name = input('Введите имя - ')
# # insert.append(name)
# # patronymic = input('Введите отчество - ')
# # insert.append(patronymic)
# # nikname = input('Введите Ник - ')
# # insert.append(nikname)
# # print(f' ФИО + Ник - {insert}')

# # #Добавление записей в таблшицу users
# # bd1 = bd.cursor()
# # bd1.execute(f"""
# # INSERT INTO 
# # users 
# #       (patronymic, name, soname, nikname) 
# # VALUES 
# #       ('{insert[0]}', '{insert[1]}', '{insert[2]}', '{insert[3]}')""")

# # Удаление записей из таблицы users
# # bd1 = bd.cursor()
# # bd1.execute(f"""
# # DELETE FROM
# #       users
# # WHERE
# #       id = 2
# # """)

# # Обновление(изменение) записей из таблицы users
# # bd1 = bd.cursor()
# # bd1.execute(f"""
# # UPDATE 
# #      users
# # SET 
# #      age = 30,gender = 'М'
# # WHERE
# #      id = 2
# # """)

# # Просмотр всех записей из таблицы users
# # bd1 = bd.cursor()
# # bd1.execute("SELECT * FROM users")
# # id = bd1.fetchall()
# # for i in id:
# #     print(i)

# # Просмотр поля id из таблицы users и вывод первой записи
# # bd1.execute("SELECT id FROM users")
# # id = bd1.fetchall()

# # print(f'Тип - {type(id)}')
# # print(id[0])

# bd.commit()
# bd.close()
