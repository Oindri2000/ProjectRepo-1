from tkinter import *
from tkinter import ttk,messagebox
import sqlite3

class catagoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+200+130")
        self.root.title("SHOP MANAGEMENT SYSTEM")
        self.root.focus_force()
        #====veriables===
        self.var_cat_id=StringVar()
        self.var_name=StringVar()

        #=====title===
        lbl_title=Label(self.root,text="Manage Product Catagory",font=("goudy old style",30),bg="#184a45",fg="white",relief=RIDGE,bd=3).pack(side=TOP,fill=X,padx=10,pady=2)

        lbl_name=Label(self.root,text="Enter Catagory Name",font=("goudy old style",30),bg="white").place(x=50,y=100)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",30),bg="lightyellow").place(x=50,y=170,width=300)
        btn_add=Button(self.root,text="ADD",command=self.add,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=360,y=170,width=150,height=30)
        btn_delete=Button(self.root,text="DELETE",command=self.delete,font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=520,y=170,width=150,height=30)


        #catagory details
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=0,y=350,relwidth=1,height=150)
        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)
        self.catagory_tableTable=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.catagory_tableTable.xview)
        scrolly.config(command=self.catagory_tableTable.yview)
        

        self.catagory_tableTable.heading ("cid",text="C ID")
        self.catagory_tableTable.heading ("name",text="NAME")
        
        
        
        self.catagory_tableTable["show"]="headings"

         
        self.catagory_tableTable.column ("cid",width=90)
        self.catagory_tableTable.column ("name",width=100)
        
       
        #self.catagory_tableTable["show"]="headings"

        self.catagory_tableTable.pack(fill=BOTH,expand=1)
        self.catagory_tableTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#functions====
    def add(self):
        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("error","catagory name should be required",parent=self.root)
            else:
                cur.execute("select * from catagory where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("error","catagory already present try different",parent=self.root)
                else:
                    cur.execute("insert into catagory (name) values (?)",(
                                        self.var_name.get(),
                                        
                                        
                                        


                    ))
                    con.commit()
                    messagebox.showinfo("success","catagory added succesfuly",parent=self.root)
                    self.show()
        
        except Exception as ex:
            messagebox.showerror("Error",f"error due to:{str(ex)}",parent=self.root)

    
            
    def show(self):
        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        try:
            cur.execute("select * from catagory")
            rows=cur.fetchall()
            self.catagory_tableTable.delete(*self.catagory_tableTable.get_children())
            for row in rows:
                self.catagory_tableTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("error",f"error due to: {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.catagory_tableTable.focus()
        content=(self.catagory_tableTable.item(f))
        row=content['values']
       # print(row)
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])
    def delete (self):
        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("error","please select catagory from the list",parent=self.root)
            else:
                cur.execute("select * from catagory where cid=?",(self.var_cat_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error","Error,please try again",parent=self.root)
                else:
                    op=messagebox.askyesno("copnfirm","do you really want to delete?",parent=self.root)
                    if op==True:

                        cur.execute("delete  from catagory where cid=?",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("delete","catagory deleted successf ully")
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")
    
        except Exception as ex:
                messagebox.showerror("Error",f"error due to:{str(ex)}",parent=self.root)

        
    
        









if __name__=="__main__":    
    root=Tk()
    obj=catagoryClass(root)
    root.mainloop ()