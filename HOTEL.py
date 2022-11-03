import datetime 
def database():
    import mysql.connector as ms
    my=ms.connect(host="localhost",user="root",password="")
    cur=my.cursor()
    cur.execute("create database if not exists HOTEL")
    print("Database Hotel Created sucessfuly!!")
database()

def create_customer_details():
    import mysql.connector as ms
    my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
    con=my.cursor()
    con.execute("create table if not exists Customer_Details(Code int(3) PRIMARY KEY,Destination varchar(25),First_Name varchar(25),\
                Last_Name varchar(25),Mobile_No bigint(10),Email_ID varchar(25),Country varchar(25))")
    print("Table Customer_Deatils Created sucessfuly!!")

def create_service_details():
    import mysql.connector as ms
    my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
    con=my.cursor()
    con.execute("create table if not exists Service_Details(Code int(3) PRIMARY KEY,Destination varchar(25),Checkin date,Checkout date,\
                Number_of_Adults int(2),Numer_Of_Children int(2), Room_Type varchar(15),No_Of_Rooms int(3), Special_Requests varchar(30))")
    print("Table Service_Deatils Created sucessfuly!!")

def create_payment_details():
    import mysql.connector as ms
    my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
    con=my.cursor()
    con.execute("create table if not exists Payment_Details(Code int(3) PRIMARY KEY,Amount int(5), Mode_Of_Payment varchar(15),\
                Credit_card_Number varchar(16))")
    print("Table Payment_Deatils Created sucessfuly!!")    

def create_room_types():
    import mysql.connector as ms
    my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
    con=my.cursor()
    con.execute("create table if not exists Room_Types(SNO int(3),Room_Type varchar(25), Charges_per_night int(10))")
    my.commit()
    my.close()   
    print("Table Room_Types Created sucessfuly!!")

def insert_into_room_Types():
    import mysql.connector as ms
    my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
    con=my.cursor()
    con.execute("insert into Room_Types(SNO,Room_Type,Charges_per_night) values(1,'Deluxe Room',7600)")   
    con.execute("insert into Room_Types(SNO,Room_Type,Charges_per_night) values(2,'Classic Room',7000)")
    con.execute("insert into Room_Types(SNO,Room_Type,Charges_per_night) values(3,'Suite',13000)")
    my.commit()
    my.close()    
#insert_into_room_Types()

def create_restaurant():
    import mysql.connector as ms
    my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
    con=my.cursor()
    con.execute("create table if not exists Restaurant(SNO int(3),Menu varchar(25), Price int(10))")
    print("Table Restaurant Created sucessfuly!!")
    con.execute("create table if not exists Restaurant_Booking(Code int(3),Menu varchar(25),Plates int(10), Amount int(10))")
    print("Table Restaurant_Booking Created sucessfuly!!") 

def insert_into_restaurant():
    import mysql.connector as ms
    my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
    con=my.cursor()
    con.execute("insert into Restaurant(SNO,Menu,Price) values(1,'Maggi',50)")   
    con.execute("insert into Restaurant(SNO,Menu,Price) values(2,'Stuffed Sandwich',70)")
    con.execute("insert into Restaurant(SNO,Menu,Price) values(3,'Veg.Momos',80)")
    con.execute("insert into Restaurant(SNO,Menu,Price) values(4,'Spring Roll',70)")
    con.execute("insert into Restaurant(SNO,Menu,Price) values(5,'Chilli Potatoes',80)")
    my.commit()
    my.close()
#insert_into_restaurant()

def create_spa():
    import mysql.connector as ms
    my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
    con=my.cursor()
    con.execute("create table if not exists Spa(SNO int(3),Package_Name varchar(25),Duration varchar(25), Price int(10))")
    print("Table Spa Created sucessfuly!!")
    con.execute("create table if not exists Spa_Booking(Code int(3),Package_Name varchar(25),No_Of_People int(10), Amount int(10))")
    print("Table Spa_Booking Created sucessfuly!!")    
#create_spa()

def insert_into_spa():
    import mysql.connector as ms
    my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
    con=my.cursor()
    con.execute("insert into Spa(SNO,Package_Name,Duration,Price) values(1,'Deep Relaxation Package','1 hr 30 min',3900)")   
    con.execute("insert into Spa(SNO,Package_Name,Duration,Price) values(2,'Home Makers Package','1 hr 30 min',3800)")
    con.execute("insert into Spa(SNO,Package_Name,Duration,Price) values(3,'Ayurvedic Wisdom','1 hr 45 min',4750)")
    my.commit()
    my.close()  
#insert_into_spa()

def show_restaurant():
    import mysql.connector as ms
    my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
    con=my.cursor()
    con.execute("SELECT*FROM Restaurant")
    data=con.fetchall()
    print("+----+-------------------+-----+")
    print("┊SNO","┊       MENU       ","┊PRICE┊")
    print("+----+-------------------+-----+")
    for i in data:
        print("┊",i[0]," ┊",i[1]," "*(16-len(str(i[1]))),"┊",i[2]," ┊")
    print("+----+-------------------+-----+")
    ORDER=[]
    while True:
        spa=input("WOULD YOU LIKE TO ORDER SOMETHING?(Y/N): ")
        if spa.upper()=="N":
            break
        elif spa.upper()=="Y":
            codes=[]
            while True:
                import mysql.connector as ms
                my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
                con=my.cursor()
                con.execute("SELECT CODE FROM Customer_Details")
                data=con.fetchall()
                for i in data:
                    codes.append(i[0])
                while True:
                    try:
                        code_res=int(input("ENTER THE CODE: "))
                        if code_res not in codes:
                            print("No such entry exists!!")
                        else:
                            ORDER.append(code_res)
                            while True:
                                res_choice=int(input("ENTER SERIAL NUMBER OF YOUR CHOICE: "))
                                if res_choice not in [1,2,3,4,5]:
                                    print("Enter correct value!")
                                else:
                                    if res_choice==1:
                                        res_choice="MAGGI"
                                        rate=50
                                        ORDER.append(res_choice)
                                        break
                                    elif res_choice==2:
                                        res_choice="STUFFED SANDWICH"
                                        rate=70
                                        ORDER.append(res_choice)     
                                        break
                                    elif res_choice==3:
                                        res_choice="VEG.MOMOS"
                                        rate=80
                                        ORDER.append(res_choice)
                                        break
                                    elif res_choice==4:
                                        res_choice="SPRING ROLL"
                                        rate=70
                                        ORDER.append(res_choice)
                                        break
                                    elif res_choice==5:
                                        res_choice="CHILLI POTATOES"
                                        rate=80
                                        ORDER.append(res_choice)
                                        break
                            while True:
                                try:
                                    plates=int(input("NO OF PLATES: "))
                                    ORDER.append(plates)
                                    amount=rate*plates
                                    ORDER.append(amount)
                                    break         
                                except ValueError:
                                    print("Enter correct value!")
                            sql="INSERT INTO Restaurant_Booking(Code, Menu, Plates, Amount) VALUES (%s,%s,%s,%s)"
                            res1=(ORDER)
                            con.execute(sql,res1)
                            my.commit()
                            break
                    except ValueError:
                        print("Enter correct value!!")
                break
            break
        else:
            print("Enter correct value!")            

def show_spa():
    import mysql.connector as ms
    my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
    con=my.cursor()
    con.execute("SELECT*FROM Spa")
    data=con.fetchall()
    print("+----+---------------------------+-------------+------+")
    print("┊SNO","┊       PACKAGE NAME        ┊","   DURATION","┊PRICE ┊")
    print("+----+---------------------------+-------------+------+")
    for i in data:
        print("┊",i[0]," ┊",i[1]," "*(24-len(str(i[1]))),"┊",i[2],"┊",i[3],"┊")
    print("+----+---------------------------+-------------+------+")
    SPA=[]
    while True:
        spa=input("WOULD YOU LIKE TO BOOK A SPA SESSION?(Y/N): ")
        if spa.upper()=="N":
            break
        elif spa.upper()=="Y":
            while True:
                codes=[]
                import mysql.connector as ms
                my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
                con=my.cursor()
                con.execute("SELECT CODE FROM Customer_Details")
                data=con.fetchall()
                for i in data:
                    codes.append(i[0])
                while True:
                    try:
                        code_spa=int(input("ENTER THE CODE: "))
                        if code_spa not in codes:
                            print("No such entry exists!!")
                        else:
                            SPA.append(code_spa)
                            while True:
                                try:
                                    spa_choice=int(input("ENTER SERIAL NUMBER OF THE SPA PACKAGE: "))
                                    if spa_choice not in [1,2,3]:
                                        print("Enter correct value!")
                                    else:
                                        if spa_choice==1:
                                            spa_choice="DEEP RELAXATION PACKAGE"
                                            rate=3900
                                            SPA.append(spa_choice)
                                            break
                                        elif spa_choice==2:
                                            spa_choice="HOME MAKERS PACKAGE"
                                            rate=3800
                                            SPA.append(spa_choice)
                                            break
                                        else:
                                            spa_choice="AYURVEDIC WISDOM PACKAGE"
                                            rate=4750
                                            SPA.append(spa_choice)
                                            break
                                except ValueError:
                                    print("Enter correct value!!..")
                            while True:
                                try:
                                    spa_people=int(input("NO OF PEOPLE: "))
                                    SPA.append(spa_people)
                                    amount=rate*spa_people
                                    SPA.append(amount)
                                    break
                                except ValueError:
                                    print("Enter correct value!")
                            sql="INSERT INTO Spa_Booking(Code, Package_Name, No_Of_People, Amount) VALUES (%s,%s,%s,%s)"
                            spa1=(SPA)
                            con.execute(sql,spa1)
                            my.commit()
                            break
                    except ValueError:
                        print("Enter correct value!!")
                break 
            break
        else:
            print("Enter correct value!")            

def show_room_types():
    import mysql.connector as ms
    my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
    con=my.cursor()
    con.execute("SELECT*FROM Room_Types")
    data=con.fetchall()
    print("+----+-------------------------+-------------------+")
    print("┊SNO","┊       ROOM TYPES       ","┊ CHARGES PER NIGHT ┊")
    print("+----+-------------------------+-------------------+")
    for i in data:
        print("┊",i[0]," ┊",i[1]," "*(22-len(str(i[1]))),"┊",i[2]," "*(16-len(str(i[2]))),"┊")
    print("+----+-------------------------+-------------------+")  

def enter_values():
    C=[]
    S=[]
    P=[]
    #Code
    import mysql.connector as ms
    my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
    con=my.cursor()
    con.execute("SELECT CODE FROM Customer_Details")
    data=con.fetchall()
    import random
    while True:
        code=random.randint(100, 999)
        if code not in data:
            break
    C.append(code)
    S.append(code)
    P.append(code)
    print(" ")
    print("                     **********************************************************************")
    print("                                                 𝓒𝓾𝓼𝓽𝓸𝓶𝓮𝓻 𝓓𝓮𝓽𝓪𝓲𝓵𝓼")
    def customer_details():
        #Destination
        options=["MANALI","NAINITAL","DARJEILING","SHIMLA","OOTY","RANIKHET","MUSSORIE","LADAKH","AULI","SRINAGAR","GULMARG"]
        print("We have hotels at the following hill sations:\n"
              "MANALI","                        NAINITAL\n"
              "DARJEILING","                    SHIMLA\n"
              "OOTY","                          RANIKHET\n"
              "MUSSORIE","                      LADAKH\n"
              "AULI","                          SRINAGAR\n"
              "GULMARG")
        while True:
            destination=input("ENTER PLACE YOU WANT TO VISIT: ")
            if destination.upper() in options:
                C.append(destination.upper())
                S.append(destination.upper())
                break
            else:
                print("We do not have hotels in",destination)
                continue
            
            
            
        #First Name
        while True:
             first_name=input("ENTER FIRST NAME: ")
             if first_name.isalpha()==True:
                 C.append(first_name.upper())
                 break
             else:
                 print("Enter correct name!")
                 continue
                
                
                
        #Last Name
        while True:
            last_name=input("ENTER LAST NAME: ")
            if last_name.isalpha()==True:
                C.append(last_name.upper())
                break
            else:
                print("Enter correct name!")
                continue
                    
                    
        #Mobile Number
        while True:
            mobile_number=input("ENTER MOBILE NUMBER: ")
            if mobile_number.isdigit()==True and len(mobile_number)==10:
                C.append(mobile_number)
                break
            else:
                print("Enter correct mobile number!")
                continue
                        
        #Email ID
        while True:
            email_id=input("ENTER EMAIL ID (only Gmail ID): ").lower()
            if "@gmail.com" in email_id:
                C.append(email_id)
                break
            else:
                print("Enter the correct email ID")
                
        #Country
        print("\nWe accomodate people of the following counties:\n"
              "INDIA","                        FRANCE\n"
              "AUSTRALIA","                    BELGIUM\n"
              "BANGLADESH","                   CANADA\n"
              "GERMANY","                      GREECE\n"
              "NEPAL","                        SPAIN\n"
              "SWITZERLAND","                  SRI LANKA\n")
        while True:
            countries=["INDIA","FRANCE","AUSTRALIA","BELGIUM","BANGLADESH","CANADA","GERMANY","GREECE","NEPAL","SPAIN","SWITZERLAND","SRI LANKA"]
            country=input("ENTER COUNTRY: ")
            if country.isalpha()==False:
                print("Enter correct country!")
            if country.upper()  not in countries:
                print("We don't accomodate people of",country.upper()) 
            else:
                C.append(country.upper())
                break  
        import mysql.connector as ms
        my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
        cur=my.cursor()
        cust=(C)
        sql="insert into Customer_Details(Code,Destination,First_Name,Last_Name,Mobile_No,Email_ID,Country) values (%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(sql,cust)
        my.commit()
    customer_details()
    print(" ")

    print("                     **********************************************************************")
    print("                                               𝓗𝓸𝓽𝓮𝓵 𝓓𝓮𝓽𝓪𝓲𝓵𝓼")   
    def service_details():
        #import datetime
        #Chekin-Checkout dates
        while True:
            while True:
                try:
                    date_entry = input('ENTER CHECKIN DATE IN YYYY-MM-DD FORMAT: ')
                    year, month, day = map(int, date_entry.split('-'))
                    checkin = datetime.date(year, month, day)
                    current = datetime.datetime.now().date()
                    if checkin<current:
                        print("Enter correct date!!")
                    else:
                        break
                except ValueError:
                    print("Enter correct date!!")
            while True:
                try:
                    date_entry = input('ENTER CHECKOUT DATE IN YYYY-MM-DD FORMAT: ')
                    year, month, day = map(int, date_entry.split('-'))
                    checkout = datetime.date(year, month, day)
                    #import datetime
                    current = datetime.datetime.now().date()
                    if checkout<current:
                        print("Enter correct date!!")
                    else:
                        break
                    break
                except ValueError:
                    print("Enter correct date!!")
            checking=checkin + datetime.timedelta(days=10)
            if checkout<=(checking):
                break
            else:
                print("Sorry we dont permit a stay of more than 10 days!")
        S.append(checkin)
        S.append(checkout)
        #Number_Of_People
        while True:
            #Adults
            while True:
                try:
                    adult=int(input("ENTER NUMBER OF ADULTS: "))
                    if adult<0:
                        print("Enter the correct number of adults!")
                    else:
                        break
                except ValueError:
                    print("Enter the correct number!")
                    continue
            #Children            
            while True:
                children=int(input("ENTER NUMBER OF CHILDREN: "))
                if children<0:
                    print("Enter the correct number of children")
                else:
                    break                    
            if adult+children>4:
                    print("One room cannot accomodate more than 4 people")
            else:
                    S.append(adult)
                    S.append(children)
                    break
        
        #Room_Type
        show_room_types()
        while True:
            room=input("ENTER THE ROOM TYPE: ")
            if room.upper() in ["DELUXE","CLASSIC","SUITE"]:
                S.append(room.upper())
                break
            else:
                print("Enter the correct value!")
                continue
            
        #No_Of_Rooms
        while True:
            try:
                nor=int(input("ENTER NUMBER OF ROOMS: "))
                S.append(nor)
                break
            except ValueError:
                print("Enter the correct value!")
        if room.upper()=="DELUXE":
            amount=7600*nor
            P.append(amount)
        elif room.upper()=="CLASSIC":
            amount=7000*nor
            P.append(amount)
        elif room.upper()=="SUITE":
            amount=13000*nor
            P.append(amount)
        
             
        #Special_Requests             
        request=input("ANY SPECIAL REQUEST(OR NO): ")
        if request.upper()=="NO":
            request="NULL"
        S.append(request)
        
        import mysql.connector as ms
        my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
        cur=my.cursor()
        cust=(S)
        sql="insert into Service_Details(Code, Destination,Checkin,Checkout, Number_of_Adults, Numer_Of_Children, Room_Type, No_Of_Rooms,\
            Special_Requests) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(sql,cust)
        my.commit()
    service_details()
    print(" ")
    print("                     **********************************************************************")
    print("                                                 𝓟𝓪𝔂𝓶𝓮𝓷𝓽 𝓓𝓮𝓽𝓪𝓲𝓵𝓼")    
    def payment_details():
        
        #Mode_Of_Payment
        while True:
            mode_of_payment=input("ENTER MODE OF PAYMENT(Cash/Credit Card): ")
            if mode_of_payment.upper() not in ["CASH","CREDIT CARD"]:
                print("Enter correct value!")
                continue
            else:
                P.append(mode_of_payment.upper())
                break
            
        #Credit_Card_Number
        if mode_of_payment.upper()=="CREDIT CARD":
            while True:
                ccn=input("ENTER CREDIT CARD NUMBER: ")
                if len(ccn)!=16 or ccn.isdigit()==False:
                    print("Enter correct value!")
                else:
                    P.append(ccn)
                    break
        #Cash
        if mode_of_payment.upper()=="CASH":
            P.append("NULL")
        
        import mysql.connector as ms
        my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
        cur=my.cursor()
        cust=(P)
        sql="insert into Payment_Details(Code, Amount, Mode_Of_Payment, Credit_card_Number) values (%s,%s,%s,%s)"
        cur.execute(sql,cust)
        my.commit()
    payment_details() 
    print(" ")
    print("                             ****************************************************************** ")                 
    print("                                  𝕿𝖍𝖆𝖓𝖐𝖞𝖔𝖚 𝖋𝖔𝖗 𝖏𝖔𝖎𝖓𝖎𝖓𝖌 𝖜𝖎𝖙𝖍 𝖚𝖘!! 𝖄𝖔𝖚𝖗 𝖇𝖔𝖔𝖐𝖎𝖓𝖌 𝕴𝕯 𝖎𝖘 %s"%(code))

def view_details():
    pas=input("ENTER THE PASSWORD: ")
    if pas=="pleasing hotel":
        print("                                                 𝓒𝓾𝓼𝓽𝓸𝓶𝓮𝓻 𝓔𝓷𝓽𝓻𝓲𝓮𝓼 ")
        print("+-----+-------------+--------------------+-------------+--------------------+--------------+-------------+--------------+-------+----------+")
        print("┊CODE","┊DESTINATION"," ┊NAME               ","┊MOBILE NUMER","┊EMAIL ID           ","┊COUNTRY      ","┊CHECKIN DATE","┊CHECKOUT DATE","┊ADULTS","┊CHILDREN  ┊")
        print("+-----+-------------+--------------------+-------------+--------------------+--------------+-------------+--------------+-------+----------+")
        import mysql.connector as ms
        my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
        con=my.cursor()
        con.execute("SELECT * FROM Customer_Details LEFT JOIN Service_Details ON Service_Details.Code = Customer_Details.Code")
        data=con.fetchall()
        for i in data:
            print("┊",i[0],"┊",i[1]," "*(10-len(str(i[1]))),"┊",i[2],i[3]," "*(10-len(str(i[3]))),"┊",i[4]," "*(10-len(str(i[4]))),"┊",i[5]," "*(17-len(str(i[5]))),"┊",i[6]," "*(11-len(str(i[6]))),"┊",i[9]," "*(4-len(str(i[9]))),"┊",i[10]," "*(6-len(str(i[10])))," ┊",i[11]," "*(4-len(str(i[11]))),"┊",i[12]," "*(7-len(str(i[12]))),"┊")
        print("+-----+-------------+--------------------+-------------+--------------------+--------------+-------------+--------------+-------+----------+")
        print()
        print("                                                 𝓐𝓭𝓭𝓲𝓽𝓲𝓸𝓷𝓪𝓵 𝓓𝓮𝓽𝓪𝓲𝓵𝓼 ")
        print("+-----+-----------+------------+--------+----------------+-------------------+")
        print("┊CODE","┊ROOM TYPE"," ┊NO OF ROOMS","┊AMOUNT ","┊MODE OF PAYMENT","┊CREDIT CARD NUMBER","┊")
        print("+-----+-----------+------------+--------+----------------+-------------------+")
        con.execute("SELECT * FROM Service_Details LEFT JOIN Payment_Details ON Payment_Details.Code = Service_Details.Code")
        data=con.fetchall()
        for i in data:
            print("┊",i[0],"┊",i[6]," "*(8-len(str(i[6]))),"┊",i[7]," "*(9-len(str(i[7]))),"┊",i[10]," "*(5-len(str(i[10]))),"┊",i[11]," "*(13-len(str(i[11]))),"┊",i[12]," "*(11-len(str(i[12]))),"┊")
        print("+-----+-----------+------------+--------+----------------+-------------------+")
    else:
        print("Sorry! Wrong password")
def cancellation():
    codes=[]
    import mysql.connector as ms
    my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
    con=my.cursor()
    con.execute("SELECT CODE FROM Customer_Details")
    data=con.fetchall()
    for i in data:
        codes.append(i[0])
    while True:
        try:
            delete_code=int(input("ENTER THE CODE TO BE DELETED: "))
            if delete_code not in codes:
                print("No such entry exists!!")
            else:
                break
        except ValueError:
            print("Enter correct value!!")
    sql="DELETE FROM Customer_Details WHERE Code=%s"
    con.execute(sql,(delete_code,))
    sql1="DELETE FROM Service_Details WHERE Code=%s"
    con.execute(sql1,(delete_code,))
    sql2="DELETE FROM Payment_Details WHERE Code=%s"
    con.execute(sql2,(delete_code,))
    sql3="DELETE FROM Spa_Booking WHERE Code=%s"
    con.execute(sql3,(delete_code,))
    sql4="DELETE FROM Restaurant_Booking WHERE Code=%s"
    con.execute(sql4,(delete_code,))
    my.commit()
    print("Booking cancelled succesfully!!")

def search():
    codes=[]
    import mysql.connector as ms
    my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
    con=my.cursor()
    con.execute("SELECT CODE FROM Customer_Details")
    data=con.fetchall()
    for i in data:
        codes.append(i[0])
    while True:
        try:
            search_code=int(input("ENTER THE CODE TO BE SEARCHED: "))
            if search_code not in codes:
                print("No such entry exists!!")
            else:
                print("                                                 𝓒𝓾𝓼𝓽𝓸𝓶𝓮𝓻 𝓔𝓷𝓽𝓻𝓲𝓮𝓼 ")
                print("+-----+-------------+--------------------+-------------+--------------------+--------------+-------------+--------------+-------+----------+")
                print("┊CODE","┊DESTINATION"," ┊NAME               ","┊MOBILE NUMER","┊EMAIL ID           ","┊COUNTRY      ","┊CHECKIN DATE","┊CHECKOUT DATE","┊ADULTS","┊CHILDREN  ┊")
                print("+-----+-------------+--------------------+-------------+--------------------+--------------+-------------+--------------+-------+----------+")
                import mysql.connector as ms
                my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
                con=my.cursor()
                con.execute("SELECT * FROM Customer_Details LEFT JOIN Service_Details ON Service_Details.Code = Customer_Details.Code WHERE Service_Details.Code=%s",(search_code,))
                data=con.fetchall()
                for i in data:
                    print("┊",i[0],"┊",i[1]," "*(10-len(str(i[1]))),"┊",i[2],i[3]," "*(10-len(str(i[3]))),"┊",i[4]," "*(10-len(str(i[4]))),"┊",i[5]," "*(17-len(str(i[5]))),"┊",i[6]," "*(11-len(str(i[6]))),"┊",i[9]," "*(4-len(str(i[9]))),"┊",i[10]," "*(6-len(str(i[10])))," ┊",i[11]," "*(4-len(str(i[11]))),"┊",i[12]," "*(7-len(str(i[12]))),"┊")
                print("+-----+-------------+--------------------+-------------+--------------------+--------------+-------------+--------------+-------+----------+")
                print()
                print("                                                 𝓐𝓭𝓭𝓲𝓽𝓲𝓸𝓷𝓪𝓵 𝓓𝓮𝓽𝓪𝓲𝓵𝓼 ")
                print("+-----+-----------+------------+--------+----------------+-------------------+")
                print("┊CODE","┊ROOM TYPE"," ┊NO OF ROOMS","┊AMOUNT ","┊MODE OF PAYMENT","┊CREDIT CARD NUMBER","┊")
                print("+-----+-----------+------------+--------+----------------+-------------------+")
                con.execute("SELECT * FROM Service_Details LEFT JOIN Payment_Details ON Payment_Details.Code = Service_Details.Code WHERE Service_Details.Code=%s",(search_code,))
                data=con.fetchall()
                for i in data:
                    print("┊",i[0],"┊",i[6]," "*(8-len(str(i[6]))),"┊",i[7]," "*(9-len(str(i[7]))),"┊",i[10]," "*(5-len(str(i[10]))),"┊",i[11]," "*(13-len(str(i[11]))),"┊",i[12]," "*(11-len(str(i[12]))),"┊")                 
                print("+-----+-----------+------------+--------+----------------+-------------------+")
                break
        except ValueError:
            print("Enter correct value!!")

def update():
    codes=[]
    import mysql.connector as ms
    my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
    con=my.cursor()
    con.execute("SELECT CODE FROM Customer_Details")
    data=con.fetchall()
    for i in data:
        codes.append(i[0])
    while True:
        try:
            update_code=int(input("ENTER THE CODE TO BE UPDATED: "))
            if update_code not in codes:
                print("No such entry exists!!")
            else:
                break
        except ValueError:
            print("Enter correct value!!")
    
    print("What would you like to update?")
    print("1. Destination ")
    print("2. First Name")
    print("3. Last Name")
    print("4. Mobile Number")
    print("5. Email ID")
    print("6. Country")
    print("7. Number of people")
    print("8. Room Details")
    print("9. Payment Details")
    while True:     #update_choice
        try:
            update=int(input("ENTER SERIAL NUMBER OF YOUR CHOICE: "))
            if update not in [1,2,3,4,5,6,7,8,9,10,11,12]:
                print("Enter correct value!!")
            else:
                break
        except ValueError:
            print("Enter correct value!!")
    if update==1:
        options=["MANALI","NAINITAL","DARJEILING","SHIMLA","OOTY","RANIKHET","MUSSORIE","LADAKH","AULI","SRINAGAR","GULMARG"]
        print("We have hotels at the following hill sations:\n"
              "MANALI","                        NAINITAL\n"
              "DARJEILING","                    SHIMLA\n"
              "OOTY","                          RANIKHET\n"
              "MUSSORIE","                      LADAKH\n"
              "AULI","                          SRINAGAR\n"
              "GULMARG")
        while True:
            destination=input("ENTER PLACE YOU WANT TO VISIT: ").upper()
            if destination in options:
                break
            else:
                print("We do not have hotels in",destination)
                continue
        import mysql.connector as ms
        my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
        cur=my.cursor()
        sql="UPDATE Customer_Details SET Destination =%s WHERE Code = %s"
        sql1="UPDATE Service_Details SET Destination =%s WHERE Code = %s"
        var=(destination,update_code)
        cur.execute(sql,var)
        cur.execute(sql1,var)
        my.commit()
    elif update==2:
        while True:
            first_name=input("ENTER FIRST NAME: ").upper()
            if first_name.isalpha()==True:
                break
            else:
                print("Enter correct name!")
                continue
        import mysql.connector as ms
        my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
        cur=my.cursor()
        var=(first_name,update_code)
        sql="UPDATE Customer_Details SET First_Name =%s WHERE Code = %s"
        cur.execute(sql,var)
        my.commit()
    elif update==3:
        while True:
            last_name=input("ENTER LAST NAME: ").upper()
            if last_name.isalpha()==True:
                break
            else:
                print("Enter correct name!")
                continue
        import mysql.connector as ms
        my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
        cur=my.cursor()
        var=(last_name,update_code)
        sql="UPDATE Customer_Details SET Last_Name =%s WHERE Code = %s"
        cur.execute(sql,var)
        my.commit()
    elif update==4:
        while True:
            mobile_number=input("ENTER MOBILE NUMBER: ")
            if mobile_number.isdigit()==True and len(mobile_number)==10:
                break
            else:
                print("Enter correct mobile number!")
                continue
        import mysql.connector as ms
        my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
        cur=my.cursor()
        var=(mobile_number,update_code)
        sql="UPDATE Customer_Details SET Mobile_No =%s WHERE Code = %s"
        cur.execute(sql,var)
        my.commit()
    elif update==5:
        while True:
            email_id=input("ENTER EMAIL ID (only Gmail ID): ").lower()
            if "@gmail.com" in email_id:
                break
            else:
                print("Enter the correct email ID")
        import mysql.connector as ms
        my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
        cur=my.cursor()
        var=(email_id,update_code)
        sql="UPDATE Customer_Details SET Email_ID =%s WHERE Code = %s"
        cur.execute(sql,var)   
        my.commit()
    elif update==6:
        print("\nWe accomodate people of the following counties:\n"
              "INDIA","                        FRANCE\n"
              "AUSTRALIA","                    BELGIUM\n"
              "BANGLADESH","                   CANADA\n"
              "GERMANY","                      GREECE\n"
              "NEPAL","                        SPAIN\n"
              "SWITZERLAND","                  SRI LANKA\n")
        while True:
            countries=["INDIA","FRANCE","AUSTRALIA","BELGIUM","BANGLADESH","CANADA","GERMANY","GREECE","NEPAL","SPAIN","SWITZERLAND","SRI LANKA"]
            country=input("ENTER COUNTRY: ").upper()
            if country.isalpha()==False:
                print("Enter correct country!")
            if country.upper()  not in countries:
                print("We don't accomodate people of",country) 
            else:
                break
        import mysql.connector as ms
        my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
        cur=my.cursor()
        var=(country,update_code)
        sql="UPDATE Customer_Details SET Country =%s WHERE Code = %s"
        cur.execute(sql,var)
        my.commit()
    elif update==7:
        while True:
            #Adults
            while True:
                try:
                    adult=int(input("Enter Number of adults: "))
                    if adult<0:
                        print("Enter the correct number of adults!")
                    else:
                        break
                except ValueError:
                    print("Enter the correct number!")
                    continue
            #Children            
            while True:
                children=int(input("Enter the Number of childen: "))
                if children<0:
                    print("Enter the correct number of children")
                else:
                    break                    
            if adult+children>4:
                    print("One room cannot accomodate more than 4 people")
            else:
                    break
        my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
        cur=my.cursor()
        var=(adult,children,update_code)
        sql="UPDATE Service_Details SET Number_of_Adults =%s, Numer_of_Children=%s WHERE Code = %s"
        cur.execute(sql,var)
        my.commit()
    elif update==8:
        show_room_types()
        while True:
            room=input("Enter the room type: ").upper()
            if room in ["DELUXE","CLASSIC","SUITE"]:
                break
            else:
                print("Enter the correct value!")
                continue 
        while True:
            try:
                nor=int(input("Enter Number of Rooms: "))
                break
            except ValueError:
                print("Enter the correct value!")
        if room=="DELUXE":
            amount=7600*nor
        elif room=="CLASSIC":
            amount=7000*nor
        elif room=="SUITE":
            amount=13000*nor
        my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
        cur=my.cursor()
        var=(room,nor,update_code)
        var1=(amount,update_code)
        sql="UPDATE Service_Details SET Room_Type=%s,No_Of_Rooms=%s WHERE Code = %s"
        sql1="UPDATE Payment_Details SET Amount =%s WHERE Code = %s"
        cur.execute(sql,var)
        cur.execute(sql1,var1)
        my.commit()
    elif update==9:
        #Mode_Of_Payment
        while True:
            mode_of_payment=input("ENTER MODE OF PAYMENT(Cash/Credit Card): ").upper()
            if mode_of_payment not in ["CASH","CREDIT CARD"]:
                print("Enter correct value!")
                continue
            else:
                break
            
        #Credit_Card_Number
        if mode_of_payment=="CREDIT CARD":
            while True:
                ccn=input("ENTER CREDIT CARD NUMBER: ")
                if len(ccn)!=16 or ccn.isdigit()==False:
                    print("Enter correct value!")
                else:
                    break
        #Cash
        if mode_of_payment=="CASH":
            ccn="NULL"
        import mysql.connector as ms
        my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
        cur=my.cursor()
        var=(mode_of_payment,ccn,update_code)
        sql="UPDATE Payment_Details SET Mode_Of_Payment =%s,Credit_card_Number=%s WHERE Code = %s"
        cur.execute(sql,var)
        my.commit()

def billing():
    codes=[]
    D=[]
    import mysql.connector as ms
    my=ms.connect(host="localhost",user="root",password="",database="HOTEL")
    con=my.cursor()
    con.execute("SELECT CODE FROM Customer_Details")
    data=con.fetchall()
    for i in data:
        codes.append(i[0])
    while True:
        try:
            code_bill=int(input("ENTER THE CODE: "))
            if code_bill not in codes:
                print("No such entry exists!!")
            else:
                break
        except ValueError:
            print("Enter correct value!!")
    #Check-in
    con.execute("SELECT Checkin FROM Service_Details WHERE CODE=%s"%(code_bill))
    data=con.fetchall()
    D.append(str(data)[16:26])
    
    #Check-out
    con.execute("SELECT Checkout FROM Service_Details WHERE CODE=%s"%(code_bill))
    data=con.fetchall()
    D.append(str(data)[16:26])
    
    #First_Name
    con.execute("SELECT First_Name FROM Customer_Details WHERE CODE=%s"%(code_bill))
    data=con.fetchall()
    D.append(str(data)[3:len(data)-5])
    
    #Last_Name
    con.execute("SELECT Last_Name FROM Customer_Details WHERE CODE=%s"%(code_bill))
    data=con.fetchall()
    D.append(str(data)[3:len(data)-5])
    
    #Mobile_No
    con.execute("SELECT Mobile_No FROM Customer_Details WHERE CODE=%s"%(code_bill))
    data=con.fetchall()
    D.append(str(data)[3:len(data)-4])
    
    #Amount
    con.execute("SELECT Amount FROM Payment_Details WHERE CODE=%s"%(code_bill))
    data=con.fetchall()
    D.append(int(str(data)[2:len(data)-4]))
    
    #NO_Of_Rooms
    con.execute("SELECT No_Of_Rooms FROM Service_Details WHERE CODE=%s"%(code_bill))
    data=con.fetchall()
    D.append(int(str(data)[2:len(data)-4]))
    
    #Room_Types
    con.execute("SELECT Room_Type FROM Service_Details WHERE CODE=%s"%(code_bill))
    data=con.fetchall()
    D.append(str(data)[3:len(data)-5])
    
    #Rate_of_room
    Rate_of_room=D[5]//D[6]
    D.append(Rate_of_room)
    
    #Order
    con.execute("SELECT Menu FROM Restaurant_Booking WHERE CODE=%s"%(code_bill))
    data=con.fetchall()
    D.append(str(data)[3:len(data)-5])
    
    #Order_Rate
    con.execute("SELECT Amount FROM Restaurant_Booking WHERE CODE=%s"%(code_bill))
    data=con.fetchall()
    Amount_res=str(data)[2:len(data)-4]
    if Amount_res=='':
        Amount_res=0
    D.append(Amount_res)
    
    con.execute("SELECT Plates FROM Restaurant_Booking WHERE CODE=%s"%(code_bill))
    data=con.fetchall()
    RP=str(data)[2:len(data)-4]
    if RP=='':
        RP=1
    D.append(RP)
    
    #Rate_of_order
    if D[10]=='':
        Rate_of_order=0
    else:
        Rate_of_order=int(D[10])//int(D[11])
    D.append(Rate_of_order)

    #Spa
    con.execute("SELECT Package_Name FROM Spa_Booking WHERE CODE=%s"%(code_bill))
    data=con.fetchall()
    D.append(str(data)[3:len(data)-5])
    
    #Spa_Rate
    con.execute("SELECT Amount FROM Spa_Booking WHERE CODE=%s"%(code_bill))
    data=con.fetchall()
    Amount_spa=str(data)[2:len(data)-4]
    if Amount_spa=='':
        Amount_spa=0
    D.append(Amount_spa)
    
    con.execute("SELECT No_Of_People FROM Spa_Booking WHERE CODE=%s"%(code_bill))
    data=con.fetchall()
    NOP=str(data)[2:len(data)-4]
    if NOP=='':
        NOP=1
    D.append(NOP) 
    
    #Rate_of_spa
    Rate_of_spa=int(D[14])//int(D[15])
    D.append(Rate_of_spa)
    Total=int(D[5])+int(D[10])+int(D[14])
    '''D=[CHECKIN,CHECKOUT,FIRST NAME, LAST NAME, PHONE NO, AMOUNT OF ROOM, NO OF ROOMS, TYPE OF ROOMS, RATE OF ROOM, MENU, AMOUNT OF MENU,\
         NO OF PLATES, RATE OF MENU, SPA TYPE, AMOUNT OF SPA, NO OF PEOPLE IN SPA, RATE OF SPA]'''
    print("                           **********************************************************************")
    print("                                                    𝐻𝑜𝓉𝑒𝓁 𝒮𝓃𝑜𝓌 𝒞𝒾𝓉𝓎                                ")
    print("                                                       𝐵𝒾𝓁𝓁𝒾𝓃𝑔                                      ")
    print("                            BOOKING ID: %s"%(code_bill))
    print("                   -------------------------------------------------------------------------------------------------")
    print("                   CHECKIN DATE        : %s"%(D[0]))
    print("                   CHECKOUT DATE       : %s"%(D[1]))
    print("                   CUSTOMER NAME       : %s %s"%(D[2],D[3]))
    print("                   CUSTOMER CONTACT NO : %s"%(D[4]))    
    print("                   -------------------------------------------------------------------------------------------------")    
    print("                    DESCRIPTION                                    ┊ RATE          ┊ AMOUNT")
    print("                   -------------------------------------------------------------------------------------------------") 
    print("                    %s %s ROOM"%(D[6],D[7])," "*(44-(len(str(D[5]))+len(str(D[6]))+6)),"┊","%s"%(D[8])," "*(12-(len(str(D[8])))),"┊","%s"%(D[5]))
    if Amount_res!=0:
        print("                    %s %s"%(D[11],D[9])," "*(44-(len(str(D[11]))+len(str(D[9])))),"┊","%s"%(D[12])," "*(12-(len(str(D[12])))),"┊","%s"%(D[10]))
    if Amount_spa!=0:
        print("                    %s %s"%(D[15],D[13])," "*(44-(len(str(D[15]))+len(str(D[13])))),"┊","%s"%(D[16])," "*(12-(len(str(D[16])))),"┊","%s"%(D[14]))
    print("                                                                   ┊ TOTAL PRICE   ┊ %s"%(Total))      
    print("                   -------------------------------------------------------------------------------------------------")    

def backtomenu():
    while True:
        backtomenu=""
        backtomenu=input("Press any key to Go To Menu: ")
        if len(backtomenu)>0 and backtomenu!="\n":
            menu()
            choice()                
        else:
            break     

def menu():
    print("                                                     1. Table Creation  ")    
    print("                                                     2. Manage Room  ")
    print("                                                     3. Spa Facilities")
    print("                                                     4. Restaurant")
    print("                                                     5. Billing")
    print("                                                     6. Exit")
menu() 

def choice(): 
    while True:
        try:
            choose=int(input("ENTER SERIAL NUMBER OF YOUR CHOICE: "))
            if choose not in [1,2,3,4,5,6]:
                print("Enter correct value!!")
            else:
                break
        except ValueError:
            print("Enter correct value!!")
    if choose==1:
        print("                                                     1. Create Table Customer_Deatils  ")
        print("                                                     2. Create Table Service_Deatils")
        print("                                                     3. Create Table Payment_Deatils")
        print("                                                     4. Create Table Room_Types")
        print("                                                     5. Create Table Restaurant")
        print("                                                     6. Create Table Spa")
        while True:
            try:
                choose1=int(input("ENTER SERIAL NUMBER OF YOUR CHOICE: "))
                if choose1 not in [1,2,3,4,5,6]:
                    print("Enter correct value!!")
                else:
                        break
            except ValueError:
                print("Enter correct value!!")
        if choose1==1:
            create_customer_details() 
            backtomenu()
        elif choose1==2:
            create_service_details()
            backtomenu()
        elif choose1==3:
            create_payment_details()
            backtomenu()
        elif choose1==4:
            create_room_types()
            backtomenu()
        elif choose1==5:
            create_restaurant()
            backtomenu()
        elif choose1==6:
            create_spa()    
            backtomenu()
    elif choose==2:
        print("                                                     1. Book A Room  ")
        print("                                                     2. View Your Registered Details")
        print("                                                     3. Cancel the bookings  ")
        print("                                                     4. Search for Details")
        print("                                                     5. Update the bookings")
        while True:
            try:
                choose2=int(input("ENTER SERIAL NUMBER OF YOUR CHOICE: "))
                if choose2 not in [1,2,3,4,5]:
                    print("Enter correct value!!")
                else:
                        break
            except ValueError:
                print("Enter correct value!!")
        if choose2==1:
            enter_values()
            backtomenu() 
        elif choose2==2:
            view_details()
            backtomenu() 
        elif choose2==3:
            cancellation()
            backtomenu() 
        elif choose2==4:
            search()
            backtomenu() 
        elif choose2==5:
            update()
            backtomenu()
    elif choose==3:
        show_spa()
        backtomenu() 
    elif choose==4:
        show_restaurant()
        backtomenu() 
    elif choose==5:
        billing()
        backtomenu() 
    elif choose==6:
        print("𝕿𝖍𝖆𝖓𝖐𝖞𝖔𝖚 𝖋𝖔𝖗 𝖗𝖊𝖆𝖈𝖍𝖎𝖓𝖌 𝖚𝖘 !!")
choice()

  
     