# stream-predictor
def table9():
    print("Creating table for class 9")
    sql1=('''CREATE TABLE IF NOT EXISTS STUDENT9
          (Blrno varchar(20) primary key not null,
          name varchar (25) not null,
          section char(5),
          eng int,
          math int,
          science int,
          sst int,
          comp int,
          2ndlang int)''')
    cursor.execute(sql1)
    print("Table created successfully")
    ans=input("Do you want to view the structure of the table?? (Yes/No)")
    while ans=="Yes":
        cursor.execute('''describe STUDENT9''')
        row = cursor.fetchall()
        print("Column","   ","Datatype","   ","Null","   ","Key","   ","Default","   ","Extra")
        for c in row:
            print(c[0],"   ",c[1],"   ",c[2],"   ",c[3],"   ",c[4],"   ",c[5])
        ans="Stop"
def table10():
    print("Creating table for class 10")
    sql2=('''CREATE TABLE IF NOT EXISTS STUDENT10
          (Blrno varchar(20) primary key not null,
          name varchar (25) not null,
          section char(5),
          eng int,
          math int,
          science int,
          sst int,
          comp int,
          2ndlang int)''')
    cursor.execute(sql2)
    print("Table created successfully")
    ans=input("Do you want to view the structure of the table?? (Yes/No)")
    while ans=="Yes":
        cursor.execute('''describe STUDENT10''')
        row = cursor.fetchall()
        print("Column","   ","Datatype","   ","Null","   ","Key","   ","Default","   ","Extra")
        for c in row:
            print(c[0],"   ",c[1],"   ",c[2],"   ",c[3],"   ",c[4],"   ",c[5])
        ans="Stop"
def insert9():
    print("Please enter details for class 9")
    a=input('Enter Blrno.')
    b=input('Enter name')
    c=input('Enter section')
    d=int(input('Enter English marks'))
    e=int(input('Enter Math marks'))
    f= int(input("Enter Science marks"))
    g = int(input('Enter SST marks'))
    h = int(input('Enter Computer marks'))
    i=int(input('Enter 2nd lang marks'))
    query="INSERT INTO STUDENT9 VALUES ('{Blrno}','{name}','{section}',{english},{math},{science},{sst},{computer},{lang})".format(Blrno=a,name=b,section=c,english=d,math=e,science=f,sst=g,computer=h,lang=i)
    cursor.execute(query)
    mycon.commit()
def insert10():
    print("Please enter details for class 10")
    a=input('Enter Blrno.')
    b=input('Enter name')
    c=input('Enter section')
    d=int(input('Enter English marks'))
    e=int(input('Enter Math marks'))
    f= int(input("Enter Science marks"))
    g = int(input('Enter SST marks'))
    h = int(input('Enter Computer marks'))
    i=int(input('Enter 2nd lang marks'))
    query="INSERT INTO STUDENT10 VALUES ('{Blrno}','{name}','{section}',{english},{math},{science},{sst},{computer},{lang})".format(Blrno=a,name=b,section=c,english=d,math=e,science=f,sst=g,computer=h,lang=i)
    cursor.execute(query)
    mycon.commit()

def report(n):
    print("YOUR DETAILED REPORT IS AS FOLLOWS :P")
    print("\n")
    def avg9():     
        cursor.execute("select name,eng,math,science,sst,comp,2ndlang from STUDENT9")
        mydata1=cursor.fetchall()
        data1=list(mydata1)
        l1=[]
        for i in data1:
            avg1=((i[1]+i[2]+i[3]+i[4]+i[5]+i[6])//6) 
            print("Average score of",i[0],"in class 9 is",avg1)
            l1.append(str(avg1))
            print("\n")
        return l1
    def avg10():
        cursor.execute("select name,eng,math,science,sst,comp,2ndlang from STUDENT10")
        mydata2=cursor.fetchall()
        data2=list(mydata2)
        l2=[]
        for i in data2:
            avg2=((i[1]+i[2]+i[3]+i[4]+i[5]+i[6])//6) 
            print("Average score of",i[0],"in class 10 is",avg2)
            l2.append(str(avg2))
            print("\n")
        return l2
    def greatest9():
        cursor.execute("select name,eng,math,science,sst,comp,2ndlang from STUDENT9")
        mydata1=cursor.fetchall()
        l1=list(mydata1)
        k=0
        lst1=[]
        for i in l1:
            j=list(i)
            name=j.pop(0)
            j.sort()
            length1=len(j)
            grt1=j[length1-1]
            if grt1==mydata1[k][1]:
                sub1="English"
                stream1="Arts"
            elif grt1==mydata1[k][2]:
                sub1="Mathematics"
                stream1="Commerce"
            elif grt1==mydata1[k][3]:
                sub1="Science"
                stream1="science"
            elif grt1==mydata1[k][4]:
                sub1="Social Studies"
                stream1="Arts"
            elif grt1==mydata1[k][5]:
                sub1="Computer Science"
                stream1="Science"
            elif grt1==mydata1[k][6]:
                sub1="2nd Language"
                stream1="Arts"
            k+=1
            print("Highest marks scored by",name,"in class 9 is",grt1,"in",sub1)
            print("Your suggested preference can be:",stream1)
            print("\n")
            lst0=[name,str(grt1),stream1]
            lst1.append(lst0)
        return lst1
    def greatest10():
        cursor.execute("select name,eng,math,science,sst,comp,2ndlang from STUDENT10")
        mydata2=cursor.fetchall()
        l2=list(mydata2)
        k=0
        lst2=[]
        for i in l2:
            j=list(i)
            name=j.pop(0)
            j.sort()
            length2=len(j)
            grt2=j[length2-1]
            if grt2==mydata2[k][1]:
                sub2="English"
                stream2="Arts"
            elif grt2==mydata2[k][2]:
                sub2="Mathematics"
                stream2="Commerce"
            elif grt2==mydata2[k][3]:
                sub2="Science"
                stream2="Science"
            elif grt2==mydata2[k][4]:
                sub2="Social Studies"
                stream2="Arts"
            elif grt2==mydata2[k][5]:
                sub2="Computer Science"
                stream2="Science"
            elif grt2==mydata2[k][6]:
                sub2="2nd Language"
                stream2="Arts"
            k+=1
            print("Highest marks scored by",name,"in class 10 is",grt2,"in",sub2)
            print("Your suggested second preference can be:",stream2)
            print("\n")
            lst0=[str(grt2),stream2]
            lst2.append(lst0)
        return lst2
    avg1=avg9()
    print("\n")
    avg2=avg10()
    print("\n")
    grt9=greatest9()
    print("\n")
    grt10=greatest10()
    lst_fin=[]
    for i in range(n):
        a=avg1[i]
        b=grt9[i]
        b.insert(2,a)
        c=grt10[i]
        d=avg2[i]
        c.insert(1,d)
        b.extend(c)
        lst_fin.append(b)
    return lst_fin
    
        
#_main_

import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="root123",database="project")
cursor=mycon.cursor()
print("Welcome to stream identifier")
print("You are required to enter class 9 and 10 marks in various subjects and we will help you find the perfect stream for you!!!!")
print("\n")
n=int(input("Enter no.of times you would like to try"))
cursor.execute("drop table student9")
cursor.execute("drop table student10")
table9()
print("\n")
table10()
print("\n")
for i in range(n):
    insert9()
    print("---------------------------------------------------------------------------------------")
    insert10()
    print("---------------------------------------------------------------------------------------")



list1=report(n)
print("\n")
print("\n")
print("\n")


print("FINAL REPORT")
print("---------------------------------------------------------------------------------------------------------------------------------------")
print("NAME"," "*10,"HIGHEST IN 9TH"," "*10,"AVERAGE IN 9TH"," "*10,"PREDICTED STREAM1"," "*10,"HIGHEST IN 10TH"," "*10,"AVERAGE IN 10TH"," "*10,"PREDICTED STREAM2")
for i in list1:
    print(i[0]," "*(14-len(i[0])),i[1]," "*(24-len(i[1])),i[2]," "*(24-len(i[2])),i[3]," "*(27-len(i[3])),i[4]," "*(24-len(i[4])),i[5]," "*(24-len(i[5])),i[6]," "*(27-len(i[6])))


print("\n")
print("According to the machine's understanding and the code, upon detailed analysis your suggested streams are recommended above")
print("""Choose these streams only if you are passionate about them.
       If you make the right decision life is hard enough,but if you make wrong ones, life gets even harder.""")
print("ALL THE BEST :D")
print("\n")
print("THANKYOU FOR USING THE STREAM PREDICTOR.WE HOPE IT WAS HELPFUL!!")
