import sqlite3
import os

def createDatabase():
    if os.path.exists("students.db"):
        os.remove("students.db") #eğer içerisinde varsa bunu silerek devam et anlamına gelmektedir burada oolsun gibi düşünerek ilerle
    conn=  sqlite3.connect("students.db")

    cursor = conn.cursor()
    return conn, cursor

def create_tables(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students(
    id integer primary key,
    name text not null,
    age integer,
    email varchar unique,
    city varchar)
    
    
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Courses(
    id integer primary key,
    course_name text not null,
    instructor text,
    credits integer)
    ''')


def insert_into_tables(cursor):
    students = [
        (1,'Alice',20,'alice@gmail.com','New York'),
        (2, 'Bob Smith', 19, 'bob@gmail.com', 'New York'),
        (3, 'Carol White', 21, 'carol@gmail.com', 'Chicago'),
        (4, 'David Brown', 20, 'david@gmail.com', 'New York'),
        (5, 'Emma Davis', 22, 'emma@gmail.com', 'Seattle'),
    ]
    cursor.executemany("INSERT INTO students VALUES (?,?,?,?,?)", students)

    courses = [
        (1, 'Python Programming', 'Dr. Anderson', 3),
        (2, 'Web Development', 'Prof. Wilson', 4),
        (3, 'Data Science', 'Dr. Taylor', 3),
        (4, 'Mobile Apps', 'Prof. Garcia', 2)
    ]

    cursor.executemany("INSERT INTO Courses VALUES (?,?,?,?)", courses)

    print("Tables inserted successfully")

def basic_sql_operations(cursor):
    # 1) SELECT ALL
    print("----------Select All----------")
    cursor.execute("SELECT * FROM Students")
    records = cursor.fetchall()
    for row in records:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Email: {row[3]}, City: {row[4]}")

    # 2) SELECT Columns
    print("----------Select Columns----------")
    cursor.execute("SELECT name, age FROM Students")
    records = cursor.fetchall()
    print(records)

    # 3) WHERE clause
    print("----------Where Age = 20 ----------")
    cursor.execute("SELECT * FROM Students WHERE age = 20")
    records = cursor.fetchall()
    for row in records:
        print(row)

    # 4) WHERE with string
    print("----------Where city = New York ----------")
    cursor.execute("SELECT * FROM Students WHERE city = 'New York'")
    records = cursor.fetchall()
    for row in records:
        print(row)

    # 5) ORDER BY
    print("----------Order by age ----------")
    cursor.execute("SELECT * FROM Students ORDER BY age")
    records = cursor.fetchall()
    for row in records:
        print(row)

    # 6) LIMIT
    print("----------Limit by 3 ----------")
    cursor.execute("SELECT * FROM Students LIMIT 3")
    records = cursor.fetchall()
    for row in records:
        print(row)


def sql_update_delete_insert_operations(conn,cursor):
    # 1) Insert
    cursor.execute("INSERT INTO Students VALUES (6, 'Frank Miller', 23, 'frank@gmail.com','Miami')")
    conn.commit()

    # 2) UPDATE
    cursor.execute("UPDATE Students SET age = 24 WHERE id = 6")
    conn.commit()

    # 3) DELETE
    cursor.execute("DELETE FROM Students WHERE id = 6")
    conn.commit()

def aggregate_funcitons(cursor):
    #Conunt
    print("----------Aggregate Functions----------")
    cursor.execute("Select Count(*) from Students")
    result = cursor.fetchall() #Burada bana tuple list dnmekkedtir bir altta bende bunu tupple içerisinden çıkarıyorum
    print(result[0][0])

    #Avarage
    cursor.execute("Select AVG(age) from Students")
    result = cursor.fetchall()
    print(result[0][0])

    #Max-Min
    cursor.execute("Select max(age),min(age) from Students")
    result = cursor.fetchall()
    print(result[0])

    #GroupBy
    cursor.execute("Select city, count(*) from Students group by city")
    result = cursor.fetchall()
    print(result)

def main():
    conn, cursor = createDatabase()
    try:
        create_tables(cursor)
        insert_into_tables(cursor)
        basic_sql_operations(cursor)
        sql_update_delete_insert_operations(conn,cursor)
        aggregate_funcitons(cursor)
        conn.commit()
    except sqlite3.OperationalError as e:
        print(e)
    finally:
        conn.close()

if __name__ == "__main__":
    main()