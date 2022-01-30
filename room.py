from tkinter import *
from PIL import Image,ImageTk  # pip install pillow
from tkinter import ttk
import random
import mysql.connector

from tkinter import messagebox

class room_details:
    def __init__(self,root):
        self.root=root
        self.root.title("Room Details")
        self.root.geometry("1050x428+230+220")

        # =============================================== VARIABLES =================================================

        
        self.var_Building=StringVar()
        self.var_Room_Number=StringVar()
        self.var_Room_Type=StringVar()
        self.var_Room_Size=StringVar()
        self.var_Room_Status=StringVar()
        self.var_Last_Cleaned=StringVar()
        
        

        # ================================================ TITLE ====================================================
        lbl_title = Label(self.root,text = "ROOM  WINDOW",font=("times new roman",20,"bold"), bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1050,height=50)

        # ================================================ LOGO =======================================================
        img2=Image.open(r"C:\Users\HP\Desktop\Computer Science\Computer Programs\Python\Projects\logo2.PNG")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=5,width=100,height=40)

        # ============================================= LABEL FRAME ==================================================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Details",padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=390,height=250)
        # ============================================= LABELS AND ENTRIES ============================================
        # Student Building (combobox)
        Student_Building = Label(labelframeleft,text="Building",font=("times new roman",10,"bold"),padx=2,pady=6)
        Student_Building.grid(row=0,column=0,sticky=W)

        combo_building=ttk.Combobox(labelframeleft,textvariable=self.var_Building,font=("times new roman",11,"bold"),width=20) #,state="readonly"
        combo_building["value"]=("boys hostel","girls hostel")
        #combo_building.current(0)
        combo_building.grid(row=0,column=1,sticky=W)

        # Student's Room Number
        room_number = Label(labelframeleft,text="Room Number",font=("times new roman",10,"bold"),padx=2,pady=6)
        room_number.grid(row=1,column=0,sticky=W)

        entry_room_number=ttk.Entry(labelframeleft,textvariable=self.var_Room_Number,width=23,font=("times new roman",11,"bold"))
        entry_room_number.grid(row=1,column=1,sticky=W)
        

        # Fetch Data Button
        btn_fetch_data=Button(labelframeleft,command=self.Fetch_Info,text="FETCH \nDATA",font=("times new roman",11,"bold"),bg="black",fg="gold",width=10)
        btn_fetch_data.place(x=278,y=8)

        # Room Type (combobox)
        Room_Type= Label(labelframeleft,text="Room Type",font=("times new roman",10,"bold"),padx=2,pady=6)
        Room_Type.grid(row=2,column=0,sticky=W)

        combo_room_Type=ttk.Combobox(labelframeleft,textvariable=self.var_Room_Type,font=("times new roman",11,"bold"),width=27,state="readonly")
        combo_room_Type["value"]=("AC","Non AC")
        combo_room_Type.current(1)
        combo_room_Type.grid(row=2,column=1)

        # Room occupancy (combobox)
        Room_Occupancy= Label(labelframeleft,text="Room Size",font=("times new roman",10,"bold"),padx=2,pady=6)
        Room_Occupancy.grid(row=3,column=0,sticky=W)

        combo_room_occupancy=ttk.Combobox(labelframeleft,textvariable=self.var_Room_Size,font=("times new roman",11,"bold"),width=27,state="readonly")
        combo_room_occupancy["value"]=("Single Bed","Double Bed")
        #combo_room_occupancy.current(1)
        combo_room_occupancy.grid(row=3,column=1)

        # Room Status (combobox)
        Room_Status= Label(labelframeleft,text="Room Status",font=("times new roman",10,"bold"),padx=2,pady=6)
        Room_Status.grid(row=4,column=0,sticky=W)

        combo_room_status=ttk.Combobox(labelframeleft,textvariable=self.var_Room_Status,font=("times new roman",11,"bold"),width=27,state="readonly")
        combo_room_status["value"]=("Available","Full")
        #combo_room_status.current(0)
        combo_room_status.grid(row=4,column=1)

        # Last Cleaned (combobox)
        Room_Clean= Label(labelframeleft,text="Last Cleaned",font=("times new roman",10,"bold"),padx=2,pady=6)
        Room_Clean.grid(row=5,column=0,sticky=W)

        combo_room_clean=ttk.Combobox(labelframeleft,textvariable=self.var_Last_Cleaned,font=("times new roman",11,"bold"),width=27,state="readonly")
        combo_room_clean["value"]=("Within a Week","Within a Month")
        #combo_room_clean.current(1)
        combo_room_clean.grid(row=5,column=1)
        
        # ======================================================== BUTTONS ====================================================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=190,width=356,height=30)

        btn_add=Button(btn_frame,text="ADD",command=self.add_data,font=("times new roman",10,"bold"),bg="red",fg="gold",width=11)
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="UPDATE",command=self.update,font=("times new roman",10,"bold"),bg="red",fg="gold",width=11)
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="DELETE",command=self.room_delete,font=("times new roman",10,"bold"),bg="red",fg="gold",width=11)
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text="RESET",command=self.reset,font=("times new roman",10,"bold"),bg="red",fg="gold",width=11)
        btn_reset.grid(row=0,column=3,padx=1)

        # =========================================================== TABLE FRAME OF BOYS ==================================================================

        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="VIEW AND SEARCH DETAILS OF BOYS HOSTEL",font=("times new roman",12,"bold"))
        Table_Frame.place(x=405,y=50,width=860,height=180)

        # Search Label
        lblSearchBy = Label(Table_Frame,text="FILTER",font=("times new roman",10,"bold"),bg="black",fg="red")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()

        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("times new roman",11,"bold"),width=20,state="readonly")
        combo_Search["value"]=("Room Number","Room Type")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()

        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,width=20,font=("times new roman",11,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",command=self.search_data_boys,font=("times new roman",10,"bold"),bg="red",fg="gold",width=11)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",font=("times new roman",10,"bold"),bg="red",fg="gold",width=11)
        btnShowAll.grid(row=0,column=4,padx=1)

        # ================================================ TABLE FRAME OF GIRLS =================================================
        Table_Frame_girl=LabelFrame(self.root,bd=2,relief=RIDGE,text="VIEW AND SEARCH DETAILS OF GIRLS HOSTEL",font=("times new roman",12,"bold"))
        Table_Frame_girl.place(x=405,y=240,width=860,height=180)

        # Search Label
        lblSearchBy_girl = Label(Table_Frame_girl,text="FILTER",font=("times new roman",10,"bold"),bg="black",fg="red")
        lblSearchBy_girl.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var_girl=StringVar()

        combo_Search_girl=ttk.Combobox(Table_Frame_girl,textvariable=self.search_var,font=("times new roman",11,"bold"),width=20,state="readonly")
        combo_Search_girl["value"]=("Room Number","Room Type")
        combo_Search_girl.current(0)
        combo_Search_girl.grid(row=0,column=1,padx=2)

        self.txt_search_girl=StringVar()

        txtSearch_girl=ttk.Entry(Table_Frame_girl,textvariable=self.txt_search,width=20,font=("times new roman",11,"bold"))
        txtSearch_girl.grid(row=0,column=2,padx=2)

        btnSearch_girl=Button(Table_Frame_girl,text="Search",command=self.search_data_girls,font=("times new roman",10,"bold"),bg="red",fg="gold",width=11)
        btnSearch_girl.grid(row=0,column=3,padx=1)

        btnShowAll_girl=Button(Table_Frame_girl,text="Show All",font=("times new roman",10,"bold"),bg="red",fg="gold",width=11)
        btnShowAll_girl.grid(row=0,column=4,padx=1)

        # =============================================== DISPLAY BOYS TABLE ==============================================
        
        details_table=LabelFrame(Table_Frame,bd=2,relief=RIDGE,font=("times new roman",12,"bold"))
        details_table.place(x=2,y=30,width=630,height=135)

        # Scrollbar
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.boys_Details_Table=ttk.Treeview(details_table,column=("room_number","room_type","room_size","room_status","last_cleaned"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.boys_Details_Table.xview)
        scroll_y.config(command=self.boys_Details_Table.yview)

        self.boys_Details_Table.heading("room_number",text="room_number")
        self.boys_Details_Table.heading("room_type",text="room_type")
        self.boys_Details_Table.heading("room_size",text="room_size")
        self.boys_Details_Table.heading("room_status",text="room_status")
        self.boys_Details_Table.heading("last_cleaned",text="last_cleaned")
        

        self.boys_Details_Table["show"]="headings"

        self.boys_Details_Table.column("room_number",width=100)
        self.boys_Details_Table.column("room_type",width=100)
        self.boys_Details_Table.column("room_size",width=100)
        self.boys_Details_Table.column("room_status",width=100)
        self.boys_Details_Table.column("last_cleaned",width=100)
        
        
        
        
        


        


        self.boys_Details_Table.pack(fill=BOTH,expand=1)
        self.boys_Details_Table.bind("<ButtonRelease-1>",self.get_cursor_boys)
        self.fetch_data_boys()

        # =============================================== DISPLAY GIRLS TABLE ==============================================
        
        details_table=LabelFrame(Table_Frame_girl,bd=2,relief=RIDGE,font=("times new roman",12,"bold"))
        details_table.place(x=2,y=30,width=630,height=135)

        # Scrollbar
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.girls_Details_Table=ttk.Treeview(details_table,column=("room_number","room_type","room_size","room_status","last_cleaned"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.girls_Details_Table.xview)
        scroll_y.config(command=self.girls_Details_Table.yview)

        self.girls_Details_Table.heading("room_number",text="room_number")
        self.girls_Details_Table.heading("room_type",text="room_type")
        self.girls_Details_Table.heading("room_size",text="room_size")
        self.girls_Details_Table.heading("room_status",text="room_status")
        self.girls_Details_Table.heading("last_cleaned",text="last_cleaned")
        

        self.girls_Details_Table["show"]="headings"

        self.girls_Details_Table.column("room_number",width=100)
        self.girls_Details_Table.column("room_type",width=100)
        self.girls_Details_Table.column("room_size",width=100)
        self.girls_Details_Table.column("room_status",width=100)
        self.girls_Details_Table.column("last_cleaned",width=100)
        
        
        
        
        


        


        self.girls_Details_Table.pack(fill=BOTH,expand=1)
        self.girls_Details_Table.bind("<ButtonRelease-1>",self.get_cursor_girls)
        self.fetch_data_girls()

    # ================================================= ADD FUNCTION ===================================================
    def add_data(self):
        if self.var_Building.get() not in ["girls hostel","boys hostel"]:
            messagebox.showerror("Error"," wrong input in building \n either boys hostel or girls hostel",parent=self.root)
        else:
            if self.var_Building.get()=="girls hostel":
                if self.var_Room_Number.get()=="" or self.var_Room_Type.get()=="" or self.var_Room_Status.get()=="" :
                    messagebox.showerror("Error","ALL FIELDS ARE MANDATORY",parent=self.root)
                else:
                    try:
                        con=mysql.connector.connect(host="localhost",user="root",password="Soujatya@2003",database="hostel_management",auth_plugin='mysql_native_password')
                        my_cursor=con.cursor()
                        my_cursor.execute("insert into girl_building values(%s,%s,%s,%s,%s)",(
                                
                
                                self.var_Room_Number.get(),
                                self.var_Room_Type.get(),
                                self.var_Room_Size.get(),
                                self.var_Room_Status.get(),
                                self.var_Last_Cleaned.get()
                            ))
                        con.commit()
                        self.fetch_data_girls()
                        con.close()
                        messagebox.showinfo("Success","record has been added",parent=self.root)
                    except Exception as es:
                        messagebox.showwarning("Warning",f"something went wrong...please try again:{str(es)}",parent=self.root)
            
            if self.var_Building.get()=="boys hostel":
                if self.var_Room_Number.get()=="" or self.var_Room_Type.get()=="" or self.var_Room_Status.get()=="" :
                    messagebox.showerror("Error","ALL FIELDS ARE MANDATORY",parent=self.root)
                else:
                    try:
                        con=mysql.connector.connect(host="localhost",user="root",password="Soujatya@2003",database="hostel_management",auth_plugin='mysql_native_password')
                        my_cursor=con.cursor()
                        my_cursor.execute("insert into boy_building values(%s,%s,%s,%s,%s)",(
                                
                
                                self.var_Room_Number.get(),
                                self.var_Room_Type.get(),
                                self.var_Room_Size.get(),
                                self.var_Room_Status.get(),
                                self.var_Last_Cleaned.get()
                            ))
                        con.commit()
                        self.fetch_data_boys()
                        con.close()
                        messagebox.showinfo("Success","record has been added",parent=self.root)
                    except Exception as es:
                        messagebox.showwarning("Warning",f"something went wrong...please try again:{str(es)}",parent=self.root)
        
    # ================================================= FETCH ROOM DATA FUNCTION =======================================
    
    
    def fetch_data_girls(self):         
        con=mysql.connector.connect(host="localhost",user="root",password="Soujatya@2003",database="hostel_management",auth_plugin='mysql_native_password')
        my_cursor=con.cursor()
        my_cursor.execute("select * from girl_building")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.girls_Details_Table.delete(*self.girls_Details_Table.get_children())
            for i in rows:
                self.girls_Details_Table.insert("",END,values=i)
            con.commit()
        con.close()

    def get_cursor_girls(self,event=""):
        cursor_row=self.girls_Details_Table.focus()
        content=self.girls_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_Room_Number.set(row[0]),
        self.var_Room_Type.set(row[1]),
        self.var_Room_Size.set(row[2]),
        self.var_Room_Status.set(row[3]),
        self.var_Last_Cleaned.set(row[4])
        
    def fetch_data_boys(self):    
        con_2=mysql.connector.connect(host="localhost",user="root",password="Soujatya@2003",database="hostel_management",auth_plugin='mysql_native_password')
        my_cursor_2=con_2.cursor()
        my_cursor_2.execute("select * from boy_building")
        rows=my_cursor_2.fetchall()
        if len(rows)!=0:
            self.boys_Details_Table.delete(*self.boys_Details_Table.get_children())
            for i in rows:
                self.boys_Details_Table.insert("",END,values=i)
            con_2.commit()
        con_2.close()

    def get_cursor_boys(self,event=""):
        cursor_row=self.boys_Details_Table.focus()
        content=self.boys_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_Room_Number.set(row[0]),
        self.var_Room_Type.set(row[1]),
        self.var_Room_Size.set(row[2]),
        self.var_Room_Status.set(row[3]),
        self.var_Last_Cleaned.set(row[4])
        
    
    
    # ================================================= FETCH INFO FUNCTION ============================================

    def Fetch_Info(self):
        if self.var_Building.get()=="" or self.var_Room_Number.get()=="":
            messagebox.showerror("error", "please enter building and room number" , parent=self.root)
        
        else:
            con=mysql.connector.connect(host="localhost",user="root",password="Soujatya@2003",database="hostel_management",auth_plugin='mysql_native_password')
            
            my_cursor = con.cursor(buffered=True)
            query=("select Student_Name from student where Student_Building=%s and Room_Number=%s")
            value=(self.var_Building.get(),self.var_Room_Number.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchall()

            
            con.commit()
            con.close()

            showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
            showDataframe.place(x=5,y=305,width=392,height=120)

            lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
            lblName.place(x=0,y=0)

            lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl.place(x=60,y=0)

            con=mysql.connector.connect(host="localhost",user="root",password="Soujatya@2003",database="hostel_management",auth_plugin='mysql_native_password')
            
            my_cursor = con.cursor(buffered=True)
            query=("select Course from student where Student_Building=%s and Room_Number=%s")
            value=(self.var_Building.get(),self.var_Room_Number.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchall()

            lblCourse=Label(showDataframe,text="Course:",font=("arial",12,"bold"))
            lblCourse.place(x=0,y=25)

            lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl2.place(x=80,y=25)

            con=mysql.connector.connect(host="localhost",user="root",password="Soujatya@2003",database="hostel_management",auth_plugin='mysql_native_password')
            
            my_cursor = con.cursor(buffered=True)
            query=("select Student_ID from student where Student_Building=%s and Room_Number=%s")
            value=(self.var_Building.get(),self.var_Room_Number.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchall()

            lblID=Label(showDataframe,text="Student ID:",font=("arial",12,"bold"))
            lblID.place(x=0,y=50)

            lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl3.place(x=90,y=50)

            con=mysql.connector.connect(host="localhost",user="root",password="Soujatya@2003",database="hostel_management",auth_plugin='mysql_native_password')
            
            my_cursor = con.cursor(buffered=True)
            query=("select Student_Number from student where Student_Building=%s and Room_Number=%s")
            value=(self.var_Building.get(),self.var_Room_Number.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchall()

            lblNumber=Label(showDataframe,text="Student's Number:",font=("arial",12,"bold"))
            lblNumber.place(x=0,y=75)

            lbl4=Label(showDataframe,text=row,font=("arial",12,"bold"))
            lbl4.place(x=150,y=75)
    
    # ================================================= UPDATE FUNCTION ===============================================
    def update(self):
        if self.var_Building.get() not in ["girls hostel","boys hostel"]:
            messagebox.showerror("Error"," wrong input in building \n either boys hostel or girls hostel",parent=self.root)
        
        elif self.var_Building.get()=="boys hostel":
            if self.var_Room_Number.get()=="" or self.var_Room_Type.get()=="" or self.var_Room_Status.get()=="":
                messagebox.showerror("Error","Please Enter all details",parent=self.root)
            else:
                con=mysql.connector.connect(host="localhost",user="root",password="Soujatya@2003",database="hostel_management",auth_plugin='mysql_native_password')
                my_cursor=con.cursor()
                
                my_cursor.execute("UPDATE boy_building set room_type=%s,room_size=%s,room_status=%s,last_cleaned=%s WHERE room_number=%s",(
                # UPDATE `hostel_management`.`student` SET `Student_Name` = 'Rahul' WHERE (`Student_ID` = '9972');
                
                    
                
                
                self.var_Room_Type.get(),
                self.var_Room_Size.get(),
                self.var_Room_Status.get(),
                self.var_Last_Cleaned.get(),
                self.var_Room_Number.get() ))

                con.commit()
                self.fetch_data_boys()
                con.close()
                messagebox.showinfo("update","Room details has been updated successfully",parent=self.root)

        else:
            if self.var_Room_Number.get()=="" or self.var_Room_Type.get()=="" or self.var_Room_Status.get()=="":
                messagebox.showerror("Error","Please Enter all details",parent=self.root)
            else:
                con=mysql.connector.connect(host="localhost",user="root",password="Soujatya@2003",database="hostel_management",auth_plugin='mysql_native_password')
                my_cursor=con.cursor()
                
                my_cursor.execute("UPDATE girl_building set room_type=%s,room_size=%s,room_status=%s,last_cleaned=%s WHERE room_number=%s",(
                # UPDATE `hostel_management`.`student` SET `Student_Name` = 'Rahul' WHERE (`Student_ID` = '9972');
                
                    
                
                
                self.var_Room_Type.get(),
                self.var_Room_Size.get(),
                self.var_Room_Status.get(),
                self.var_Last_Cleaned.get(),
                self.var_Room_Number.get() ))

                con.commit()
                self.fetch_data_girls()
                con.close()
                messagebox.showinfo("update","Room details has been updated successfully",parent=self.root)

    # ================================================= DELETE FUNCTION =================================================
    def room_delete(self):
        if self.var_Building.get()=="boys hostel":
            stu_delete=messagebox.askyesno("Hostel Management System","Do you want to delete the room?",parent=self.root)
            if stu_delete>0:
                con=mysql.connector.connect(host="localhost",user="root",password="Soujatya@2003",database="hostel_management",auth_plugin='mysql_native_password')
                my_cursor=con.cursor()
                query="delete from boy_building where room_number=%s"
                value=(self.var_Room_Number.get(),)
                my_cursor.execute(query,value)
            else:
                if not room_delete():
                    return
            con.commit()
            self.fetch_data_boys()
            con.close()
            messagebox.showinfo("update","Room has been deleted successfully",parent=self.root)

        if self.var_Building.get()=="girls hostel":
            stu_delete=messagebox.askyesno("Hostel Management System","Do you want to delete the room?",parent=self.root)
            if stu_delete>0:
                con=mysql.connector.connect(host="localhost",user="root",password="Soujatya@2003",database="hostel_management",auth_plugin='mysql_native_password')
                my_cursor=con.cursor()
                query="delete from girl_building where room_number=%s"
                value=(self.var_Room_Number.get(),)
                my_cursor.execute(query,value)
            else:
                if not room_delete():
                    return
            con.commit()
            self.fetch_data_girls()
            con.close()
            messagebox.showinfo("update","Room has been deleted successfully",parent=self.root)
    
    # ================================================= RESET FUNCTION ================================================
    def reset(self):
        self.var_Building.set(""),
        self.var_Room_Type.set(""),
        self.var_Room_Size.set(""),
        self.var_Room_Status.set(""),
        self.var_Last_Cleaned.set(""),
        self.var_Room_Number.set("") 
    # ================================================= SEARCH FUNCTION ================================================
    def search_data_boys(self):
        
            if self.search_var.get()=="Room Number":
                con=mysql.connector.connect(host="localhost",user="root",password="Soujatya@2003",database="hostel_management",auth_plugin='mysql_native_password')
                my_cursor=con.cursor()
            
                my_cursor.execute("select * from boy_building where room_number LIKE '%" +str(self.txt_search.get())+"%'")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.boys_Details_Table.delete(*self.boys_Details_Table.get_children())
                    for i in rows:
                        self.boys_Details_Table.insert("",END,values=i)
                    con.commit()
                con.close()

    def search_data_girls(self):
        
            if self.search_var.get()=="Room Number":
                con=mysql.connector.connect(host="localhost",user="root",password="Soujatya@2003",database="hostel_management",auth_plugin='mysql_native_password')
                my_cursor=con.cursor()
            
                my_cursor.execute("select * from girl_building where room_number LIKE '%" +str(self.txt_search.get())+"%'")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.girls_Details_Table.delete(*self.girls_Details_Table.get_children())
                    for i in rows:
                        self.girls_Details_Table.insert("",END,values=i)
                    con.commit()
                con.close()
    
                



                


















if __name__== "__main__":
    root=Tk()
    obj=room_details(root)
    root.mainloop()