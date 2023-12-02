import mysql.connector as mycon
con=mycon.connect(host="localhost",user="root",passwd="muskan@123",database="supermarketmanagement")
cur=con.cursor()
def create():
    cur.execute("create table supermarket(PRODUCT_ID varchar(255),PRODUCT_NAME varchar(255),PRICE int,QUANTITY int);")
def add():
    while True:
        proid=int(input("ENTER THE PRODUCT ID - "))
        proname=input("ENTER THE PRODUCT NAME - ")
        price=int(input("ENTER THE PRICE OF THE PRODUCT - "))
        qua=int(input("ENTER THE QUANTITY OF THE PRODUCT - "))
        cur.execute("insert into supermarket values({},'{}',{},{})".format(proid,proname,price,qua))
        con.commit()
        print("Enter y to add more and n to leave - ")
        c=input("Enter your choice - ")
        if c=="n":
            break
def display():
    cur.execute("select* from supermarket")
    data=cur.fetchall()
    if len(data)==0:
        print ("empty")
    else :
        for i in data:
            print(i)
def search():
    proid=int(input("Enter the product id to be searched - "))
    cur.execute("select * from supermarket where PRODUCT_ID ={}".format(proid))
    x=cur.fetchall()
    if len(x)==0:
        print ("empty")
    else:
        for i in x:
            print(x)
        if cur.rowcount>0:
            print(" FOUND")
        else:
            print(" not FOUND")
def modify():
    cur.execute("select* from supermarket")
    data=cur.fetchall()
    if len(data)==0:
        print ("empty")
    else:
        proid=int(input("Enter the product id whose details have to be modified - "))
        while True:
            print("1.To modify product name.\n2. To update price of the products.\n3. To update quantity of the product.\n4. Quit")
            ch=int(input("Enter your choice = "))
            if ch==1:
                proname=input("Enter new name of the product- ")
                cur.execute("update supermarket set PRODUCT_NAME='{}' where PRODUCT_ID={}".format(proname,proid))
            if ch==2:
                price=int(input("Enter new price of product- "))
                cur.execute("update supermarket set PRICE={} where PRODUCT_ID={}".format(price,proid))
            if ch==3:
                qua=int(input("Enter the new quantity of the product - "))
                cur.execute("update supermarket set QUANTITY={} where PRODUCT_ID={}".format(qua,proid))
            if ch==4:
                break
            con.commit()
        cur.fetchall()
        if cur.rowcount==0:
            print("Not FOUND")
        else:
            print("FOUND")
def remove():
    cur.execute("select* from supermarket")
    data=cur.fetchall()
    if len(data)==0:
        print ("empty")
    else:
        proid=int(input('Enter the product id which is sold - '))
        cur.execute("delete from supermarket where PRODUCT_ID={}".format(proid))
        con.commit()
        print("deleted")
def decreasesoldquantity():
    cur.execute("select* from supermarket")
    data=cur.fetchall()
    if len(data)==0:
        print ("empty")
    else:
        proid=int(input('Enter the product id which is sold - '))
        quasold=int(input("Enter the quantity sold - "))
        cur.execute("update supermarket set QUANTITY=QUANTITY-{} where PRODUCT_ID={}".format(quasold,proid))
        con.commit()
        print("quantity changed")
while True:
    print(" 1.To create the table supermarket.\n 2.To add product details in the table.\n 3.To display all the details of the product.\n 4.To modify details of an item.\n 5.To remove an item.\n 6.To decrease the quantity of the sold product.\n 7.Quit.")
    ch=int(input("Enter your choice : "))
    if ch==1:
        create()
    elif ch==2:
        add()
    elif ch==3:
        display()
    elif ch==4:
        modify()
    elif ch==5:
        remove()
    elif ch==6:
        decreasesoldquantity()
    else:
        break
