from tkinter import *
import tkinter as Tk
from tkinter import ttk
import pymysql
from tkinter import messagebox
from PIL import Image, ImageTk

class LibraryManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")


        #=====================================Variable==========================================================

        self.id_var = StringVar()
        self.name_var = StringVar()
        self.author_var = StringVar()
        self.quantity_var= StringVar()

        lbltitle = Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="NavajoWhite2",fg="NavajoWhite4",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="NavajoWhite4")
        frame.place(x=0,y=130,width=1530,height=350)

        #=====================================DataFrame Left=================================================

        DataFrameLeft=LabelFrame(frame,text="Admin Section",bg="NavajoWhite2",fg="NavajoWhite4",bd=12,relief=RIDGE,font=("arial",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=680,height=300)


        lblBookId=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Id",padx=2,bg="NavajoWhite2")
        lblBookId.grid(row=0,column=0,sticky=W)
        txtBookId=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.id_var,width=29)
        txtBookId.grid(row=0,column=1)
        
        lblBlank1=Label(DataFrameLeft,font=("arial",12,"bold"),text="",padx=2,bg="NavajoWhite2")
        lblBlank1.grid(row=1,column=0,sticky=W)

        lblBookName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Name",padx=2,bg="NavajoWhite2")
        lblBookName.grid(row=2,column=0,sticky=W)
        txtBookName=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.name_var,width=29)
        txtBookName.grid(row=2,column=1)

        lblBlank2=Label(DataFrameLeft,font=("arial",12,"bold"),text="",padx=2,bg="NavajoWhite2")
        lblBlank2.grid(row=3,column=0,sticky=W)

        lblBookAuthor=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Author",padx=2,bg="NavajoWhite2")
        lblBookAuthor.grid(row=4,column=0,sticky=W)
        txtBookAuthor=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.author_var,width=29)
        txtBookAuthor.grid(row=4,column=1)

        lblBlank3=Label(DataFrameLeft,font=("arial",12,"bold"),text="",padx=2,bg="NavajoWhite2")
        lblBlank3.grid(row=5,column=0,sticky=W)

        lblBookQuantity=Label(DataFrameLeft,font=("arial",12,"bold"),text="Book Quantity",padx=2,bg="NavajoWhite2")
        lblBookQuantity.grid(row=6,column=0,sticky=W)
        txtBookQuantity=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.quantity_var,width=29)
        txtBookQuantity.grid(row=6,column=1)

        #======================DataFrameRight========================================================================================================

        DataFrameRight=LabelFrame(frame,text="Book Names",bg="NavajoWhite2",fg="NavajoWhite4",bd=12,relief=RIDGE,font=("arial",12,"bold"))
        DataFrameRight.place(x=710,y=5,width=540,height=300)

        lblBook_Name=Label(DataFrameRight,font=("arial",12,"bold"),text="",padx=2,bg="NavajoWhite2",fg="NavajoWhite4")
        lblBook_Name.grid(row=0,column=0,sticky=W)

        temp = []
        conn=pymysql.connect(host="localhost",user="root",password="",database="librarymanagement")
        a = "select Book_Name from admin"
        my_cursor=conn.cursor()
        my_cursor.execute(a)
        result = my_cursor.fetchall()

        for i in result:
            temp.append(i[0])
        conn.close()
        
        listBooks = temp

        def SelectedBook(event=''):
            value=listBox.get(listBox.curselection())
            w=value
            conn=pymysql.connect(host="localhost",user="root",password="",database="librarymanagement")
            c=conn.cursor()        
            c.execute("SELECT * FROM admin WHERE Book_Name =%s",(w,))
            for row in c.fetchall():
                self.id_var.set(str(row[0]))
                self.name_var.set(str(row[1]))
                self.author_var.set(str(row[2]))
                self.quantity_var.set(str(row[3]))
                                      
        listBox = Listbox(DataFrameRight,font=("arial",12,"bold"),bg="bisque",fg="black",width=40,height=12)
        listBox.bind('<<ListboxSelect>>',SelectedBook)
        listBox.grid(row=0,column=0,padx=4)

        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)

        #====================================================Button Frame ==========================================================

        Framebutton =Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="NavajoWhite2")
        Framebutton.place(x=0,y=455,width=1530,height=70)

        btnAddData=Button(Framebutton,command=self.add_data,text="Add Books",font=("arial",12,"bold"),width=23,bg="NavajoWhite4",fg="white")
        btnAddData.grid(row=0,column=0)

        btnUpdateData=Button(Framebutton,command=self.update_data,text="Update Books",font=("arial",12,"bold"),width=23,bg="NavajoWhite4",fg="white")
        btnUpdateData.grid(row=0,column=1)

        btnDeleteData=Button(Framebutton,command=self.dbook,text="Delete Books",font=("arial",12,"bold"),width=23,bg="NavajoWhite4",fg="white")
        btnDeleteData.grid(row=0,column=2)

##        btnReset=Button(Framebutton,text="Reset",font=("arial",12,"bold"),width=23,bg="NavajoWhite4",fg="white")
##        btnReset.grid(row=0,column=3)

        btnExit=Button(Framebutton,command=self.iexit,text="Exit",font=("arial",12,"bold"),width=23,bg="NavajoWhite4",fg="white")
        btnExit.grid(row=0,column=3)

        

        #==========================================================Information Frame==========================================================
        
##        FrameDetails =Frame(self.root,bd=12,relief=RIDGE,padx=20)
##        FrameDetails.place(x=0,y=510,width=1530,height=195)
        
        
        load= Image.open("top4.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self.root,image=render)
        img.image=render
        img.place(x=0,y=500)
        #img.pack()

    def add_data(self):
        conn=pymysql.connect(host="localhost",user="root",password="",database="librarymanagement")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into admin values(%s,%s,%s,%s)",(
                                                                self.id_var.get(),
                                                                self.name_var.get(),
                                                                self.author_var.get(),
                                                                self.quantity_var.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success","Book details added succesfully",parent=self.root)
        self.root.destroy()
        self.__init__(Tk.Toplevel())


    def update_data(self):
        conn=pymysql.connect(host="localhost",user="root",password="",database="librarymanagement")
        my_cursor=conn.cursor()
        my_cursor.execute("update admin set Book_Name=%s,Book_Author=%s,Book_Quantity=%s where Book_Id=%s",(
                                                                self.name_var.get(),
                                                                self.author_var.get(),
                                                                self.quantity_var.get(),
                                                                self.id_var.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success","Details updated succesfully",parent=self.root)
        self.root.destroy()
        self.__init__(Tk.Toplevel())
    

    def dbook(self):
        conn=pymysql.connect(host="localhost",user="root",password="",database="librarymanagement")
        my_cursor=conn.cursor()
        my_cursor.execute("delete from admin where Book_Id=%s",(self.id_var.get(),))
        conn.commit()
        messagebox.showinfo("Success","Details deleted succesfully",parent=self.root)
        self.root.destroy()
        self.__init__(Tk.Toplevel())
       

    def iexit(self):
        iexit = messagebox.askyesno("Library Managemment System", "Do you want to exit",parent=self.root)
        if iexit>0:
            self.root.destroy()
            return




def ucall():
    window = Tk.Toplevel()
    obj = LibraryManagementSystem(window)
    window.mainloop()
ucall()





















