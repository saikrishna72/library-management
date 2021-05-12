from tkinter import*
from tkinter import messagebox
import pymysql
 
mycone=pymysql.connect(
    host="localhost",
    user="root",
    password="",
   )
cursor=mycone.cursor()
usedb=cursor.execute("use librarymanagement")
table=cursor.execute("select Username,password from register")
row=cursor.fetchone()
d={}
while row is not None:
    d[row[0]]=row[1]
    row=cursor.fetchone()
from PIL import ImageTk
from  tkinter import ttk
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("library window")
        self.root.geometry("1350x700+0+0")
        Frame_login = Frame(self.root, bg="pink")
        Frame_login.place(x=0, height=1000, width=3000)
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=100, y=90, height=60, width=500)
        btn_mlogin = Button(self.root, text="OJA'S LIBRABRY",bg="LavenderBlush3",fg="#d77337",font=("time new roman", 28), bd=1).place(x=100, y=90, height=60, width=500)

       # Frame_login = Frame(self.root,bg="green")
        #Frame_login.place(x=100,y=150, height=400, width=500)
        btn_ylogin = Button(self.root, text="Libraries will get you through\n times of no money better than \nmoney will get you through\n times of no libraries.\n – Anne Herbert", bg="plum3",fg="#d77337",font=("time new roman", 28), bd=1).place(x=100,y=150, height=400, width=500)


        #btn_rlogin = Button(self.root, text="ADMIN login", font=("time new roman", 19), bd=1)
       # btn_rlogin.place(x=650, y=35)

        btn_login=Button(self.root ,text="USER LOGIN",font=("time new roman",19),bd=1)
        btn_login.place(x=900,y=35)
       # btn_rlogin = Button(self.root, text="registeration login", font=("time new roman", 19), bd=1)
        #btn_rlogin.place(x=1100,y=35)
class login:
    def __init__(self,root,d):
        self.d=d
        self.root=root

        Frame_login=Frame(self.root,bg="pink")
        Frame_login.place(x=600,y=100,height=480,width=500)
       # title=Label(Frame_login,text="login here",font=("Impact",35,"bold")).place(x=90,y=30)
        desc=Label(Frame_login, text="library login", font=("Goudy old style", 30, "bold")).place(x=90, y=100)
        lbl_user=Label(Frame_login, text="User id", font=("Goudy old style", 15, "bold")).place(x=90, y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15))
        self.txt_user.place(x=90,y=170,width=350,height=35)
        lbl_pass= Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold")).place(x=90, y=210)
        self.txt_pass = Entry(Frame_login, font=("times new roman", 15))
        self.txt_pass.place(x=90, y=240, width=350, height=35)
        forget_btn=Button(Frame_login,text="Forget password?",bg="pink",fg="#d77337",bd=0,font=("time new roman",12)).place(x=900,y=280)
        login_btn = Button(self.root,command=self.login_function, text="login", bg="white", fg="#d77337",
                        font=("time new roman", 12)).place(x=900, y=400,width=180,height=40)

    def login_function(self):
        print(self.d)
        print("User ID  : ",self.txt_user.get())
        print("Password : ",self.txt_pass.get())
        try:
            if self.txt_pass.get()=="" or self.txt_user.get()=="":
                messagebox.showerror("Error","All feilds are required",parent=self.root)
            elif self.txt_pass.get()==self.d[self.txt_user.get()] and self.txt_user.get() in self.d:
                #murali page
                #page fun or method
                
                cursor.execute(f"insert into login(Username,Password) values('{self.txt_user.get()}','{self.txt_pass.get()}')")
                mycone.commit()
                messagebox.showinfo("Welcome", f"Welcome{self.txt_user.get()}\nYour password:{self.txt_pass.get()}",
                                    parent=self.root)

                
                import lib_user
                #lib_user.lcall()
                
            else:
                messagebox.showerror("Error","Invalid username/password",parent=self.root)
        except:
            messagebox.showerror("Error", "Invalid username/password", parent=self.root)

def ucall():
    root=Tk()
    obj = Register(root)
    obj=login(root,d)
    root.mainloop()
ucall()



