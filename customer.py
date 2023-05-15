from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import mysql.connector
import random

class Cust_Win:
    def __init__(self,root):
        self.root = root
        self.root.title("Customer Management")
        self.root.geometry("1315x560+305+260")

        #----------------VARIABLES---------------
        self.var_ref = StringVar()
        x=random.randint(1000,9999)
        
        self.var_ref.set(str(x))
        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_postcode=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_idproof=StringVar()
        self.var_idnumber=StringVar()
        self.var_address=StringVar()

        #-----------------TITLE------------------
        lbl_title=Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1315,height=50)

        #----------------LOGO-------------------
        img_logo = Image.open('images/hotel_logo.jpg')
        img_logo = img_logo.resize((100,45),Image.ANTIALIAS)
        self.photoimg_logo = ImageTk.PhotoImage(img_logo)
        lblimg_logo = Label(self.root,image=self.photoimg_logo,bd=0,relief=RIDGE)
        lblimg_logo.place(x=1,y=2,width=100,height=45)

        #-----------------Label Frame---------------
        lblfr_cust_details=LabelFrame(self.root,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=2,pady=2)
        lblfr_cust_details.place(x=5,y=50,width=425,height=490)

        #----------------Labels and Entry-------------
        # Customer Ref
        lbl_cust_ref = Label(lblfr_cust_details,text="Customer Ref.:", font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        entry_cust_ref= ttk.Entry(lblfr_cust_details, width=29,textvariable=self.var_ref,state='readonly', font=("times new roman",13,"bold"))
        entry_cust_ref.grid(row=0,column=1)

        # Customer Name
        lbl_cust_name = Label(lblfr_cust_details, text="Customer Name:", font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_name.grid(row=1,column=0,sticky=W)
        entry_cust_name= ttk.Entry(lblfr_cust_details, width=29,textvariable=self.var_cust_name, font=("times new roman",13,"bold"))
        entry_cust_name.grid(row=1,column=1)

        # Mother's name
        lbl_cust_mname = Label(lblfr_cust_details, text="Mother's Name:", font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_mname.grid(row=2,column=0,sticky=W)
        entry_cust_mname= ttk.Entry(lblfr_cust_details, width=29, font=("times new roman",13,"bold"),textvariable=self.var_mother)
        entry_cust_mname.grid(row=2,column=1)

        #Gender Combo Box
        lbl_gender = Label(lblfr_cust_details, text="Gender:", font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_gender.grid(row=3,column=0,sticky=W)
        combo_gender = ttk.Combobox(lblfr_cust_details,textvariable=self.var_gender,font=("times new roman",13,"bold"),width=27,state="readonly")
        combo_gender["values"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)


        # Postal Code
        lbl_postcode = Label(lblfr_cust_details, text="Postal Code:", font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_postcode.grid(row=4,column=0,sticky=W)
        entry_postcode= ttk.Entry(lblfr_cust_details, width=29,textvariable=self.var_postcode, font=("times new roman",13,"bold"))
        entry_postcode.grid(row=4,column=1)

        # Mobile Number
        lbl_mobile = Label(lblfr_cust_details, text="Mobile No.:", font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_mobile.grid(row=5,column=0,sticky=W)
        entry_mobile= ttk.Entry(lblfr_cust_details, width=29,textvariable=self.var_mobile, font=("times new roman",13,"bold"))
        entry_mobile.grid(row=5,column=1)

        # Email
        lbl_email = Label(lblfr_cust_details, text="Email:", font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_email.grid(row=6,column=0,sticky=W)
        entry_email= ttk.Entry(lblfr_cust_details, width=29,textvariable=self.var_email, font=("times new roman",13,"bold"))
        entry_email.grid(row=6,column=1)

        # Nationality Combo Box
        lbl_nationality = Label(lblfr_cust_details, text="Nationality:", font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_nationality.grid(row=7,column=0,sticky=W)
        combo_nationality = ttk.Combobox(lblfr_cust_details,textvariable=self.var_nationality,font=("times new roman",13,"bold"),width=27,state="readonly")
        combo_nationality["values"]=("Indian","American","British")
        combo_nationality.current(0)
        combo_nationality.grid(row=7,column=1)


        # ID Proof Combo Box
        lbl_id_proof = Label(lblfr_cust_details, text="ID Proof:", font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_id_proof.grid(row=8,column=0,sticky=W)
        combo_id_proof = ttk.Combobox(lblfr_cust_details,textvariable=self.var_idproof,font=("times new roman",13,"bold"),width=27,state="readonly")
        combo_id_proof["values"]=("AADHAR","Passport","Diving License")
        combo_id_proof.current(0)
        combo_id_proof.grid(row=8,column=1)

        # ID Number
        lbl_id_number = Label(lblfr_cust_details, text="ID No.:", font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_id_number.grid(row=9,column=0,sticky=W)
        entry_id_number= ttk.Entry(lblfr_cust_details, width=29,textvariable=self.var_idnumber, font=("times new roman",13,"bold"))
        entry_id_number.grid(row=9,column=1)

        # Address
        lbl_address = Label(lblfr_cust_details, text="Address:", font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_address.grid(row=10,column=0,sticky=W)
        entry_address= ttk.Entry(lblfr_cust_details, width=29,textvariable=self.var_address, font=("times new roman",13,"bold"))
        entry_address.grid(row=10,column=1)

        #-------------Buttons----------------
        btn_frame = LabelFrame(lblfr_cust_details,bd=2, relief=RIDGE)
        btn_frame.place(x=0,y=400,width=410,height=40)

        btn_add = Button(btn_frame,text="ADD",command=self.add_data,font=("Arial",12,"bold"),bg="black",fg="gold",width=8,)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update = Button(btn_frame,text="UPDATE",font=("Arial",12,"bold"),bg="black",fg="gold",width=8,)
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete = Button(btn_frame,text="DELETE",font=("Arial",12,"bold"),bg="black",fg="gold",width=8,)
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset = Button(btn_frame,text="RESET",font=("Arial",12,"bold"),bg="black",fg="gold",width=8,)
        btn_reset.grid(row=0,column=3,padx=1)

        #--------------------Table Frame------------------------------
        table_frame=LabelFrame(self.root, text="View Details and Search System", font=("times new roman",18,"bold"),bd=4,relief=RIDGE)
        table_frame.place(x=435,y=50,width=860,height=490)

        lbl_searchby = Label(table_frame, text="Search By:", font=("times new roman",12,"bold"),bg="red", fg="white")
        lbl_searchby.grid(row=0,column=0,sticky=W,padx=2)
        
        combo_search=ttk.Combobox(table_frame,font=("times new roman",13,"bold"),width=24,state="readonly")
        combo_search["values"]=("Mobile","Ref")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        entry_search=Entry(table_frame,font=("times new roman",13,"bold"),width=29)
        entry_search.grid(row=0,column=2,padx=2)

        btn_search=Button(table_frame,text="SEARCH",font=("Aial",12,"bold"),bg="black",fg="gold")
        btn_search.grid(row=0,column=3,padx=2)

        btn_showall=Button(table_frame,text="SHOW ALL",font=("Aial",12,"bold"),bg="black",fg="gold")
        btn_showall.grid(row=0,column=4,padx=2)

        #--------------Show Data Table----------------
        details_table=LabelFrame(table_frame,text="Details",font=("times new roman",12,"bold"),bd=4,relief=RIDGE)
        details_table.place(x=0,y=50,width=850,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.cust_details_table=ttk.Treeview(details_table,columns=("ref","name","mother","gender","postcode","mobile",
                                                                    "email","nationality","idproof","idnumber","address"),
                                                                    xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)

        self.cust_details_table.heading("ref",text="Ref No.")
        self.cust_details_table.heading("name",text="Name")
        self.cust_details_table.heading("mother",text="Mother's Name")
        self.cust_details_table.heading("gender",text="Gender")
        self.cust_details_table.heading("postcode",text="Post Code")
        self.cust_details_table.heading("mobile",text="Mobile No.")
        self.cust_details_table.heading("email",text="Email")
        self.cust_details_table.heading("nationality",text="Nationality")
        self.cust_details_table.heading("idproof",text="ID Proof")
        self.cust_details_table.heading("idnumber",text="ID No.")
        self.cust_details_table.heading("address",text="Address")

        self.cust_details_table["show"]="headings"

        self.cust_details_table.column("ref",width=100)
        self.cust_details_table.column("name",width=100)
        self.cust_details_table.column("mother",width=130)
        self.cust_details_table.column("gender",width=100)
        self.cust_details_table.column("postcode",width=100)
        self.cust_details_table.column("mobile",width=100)
        self.cust_details_table.column("email",width=100)
        self.cust_details_table.column("nationality",width=100)
        self.cust_details_table.column("idproof",width=100)
        self.cust_details_table.column("idnumber",width=100)
        self.cust_details_table.column("address",width=100)

        self.cust_details_table.pack(fill=BOTH,expand=1 )

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:

                conn=mysql.connector.connect(host='localhost',username='zab',password='pass123',database='management')
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (self.var_ref.get(),self.var_cust_name.get(),self.var_mother.get(),
                                self.var_gender.get(),self.var_postcode.get(),self.var_mobile.get(),
                                self.var_email.get(),self.var_nationality.get(),self.var_idproof.get(),
                                self.var_idnumber.get(),self.var_address.get()))
                messagebox.showinfo("Success","Customer has been added!",parent=self.root)
                conn.commit()
                conn.close()
            except Exception as ex:
                messagebox.showwarning("Warning",f"Something went wrong:{str(ex)}",parent=self.root)


if __name__ == "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()