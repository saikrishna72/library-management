# User interface

import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox
from PIL import Image, ImageTk


    
class LibraryManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1500x800+0+0")
        self.id_var=StringVar()
        self.name_var=StringVar()
        self.author_var=StringVar()
        self.price_var=StringVar()
        self.issue_var=StringVar()
        self.return_var=StringVar()
        

        lbltitle = Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="NavajoWhite2",fg="NavajoWhite4",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        

        frame = Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="NavajoWhite4")
        frame.place(x=0,y=130,width=1500,height=350)


        #IMAGE=================================================
        
        image = Image.open('lib.jpg')
        img = ImageTk.PhotoImage(image)
        label1 = Label(self.root,image=img)
        label1.image=img
        label1.place(x=0,y=530)

        
        #DataFrame Left=================================================
        

        

        DataFrameLeft=LabelFrame(frame,text="User Section",bg="NavajoWhite2",fg="NavajoWhite4",bd=12,relief=RIDGE,font=("arial",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=500,height=320)


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

        lblBookPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text=" Price",padx=2,bg="NavajoWhite2")
        lblBookPrice.grid(row=6,column=0,sticky=W)
        txtBookPrice=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.price_var,width=29)
        txtBookPrice.grid(row=6,column=1)
        
        lblBlank1=Label(DataFrameLeft,font=("arial",12,"bold"),text="",padx=2,bg="NavajoWhite2")
        lblBlank1.grid(row=7,column=0,sticky=W)

        lblBookIssue=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date",padx=2,bg="NavajoWhite2")
        lblBookIssue.grid(row=8,column=0,sticky=W)
        txtBookIssue=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.issue_var,width=29)
        txtBookIssue.grid(row=8,column=1)

        lblBlank1=Label(DataFrameLeft,font=("arial",12,"bold"),text="",padx=2,bg="NavajoWhite2")
        lblBlank1.grid(row=9,column=0,sticky=W)

        lblBookReturn=Label(DataFrameLeft,font=("arial",12,"bold"),text="Return Date",padx=2,bg="NavajoWhite2")
        lblBookReturn.grid(row=10,column=0,sticky=W)
        txtBookReturn=Entry(DataFrameLeft,font=("arial",12,"bold"),textvariable=self.return_var,width=29)
        txtBookReturn.grid(row=10,column=1)


        #DataFrame RIGHT==============================================================================================

        DataFrameRight=LabelFrame(frame,text="Available Books",bg="NavajoWhite2",fg="NavajoWhite4",bd=12,relief=RIDGE,font=("arial",12,"bold"))
        DataFrameRight.place(x=515,y=5,width=360,height=320)

##        Active User
        
        mydb=pymysql.connect(host="localhost",user="root",password="",database="librarymanagement")
        mycursor=mydb.cursor()
        mycursor.execute("select Username from login")
        lst1=[]
        for i in mycursor.fetchall():
            lst1.append(i[0])
        demo=len(lst1)-1
        global obj1
        obj1=lst1[demo]
        print(obj1)
        mydb.close()
        lbltitle1 = Label(self.root,text=f"Welcome  {obj1}",bg="NavajoWhite2",fg="NavajoWhite4",font=("times new roman",20,"bold"),padx=2,pady=6)
        lbltitle1.place(x=30,y=100)

        def show():
            mydb=pymysql.connect(host="localhost",user="root",password="",database="librarymanagement")
            mycursor=mydb.cursor()
            mycursor.execute("SELECT * FROM admin")
            rows= mycursor.fetchall()

            for row in rows:
                insertdata=row[1]
                txtDisplayR.insert(END,insertdata)
                txtDisplayR.pack()
            mydb.close()

        def SelectedBook(event=''):
            value=txtDisplayR.get(txtDisplayR.curselection())
            w=value
            conn=pymysql.connect(host="localhost",user="root",password="",database="librarymanagement")
            c=conn.cursor()        
            c.execute("SELECT * FROM admin WHERE Book_Name =%s",(w,))
            
            for row in c.fetchall():
                self.id_var.set(str(row[0]))
                self.name_var.set(str(row[1]))
                self.author_var.set(str(row[2]))
                self.price_var.set(str(row[3]))
                
                import datetime

                d1=datetime.date.today()
                d2=datetime.timedelta(14)
                d3=d1+d2
                self.issue_var.set(str(d1))
                self.return_var.set(str(d3))
            
        txtDisplayR=Listbox(DataFrameRight, font=("arial", 12, "bold"),width=30, height=13)
        show()
        #
        txtDisplayR.grid(row=0, column=2)
        txtDisplayR.bind('<<ListboxSelect>>',SelectedBook)
        scrollbar=Scrollbar(DataFrameRight)
        scrollbar.grid(row=0,column=3,sticky='ns')
        

        #DataFrameRight1==================================================================================================

        DataFrameRight1=LabelFrame(frame,text="Issued Books",bg="NavajoWhite2",fg="NavajoWhite2",bd=12,relief=RIDGE,font=("arial",12,"bold"))
        DataFrameRight1.place(x=890,y=5,width=450,height=320)

        lblBook_Name1=Label(DataFrameRight1,font=("arial",12,"bold"),text="Book Names",padx=5,bg="NavajoWhite2",fg="NavajoWhite4")
        lblBook_Name1.grid(row=0,column=0,sticky=W)

        

        lblBook_Name1=Label(DataFrameRight1,font=("arial",12,"bold"),text="Return Date",padx=5,bg="NavajoWhite2",fg="NavajoWhite4")
        lblBook_Name1.grid(row=0,column=1,sticky=W)

        def show_issued_books():
            global temp
            temp =[]
            mydb=pymysql.connect(host="localhost",user="root",password="",database="librarymanagement")
            mycursor=mydb.cursor()
            mycursor.execute("SELECT Book_Name, Return_date FROM issuedbooks where Username =%s",(obj1,))
            rows= mycursor.fetchall()
            for row in rows:
                temp2=[]
                temp2.append(row[0])
                temp2.append(row[1])
                temp.append(temp2)
            mydb.close()
        def Selected_IssueBook(event=''):
            value=issueBox.get(issueBox.curselection())
            w=value
            print(w)
            conn=pymysql.connect(host="localhost",user="root",password="",database="librarymanagement")
            c=conn.cursor()
            c.execute("SELECT * FROM issuedbooks WHERE Book_Name =%s",(w,))
            for row in c.fetchall():
                self.id_var.set(str(row[0]))
                self.name_var.set(str(row[1]))
                self.author_var.set(str(row[6]))
                self.price_var.set(str(row[3]))
                self.issue_var.set(str(row[4]))

 

                import datetime

 

                d1=datetime.date.today()
                self.return_var.set(str(d1))
            
        issueBox = Listbox(DataFrameRight1,font=("arial",12,"bold"),bg="bisque",fg="black",width=24,height=12)
        issueBox.grid(row=1,column=0,padx=4)
        show_issued_books()
        issueBox.bind('<<ListboxSelect>>',Selected_IssueBook)
        listScrollbar = Scrollbar(DataFrameRight1)
        listScrollbar.grid(row=1,column=1,sticky="ns")
        listScrollbar.config(command=issueBox.yview)

        issueBox1 = Listbox(DataFrameRight1,font=("arial",12,"bold"),bg="bisque",fg="black",width=19,height=12)
        issueBox1.grid(row=1,column=1,padx=4)

        for item in temp:
            issueBox.insert(END,item[0])
            issueBox1.insert(END,item[1])
        
        #====================================================Button Frame ==========================================================

        Framebutton =Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="NavajoWhite2")
        Framebutton.place(x=0,y=480,width=1500,height=70)
        la1=Label(Framebutton,text="                                                  ")
        la1.grid(row=0,column=1)
        
        la2=Label(Framebutton,text="                                                  ")
        la2.grid(row=0,column=3)

        la3=Label(Framebutton,text="                                                  ")
        la3.grid(row=0,column=5)


        btnAddData=Button(Framebutton,text="Apply Book",font=("arial",12,"bold"),width=23,bg="NavajoWhite4",fg="white",command=self.apply_book)
        btnAddData.grid(row=0,column=0)

        btnUpdateData=Button(Framebutton,text="Return Books",font=("arial",12,"bold"),width=23,bg="NavajoWhite4",fg="white",command=self.return_book)
        btnUpdateData.grid(row=0,column=2)

        btnDeleteData=Button(Framebutton,text="Reset",font=("arial",12,"bold"),width=23,bg="NavajoWhite4",fg="white",command=self.iReset2)
        btnDeleteData.grid(row=0,column=4)

        btnReset=Button(Framebutton,text="Exit",font=("arial",12,"bold"),width=23,bg="NavajoWhite4",fg="white",command=self.iexit)
        btnReset.grid(row=0,column=6)
        


        #==========================================================Information Frame==========================================================


    def apply_book(self):
        mydb=pymysql.connect(host="localhost",user="root",password="",database="librarymanagement")
        mycursor=mydb.cursor()
##        mycursor.execute("select Username from login")
##        lst1=[]
##        
##        for i in mycursor.fetchall():
##            lst1.append(i[0])
##        obj=len(lst1)-1
##        obj1=lst1[obj]
##        print(obj1)
        mycursor.execute("insert into issuedbooks values(%s,%s,%s,%s,%s,%s,%s)",(

                                                                        self.id_var.get(),
                                                                        self.name_var.get(),
                                                                        obj1,
                                                                        self.price_var.get(),
                                                                        self.issue_var.get(),
                                                                        self.return_var.get(),
                                                                        self.author_var.get()                                                                                                                                             
                                                                        
                                                                        ))
        
        
        mycursor.execute("select Book_Quantity from admin where Book_Id=%s",(self.id_var.get(),))
        for item in mycursor.fetchall():
                new_quantity = item[0]-1
       
        mycursor.execute("UPDATE admin set Book_Quantity=%s where Book_Id=%s",(new_quantity, self.id_var.get(),))
                                                                        
                                                                        
                                                                        
                                                        
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Library Issued Details","Book has been Issued successfully",parent=self.root)
        self.root.destroy()
        self.__init__(tkinter.Toplevel())


    def return_book(self):
        mydb=pymysql.connect(host="localhost",user="root",password="",database="librarymanagement")
        mycursor=mydb.cursor()
        mycursor.execute("DELETE FROM issuedbooks WHERE Book_Id=%s",(
##                                                                        self.name_var.get(),))
                                                                        #self.author_var.get(),
                                                                        self.id_var.get(),))
                                                                        #self.price_var.get(),
                                                                        #self.issue_var.get(),
        mycursor.execute("select Book_Quantity from admin where Book_Id=%s",(self.id_var.get(),))
        for item in mycursor.fetchall():
                new_quantity = item[0]+1
        
        mycursor.execute("UPDATE admin set Book_Quantity=%s where Book_Id=%s",(new_quantity, self.id_var.get(),)) 
                                                
        mydb.commit()
        messagebox.showinfo("Library Returned Details","Book is returned successfully",parent=self.root)
        self.root.destroy()
        self.__init__(tkinter.Toplevel())

    def iReset2(self):
        self.id_var.set("")
        self.name_var.set("")
        self.author_var.set("")
        self.price_var.set("")
        self.issue_var.set("")
        self.return_var.set("")
            
            
        
    def iexit(self):
        iexit=messagebox.askyesno("Library management system","Do you want to exit",parent=self.root)
        if iexit>0:
            self.root.destroy()
            return
    
        


#if __name__ == "__main__":
    #root = Tk()
def lcall():
    window=tkinter.Toplevel()
    obj = LibraryManagementSystem(window)
    window.mainloop()


lcall()
