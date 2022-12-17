import sqlite3
from sqlite3 import Error

# Соединение с БД
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Соединение с бд установлено")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

# Создание таблиц в инициализированной бд
def create_table(connection, query,name_table):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print(f"Таблица {name_table} успешно создана")
    except Error as e:
        print(f"The error '{e}' occurred")

bd = create_connection('direkt.db')

# Добавление данных в таблицу в инициализированной бд
# def insert_in_table(connection, query):
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         connection.commit()
#         print("Данные успешно внесены")
#     except Error as e:
#         print(f"The error '{e}' occurred")

# команда для создания таблицы user в базе данных
user_table ="""
      CREATE TABLE IF NOT EXISTS users(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      patronymic TEXT,
      name TEXT NOT NULL,
      soname TEXT NOT NULL,
      nikname TEXT NOT NULL,
      age INTEGER,
      gender TEXT,
      nationality TEXT
      );"""

# команда для создания таблицы phone в базе данных
phone_table = """
      CREATE TABLE IF NOT EXISTS phone(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      phone INTEGER NOT NULL,
      comment TEXT,
      user_id INTEGER NOT NULL, 
      FOREIGN KEY (user_id) REFERENCES users(id)
      );"""

create_table(bd, user_table, 'users')
create_table(bd, phone_table, 'phone')

#Внесение данных пользователя
insert=[]

soname = input('Введите фамилию - ')
insert.append(soname)

name = input('Введите имя - ')
insert.append(name)

patronymic = input('Введите отчество - ')
insert.append(patronymic)

nikname = input('Введите Ник - ')
insert.append(nikname)

print(f' ФИО + Ник - {insert}')


# #Добавление записей в таблшицу users
bd1 = bd.cursor()
bd1.execute(f"""
INSERT INTO 
users 
      (patronymic, name, soname, nikname) 
VALUES 
      ('{insert[0]}', '{insert[1]}', '{insert[2]}', '{insert[3]}')""")

# Удаление записей из таблицы users
# bd1 = bd.cursor()
# bd1.execute(f"""
# DELETE FROM
#       users
# WHERE
#       id = 2
# """)

# Обновление(изменение) записей из таблицы users
# bd1 = bd.cursor()
# bd1.execute(f"""
# UPDATE 
#      users
# SET 
#      age = 30,gender = 'М'
# WHERE
#      id = 2
# """)

bd1 = bd.cursor()
bd1.execute("SELECT * FROM users")
id = bd1.fetchall()
print(f'Тип - {type(id)}')
n=1
for i in id:
    print(i)

#bd1 = bd.cursor()
bd1.execute("SELECT id FROM users")
id = bd1.fetchall()
print(f'Тип - {type(id)}')
#for i in id:
print(id[0])
#         rows = cur.fetchall()
#         for row in rows:
#             print(row[0], row[1])
#     else:
#         print("Вы ошиблись")
bd.commit()
bd.close()
