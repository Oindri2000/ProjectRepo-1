

from asyncore import compact_traceback
from gettext import Catalog
from tkinter import *
from unicodedata import category
from employe import employeclass
from supplier import suppierClass
from catagory import catagoryClass
from product import productclass
from sales import salesclass
from billing import billclass
import sqlite3
from tkinter import messagebox
import os
import time
from asyncore import compact_traceback
class ims:
    def __init__(self,root,):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("shop management")
        self.root.config(bg="blue")
        title=Label(self.root,text="shop management system",font=("time new roman",40,"bold"),anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        #btn_logout=Button(self.root,text="logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1100,y=10,height=30,width=150)
        self.lbl_clock=Label(self.root,text="welcom \t\t Date:DD-MM-YYYY \t\t Time:HH:MM:SS \t\t",font=("times new roman",15),bg="green",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        left_Menu=Frame(self.root,bd=2,relief=RIDGE)
        left_Menu.place(x=0,y=102,width=200,height=568)
        lbl_menu=Label(left_Menu,text="Menu",font=("times new roman ",20),bg="red").pack(side= TOP,fill=X)
        
        btn_employe=Button(left_Menu,text="employe",command=self.employe,font=("time new roman",20,"bold"),bg="skyblue",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supply=Button(left_Menu,text="supply",command=self.supplier,font=("time new roman",20,"bold"),bg="yellow",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_catagory=Button(left_Menu,text="catagory",command=self.catagory,font=("time new roman",20,"bold"),bg="pink",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(left_Menu,text="product",command=self.product,font=("time new roman",20,"bold"),bg="purple",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(left_Menu,text="sales",command=self.sales,font=("time new roman",20,"bold"),bg="orange",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_bill=Button(left_Menu,text="billing",command=self.billing,font=("time new roman",20,"bold"),bg="green",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        

        #btn_exit=Button(left_Menu,text="exit",font=("time new roman",20,"bold"),bg="red",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        lbl_footer=Label(self.root,text="store management system | developed by Oindrila",font=("time new roman",15),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)


       
        self.lbl_employe=Label(self.root,text="Total Employe \n[0]",bg="black",fg="white",font=("time new roman",20,"bold"))
        self.lbl_employe.place(x=650,y=120,height=150,width=300)
        self.lbl_supply=Label(self.root,text="Total Supply \n[0]",bg="black",fg="white",font=("time new roman",20,"bold"))
        self.lbl_supply.place(x=1000,y=120,height=150,width=300)
        self.lbl_catagory=Label(self.root,text="Total Catagory \n[0]",bg="black",fg="white",font=("time new roman",20,"bold"))
        self.lbl_catagory.place(x=300,y=300,height=150,width=300)
        self.lbl_product=Label(self.root,text="Total Product \n[0]",bg="black",fg="white",font=("time new roman",20,"bold"))
        self.lbl_product.place(x=650,y=300,height=150,width=300)
        self.lbl_sales=Label(self.root,text="Total Sales \n[0]",bg="black",fg="white",font=("time new roman",20,"bold"))
        self.lbl_sales.place(x=1000,y=300,height=150,width=300)
        self.update_content()


        
    def employe(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeclass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=suppierClass(self.new_win)

    def catagory(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=catagoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productclass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesclass(self.new_win)

    def billing(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=billclass(self.new_win)


    def update_content(self):
        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f'Total Product \n[{str(len(product))}]')

            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supply.config(text=f'Total supplier \n[{str(len(supplier))}]')
            bill=len(os.listdir('bill'))

            self.lbl_sales.config(text=f'Total Sales  [{str(bill)}]')

            cur.execute("select * from catagory")
            catagory=cur.fetchall()
            self.lbl_catagory.config(text=f'Total catagory \n[ {str(len(catagory))}]')


            cur.execute("select * from employe")
            employe=cur.fetchall()
            self.lbl_employe.config(text=f'Total employe \n[ {str(len(employe))}]')
            

            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-:%m-:%Y")
            self.lbl_clock.config(text=f"welcom \t\t Date:{str(date_)} \t\t Time:{str(time_)}")
            self.lbl_clock.after(200,self.update_content)

        except Exception as ex:
            messagebox.showerror("Error",f"error due to:{str(ex)}",parent=self.root)
    
 

if __name__=="__main__":    
    root=Tk()
    obj=ims(root)
    root.mainloop ()  
 