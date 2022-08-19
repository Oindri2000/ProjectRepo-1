
from tkinter import *
from tkinter import ttk,messagebox
import sqlite3

class suppierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+200+130")
        self.root.title("SHOP MANAGEMENT SYSTEM")
        self.root.focus_force()
        # all veriables
        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
       
        self.var_contact=StringVar()
       
       
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        
        #searchFrame
        SearchFrame=LabelFrame(self.root,text="Search employee",font=("goudy old style",12,"bold"),bd=2,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)
        lbl_search=Label(SearchFrame,text="search by invoice no. ",font=("goudy old style",15))
        lbl_search.place(x=10,y=10)
       
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="search",command=self.search,font=("goudy old style",15),bg="blue",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)
        #title
        title=Label(self.root,text="Supplier details",font=("goudy old style",20,"bold"),bg="green",fg="white").place(x=50,y=100,width=1000)
        #content
        lbl_supplier_invoice=Label(self.root,text="invoice no.",font=("goudy old style",15),bg="white").place(x=50,y=150)
        
        txt_supplier=Entry(self.root,textvariable=self.var_sup_invoice,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)
        
        lbl_name=Label(self.root,text="name",font=("goudy old style",15),bg="white").place(x=50,y=190)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)
       
        lbl_contact=Label(self.root,text="contact",font=("goudy old style",15),bg="white").place(x=50,y=230)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=150,y=230,width=180)
        
        lbl_desc=Label(self.root,text="description",font=("goudy old style",15),bg="white").place(x=50,y=270)
        
        self.txt_desc=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_desc.place(x=150,y=270,width=300,height=60)
        #button
        btn_add=Button(self.root,text="save", command=self.add,font=("goudy old style",15),bg="green",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.root,text="update",command=self.update,font=("goudy old style",15),bg="lightblue",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)
        btn_deleter=Button(self.root,text="delete",command=self.delete,font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=28)
        btn_clear=Button(self.root,text="clear",command=self.clear,font=("goudy old style",15),bg="orange",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)
        #emp details
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        self.supplierTable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)
        

        self.supplierTable.heading ("invoice",text="Invoice No.")
        self.supplierTable.heading ("name",text="NAME")
        
        self.supplierTable.heading ("contact",text="PH_NO")
        
        self.supplierTable.heading ("desc",text="Description")
        
        self.supplierTable["show"]="headings"

         
        self.supplierTable.column ("invoice",width=90)
        self.supplierTable.column ("name",width=100)
        self.supplierTable.column ("contact",width=100)
        self.supplierTable.column("desc",width=100)
       
        self.supplierTable["show"]="headings"

        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#==================
    def add(self):
        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("error","invoice must be required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("error","this invoiced no. is already assigned try different",parent=self.root)
                else:
                    cur.execute("insert into supplier (invoice,name,contact,desc) values (?,?,?,?)",(
                                        self.var_sup_invoice.get(),
                                        self.var_name.get(),
                                        
                                        self.var_contact.get(),
                                        
                                        self.txt_desc.get('1.0',END),
                                        


                    ))
                    con.commit()
                    messagebox.showinfo("success","supplier address succesfuly",parent=self.root)
                    self.show()
        

        except Exception as ex:
            messagebox.showerror("Error",f"error due to:{str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            rows=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("error",f"error due to: {str(ex)}",parent=self.root)
    def get_data(self,ev):
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        row=content['values']
       # print(row)
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        
        self.var_contact.set(row[2])
        
        self.txt_desc.delete('1.0',END)
        self.txt_desc.insert(END,row[3])
        
    def update(self):
        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("error","invoice no. must be required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error","invalid invoice no.",parent=self.root)
                else:
                    cur.execute("update supplier set name=?,contact=?,desc=? where invoice=?",(
                                        
                                        self.var_name.get(),
                                       
                                        self.var_contact.get(),
                                        
                                        self.txt_desc.get('1.0',END),
                                       
                                        self.var_sup_invoice.get(),


                    ))
                    con.commit()
                    messagebox.showinfo("success","supplier updated succesfuly",parent=self.root)
                    self.show()
        

        except Exception as ex:
            messagebox.showerror("Error",f"error due to:{str(ex)}",parent=self.root)

    def delete (self):
        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("error","invoice no. must be required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error","invalid invoice no.",parent=self.root)
                else:
                    op=messagebox.askyesno("copnfirm","do you really want to delete?",parent=self.root)
                    if op==True:

                        cur.execute("delete  from supplier where invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("delete","supplier deleted successf ully")
                        self.clear()
    
        except Exception as ex:
                messagebox.showerror("Error",f"error due to:{str(ex)}",parent=self.root)

        
    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        
        self.var_contact.set("")
        
        self.txt_desc.delete('1.0',END)
        
        
        self.var_searchtxt.set("")
        
        self.show()

    def search(self):
        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("error","invoice no. should be required",parent=self.root)
            else:
                cur.execute("select * from supplier where invoice=?",(self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    
                    self.supplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("error","no record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("error",f"error due to: {str(ex)}",parent=self.root)




if __name__=="__main__":    
    root=Tk()
    obj=suppierClass(root)
    root.mainloop ()
