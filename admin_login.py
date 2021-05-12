#admin function

from tkinter import *
from tkinter import messagebox

class login:
    def __init__(self,root):
        self.root=root
        self.root.title("login system")
        self.root.geometry("1199x600+100+50")
       # self.bg=Image.Tk.PhotoImage(file="images/image")
       # self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)



        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=150,y=50,height=340,width=500)

        title=Label(Frame_login,text="login here",font=("Impact",35,"bold")).place(x=90,y=30)
        desc=Label(Frame_login, text="Admin login", font=("Goudy old style", 15, "bold")).place(x=90, y=100)
        lbl_user=Label(Frame_login, text=" Admin username", font=("Goudy old style", 15, "bold")).place(x=90, y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15))
        self.txt_user.place(x=90,y=170,width=350,height=35)
        lbl_pass= Label(Frame_login, text="password", font=("Goudy old style", 15, "bold")).place(x=90, y=210)
        self.txt_pass = Entry(Frame_login,show="*" , font=("times new roman", 15))
        self.txt_pass.place(x=90, y=240, width=350, height=35)
        forget_btn=Button(Frame_login,text="Forget password?",bg="pink",fg="#d77337",bd=0,font=("time new roman",12)).place(x=90,y=280)
        login_btn = Button(self.root,command=self.login_function, text="login", bg="pink", fg="#d77337",
                        font=("time new roman", 12)).place(x=400, y=300,width=180,height=40)


    
        
    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All feilds are required",parent=self.root)
        elif self.txt_pass.get()!="123456"or self.txt_user.get()!="shivani":
            messagebox.showerror("Error","Invalid username/password",parent=self.root)
            Lib_Admin()
        else:
            messagebox.showinfo("Welcome",f"Welcome{self.txt_user.get()}\nYour password:{self.txt_pass.get()}", parent=self.root)
            import lib_admin

def Lib_Admin(self):
        import Library_Admin
        self.root.destroy()
        
def ucall():
   root=Tk()
   obj=login(root)
   root.mainloop()
ucall()

