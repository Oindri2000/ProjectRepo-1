from logging import root
from operator import concat
from tkinter import *
from tkinter import ttk
from turtle import right
import sqlite3
from tkinter import messagebox
class PharmacyManagementSystem:
    def __init__(self,root,):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Pharmacy Management")
        self.root.config(bg="pink")

        lbltitle=Label(self.root,text="PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE,bg='white',fg="darkgreen",font=("times new roman",50,"bold"),padx=2,pady=4)
        lbltitle.pack(side=TOP,fill=X)
        #=============addveriables
        self.addmed_var=StringVar()

        #===========all veriables===============

        self.var_ref=StringVar()
        self.var_companyname=StringVar()
        self.var_type=StringVar()
        self.var_tabletname=StringVar()
        self.var_lotno=StringVar()
        self.var_issuedate=StringVar()
        self.var_expdate=StringVar()
        self.var_uses=StringVar()
        self.var_sideeffect=StringVar()
        self.var_warning=StringVar()
        self.var_dosage=StringVar()
        self.var_price=StringVar()
        self.var_productqty=StringVar()
 #==============================DataFrame===========================
        Dataframe=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        Dataframe.place(x=0,y=120,width=1530,height=400)

        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=20,text="Medicine Information",fg="darkgreen",font=("arial",12,"bold"))

        DataframeLeft.place(x=0,y=5,width=900,height=350)

        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=20,text="Medicine Add Depertment",fg="darkgreen",font=("arial",12,"bold"))

        DataframeRight.place(x=910,y=5,width=550,height=350)
        #============buttonFrame============
        Buttonframe=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        Buttonframe.place(x=0,y=520,width=1530,height=65)

        #===========Main Button=================
        btnAddData=Button(Buttonframe,command=self.add_data,text="Medicine Add",font=("arial",12,"bold"),bg="darkgreen",fg="white")
        btnAddData.grid(row=0,column=0)

        btnUpdateMed=Button(Buttonframe,command=self.Update,text="UPDATE",font=("arial",13,"bold"),bg="darkgreen",width=14,fg="white")
        btnUpdateMed.grid(row=0,column=1)

        btnDeleteMed=Button(Buttonframe,command=self.delete,text="DELETE",font=("arial",13,"bold"),bg="red",width=14,fg="white")
        btnDeleteMed.grid(row=0,column=2)

        btnRestMed=Button(Buttonframe,command=self.reset,text="RESET",font=("arial",13,"bold"),bg="darkgreen",width=14,fg="white")
        btnRestMed.grid(row=0,column=3)

        btnExitMed=Button(Buttonframe,text="EXIT",font=("arial",13,"bold"),bg="darkgreen",width=14,fg="white")
        btnExitMed.grid(row=0,column=4)

        #=======Search By==========
        lblSearch=Label(Buttonframe,font=("arial",17,"bold"),text="Search By",padx=2,bg="red",fg="white")
        lblSearch.grid(row=0,column=5,sticky=W)

        #===variable===
        self.search_var=StringVar()

        search_combo=ttk.Combobox(Buttonframe,textvariable=self.search_var,width=12,font=("arial",13,"bold"),state="readonly")
        
        search_combo["values"]=("Ref","tabletname","lotno")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)

        self.searchTxt_var=StringVar()


        txtSearch=Entry(Buttonframe,textvariable=self.searchTxt_var,bd=3,relief=RIDGE,width=12,font=("arial",17,"bold"))
        txtSearch.grid(row=0,column=7)

        searchBtn=Button(Buttonframe,command=self.search_data,text="SEARCH",font=("arial",13,"bold"),bg="darkgreen",width=14,fg="white")
        searchBtn.grid(row=0,column=8)

        showAll=Button(Buttonframe,command=self.fetch_data,text="SHOW ALL",font=("arial",13,"bold"),bg="darkgreen",width=14,fg="white")
        showAll.grid(row=0,column=9)

        #========labels and entry============
        lblrefno=Label(DataframeLeft,font=("arial",12,"bold"),text="Reference No",bg="grey",padx=2)
        lblrefno.grid(row=0,column=0,sticky=W)
        


        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        cur.execute("select ref from pharma")
        row=cur.fetchall()

        ref_combo=ttk.Combobox(DataframeLeft,textvariable=self.var_ref,width=27,font=("arial",13,"bold"),state="readonly")
        
        ref_combo["values"]=row
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)


        lblCompanyName=Label(DataframeLeft,font=("arial",12,"bold"),text="Company Name",padx=2,pady=6)
        lblCompanyName.grid(row=1,column=0,sticky=W)
        txtCompanyName=Entry(DataframeLeft,textvariable=self.var_companyname,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtCompanyName.grid(row=1,column=1)



        lbl_TypeMedicine=Label(DataframeLeft,font=("arial",12,"bold"),text="TypeMedicine",padx=2,pady=6)
        lbl_TypeMedicine.grid(row=2,column=0,sticky=W)

        comTypeMedicine=ttk.Combobox (DataframeLeft,textvariable=self.var_type,state="readonly",font=("arial",12,"bold"),width=27)
        comTypeMedicine["value"]=("Tablet","Liquid","Capsules","Topical Medicines","Drops","Inhelers","Injections")
        comTypeMedicine.current(0)
        comTypeMedicine.grid(row=2,column=1)


        


        #========AddMedicine=============
        lbl_MedicineName=Label(DataframeLeft,font=("arial",12,"bold"),text="Medicine Name",padx=2,pady=6)
        lbl_MedicineName.grid(row=3,column=0,sticky=W)

        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        cur.execute("select medname from pharma")
        med=cur.fetchall()

        comMedicineName=ttk.Combobox (DataframeLeft,textvariable=self.var_tabletname,state="readonly",font=("arial",12,"bold"),width=27)
        comMedicineName["value"]=med
        comMedicineName.current(0)

        comMedicineName.grid(row=3,column=1)

        lblLotNo=Label(DataframeLeft,font=("arial",12,"bold"),text="Lot No",padx=2,pady=6)
        lblLotNo.grid(row=4,column=0,sticky=W)
        txtLotNo=Entry(DataframeLeft,textvariable=self.var_lotno,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtLotNo.grid(row=4,column=1)

        lblIssueDate=Label(DataframeLeft,font=("arial",12,"bold"),text="Issue Date",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataframeLeft,textvariable=self.var_issuedate,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtIssueDate.grid(row=5,column=1)

        lblExDate=Label(DataframeLeft,font=("arial",12,"bold"),text="Exp Date",padx=2,pady=6)
        lblExDate.grid(row=6,column=0,sticky=W)
        txtExDate=Entry(DataframeLeft,textvariable=self.var_expdate,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtExDate.grid(row=6,column=1)

        lblUses=Label(DataframeLeft,font=("arial",12,"bold"),text="Uses",padx=2,pady=6)
        lblUses.grid(row=7,column=0,sticky=W)
        txtUses=Entry(DataframeLeft,textvariable=self.var_uses,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtUses.grid(row=7,column=1)

        lblSideEffect=Label(DataframeLeft,font=("arial",12,"bold"),text="SideEffect",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataframeLeft,textvariable=self.var_sideeffect,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtSideEffect.grid(row=8,column=1)

        lblPrecWarming=Label(DataframeLeft,font=("arial",12,"bold"),text="PrecWarming",padx=2,pady=6)
        lblPrecWarming.grid(row=0,column=2,sticky=W)
        txtPrecWarming=Entry(DataframeLeft,textvariable=self.var_warning,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtPrecWarming.grid(row=0,column=3)

        lblDosAge=Label(DataframeLeft,font=("arial",12,"bold"),text="DosAge",padx=2,pady=6)
        lblDosAge.grid(row=1,column=2,sticky=W)
        txtDosAge=Entry(DataframeLeft,textvariable=self.var_dosage,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtDosAge.grid(row=1,column=3)

        lblPrice=Label(DataframeLeft,font=("arial",12,"bold"),text="Price",padx=2,pady=6)
        lblPrice.grid(row=2,column=2,sticky=W)
        txtPrice=Entry(DataframeLeft,textvariable=self.var_price,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtPrice.grid(row=2,column=3)

        lblProductQty=Label(DataframeLeft,font=("arial",12,"bold"),text="ProducQty",padx=2,pady=6)
        lblProductQty.grid(row=3,column=2,sticky=W)
        txtProductQty=Entry(DataframeLeft,textvariable=self.var_productqty,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtProductQty.grid(row=3,column=3)


        #===============dataframeright==============
        lblrefno=Label(DataframeRight,font=("arial",12,"bold"),text="Reference No:",padx=2,pady=6)
        lblrefno.place(x=0,y=80)
        txtrefno=Entry(DataframeRight,textvariable=self.refMed_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtrefno.place(x=135,y=80)

        lblmedicineName=Label(DataframeRight,font=("arial",12,"bold"),text="Medicine Name:",padx=2,pady=6)
        lblmedicineName.place(x=0,y=110)
        txtmedicineName=Entry(DataframeRight,textvariable=self.addmed_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtmedicineName.place(x=135,y=110)

        #===============sideFrame============
        side_frame=Frame(DataframeRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=150,width=290,height=160)

        sc_x=Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicin_table=ttk.Treeview(side_frame,column=("ref","medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)
        sc_x.config(command=self.medicin_table.xview)
        sc_y.config(command=self.medicin_table.yview)

        self.medicin_table.heading("ref",text="Ref")
        self.medicin_table.heading("medname",text="Medicine Name")

        self.medicin_table["show"]="headings"
        self.medicin_table.pack(fill=BOTH,expand=1)

        self.medicin_table.column("ref",width=100)
        self.medicin_table.column("medname",width=100)

        self.medicin_table.bind("<ButtonRelease-1>",self.Medget_cursor)
        

        #==========Medicine Add button=============
        down_frame=Frame(DataframeRight,bd=4,relief=RIDGE,bg="darkgreen")
        down_frame.place(x=330,y=150,width=135,height=160)

        btnAddmed=Button(down_frame,text="ADD",font=("arial",12,"bold"),command=self.AddMedicine,width=12,bg="lime",fg="white",pady=4)
        btnAddmed.grid(row=0,column=0)

        btnUpdatemed=Button(down_frame,text="UPDATE",font=("arial",12,"bold"),command=self.UpdateMed,width=12,bg="purple",fg="white",pady=4)
        btnUpdatemed.grid(row=1,column=0)

        btnDeletemed=Button(down_frame,text="DELETE",font=("arial",12,"bold"),command=self.DeleteMed,width=12,bg="red",fg="white",pady=4)
        btnDeletemed.grid(row=2,column=0)

        btnClearmed=Button(down_frame,text="CLEAR",font=("arial",12,"bold"),command=self.ClearMed,width=12,bg="orange",fg="white",pady=4)
        btnClearmed.grid(row=3,column=0)
        #====framedetails===============

        Freamedetails=Frame(self.root,bd=15,relief=RIDGE,bg="pink")
        Freamedetails.place(x=0,y=580,width=1530,height=210)

        #=======main table and scrollbar============
        Table_frame=Frame(self.root,bd=15,relief=RIDGE,bg="pink")
        Table_frame.place(x=0,y=590,width=1460,height=180)


        scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.pharmacy_table=ttk.Treeview(Table_frame,column=("ref","companyname","type","tabletname","lotno","issuedate","expdate","uses","sideeffect","warning","dosage","price","productqty"),xscrollcommand=scroll_x,yscrollcommand=scroll_y)
        

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"]="headings"

        self.pharmacy_table.heading("ref",text="Reference No")
        self.pharmacy_table.heading("companyname",text="Company Name")
        self.pharmacy_table.heading("type",text="Type Of Medicine")
        self.pharmacy_table.heading("tabletname",text="Tablet Name")
        self.pharmacy_table.heading("lotno",text="Lot No")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Exp Date")
        self.pharmacy_table.heading("uses",text="Uses")
        self.pharmacy_table.heading("sideeffect",text="Side Effect")
        self.pharmacy_table.heading("warning",text="Prec&Warning")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("productqty",text="Product Qty")
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        self.pharmacy_table.column("ref",width=100)
        self.pharmacy_table.column("companyname",width=100)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("tabletname",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("issuedate",width=100)
        self.pharmacy_table.column("expdate",width=100)
        self.pharmacy_table.column("uses",width=100)
        self.pharmacy_table.column("sideeffect",width=100)
        self.pharmacy_table.column("warning",width=100)
        self.pharmacy_table.column("dosage",width=100)
        self.pharmacy_table.column("price",width=100)
        self.pharmacy_table.column("productqty",width=100)
        self.fetch_dataMed()
        self.fetch_data()

        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)

        #========================= add medicine funcanility=================================
    def AddMedicine(self):
            con=sqlite3.connect(database=r'python.db')
            cur=con.cursor()
            cur.execute("insert into pharma(ref,medname) values(?,?)",(
                                        self.refMed_var.get(),
                                        self.addmed_var.get(),
            ))
            con.commit()
            self.fetch_dataMed()
            self.Medget_cursor()
            con.close()
            
            messagebox.showinfo("success","Medicine Added")

    def fetch_dataMed(self):
        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        cur.execute("select * from pharma")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.medicin_table.delete(*self.medicin_table.get_children())
            for i in rows:
                self.medicin_table.insert("",END,values=i)
            con.commit()
        con.close()


        #=============medgetcursor===============
    def Medget_cursor(self,ev="") :
        cursor_row=self.medicin_table.focus()
        content=self.medicin_table.item(cursor_row)
        row=content["values"]
        self.refMed_var.set(row[0])
        self.addmed_var.set(row[1]) 

    def UpdateMed(self):
        if self.refMed_var.get()=="" or self.addmed_var.get()=="":
            messagebox.showerror("Error","All fields are Required")
        else:
            con=sqlite3.connect(database=r'python.db')
            cur=con.cursor()
            cur.execute("update pharma set medname=? where ref=?",(
                self.addmed_var.get(),
    
                self.refMed_var.get(),
        
            ))
        con.commit()
        self.fetch_dataMed()
        con.close()    

        messagebox.showinfo("Success","Medicine has been Updated")

    def DeleteMed(self):
        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        cur.execute("delete  from pharma where ref=?",(self.refMed_var.get(),))

        con.commit()
        self.fetch_dataMed()
        con.close()

    def ClearMed(self):
        self.refMed_var.set("")
        self.addmed_var.set("")
        #==== Main Table============
    def add_data(self):
        if self.var_ref.get()=="" or self.var_lotno.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            con=sqlite3.connect(database=r'python.db')
            cur=con.cursor()
            cur.execute("insert into pharmacy(ref,companyname,type,tabletname,lotno,issuedate,expdate,uses,sideeffect,warning,dosage,price,productqty) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(
                self.var_ref.get(),
                self.var_companyname.get(),
                self.var_type.get(),
                self.var_tabletname.get(),
                self.var_lotno.get(),
                self.var_issuedate.get(),
                self.var_expdate.get(),
                self.var_uses.get(),
                self.var_sideeffect.get(),
                self.var_warning.get(),
                self.var_dosage.get(),
                self.var_price.get(),
                self.var_productqty.get(),
            ))

            con.commit()
            self.fetch_data()
            con.close()
            messagebox.showinfo("Success","Data has been insearted")

    def fetch_data(self):
        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        cur.execute("select * from pharmacy")
        row=cur.fetchall()
        if len(row)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("",END,values=i)
            con.commit()
        con.close()

    def get_cursor(self,ev):
        cursor_row=self.pharmacy_table.focus()
        content=self.pharmacy_table.item(cursor_row)
        row=content["values"]
        
        self.var_ref.set(row[0]),
        self.var_companyname.set(row[1]),
        self.var_type.set(row[2]),
        self.var_tabletname.set(row[3]),
        self.var_lotno.set(row[4]),
        self.var_issuedate.set(row[5]),
        self.var_expdate.set(row[6]),
        self.var_uses.set(row[7]),
        self.var_sideeffect.set(row[8]),
        self.var_warning.set(row[9]),
        self.var_dosage.set(row[10]),
        self.var_price.set(row[11]),
        self.var_productqty.set(row[12])

    def Update(self):
        if self.var_ref.get()=="" or self.var_lotno.get()=="":
            messagebox.showerror("Error","All fields are Required")
        else:
            con=sqlite3.connect(database=r'python.db')
            cur=con.cursor()
            cur.execute("update pharmacy set companyname=?,type=?,tabletname=?,lotno=?,issuedate=?,expdate=?,uses=?,sideeffect=?,warning=?,dosage=?,price=?,productqty=? where ref=?",(
                
                self.var_companyname.get(),
                self.var_type.get(),
                self.var_tabletname.get(),
                self.var_lotno.get(),
                self.var_issuedate.get(),
                self.var_expdate.get(),
                self.var_uses.get(),
                self.var_sideeffect.get(),
                self.var_warning.get(),
                self.var_dosage.get(),
                self.var_price.get(),
                self.var_productqty.get(),
                self.var_ref.get()
        
            ))
            con.commit()
            self.fetch_data()
            con.close()
            messagebox.showinfo("Update","Record has been updayed successfully")

    def delete(self):
        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        cur.execute("delete  from pharmacy where ref=?",(self.var_ref.get(),))

        con.commit()
        self.fetch_data()
        con.close()
        messagebox.showinfo("DELETE","Information deleted successfully")

    def reset(self):
        #self.var_ref.set(""),
        self.var_companyname.set(""),
        #self.var_type.set(""),
        #self.var_tabletname.set(""),
        self.var_lotno.set(""),
        self.var_issuedate.set(""),
        self.var_expdate.set(""),
        self.var_uses.set(""),
        self.var_sideeffect.set(""),
        self.var_warning.set(""),
        self.var_dosage.set(""),
        self.var_price.set(""),
        self.var_productqty.set("")

    def search_data(self):
        con=sqlite3.connect(database=r'python.db')
        cur=con.cursor()
        cur.execute("select * from pharmacy where "+str(self.search_var.get())+" LIKE '%"+str(self.searchTxt_var.get())+"%'")

        rows=cur.fetchall()
        if len(rows)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("",END,values=i)
            con.commit()
        con.close() 

        






    

        




 
 
 
 
 

if __name__=="__main__":    
    root=Tk()
    obj=PharmacyManagementSystem(root)
    root.mainloop ()  
 