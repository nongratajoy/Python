import sqlite3;
con = sqlite3.connect("DB.db")
cursor = con.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS workers 
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                salary INTEGER)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS pages 
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                surname TEXT,
                name TEXT,
                article TEXT)''')
people = [("Ладюша", 18, 400), ("Дилярушка", 17, 500), ("Лейладжон", 14, 500), ("Аделинаджон", 16, 1000),
          ("Элинушка", 19, 500), ("Анюша", 15, 1000), ("Эльзахон", 17, 2000),
          ("Амалишка", 18, 1700), ("Сонюша", 16, 2540), ("Каринушка", 16, 1890),
          ("Луизахон", 18, 2570), ("Настюша (Шеф)", 14, 1698), ("Иделиябону", 19, 2578)]
cursor.executemany("INSERT INTO workers (name, age, salary) VALUES (?, ?, ?)", people)
authors = [("Архипов", "Артем", "В своей статье рассказывает о машинах."),
           ("Бабаджанов", "Камолджон", "Написал статью об инфляции."),
           ("Веткин", "Даниил", "Придумал новый химический элемент."),
           ("Коснырев", "Лев", "Также писал о машинах."),
           ("Низамов", "Ильнар", "Написал статью о том, как разрабатывать элементы дизайна."),
           ("Мубаракшин", "Булат", "Написал статью о своей девушке."),
           ("Трифонов", "Илья", "Также писал о девушке")]
cursor.executemany("INSERT INTO pages (surname, name, article) VALUES (?, ?, ?)", authors)
def limittask1():
    cursor.execute("SELECT * FROM pages LIMIT 6")
    print(cursor.fetchall())
def limittask2():
    cursor.execute("SELECT * FROM workers LIMIT 3 OFFSET 1")
    print(cursor.fetchall())
def orderbytask1():
    cursor.execute("SELECT * FROM workers ORDER BY salary")
    print(cursor.fetchall())
def orderbytask2():
    cursor.execute("SELECT * FROM workers ORDER BY salary DESC")
    print(cursor.fetchall())
def orderbytask3():
    cursor.execute("SELECT  * FROM workers WHERE id>=2 AND id<=6 "
                   "ORDER BY age")
    print(cursor.fetchall())
def counttask1():
    cursor.execute("SELECT COUNT (*) FROM workers")
    print(cursor.fetchone())
def counttask2():
    cursor.execute("SELECT COUNT (*) FROM workers WHERE salary > 1000")
    print(cursor.fetchone())
def liketask1():
    cursor.execute("SELECT * FROM pages WHERE surname LIKE '%ов'")
    print(cursor.fetchall())
def liketask2():
    cursor.execute("SELECT * FROM pages WHERE article LIKE '%элемент%'")
    print(cursor.fetchall())
def liketask3():
    cursor.execute("SELECT * FROM workers WHERE age LIKE '1%'")
    print(cursor.fetchall())
def liketask4():
    cursor.execute("SELECT * FROM workers WHERE name LIKE 'Л%'")
    print(cursor.fetchall())
liketask4()
con.close()