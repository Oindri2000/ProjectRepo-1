from tkinter import *
from tkinter import ttk,messagebox
import sqlite3

from setuptools import Command
import time
import os
import tempfile

class billclass:
    def __init__(self,root,):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("shop management")
        self.root.config(bg="blue")
        self.cart_list=[]
        self.chk_print=0
        title=Label(self.root,text="shop management system",font=("time new roman",40,"bold"),anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        btn_logout=Button(self.root,text="logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1100,y=10,height=30,width=150)
        self.lbl_clock=Label(self.root,text="welcom \t\t Date:DD-MM-YYYY \t\t Time:HH:MM:SS \t\t",font=("times new roman",15),bg="green",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #====product_Frame====
        

        
        productFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        productFrame1.place(x=6,y=110,width=410,height=550)

        pTitle=Label(productFrame1,text="ALL PRODUCTS",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        #=====product search frame=====

        self.var_search=StringVar()


        productFrame2=Frame(productFrame1,bd=2,relief=RIDGE,bg="white")
        productFrame2.place(x=2,y=42,width=398,height=90)

        lbl_search=Label(productFrame2,text="Search Product | By Name",font=("times new roman",15,"bold"),bg="white",fg="green").place(x=2,y=5)
        lbl_search=Label(productFrame2,text="Product Name",font=("times new roman",15,"bold"),bg="white").place(x=2,y=45)

        txt_search=Entry(productFrame2,textvariable=self.var_search,font=("times new roman",15),bg="lightyellow").place(x=128,y=47,width=150,height=22)

        btn_search=Button(productFrame2,text="search",command=self.search,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=285,y=45,width=100,height=25)
        btn_show_all=Button(productFrame2,text="Show All",command=self.show,font=("goudy old style",15),bg="#083531",fg="white",cursor="hand2").place(x=285,y=10,width=100,height=25)
         #emp details
        cart_frame=Frame(productFrame1,bd=3,relief=RIDGE)
        
        cart_frame.place(x=2,y=140,width=398,height=375)
        scrolly=Scrollbar(cart_frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_frame,orient=HORIZONTAL)
        self.product_table=ttk.Treeview(cart_frame,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)
        

        self.product_table.heading ("pid",text="PID ")
        self.product_table.heading ("name",text="NAME")
        
        self.product_table.heading ("price",text="PRICE")
        
        self.product_table.heading ("qty",text="QTY")
        self.product_table.heading ("status",text="Status")
        
        
        self.product_table["show"]="headings"

         
        self.product_table.column ("pid",width=90)
        self.product_table.column ("name",width=100)
        self.product_table.column ("price",width=100)
        self.product_table.column("qty",width=100)
        self.product_table.column("status",width=100)
       # self.product_table["show"]="headings"

        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)
       
        lbl_note=Label(productFrame1,text="Note:'Enter o Quantity to remove productfrom the Cart'",font=("goudy old style",12),anchor='w',bg="white",fg="red").pack(side=BOTTOM,fill=X)
        #=====Customer Frame====
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=420,y=110,width=530,height=70)
        cTitle=Label(CustomerFrame,text="Customer Details",font=("goudy old style",15),bg="lightgray",fg="black").pack(side=TOP,fill=X)
        lbl_name=Label(CustomerFrame,text=" Name",font=("times new roman",15),bg="white").place(x=5,y=35)

        txt_name=Entry(CustomerFrame,textvariable=self.var_cname,font=("times new roman",13),bg="lightyellow").place(x=80,y=35,width=180)

        lbl_contact=Label(CustomerFrame,text=" Contact",font=("times new roman",15),bg="white").place(x=270,y=35)

        txt_contact=Entry(CustomerFrame,textvariable=self.var_contact,font=("times new roman",13),bg="lightyellow").place(x=380,y=35,width=140)

        Cal_Cart_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Cal_Cart_Frame.place(x=420,y=190,width=530,height=360)
        #=======calculator Frame======
        self.var_cal_input=StringVar()

        Cal_Frame=Frame(Cal_Cart_Frame,bd=9,relief=RIDGE,bg="white")
        Cal_Frame.place(x=5,y=10,width=268,height=340)
        txt_cal_input=Entry(Cal_Frame,textvariable=self.var_cal_input,font=('arial',15,"bold"),width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)
        btn_7=Button(Cal_Frame,text='7',font=('arial',15,'bold'),command=lambda:self.get_input(7),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=0)
        btn_8=Button(Cal_Frame,text='8',font=('arial',15,'bold'),command=lambda:self.get_input(8),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=1)
        btn_9=Button(Cal_Frame,text='9',font=('arial',15,'bold'),command=lambda:self.get_input(9),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=2)
        btn_sum=Button(Cal_Frame,text='+',font=('arial',15,'bold'),command=lambda:self.get_input('+'),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=3)

        btn_4=Button(Cal_Frame,text='4',font=('arial',15,'bold'),command=lambda:self.get_input(4),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=0)
        btn_5=Button(Cal_Frame,text='5',font=('arial',15,'bold'),command=lambda:self.get_input(5),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=1)
        btn_6=Button(Cal_Frame,text='6',font=('arial',15,'bold'),command=lambda:self.get_input(6),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=2)
        btn_sub=Button(Cal_Frame,text='-',font=('arial',15,'bold'),command=lambda:self.get_input('-'),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=3)

        btn_3=Button(Cal_Frame,text='3',font=('arial',15,'bold'),command=lambda:self.get_input(3),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=0)
        btn_2=Button(Cal_Frame,text='2',font=('arial',15,'bold'),command=lambda:self.get_input(2),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=1)
        btn_1=Button(Cal_Frame,text='1',font=('arial',15,'bold'),command=lambda:self.get_input(1),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=2)
        btn_mul=Button(Cal_Frame,text='*',font=('arial',15,'bold'),command=lambda:self.get_input('*'),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=3)

        btn_0=Button(Cal_Frame,text='0',font=('arial',15,'bold'),command=lambda:self.get_input(0),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=0)
        btn_c=Button(Cal_Frame,text='c',font=('arial',15,'bold'),command=self.clear_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=1)
        btn_eq=Button(Cal_Frame,text='=',font=('arial',15,'bold'),command=self.perform_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=2)
        btn_div=Button(Cal_Frame,text='/',font=('arial',15,'bold'),command=lambda:self.get_input('/'),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=3)

         #emp details
        cart_frame=Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)
        
        cart_frame.place(x=280,y=8,width=245,height=342)
        self. cartTitle=Label(cart_frame,text="Caet\t Total Product:[0]",font=("goudy old style",15),bg="lightgray",fg="black")
        self.cartTitle.pack(side=TOP,fill=X)

        scrolly=Scrollbar(cart_frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_frame,orient=HORIZONTAL)
        self.CartTable=ttk.Treeview(cart_frame,columns=("pid","name","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)
 
        self.CartTable.heading ("pid",text="PID ")
        self.CartTable.heading ("name",text="NAME")
            
        self.CartTable.heading ("price",text="PRICE")
            
        self.CartTable.heading ("qty",text="QTY")
        
            
        self.CartTable["show"]="headings"

            
        self.CartTable.column ("pid",width=40)
        self.CartTable.column ("name",width=90)
        self.CartTable.column ("price",width=90)
        self.CartTable.column("qty",width=50)
        
            #self.CartTable["show"]="headings"

        self.CartTable.pack(fill=BOTH,expand=1)
        self.CartTable.bind("<ButtonRelease-1>",self.get_data_cart)
        #===ADD CART BUTTONS======

        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_qty=StringVar()
        self.var_price=StringVar()
        self.var_stock=StringVar()

        Add_CartWidgetsFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Add_CartWidgetsFrame.place(x=420,y=550,width=530,height=110)


        lbl_p_name=Label(Add_CartWidgetsFrame,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_p_name=Entry(Add_CartWidgetsFrame,textvariable=self.var_pname,font=("times new roman",15),state='readonly',bg="lightyellow").place(x=5,y=35,width=190,height=22)

        lbl_p_price=Label(Add_CartWidgetsFrame,text="Price per Qty",font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_p_price=Entry(Add_CartWidgetsFrame,textvariable=self.var_price,font=("times new roman",15),state='readonly',bg="lightyellow").place(x=230,y=35,width=150,height=22)

        lbl_p_qty=Label(Add_CartWidgetsFrame,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_p_qty=Entry(Add_CartWidgetsFrame,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow").place(x=390,y=35,width=120,height=22)

        self.lbl_instock=Label(Add_CartWidgetsFrame,text="In stock ",font=("times new roman",15),bg="white")
        self.lbl_instock.place(x=5,y=70)

        btn_clear_caet=Button(Add_CartWidgetsFrame,text="Clear",command=self.clear_cart,font=("times new roman",15,"bold"),bg="gray",cursor="hand2").place(x=180,y=70,width=150,height=30)

        btn_add_caet=Button(Add_CartWidgetsFrame,text="Add | Update Cart",command=self.add_update_cart,font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=340,y=70,width=180,height=30)

        #===========billing area
        billFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billFrame.place(x=953,y=110,width=410,height=410)
        bTitle=Label(billFrame,text="Customer Bill Area",font=("goudy old style",20,"bold"),bg="#f44336",fg="white").pack(side=TOP,fill=X)
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        self.text_bill_area=Text(billFrame,yscrollcommand=scrolly.set)
        self.text_bill_area.pack(fill=BOTH,expand=1)
        scrolly.pack(side=RIGHT,fill=Y)
        scrolly.config(command=self.text_bill_area.yview)

        #=========billing button======
        billMenuFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billMenuFrame.place(x=953,y=520,width=410,height=140)

        self.lbl_amnt=Label(billMenuFrame,text="Bill Amount[0]",font=("goudy old style",14,"bold"),bg="#3f51b5",fg="white")
        self.lbl_amnt.place(x=2,y=5,width=120,height=70)

        self.lbl_discount=Label(billMenuFrame,text="Discount[5%]",font=("goudy old style",15,"bold"),bg="#8bc34a",fg="white")
        self.lbl_discount.place(x=124,y=5,width=120,height=70)

        self.lbl_net_pay=Label(billMenuFrame,text="Net Pay[0]",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white")
        self.lbl_net_pay.place(x=246,y=5,width=160,height=70)

        btn_print=Button(billMenuFrame,text="Print",cursor="hand2",command=self.print_bill,font=("goudy old style",15,"bold"),bg="orange",fg="white")
        btn_print.place(x=2,y=80,width=120,height=50)

        btn_clear_all=Button(billMenuFrame,text="Clear All",cursor="hand2",command=self.clear_all,font=("goudy old style",15,"bold"),bg="gray",fg="white")
        btn_clear_all.place(x=124,y=80,width=120,height=50)

        btn_generate=Button(billMenuFrame,text="Generate Bill/Save Bill",command=self.generate_bill,cursor="hand2",font=("goudy old style",11,"bold"),bg="#009688",fg="white")
        btn_generate.place(x=246,y=80,width=160,height=50)

        #========Footer=====
        footer=Label(self.root,text="SHOP MANAGEMENT SYSTEM |DEVELOPED BY OINDRILA\n",font=("times new roman",15),bg="black",fg="white",bd=1,cursor="hand2").pack(side=BOTTOM,fill=X)
        self.show()
        #self.bill_top()
        self.update_date_time()

        #======all functions=======
    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)

    def clear_cal(self):
        self.var_cal_input.set('')

    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    def show(self):
        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        try:
            #self.product_table=ttk.Treeview(cart_frame,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
            cur.execute("select pid,name,price,qty,status from product")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("error",f"error due to: {str(ex)}",parent=self.root)


    def search(self):
        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        try:
           
            if self.var_search.get()=="":
                messagebox.showerror("error","search input should be required",parent=self.root)
            else:
                cur.execute("select pid,name,price,qty,status  from product where name LIKE '%"+self.var_search.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('',END,values=row)
                else:
                    messagebox.showerror("error","no record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("error",f"error due to: {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_qty.set('1')
        self.var_stock.set(row[3])
       
        self.var_price.set(row[2])
        self.lbl_instock.config(text=f"In stock[{str(row[3])}]")
    def add_update_cart(self):
        if self.var_pid.get()=='':
            messagebox.showerror('error',"please select product from the list",parent=self.root)
        
        elif self.var_qty.get()=='':
            messagebox.showerror('error',"quantity is required",parent=self.root)

        elif int(self.var_qty.get())>int(self.var_stock.get()):
            messagebox.showerror('error',"Invalid Quantity",parent=self.root)
        else:

            #price_cal=int(self.var_qty.get())*float(self.var_price.get())
            #price_cal=float(price_cal)
            price_cal=self.var_price.get()
            cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get(),self.var_stock.get()]
           
            #=====update_cart=====
            present='no'
            index_=0
            for row in self.cart_list:
                if self.var_pid.get()==row[0]:
                    
                    present='yes'
                    break
                index_+=1

            if present=='yes':
                op=messagebox.askyesno('confirm',"product alresdy present\n do you want to update or remove from the cart list",parent=self.root)
                if op==True:
                    if self.var_qty.get()=="0":
                        self.cart_list.pop(index_)
                    else:
                        #self.cart_list[index_][2]=price_cal
                        self.cart_list[index_][3]=self.var_qty.get()

            else:

                self.cart_list.append(cart_data)


            self.show_cart()
            self.bill_update()

    def bill_update(self):
        self.bill_amnt=0
        self.net_pay=0
        self.discount=0
        for row in self.cart_list:
            self.bill_amnt=self.bill_amnt+(float(row[2])*int(row[3]))


        self.discount=(self.bill_amnt*5 )/100    
        self.net_pay=self.bill_amnt-self.discount

        self.lbl_amnt.config(text=f'bill amnt\n{str(self.bill_amnt)}')
        self.lbl_net_pay.config(text=f'net pay\n{str(self.net_pay)}') 
        self.cartTitle.config(text=f"Caet\t Total Product:[{str(len(self.cart_list))}]" )    
            

    def show_cart(self):
        
        try:

            
            self.CartTable.delete(*self.CartTable.get_children())
            for row in self.cart_list:
                self.CartTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("error",f"error due to: {str(ex)}",parent=self.root)

    def get_data_cart(self,ev):
        f=self.CartTable.focus()
        content=(self.CartTable.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_qty.set(row[3])
        self.var_stock.set(row[4])
       
        self.var_price.set(row[2])
        self.lbl_instock.config(text=f"In stock[{str(row[4])}]")


    def generate_bill(self):
        if self.var_cname.get()=='' or self.var_contact.get()=='':
            messagebox.showerror("error",f"Customer Details are required",parent=self.root)
        elif len(self.cart_list)==0:
            messagebox.showerror("error",f"Please Add Product to the Cart!!",parent=self.root)
        else:
            #=========BILL TOP=====
            self.bill_top()
            #=========BILL MIDDLE=====
            self.bill_middle()
            #=========BILL BOTTOM=====
            self.bill_bottom()

            fp=open(f'bill/{str(self.invoice)}.txt','w')
            fp.write(self.text_bill_area.get('1.0',END))
            fp.close()
            messagebox.showinfo('saved',"Bill has been Generayed/Save in Backend",parent=self.root)
            self.chk_print=1
 

    def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        bill_top_temp=f'''
\t\tXYZ-Inventory
\t Phone NO. 75508***** ,Barasat-700126
{str("="*47)}
 Customer Name: {self.var_cname.get()}
 Ph no.:{self.var_contact.get()}
 Bill no. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*47)}
 Product Name\t\t\tqty\tprice
{str("="*47)}
        '''
        self.text_bill_area.delete('1.0',END)
        self.text_bill_area.insert('1.0',bill_top_temp)

    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*47)}
 Bill Amount\t\t\t\tRs.{self.bill_amnt}
 Discount\t\t\t\tRs.{self.discount}
 Net Pay\t\t\t\tRs.{self.net_pay}
{str("="*47)}\n
        '''
        self.text_bill_area.insert(END,bill_bottom_temp)

    def bill_middle(self):
        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        try:

            for row in self.cart_list:
                pid=row[0]
                name=row[1]
                qty=int(row[4])-int(row[3])
                if int(row[3])==int(row[4]):
                    status='Inactive'
                if int(row[3])<int(row[4]):
                    status='Active'    
                price=float(row[2])*int(row[3])
                price=str(price)
                self.text_bill_area.insert(END,"\n "+name+"\t\t\t"+row[3]+"\tRs."+price)
                #=======update qty in product table=======
                cur.execute('update product set qty=?,status=? where pid=?',(
                    qty,
                    status,
                    pid
                ))
                con.commit()
            con.close()
            self.show()

        except Exception as ex:
            messagebox.showerror("error",f"error due to: {str(ex)}",parent=self.root)
    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_qty.set('')
        self.var_stock.set('')
       
        self.var_price.set('')
        self.lbl_instock.config(text=f"In stock")
    def clear_all(self):
        self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.text_bill_area.delete('1.0',END)
        self.cartTitle.config(text=f"Caet\t Total Product:[0]" )
        self.var_search.set('')    
        self.clear_cart()
        self.show()
        self.show_cart()

    def update_date_time(self):
        time_=time.strftime("%I:%M:%S")
        date_=time.strftime("%d-:%m-:%Y")
        self.lbl_clock.config(text=f"welcom \t\t Date:{str(date_)} \t\t Time:{str(time_)}")
        self.lbl_clock.after(200,self.update_date_time)

    def print_bill(self):
        if self.chk_print==1:
            messagebox.showinfo('print',"Please wait while printing",parent=self.root)
            new_file=tempfile.mktemp('.txt')
            open(new_file,'w').write(self.text_bill_area.get('1.0',END))
            os.startfile(new_file,'print')

        else:
            messagebox.showerror('print',"Please Generate Bill to print the receipt",parent=self.root)

if __name__=="__main__":    
    root=Tk()
    obj=billclass(root)
    root.mainloop () 