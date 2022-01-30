from tkinter import *
from PIL import Image,ImageTk  # pip install pillow
from tkinter import ttk
import random
import mysql.connector

from tkinter import messagebox

class student_details:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Details")
        self.root.geometry("1050x428+230+220")

        # ================================================ VARIABLES =================================================
        self.var_Student_ID=StringVar()
        x=random.randint(1000,9999)
        self.var_Student_ID.set(str(x))
        
        self.var_Student_Name=StringVar()
        self.var_Gender=StringVar()
        self.var_Room_Number=StringVar()
        self.var_Course=StringVar()
        self.var_Guardian_Name=StringVar()
        self.var_Guardian_Number=StringVar()
        self.var_Student_Number=StringVar()
        
        self.var_Student_Address=StringVar()
        self.var_Student_Building=StringVar()
        


        
        
        # ================================================ TITLE ====================================================
        lbl_title = Label(self.root,text = "STUDENT WINDOW",font=("times new roman",20,"bold"), bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1050,height=50)

        # ================================================ LOGO =======================================================
        img2=Image.open(r"C:\Users\HP\Desktop\Computer Science\Computer Programs\Python\Projects\logo2.PNG")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=5,width=100,height=40)
 
        # ============================================= LABEL FRAME ==================================================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Student Details",padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=390,height=490)

        # ============================================= LABELS AND ENTRIES ============================================
        # Student ID
        student_ID = Label(labelframeleft,text="Student ID",font=("times new roman",10,"bold"),padx=2,pady=6)
        student_ID.grid(row=0,column=0,sticky=W)

        entry_ID=ttk.Entry(labelframeleft,textvariable=self.var_Student_ID,state="readonly",width=29,font=("times new roman",11,"bold"))
        entry_ID.grid(row=0,column=1)

        # Student Name
        student_name = Label(labelframeleft,text="Student Name",font=("times new roman",10,"bold"),padx=2,pady=6)
        student_name.grid(row=1,column=0,sticky=W)

        entry_name=ttk.Entry(labelframeleft,textvariable=self.var_Student_Name,width=29,font=("times new roman",11,"bold"))
        entry_name.grid(row=1,column=1)

        # Student Gender (combobox)
        label_gender = Label(labelframeleft,text="Gender",font=("times new roman",10,"bold"),padx=2,pady=6)
        label_gender.grid(row=2,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_Gender,font=("times new roman",11,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female")
        combo_gender.current(1)
        combo_gender.grid(row=2,column=1)

        
        # Student's Room Number
        room_number = Label(labelframeleft,text="Room Number",font=("times new roman",10,"bold"),padx=2,pady=6)
        room_number.grid(row=3,column=0,sticky=W)

        entry_room_number=ttk.Entry(labelframeleft,textvariable=self.var_Room_Number,width=29,font=("times new roman",11,"bold"))
        entry_room_number.grid(row=3,column=1)

        # Student's course (combobox)
        student_course = Label(labelframeleft,text="Course",font=("times new roman",10,"bold"),padx=2,pady=6)
        student_course.grid(row=4,column=0,sticky=W)

        combo_course=ttk.Combobox(labelframeleft,textvariable=self.var_Course,font=("times new roman",11,"bold"),width=27,state="readonly")
        combo_course["value"]=("UG","PG","PhD")
        combo_course.current(0)
        combo_course.grid(row=4,column=1)


        # Guardian Name
        student_guardian = Label(labelframeleft,text="Guardian Name",font=("times new roman",10,"bold"),padx=2,pady=6)
        student_guardian.grid(row=5,column=0,sticky=W)

        entry_guardian=ttk.Entry(labelframeleft,textvariable=self.var_Guardian_Name,width=29,font=("times new roman",11,"bold"))
        entry_guardian.grid(row=5,column=1)

        # Guardian contact Number
        guardian_contact = Label(labelframeleft,text="Guardian Number",font=("times new roman",10,"bold"),padx=2,pady=6)
        guardian_contact.grid(row=6,column=0,sticky=W)

        entry_guardian_contact=ttk.Entry(labelframeleft,textvariable=self.var_Guardian_Number,width=29,font=("times new roman",11,"bold"))
        entry_guardian_contact.grid(row=6,column=1)
        
        # Student Contact Number
        student_contact = Label(labelframeleft,text="Student Number",font=("times new roman",10,"bold"),padx=2,pady=6)
        student_contact.grid(row=7,column=0,sticky=W)

        entry_student_contact=ttk.Entry(labelframeleft,textvariable=self.var_Student_Number,width=29,font=("times new roman",11,"bold"))
        entry_student_contact.grid(row=7,column=1)

        # Student Building (combobox)
        Student_Building = Label(labelframeleft,text="Building",font=("times new roman",10,"bold"),padx=2,pady=6)
        Student_Building.grid(row=8,column=0,sticky=W)

        combo_building=ttk.Combobox(labelframeleft,textvariable=self.var_Student_Building,font=("times new roman",11,"bold"),width=27,state="readonly")
        combo_building["value"]=("boys hostel","girls hostel")
        combo_building.current(1)
        combo_building.grid(row=8,column=1)


        

        # Student Address
        student_address = Label(labelframeleft,text="Student Address",font=("times new roman",10,"bold"),padx=2,pady=6)
        student_address.grid(row=9,column=0,sticky=W)

        entry_address=ttk.Entry(labelframeleft,textvariable=self.var_Student_Address,width=29,font=("times new roman",11,"bold"))
        entry_address.grid(row=9,column=1)

        # ============================================= Buttons ====================================================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=320,width=356,height=30)

        btn_add=Button(btn_frame,text="ADD",command=self.add_data,font=("times new roman",10,"bold"),bg="red",fg="gold",width=11)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="UPDATE",command=self.update,font=("times new roman",10,"bold"),bg="red",fg="gold",width=11)
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="DELETE",command=self.stu_delete,font=("times new roman",10,"bold"),bg="red",fg="gold",width=11)
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text="RESET",command=self.reset,font=("times new roman",10,"bold"),bg="red",fg="gold",width=11)
        btn_reset.grid(row=0,column=3,padx=1)

        # ============================================= Table Frame ==================================================

        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="VIEW AND SEARCH DETAILS",font=("times new roman",12,"bold"))
        Table_Frame.place(x=405,y=50,width=860,height=490)

        # Search Label
        lblSearchBy = Label(Table_Frame,text="FILTER",font=("times new roman",10,"bold"),bg="black",fg="red")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()

        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("times new roman",11,"bold"),width=20,state="readonly")
        combo_Search["value"]=("Student ID","Student Name","Room Number")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()

        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,width=20,font=("times new roman",11,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,command=self.search,text="Search",font=("times new roman",10,"bold"),bg="red",fg="gold",width=11)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("times new roman",10,"bold"),bg="red",fg="gold",width=11)
        btnShowAll.grid(row=0,column=4,padx=1)


        # ============================================== Display Data Table ===========================================

        details_table=LabelFrame(Table_Frame,bd=2,relief=RIDGE,font=("times new roman",12,"bold"))
        details_table.place(x=2,y=30,width=630,height=300)

        # Scrollbar
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Student_Details_Table=ttk.Treeview(details_table,column=("Student_ID","Student_Name","Gender","Room_Number","Course","Guardian_Name","Guardian_Number","Student_Number","Student_Building","Student_Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Student_Details_Table.xview)
        scroll_y.config(command=self.Student_Details_Table.yview)

        self.Student_Details_Table.heading("Student_ID",text="Student_ID")
        self.Student_Details_Table.heading("Student_Name",text="Student_Name")
        self.Student_Details_Table.heading("Gender",text="Gender")
        self.Student_Details_Table.heading("Room_Number",text="Room_Number")
        self.Student_Details_Table.heading("Course",text="Course")
        self.Student_Details_Table.heading("Guardian_Name",text="Guardian_Name")
        self.Student_Details_Table.heading("Guardian_Number",text="Guardian_Number")
        self.Student_Details_Table.heading("Student_Number",text="Student_Number")
        self.Student_Details_Table.heading("Student_Building",text="Student_Building")
        self.Student_Details_Table.heading("Student_Address",text="Student_Address")

        self.Student_Details_Table["show"]="headings"

        self.Student_Details_Table.column("Student_ID",width=100)
        self.Student_Details_Table.column("Student_Name",width=100)
        self.Student_Details_Table.column("Gender",width=100)
        self.Student_Details_Table.column("Room_Number",width=100)
        self.Student_Details_Table.column("Course",width=100)
        self.Student_Details_Table.column("Guardian_Name",width=100)
        self.Student_Details_Table.column("Guardian_Number",width=100)
        self.Student_Details_Table.column("Student_Number",width=100)
        self.Student_Details_Table.column("Student_Building",width=100)
        self.Student_Details_Table.column("Student_Address",width=100)
        
        
        
        


        


        self.Student_Details_Table.pack(fill=BOTH,expand=1)
        self.Student_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        
        self.fetch_data()
    

    # ================================================ ADD DATA FUNCTION ===============================================

    def add_data(self):
        if self.var_Student_Number.get()=="" or self.var_Student_Building.get()=="" or self.var_Room_Number.get()=="" :
            messagebox.showerror("Error","ALL FIELDS ARE MANDATORY",parent=self.root)
        else:
            try:
                con=mysql.connector.connect(host="localhost",user="root",password="Soujatya@2003",database="hostel_management",auth_plugin='mysql_native_password')
                my_cursor=con.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_Student_ID.get(),
                
                        self.var_Student_Name.get(),
                        self.var_Gender.get(),
                        self.var_Room_Number.get(),
                        self.var_Course.get(),
                        self.var_Guardian_Name.get(),
                        self.var_Guardian_Number.get(),
                        self.var_Student_Number.get(),
                        self.var_Student_Building.get(),
                        self.var_Student_Address.get()
                    ))
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("Success","record has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"something went wrong...please try again:{str(es)}",parent=self.root)
    
    # =========================================== FETCH DATA FUNCTION ==================================================
    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="Soujatya@2003",database="hostel_management",auth_plugin='mysql_native_password')
        my_cursor=con.cursor()
        my_cursor.execute("select * from student")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Student_Details_Table.delete(*self.Student_Details_Table.get_children())
            for i in rows:
                self.Student_Details_Table.insert("",END,values=i)
            con.commit()
        con.close()

    # =============================================== GET CURSOR FUNCTION ==============================================

    def get_cursor(self,event=""):
        cursor_row=self.Student_Details_Table.focus()
        content=self.Student_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_Student_ID.set(row[0])
                
        self.var_Student_Name.set(row[1])
        self.var_Gender.set(row[2])
        self.var_Room_Number.set(row[3])
        self.var_Course.set(row[4])
        self.var_Guardian_Name.set(row[5])
        self.var_Guardian_Number.set(row[6])
        self.var_Student_Number.set(row[7])
        self.var_Student_Building.set(row[8])
        self.var_Student_Address.set(row[9])
        
        
    # ================================================ UPDATE FUNCTION =====================================================

    def update(self):
        if self.var_Student_Number.get()=="" or self.var_Student_Email_ID.get()=="" or self.var_Room_Number.get()=="":
            messagebox.showerror("Error","Please Enter all details",parent=self.root)
        else:
            con=mysql.connector.connect(host="localhost",user="root",password="Soujatya@2003",database="hostel_management",auth_plugin='mysql_native_password')
            my_cursor=con.cursor()
            
            my_cursor.execute("UPDATE student set Student_Name=%s,Gender=%s,Room_Number=%s,Course=%s,Guardian_Name=%s,Guardian_Number=%s,Student_Number=%s,Student_Building=%s,Student_Address=%s WHERE Student_ID=%s",(
            # UPDATE `hostel_management`.`student` SET `Student_Name` = 'Rahul' WHERE (`Student_ID` = '9972');
            
                
            self.var_Student_Name.get(),
            self.var_Gender.get(),
            self.var_Room_Number.get(),
            self.var_Course.get(),
            self.var_Guardian_Name.get(),
            self.var_Guardian_Number.get(),
            self.var_Student_Number.get(),
            self.var_Student_Building.get(),
            self.var_Student_Address.get(),
            self.var_Student_ID.get() ))

            con.commit()
            self.fetch_data()
            con.close()
            messagebox.showinfo("update","student details has been updated successfully",parent=self.root)


    # ==================================================== DELETE FUNCTION ===============================================
    def stu_delete(self):
        stu_delete=messagebox.askyesno("Hostel Management System","Do you want to delete the records of this student?",parent=self.root)
        if stu_delete>0:
            con=mysql.connector.connect(host="localhost",user="root",password="Soujatya@2003",database="hostel_management",auth_plugin='mysql_native_password')
            my_cursor=con.cursor()
            query="delete from student where Student_ID=%s"
            value=(self.var_Student_ID.get(),)
            my_cursor.execute(query,value)
        else:
            if not stu_delete:
                return
        con.commit()
        self.fetch_data()
        con.close()
        messagebox.showinfo("update","Room has been deleted successfully",parent=self.root)
        
    # ===================================================== RESET FUNCTION =============================================

    def reset(self):
      # self.var_Student_ID.set(""),
                
        self.var_Student_Name.set(""),
      # self.var_Gender.set(""),
        self.var_Room_Number.set(""),
        self.var_Course.set(""),
        self.var_Guardian_Name.set(""),
        self.var_Guardian_Number.set(""),
        self.var_Student_Number.set(""),
        self.var_Student_Building.set(""),
        self.var_Student_Address.set("")

        
        x=random.randint(1000,9999)
        self.var_Student_ID.set(str(x))
    
    # ================================================== SEARCH FUNCTION ===============================================
    def search(self):

        if self.search_var.get()=="Student Name":
            con=mysql.connector.connect(host="localhost",user="root",password="Soujatya@2003",database="hostel_management",auth_plugin='mysql_native_password')
            my_cursor=con.cursor()
            
            my_cursor.execute("select * from student  where Student_Name LIKE '%" +str(self.txt_search.get())+"%'")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.Student_Details_Table.delete(*self.Student_Details_Table.get_children())
                for i in rows:
                    self.Student_Details_Table.insert("",END,values=i)
                con.commit()
            con.close()
        
        if self.search_var.get()=="Student ID":
            con=mysql.connector.connect(host="localhost",user="root",password="Soujatya@2003",database="hostel_management",auth_plugin='mysql_native_password')
            my_cursor=con.cursor()
            
            my_cursor.execute("select * from student  where Student_ID LIKE '%" +str(self.txt_search.get())+"%'")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.Student_Details_Table.delete(*self.Student_Details_Table.get_children())
                for i in rows:
                    self.Student_Details_Table.insert("",END,values=i)
                con.commit()
            con.close()

        if self.search_var.get()=="Room Number":
            con=mysql.connector.connect(host="localhost",user="root",password="Soujatya@2003",database="hostel_management",auth_plugin='mysql_native_password')
            my_cursor=con.cursor()
            
            my_cursor.execute("select * from student  where Room_Number LIKE '%" +str(self.txt_search.get())+"%'")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.Student_Details_Table.delete(*self.Student_Details_Table.get_children())
                for i in rows:
                    self.Student_Details_Table.insert("",END,values=i)
                con.commit()
            con.close()










if __name__== "__main__":
    root=Tk()
    obj=student_details(root)
    root.mainloop()