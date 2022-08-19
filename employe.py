
from tkinter import *
from tkinter import ttk,messagebox
import sqlite3

from mysqlx import Row
class employeclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+200+130")
        self.root.title("SHOP MANAGEMENT SYSTEM")
        self.root.focus_force()
        # all veriables
        self.var_emp_id=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_contact=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_doje=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_salary=StringVar()
        #searchFrame
        SearchFrame=LabelFrame(self.root,text="Search employee",font=("goudy old style",12,"bold"),bd=2,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)
        Cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("select","eid","contact","name"),state="readonly",justify=CENTER)
        Cmb_search.place(x=10,y=10,width=180)
        Cmb_search.current(0)
        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="search",command=self.search,font=("goudy old style",15),bg="blue",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)
        #title
        title=Label(self.root,text="EMPLOYEE DETAILS",font=("goudy old style",15,"bold"),bg="green",fg="white").place(x=50,y=100,width=1000)
        #content
        lbl_empid=Label(self.root,text="Emp_id",font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_gender=Label(self.root,text="gender",font=("goudy old style",15),bg="white").place(x=350,y=150)
        lbl_contact=Label(self.root,text="contact",font=("goudy old style",15),bg="white").place(x=750,y=150)
        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("goudy old style",15),bg="white").place(x=150,y=150,width=180)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="white").place(x=850,y=150,width=180)
        Cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("select","male","femalet","others"),state="readonly",justify=CENTER)
        Cmb_gender.place(x=500,y=150,width=180)
        Cmb_gender.current(0)
        lbl_name=Label(self.root,text="name",font=("goudy old style",15),bg="white").place(x=50,y=190)
        lbl_dob=Label(self.root,text="dob",font=("goudy old style",15),bg="white").place(x=350,y=190)
        lbl_doj=Label(self.root,text="doj",font=("goudy old style",15),bg="white").place(x=750,y=190)
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="white").place(x=150,y=190,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15),bg="white").place(x=500,y=190,width=180)
        txt_doj=Entry(self.root,textvariable=self.var_doje,font=("goudy old style",15),bg="white").place(x=850,y=190,width=180)
        lbl_email=Label(self.root,text="email",font=("goudy old style",15),bg="white").place(x=50,y=230)
        lbl_password=Label(self.root,text="password",font=("goudy old style",15),bg="white").place(x=350,y=230)
        lbl_usertype=Label(self.root,text="user_type",font=("goudy old style",15),bg="white").place(x=750,y=230)
        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="white").place(x=150,y=230,width=180)
        txt_password=Entry(self.root,textvariable=self.var_pass,font=("goudy old style",15),bg="white").place(x=500,y=230,width=180)
        Cmb_usertype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("select","admin","employee"),state="readonly",justify=CENTER)
        Cmb_usertype.place(x=850,y=230,width=180)
        Cmb_usertype.current(0)
        lbl_address=Label(self.root,text="address",font=("goudy old style",15),bg="white").place(x=50,y=270)
        lbl_salary=Label(self.root,text="salary",font=("goudy old style",15),bg="white").place(x=500,y=270)
        self.txt_address=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_address.place(x=150,y=270,width=300,height=60)
        txt_salary=Entry(self.root,textvariable=self.var_salary,font=("goudy old style",15),bg="lightyellow").place(x=600,y=270,width=180)
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
        self.EmployeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeTable.xview)
        scrolly.config(command=self.EmployeTable.yview)
        

        self.EmployeTable.heading ("eid",text="EMP_ID")
        self.EmployeTable.heading ("name",text="NAME")
        self.EmployeTable.heading ("email",text="EMAIL")
        self.EmployeTable.heading ("gender",text="GENDER")
        self.EmployeTable.heading ("contact",text="PH_NO")
        self.EmployeTable.heading ("dob",text="DOB")
        self.EmployeTable.heading ("doj",text="DOJ")
        self.EmployeTable.heading ("pass",text="PASSWORD")
        self.EmployeTable.heading ("utype",text="U_TYPE")
        self.EmployeTable.heading ("address",text="ADDRESS")
        self.EmployeTable.heading ("salary",text="SALAEY")
        self.EmployeTable["show"]="headings"

         
        self.EmployeTable.column ("eid",width=90)
        self.EmployeTable.column ("name",width=100)
        self.EmployeTable.column ("email",width=100)
        self.EmployeTable.column("gender",width=100)
        self.EmployeTable.column ("contact",width=100)
        self.EmployeTable.column ("dob",width=100)
        self.EmployeTable.column ("doj",width=100)
        self.EmployeTable.column ("pass",width=100)
        self.EmployeTable.column ("utype",width=100)
        self.EmployeTable.column ("address",width=100)
        self.EmployeTable.column ("salary",width=200)
        #self.EmployeTable["show"]="headings"

        self.EmployeTable.pack(fill=BOTH,expand=1)
        self.EmployeTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
#==================
    def add(self):
        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("error","employe id must be required",parent=self.root)
            else:
                cur.execute("select * from employe where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("error","this employe id is already assigned try different",parent=self.root)
                else:
                    cur.execute("insert into employe(eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) values (?,?,?,?,?,?,?,?,?,?,?)",(
                                        self.var_emp_id.get(),
                                        self.var_name.get(),
                                        self.var_email.get(),
                                        self.var_contact.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_doje.get(),
                                        self.var_pass.get(),
                                        self.var_utype.get(),
                                        self.txt_address.get('1.0',END),
                                        self.var_salary.get(),


                    ))
                    con.commit()
                    messagebox.showinfo("success","employe address succesfuly",parent=self.root)
                    self.show()
        

        except Exception as ex:
            messagebox.showerror("Error",f"error due to:{str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        try:
            cur.execute("select * from employe")
            rows=cur.fetchall()
            self.EmployeTable.delete(*self.EmployeTable.get_children())
            for row in rows:
                self.EmployeTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("error",f"error due to: {str(ex)}",parent=self.root)
    def get_data(self,ev):
        f=self.EmployeTable.focus()
        content=(self.EmployeTable.item(f))
        row=content['values']
       # print(row)
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_contact.set(row[3])
        self.var_gender.set(row[4])
        self.var_dob.set(row[5])
        self.var_doje.set(row[6])
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[9])
        self.var_salary.set(row[10])
    def update(self):
        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("error","employe id must be required",parent=self.root)
            else:
                cur.execute("select * from employe where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error","invalid employe id",parent=self.root)
                else:
                    cur.execute("update employe set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",(
                                        
                                        self.var_name.get(),
                                        self.var_email.get(),
                                        self.var_contact.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_doje.get(),
                                        self.var_pass.get(),
                                        self.var_utype.get(),
                                        self.txt_address.get('1.0',END),
                                        self.var_salary.get(),
                                        self.var_emp_id.get(),


                    ))
                    con.commit()
                    messagebox.showinfo("success","employe updated succesfuly",parent=self.root)
                    self.show()
        

        except Exception as ex:
            messagebox.showerror("Error",f"error due to:{str(ex)}",parent=self.root)

    def delete (self):
        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("error","employe id must be required",parent=self.root)
            else:
                cur.execute("select * from employe where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error","invalid employe id",parent=self.root)
                else:
                    op=messagebox.askyesno("copnfirm","do you really want to delete?",parent=self.root)
                    if op==True:

                        cur.execute("delete  from employe where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("delete","employe deleted successf ully")
                        self.clear()
    
        except Exception as ex:
                messagebox.showerror("Error",f"error due to:{str(ex)}",parent=self.root)

        
    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_contact.set("")
        self.var_gender.set("select")
        self.var_dob.set("")
        self.var_doje.set("")
        self.var_pass.set("")
        self.var_utype.set("admin")
        self.txt_address.delete('1.0',END)
        
        self.var_salary.set("")
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
                cur.execute("select * from employe where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.EmployeTable.delete(*self.EmployeTable.get_children())
                    for row in rows:
                        self.EmployeTable.insert('',END,values=row)
                else:
                    messagebox.showerror("error","no record found",parent=self.root)
        except Exception as ex:
            messagebox.showerror("error",f"error due to: {str(ex)}",parent=self.root)




if __name__=="__main__":    
    root=Tk()
    obj=employeclass(root)
    root.mainloop ()
