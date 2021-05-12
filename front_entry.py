# Library Management System Full Interface

from tkinter import *
from PIL import ImageTk
from tkinter import ttk


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("library window")
        self.root.geometry("1350x700+0+0")
        Frame_login = Frame(self.root, bg="pink")
        Frame_login.place(x=0, height=1000, width=3000)
        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=100, y=90, height=60, width=500)
        btn_mlogin = Button(self.root, text="LIBRABRY", bg="LavenderBlush3", fg="#d77337",
                            font=("time new roman", 28), bd=1).place(x=100, y=90, height=60, width=500)

        Frame_login = Frame(self.root, bg="green")
        Frame_login.place(x=100, y=150, height=400, width=500)
        btn_ylogin = Button(self.root,
                            text="Libraries will get you through\n times of no money better than \nmoney will get you through\n times of no libraries.\n – Anne Herbert",
                            bg="black", fg="#d77337", font=("time new roman", 28), bd=1).place(x=100, y=150, height=400,
                                                                                               width=500)

        btn_rlogin = Button(self.root, text="Admin login", command=self.admin_page, font=("time new roman", 19), bd=1)
        btn_rlogin.place(x=650, y=35)
        btn_login = Button(self.root, text="User login", command=self.user_page, font=("time new roman", 19), bd=1)
        btn_login.place(x=900, y=35)
        btn_rlogin = Button(self.root, text="Registration login", command=self.register_page, font=("time new roman", 19),
                            bd=1)
        btn_rlogin.place(x=1100, y=35)

    def admin_page(self):

        import admin_login
        self.__init__(Tk())
        self.root.destroy()

    def user_page(self):

        import user_login
        self.__init__(Tk())
        self.root.destroy()


    def register_page(self):

        import user_reg
        self.__init__(Tk())
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()



