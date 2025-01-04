import mysql.connector as sqltor

def table9():
    print("Creating table for class 9")
    sql1 = '''
    CREATE TABLE IF NOT EXISTS STUDENT9 (
        Blrno varchar(20) PRIMARY KEY NOT NULL,
        name varchar(25) NOT NULL,
        section char(5),
        eng int,
        math int,
        science int,
        sst int,
        comp int,
        2ndlang int
    )
    '''
    cursor.execute(sql1)
    print("Table created successfully")
    ans = input("Do you want to view the structure of the table? (Yes/No): ")
    while ans.lower() == "yes":
        cursor.execute('DESCRIBE STUDENT9')
        row = cursor.fetchall()
        print("Column  Datatype  Null  Key  Default  Extra")
        for c in row:
            print(f"{c[0]}  {c[1]}  {c[2]}  {c[3]}  {c[4]}  {c[5]}")
        ans = "Stop"

def table10():
    print("Creating table for class 10")
    sql2 = '''
    CREATE TABLE IF NOT EXISTS STUDENT10 (
        Blrno varchar(20) PRIMARY KEY NOT NULL,
        name varchar(25) NOT NULL,
        section char(5),
        eng int,
        math int,
        science int,
        sst int,
        comp int,
        2ndlang int
    )
    '''
    cursor.execute(sql2)
    print("Table created successfully")
    ans = input("Do you want to view the structure of the table? (Yes/No): ")
    while ans.lower() == "yes":
        cursor.execute('DESCRIBE STUDENT10')
        row = cursor.fetchall()
        print("Column  Datatype  Null  Key  Default  Extra")
        for c in row:
            print(f"{c[0]}  {c[1]}  {c[2]}  {c[3]}  {c[4]}  {c[5]}")
        ans = "Stop"

def insert9():
    print("Please enter details for class 9")
    a = input('Enter Blrno: ')
    b = input('Enter name: ')
    c = input('Enter section: ')
    d = int(input('Enter English marks: '))
    e = int(input('Enter Math marks: '))
    f = int(input("Enter Science marks: "))
    g = int(input('Enter SST marks: '))
    h = int(input('Enter Computer marks: '))
    i = int(input('Enter 2nd language marks: '))
    query = f"INSERT INTO STUDENT9 VALUES ('{a}', '{b}', '{c}', {d}, {e}, {f}, {g}, {h}, {i})"
    cursor.execute(query)
    mycon.commit()

def insert10():
    print("Please enter details for class 10")
    a = input('Enter Blrno: ')
    b = input('Enter name: ')
    c = input('Enter section: ')
    d = int(input('Enter English marks: '))
    e = int(input('Enter Math marks: '))
    f = int(input("Enter Science marks: "))
    g = int(input('Enter SST marks: '))
    h = int(input('Enter Computer marks: '))
    i = int(input('Enter 2nd language marks: '))
    query = f"INSERT INTO STUDENT10 VALUES ('{a}', '{b}', '{c}', {d}, {e}, {f}, {g}, {h}, {i})"
    cursor.execute(query)
    mycon.commit()

def report(n):
    print("YOUR DETAILED REPORT IS AS FOLLOWS :P\n")
    avg1 = avg9()
    avg2 = avg10()
    grt9 = greatest9()
    grt10 = greatest10()
    lst_fin = []
    for i in range(n):
        b = grt9[i]
        c = grt10[i]
        b.append(avg1[i])
        c.append(avg2[i])
        b.extend(c)
        lst_fin.append(b)
    return lst_fin

# Main Program
mycon = sqltor.connect(host="localhost", user="root", passwd="root123", database="project")
cursor = mycon.cursor()

print("Welcome to the Stream Identifier!")
n = int(input("Enter the number of times you would like to try: "))

cursor.execute("DROP TABLE IF EXISTS STUDENT9")
cursor.execute("DROP TABLE IF EXISTS STUDENT10")
table9()
table10()

for i in range(n):
    insert9()
    insert10()

final_report = report(n)
print("\nFINAL REPORT")
print("-" * 80)
print("NAME    HIGHEST IN 9TH    AVG IN 9TH    STREAM1    HIGHEST IN 10TH    AVG IN 10TH    STREAM2")
for entry in final_report:
    print(entry)

print("\nThank you for using the Stream Predictor!")
