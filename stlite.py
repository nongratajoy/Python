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
def show():
    cursor.execute("SELECT * FROM workers")
    print(cursor.fetchall())
def limittask1():
    cursor.execute("SELECT * FROM workers LIMIT 6")
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
def selecttask1():
    cursor.execute("SELECT name FROM workers WHERE id = 7")
    print(cursor.fetchall())
def selecttask5():
    cursor.execute("SELECT * FROM workers WHERE salary <= 1000")
    print(cursor.fetchall())
def orandtask1():
    cursor.execute("SELECT * FROM workers WHERE (age > 17 AND age <= 19)")
    print(cursor.fetchall())
def orandtask3():
    cursor.execute("SELECT * FROM workers WHERE (name = 'Анюша') OR (name = 'Ладюша')")
    print(cursor.fetchall())
def orandtask6():
    cursor.execute("SELECT * FROM workers WHERE (age >= 17 AND age < 19) OR (salary = 1000)")
    print(cursor.fetchall())
def orandtask8():
    cursor.execute("SELECT * FROM workers WHERE age = 19 OR salary != 1000")
    print(cursor.fetchall())
def inserttask1():
    cursor.execute("INSERT INTO workers (name, age, salary) VALUES ('Никита', 26, 300)")
    print(cursor.fetchall())
p = [("Ярослав", 1200, 30), ("Петр", 1000, 31)]
def inserttask3():
    cursor.executemany("INSERT INTO workers (name, salary, age) VALUES (?, ?, ?)", p)
def deletetask1():
    cursor.execute("DELETE FROM workers WHERE id = ?", ("7",))
def deletetask3():
    cursor.execute("DELETE FROM workers WHERE age = ?", ("18",))

def updatetask1():
    cursor.execute("UPDATE workers SET age = 19 WHERE name = 'Ладюша'")

def updatetask3():
    cursor.execute("UPDATE workers SET salary = 700 WHERE salary = 500")
def updatetask5():
    cursor.execute("UPDATE workers SET name = 'Лада' WHERE name = 'Ладюша'")
def intask5():
    cursor.execute("UPDATE workers SET name = 'Лада' WHERE name = 'Ладюша'")
def astask1():
    cursor.execute("SELECT id AS userid, name AS username, salary AS usersalary FROM workers")
    print(cursor.fetchall())
def distincttask1():
    cursor.execute("SELECT DISTINCT salary FROM workers")
    print(cursor.fetchall())
def avgtask1():
    cursor.execute("SELECT AVG(salary) FROM workers")
    print(cursor.fetchone())
def avgtask2():
    cursor.execute("SELECT AVG(age) FROM workers")
    print(cursor.fetchone())
def concattask1():
    cursor.execute("SELECT salary || '-' || age AS res FROM workers")
    print(cursor.fetchall())
def groupbytask1():
    cursor.execute("SELECT age, MIN(salary) AS min_salary FROM workers GROUP BY age")
    results = cursor.fetchall()
    for row in results:
        print("Age:", row[0], "- Min Salary:", row[1])
def groupconcattask1():
    cursor.execute("""
    SELECT age, GROUP_CONCAT(id, '-') AS res
    FROM workers
    GROUP BY age
    """)
    results = cursor.fetchall()
    for row in results:
        print("Age:", row[0], "- Res:", row[1])
groupconcattask1()
#show()
con.close()