from tkinter import *
from tkinter import ttk,messagebox
import sqlite3

class productclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+200+130")
        self.root.title("SHOP MANAGEMENT SYSTEM")
        self.root.focus_force()


        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        self.var_pid=StringVar()

        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        product_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=10,width=450,height=480,)
#title=======
        title=Label(product_Frame,text=" MANAGE PRODUCT  DETAILS",font=("goudy old style",18,"bold"),bg="blue",fg="white").pack(side=TOP,fill=X)

        lbl_category=Label(product_Frame,text="Catagory",font=("goudy old style",18,"bold"),bg="white").place(x=30,y=60)
        lbl_supplier=Label(product_Frame,text="Supplier",font=("goudy old style",18,"bold"),bg="white").place(x=30,y=110)
        lbl_product_name=Label(product_Frame,text="Name",font=("goudy old style",18,"bold"),bg="white").place(x=30,y=160)
        lbl_price=Label(product_Frame,text="Price",font=("goudy old style",18,"bold"),bg="white").place(x=30,y=210)
        lbl_quantity=Label(product_Frame,text="Quantity",font=("goudy old style",18,"bold"),bg="white").place(x=30,y=260)
        lbl_status=Label(product_Frame,text="Status",font=("goudy old style",18,"bold"),bg="white").place(x=30,y=310)



       #======COLUMN2

        Cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=self.cat_list,state="readonly",justify=CENTER)
        Cmb_cat.place(x=150,y=60,width=200)
        Cmb_cat.current(0)


        Cmb_sup=ttk.Combobox(product_Frame,textvariable=self.var_sup,values=self.sup_list,state="readonly",justify=CENTER)
        Cmb_sup.place(x=150,y=110,width=200)
        Cmb_sup.current(0)

        txt_name=Entry(product_Frame,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=160,width=200)
        
        txt_price=Entry(product_Frame,textvariable=self.var_price,font=("goudy old style",15),bg="lightyellow").place(x=150,y=210,width=200)
        
        txt_qty=Entry(product_Frame,textvariable=self.var_qty,font=("goudy old style",15),bg="lightyellow").place(x=150,y=260,width=200)

        Cmb_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Activet","Inactive"),state="readonly",justify=CENTER)
        Cmb_status.place(x=150,y=310,width=200)
        Cmb_status.current(0)

        #button
        btn_add=Button(product_Frame,text="save", command=self.add,font=("goudy old style",15),bg="green",fg="white",cursor="hand2").place(x=10,y=400,width=100,height=40)
        btn_update=Button(product_Frame,text="update",command=self.update,font=("goudy old style",15),bg="lightblue",fg="white",cursor="hand2").place(x=120,y=400,width=100,height=40)
        btn_deleter=Button(product_Frame,text="delete",command=self.delete,font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=230,y=400,width=100,height=40)
        btn_clear=Button(product_Frame,text="clear",command=self.clear,font=("goudy old style",15),bg="orange",fg="white",cursor="hand2").place(x=340,y=400,width=100,height=40)
        #===SEARCHFRAME
        SearchFrame=LabelFrame(self.root,text="Search employee",font=("goudy old style",12,"bold"),bd=2,bg="white")
        SearchFrame.place(x=480,y=10,width=600,height=80)
        Cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("select","catagory","supplier","name"),state="readonly",justify=CENTER)
        Cmb_search.place(x=10,y=10,width=180)
        Cmb_search.current(0)
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="search",command=self.search,font=("goudy old style",15),bg="blue",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)

#product details=====

        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=600,height=390)
        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)
        self.product_table=ttk.Treeview(p_frame,columns=("pid","supplier","catagory","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)
        

        self.product_table.heading ("pid",text="P_ID")
        self.product_table.heading ("catagory",text="Catagory")
        self.product_table.heading ("supplier",text="Supplier")
        self.product_table.heading ("name",text="Name")
        self.product_table.heading ("price",text="Price")
        self.product_table.heading ("qty",text="Qty")
        self.product_table.heading ("status",text="Status")
        
        self.product_table["show"]="headings"

         
        self.product_table.column ("pid",width=90)
        self.product_table.column ("catagory",width=100)
        self.product_table.column ("supplier",width=100)
        self.product_table.column("name",width=100)
        self.product_table.column ("price",width=100)
        self.product_table.column ("qty",width=100)
        self.product_table.column ("status",width=100)
        
        #self.product_table["show"]="headings"

        self.product_table.pack(fill=BOTH,expand=1)
        self.product_table.bind("<ButtonRelease-1>",self.get_data)
        self.show()
       


    def fetch_cat_sup(self):
        self.cat_list.append("empty")
        self.sup_list.append("empty")
        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        try:
            cur.execute("select name from catagory")
            cat=cur.fetchall()
            self.cat_list.append("empty")
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("select")
                
           
            
            for i in cat:
                self.cat_list.append(i[0])

            

            cur.execute("select name from supplier")
            sub=cur.fetchall()
            if len(sub)>0:

                del self.sup_list[:]
                self.sup_list.append("select")
                
           
            
                for i in sub:
                    self.sup_list.append(i[0])
           


        except Exception as ex:
            messagebox.showerror("Error",f"error due to:{str(ex)}",parent=self.root)
   


    def add(self):
        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="select" or self.var_cat.get()=="emtry" or self.var_sup.get()=="select" or  self.var_name.get()=="":
                messagebox.showerror("error","All fields are  required",parent=self.root)
            else:
                cur.execute("select * from product where  name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("error","product already present try different",parent=self.root)
                else:
                    cur.execute("insert into product(catagory,supplier,name,price,qty,status) values (?,?,?,?,?,?)",(
                                        self.var_cat.get(),
                                        self.var_sup.get(),
                                        self.var_name.get(),
                                        self.var_price.get(),
                                        self.var_qty.get(),
                                        self.var_status.get(),
                                        

                    ))
                    con.commit()
                    messagebox.showinfo("success","product address succesfuly",parent=self.root)
                    self.show()
        

        except Exception as ex:
            messagebox.showerror("Error",f"error due to:{str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("error",f"error due to: {str(ex)}",parent=self.root)
    def get_data(self,ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content['values']
        self.var_pid.set(row[0])

        self.var_cat.set(row[2])
        self.var_sup.set(row[1])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])       
                                        
    def update(self):
        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("error","please select product from list",parent=self.root)
            else:
                cur.execute("select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error","invalid product",parent=self.root)
                else:
                    cur.execute("update product set catagory=?,supplier=?,name=?,price=?,qty=?,status=? where pid=?",(
                                        
                                        self.var_cat.get(),
                                        self.var_sup.get(),
                                        self.var_name.get(),
                                        self.var_price.get(),
                                        self.var_qty.get(),
                                        self.var_status.get(),
                                        self.var_pid.get()
                                        


                    ))
                    con.commit()
                    messagebox.showinfo("success","product updated succesfuly",parent=self.root)
                    self.show()
        

        except Exception as ex:
            messagebox.showerror("Error",f"error due to:{str(ex)}",parent=self.root)

    def delete (self):
        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("error","select product from the list",parent=self.root)
            else:
                cur.execute("select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error","invalid product ",parent=self.root)
                else:
                    op=messagebox.askyesno("copnfirm","do you really want to delete?",parent=self.root)
                    if op==True:

                        cur.execute("delete  from product where pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("delete","product deleted successf ully")
                        self.clear()
    
        except Exception as ex:
                messagebox.showerror("Error",f"error due to:{str(ex)}",parent=self.root)

        
    def clear(self):
        self.var_cat.set("Select")
        self.var_sup.set("Select")
        self.var_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.var_status.set("Active")
        self.var_pid.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("select")
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="select":
                messagebox.showerror("error","select search by option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("error","search input should be required",parent=self.root)
            else:
                cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('',END,values=row)
                else:
                    messagebox.showerror("error","no record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("error",f"error due to: {str(ex)}",parent=self.root)






    
       
        


 













if __name__=="__main__":    
    root=Tk()
    obj=productclass(root)
    root.mainloop ()
