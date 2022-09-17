# FIRST I CAN INSTALL MYSQL PACKAGE WITH PIP INSTALL MYSQL
import mysql.connector
mydb=mysql.connector.connect(

    #LOCAL HOST 
    host="localhost",
    user="root",
    password="root",
    #DATABASE NAME IS ATM
    database="atm" 

 )

#INSERT DATA FUNCTION IS USE TO CREATE AN USER ACCOUNT 

def insertdata(id,name,passwordd,deposit):
    res=mydb.cursor()
    sql="insert into userac(id,name,passwordd,balance) value(%s,%s,%s,%s)"
    users=(id,name,passwordd,deposit)
    res.execute(sql,users)
    mydb.commit()

#UPDATE FUNCTION IS USE TO WHEN USER CHANGE SOME DETAIL IT WILL STORE WITH HELP OF UPDATE FUNCTION
def update(deposit,id,passwordd):
    res=mydb.cursor()
    sql="update userac set balance=%s where id=%s and passwordd=%s"
    users=(deposit,id,passwordd)
    res.execute(sql,users)
    mydb.commit()

#DEPOSIT FUNCTION IS USE TO ADD AMOUNT TO THE BALANCE

def deposit(amt,id,passwordd):
    res=mydb.cursor()
    sql="update userac set balance=balance+%s where id=%s and passwordd=%s"
    users=(amt,id,passwordd)
    res.execute(sql,users)
    mydb.commit()

#WITHDRAW FUNCTION IS USE TO WHEN THE USER WITHDRAW MONEY WILL UPDATED BY THE DATABASE

def withdraw(amt,id,passwordd):
    res=mydb.cursor()
    sql="update userac set balance=balance-%s where id=%s and passwordd=%s"
    users=(amt,id,passwordd)
    res.execute(sql,users)
    mydb.commit()

#CURRENT BALANCE FUNCTION IS USE TO SHOWN THE CURRENT BALANCE IN THE CUSTOMER ACCOUNT
def currentbalance(id,passwordd):
    res=mydb.cursor()
    sql="select balance from userac where id=%s and passwordd=%s"
    users=(id,passwordd)
    res.execute(sql,users)
    r=res.fetchall()
    print(r)
   
#CREATING ACCOUNT OR REGESTRATION
user=int(input("IF YOU ARE NEW USER PRESS 1 OLD USER PRESS 2: "))

#CHECKING ID AND PASSWORD

if user==1:
    id=input("ENTER YOUR ID:")
    name=input("ENTER YOUR NAME:")
    passwordd=input("ENTER YOUR PASSWORD: ")
    deposit=input("ENTER YOUR DEPOSIT AMT:")    
    insertdata(id,name,passwordd,deposit)

elif user==2:
    id=input("ENTER YOUR ID:")
    passwordd=input("ENTER YOUR PASSWORD: ")
    
    #INFINITI LOOP
    while True:
        temp=int (input("DEPOSIT PRESS 1\nWITHDRAW PRESS 2\nVIEW BALANCE PRESS 3\n"))
    
        #HERE I CAN USE IF STATEMENT WITH 3 MAJOR CONDITIONS
        #DEPOSIT
        # WITHDRAW
        # CURRENT BALANCE

        # NO 1 IS WHEN USER WANT TO DEPOSIT THEY CAN PRESS ONE      
        if temp==1:
            print("you are select deposit")
            depositamt=(input("enter your amt to deposit: "))
            deposit(depositamt,id,passwordd)
    
        #NO 2 IS WHEN USER WANT TO WITHDRAW THEY CAN PRESS TWO
        elif temp==2:
            print("you are select withdraw")
            wamt=(input("enter your amt to withdraw: "))
            withdraw(wamt,id,passwordd)
        #NO 3 IS WHEN USER WANT TO SHOW THERE BANK CURRENT THEY PRESS THREE    
        elif temp==3:

            print("YOUR CURRENT BALANCE IS")
            currentbalance(id,passwordd)
    
        #NO 0 IS TO EXIT WHEN USER PRESS ZEOR THE INFINITI LOOP IS TERMINITED
        elif temp==0:
            break
        #INVALID INPUT
        else:
            print("INVALID INPUT")

   