import sqlite3
from sqlite3 import Error

# Соединение с БД
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

# Создание таблиц в инициализированной бд
def create_table(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

bd = create_connection('test.db')

# Добавление данных в таблицу в инициализированной бд
def insert_in_table(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

# команда для создания таблицы user в базе данных
user_table ="""
      CREATE TABLE IF NOT EXISTS users(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      patronymic TEXT NOT NULL,
      name TEXT NOT NULL,
      soname TEXT NOT NULL,
      age INTEGER,
      gender TEXT,
      nationality TEXT
      );"""

# команда для создания таблицы phone в базе данных
phone_table = """
      CREATE TABLE IF NOT EXISTS phone(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      phone integer NOT NULL,
      commit TEXT NOT NULL
      user_id INTEGER NOT NULL, 
      FOREIGN KEY (user_id) REFERENCES users (id)
      );"""

create_table(bd,user_table)
create_table(bd,phone_table)

insert=[]
soname = input('Введите имя - ')
name = input('Введите фамилию - ')
patronymic = input('Введите отчество - ')


    # if choice == 1:
    #     name = input("Name\n> ")
    #     surname = input("Surname\n> ")
    #     cur.execute(f"INSERT INTO `test` VALUES ('{name}', '{surname}')")
    # elif choice == 2:
    #     cur.execute("SELECT * FROM `test`")
    #     rows = cur.fetchall()
    #     for row in rows:
    #         print(row[0], row[1])
    # else:
    #     print("Вы ошиблись")

bd.commit()
bd.close()
