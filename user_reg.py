# User registration

from tkinter import*
from PIL import ImageTk
from  tkinter import ttk
from tkinter import messagebox
import pymysql
mycone=pymysql.connect(
    host="localhost",
    user="root",
    password="",
   )

class Registerfrom:
    def __init__(self,root):
        self.root=root
        self.root.title("library window")
        self.root.geometry("1350x700+0+0")
        Frame_login = Frame(self.root, bg="burlywood3")
        Frame_login.place(x=0, height=1000, width=3000)
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=100, y=90, height=60, width=500)
        btn_mlogin = Button(self.root, text="LIBRABRY",bg="burlywood2",fg="#d77337",font=("time new roman", 28), bd=1).place(x=100, y=90, height=60, width=500)

       # Frame_login = Frame(self.root,bg="green")
        #Frame_login.place(x=100,y=150, height=400, width=500)
        btn_ylogin = Button(self.root, text="Libraries will get you through\n times of no money better than \nmoney will get you through\n times of no libraries.\n – Anne Herbert", bg="burlywood2",fg="gray16",font=("time new roman", 28), bd=1).place(x=100,y=150, height=400, width=500)


       # btn_rlogin = Button(self.root, text="ADMIN login", font=("time new roman", 19), bd=1)
       # btn_rlogin.place(x=650, y=35)

        #btn_login=Button(self.root ,text="user login",font=("time new roman",19),bd=1)
       # btn_login.place(x=900,y=35)
        btn_rlogin = Button(self.root, text="Registration", font=("time new roman", 19), bd=1)
        btn_rlogin.place(x=1100,y=35)
        
class Register:
    def __init__(self,root):
        self.root=root
       # self.root.title("Regiseration window")
        #self.root.geometry("1350x700+0+0")
        #registertion from----------------
        frame1=Frame(self.root,bg="burlywood3")
        frame1.place(x=650,y=100,height=480,width=700)
        tittle=Label(frame1,text="REGISTER HERE",font=("time new roma",20,"bold"),bg="white",fg="green").place(x=50,y=30)
        self.var_frame=StringVar()
        name=Label(frame1,text="Name",font=("time new roma",20,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_name=Entry(frame1, font=("time new roman", 15))
        self.txt_name.place(x=50, y=130)
        u_name = Label(frame1, text="User NAME", font=("time new roman", 15, "bold"), bg="white", fg="gray").place(x=370,y=100)
        self.txt_uname = Entry(frame1, font=("time new roman", 15))
        self.txt_uname.place(x=370, y=130, width=250)
        
#=====================================================
        contact=Label(frame1,text="contact .NO",font=("time new roman",20,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("time new roman",15))

        self.txt_contact.place(x=50,y=200,width=250)
        print(type(self.txt_contact.get()))
        if not str(self.txt_contact ):
            messagebox.showinfo("information", "only digit are allow for phone number")

        #self.txt_contact.config(validate="key", validatecommand=(valid_phone, '%p'))
        email = Label(frame1, text="EMAIL", font=("time new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=170)
        self.txt_email= Entry(frame1, font=("time new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)


#===================================================================================================
        #============================================
        password=Label(frame1,text="Password",font=("time new roman",20,"bold"),bg="white",fg="gray").place(x=50,y=250)
        self.txt_password=Entry(frame1,font=("time new roman",15))
        self.txt_password.place(x=50,y=290,width=250)
        cpassword = Label(frame1, text="Confirm password", font=("time new roman", 15, "bold"), bg="white", fg="gray").place(x=370, y=250)
        self.txt_cpassword= Entry(frame1, font=("time new roman", 15))
        self.txt_cpassword.place(x=370, y=290, width=250)
        #====================================================
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions").place(x=50,y=350)
        tittle = Button(self.root,command=self.register_data, text="Register", bg="white", fg="#d77337",
                        font=("time new roman",15),bd=0).place(x=900,y=440,width=100,)
        #btn_login=Button(self.root ,text="sign in",font=("time new roman",20),bd=0).place(x=400,y=420)

    def register_data(self):
        try:
            valid_contact = self.txt_contact.get()
            valid_email = self.txt_email.get()
            valid_uname = self.txt_uname.get()

            if valid_contact.isdigit() and len(valid_contact) == 10 and valid_email.endswith(
                    ".com") and self.txt_password.get() == self.txt_cpassword.get() and valid_uname.isalnum():
                cursor = mycone.cursor()
                cursor.execute("create database if not exists librarymanagement")
                cursor.execute("use librarymanagement")
                cursor.execute(
                    "create table if not exists register(Username varchar(50),Password varchar(50),Full_name varchar(60), Mobile int(50),Email varchar(50))")
                cursor.execute(
                    f"insert into register(Full_name,Username,Mobile,Email,Password) values('{self.txt_name.get()}','{self.txt_uname.get()}','{self.txt_contact.get()}','{self.txt_email.get()}','{self.txt_password.get()}')")
                mycone.commit()
                messagebox.showinfo("Done","Registered Succesfully")
                                    
                from userid import ucall
                ucall()
            else:
                messagebox.showinfo("warning", "please enter valid details only")

        except:
            print("e")
root=Tk()
obj=Registerfrom(root)
obj=Register(root)


#obj1=db(root)
#obj1.register_data()
root.mainloop()










