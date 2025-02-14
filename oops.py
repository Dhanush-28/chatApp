from datetime import datetime
import mysql.connector

conn=mysql.connector.connect(host="localhost",password="Dhanuk#28",user="root",database="chatapp")
cursor=conn.cursor()
cursor.execute("create table if not exists chatapp(uname varchar(20),pwd varchar(20))")

class chatApp:
    d={}
    da={"admin":"password"}
    def __init__(self,name,password):
        self.name=name
        self.password=password

    def login_user(self,nam,pswd):
        if (nam in obj.da.keys() and obj.da[nam]==pswd):
            return True
        else:    
            return False
    def check_user(self,nam,pswd):
        if nam in obj.d.keys() and obj.d[nam]==pswd:
            return True
        else:
            return False
        
    def add_user(self,uname,pwd):
        self.d.update({uname:pwd})
        cursor.execute(f"insert into chatapp values('{uname}','{pwd}')")
        conn.commit()

    def chat(self,x,z):
        txt=open("chat.txt",'a')
        txt.write(f"From {self.name} To {x}:{z} \n")
        current_time = datetime.now()
        f_time=current_time.strftime("[%d-%m-%y %H:%M]\n")
        txt.write(f_time)
        txt.close()

    def delete_user(self,uname):
        del self.d[uname]

    def change_password(self,uname,pwd):
        self.d[uname]=pwd
    def show_users(self):
        cursor.execute("select * from chatapp")
        for i in cursor:
            print(i)

#Login Application
print("Welcome to the application")
uname=input("enter the username : ")
pwd=input("enter the password : ")

obj=chatApp(uname,pwd)   
flag=1
print(obj.d)

if (obj.login_user(uname,pwd)):
    while(flag==1):
        print("select the action")
        print("1. create user")
        print("2. chat with user")
        print("3. delete user")
        print("4. change password")
        print("5. show users")
        print("6. exit")

        action=int(input("enter the action : "))
        if action==1:
            x=input("enter the name : ")
            y=input("enter the password : ")
            if obj.check_user(x,y):
                print("user already exists")
            elif obj.login_user(x,y):
                print("admin cannot be added as user")
            else:    
                obj.add_user(x,y)
                print("user added successfully")

        elif action==2:
            x=input("enter the recepient name : ")
            if (x in obj.d.keys()):
                z=input("enter the message : ")
                obj.chat(x,z)
                print("message sent successfully")

        elif action==3:
            a=input("enter the uname to delete : ")
            if (a in obj.d.keys()):
                obj.delete_user(a)
                print("user deleted successfully")
            else:
                print("user does not exist")

        elif action==4:
            a=input("enter the name to change password : ")
            b=input("enter the password of the user: ")
            if (obj.check_user(a,b)):
                c=input("enter the new password : ")
                obj.change_password(a,c)
                print("password changed successfully")
            else:
                print("user does not exist")
        elif action==5:
            obj.show_users()
        else:
            flag=0
            print("exiting the application")
            obj.show_users()
else:
    print("invalid username or password")
    print("exiting the application")