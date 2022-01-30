from tkinter import *
from PIL import Image,ImageTk  # pip install pillow
from tkinter import ttk
import random
import mysql.connector

from tkinter import messagebox

class food_details:
    def __init__(self,root):
        self.root=root
        self.root.title("Food Facilities")
        self.root.geometry("1050x428+230+220")
    
    # ================================================ VARIABLES =================================================
        
        
        self.var_item_name=StringVar()
        self.var_item_price_in_Rs=IntVar()

    # ================================================ TITLE ====================================================
        lbl_title = Label(self.root,text = "FOOD FACILITIES",font=("times new roman",20,"bold"), bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1050,height=50)

    # ================================================ LOGO =======================================================
        img2=Image.open(r"C:\Users\HP\Desktop\Computer Science\Computer Programs\Python\Projects\logo2.PNG")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=5,width=100,height=40)
    # ============================================= LABEL FRAME ==================================================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Food Table",padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=390,height=490)
    
    # ============================================= LABELS AND ENTRIES ======================================

    # Student ID
        student_ID = Label(labelframeleft,text="Item Name",font=("times new roman",10,"bold"),padx=2,pady=6)
        student_ID.grid(row=0,column=0,sticky=W)

        entry_ID=ttk.Entry(labelframeleft,textvariable=self.var_item_name,width=29,font=("times new roman",11,"bold"))
        entry_ID.grid(row=0,column=1)

    # Student Name
        student_name = Label(labelframeleft,text="Item Price",font=("times new roman",10,"bold"),padx=2,pady=6)
        student_name.grid(row=1,column=0,sticky=W)

        entry_name=ttk.Entry(labelframeleft,width=29,textvariable=self.var_item_price_in_Rs,font=("times new roman",11,"bold"))
        entry_name.grid(row=1,column=1)

    # =============================================== FOOD IMAGE =============================================
    
        img3=Image.open(r"C:\Users\HP\Desktop\Computer Science\Computer Programs\Python\Projects\food.PNG")
        img3=img3.resize((370,200),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg3 = Label(labelframeleft, image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg3.place(x=5,y=90,width=370,height=200)

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
        combo_Search["value"]=("item_name","item_price_in_Rs")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()

        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,width=20,font=("times new roman",11,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("times new roman",10,"bold"),bg="red",fg="gold",width=11)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",font=("times new roman",10,"bold"),bg="red",fg="gold",width=11)
        btnShowAll.grid(row=0,column=4,padx=1)

        # ============================================== Display Data Table ===========================================

        details_table=LabelFrame(Table_Frame,bd=2,relief=RIDGE,font=("times new roman",12,"bold"))
        details_table.place(x=2,y=30,width=630,height=300)

        # Scrollbar
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Student_Details_Table=ttk.Treeview(details_table,column=("item_name","item_price_in_Rs"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Student_Details_Table.xview)
        scroll_y.config(command=self.Student_Details_Table.yview)

        self.Student_Details_Table.heading("item_name",text="item_name")
        self.Student_Details_Table.heading("item_price_in_Rs",text="item_price_in_Rs")
        

        self.Student_Details_Table["show"]="headings"

        self.Student_Details_Table.column("item_name",width=100)
        self.Student_Details_Table.column("item_price_in_Rs",width=100)
        self.Student_Details_Table.pack(fill=BOTH,expand=1)
        self.Student_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

    # ================================================ ADD DATA FUNCTION ===============================================

    def add_data(self):
        if self.var_item_name.get()=="" or self.var_item_price_in_Rs.get()=="" :
            messagebox.showerror("Error","ALL FIELDS ARE MANDATORY",parent=self.root)
        else:
            try:
                con=mysql.connector.connect(host="localhost",user="root",password="Soujatya@2003",database="hostel_management",auth_plugin='mysql_native_password')
                my_cursor=con.cursor()
                my_cursor.execute("insert into food values(%s,%s)",(
                        
                
                        self.var_item_name.get(),
                        self.var_item_price_in_Rs.get(),
                        
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
        my_cursor.execute("select * from food")
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

        self.var_item_name.set(row[0])
                
        self.var_item_price_in_Rs.set(row[1])

    # ================================================ UPDATE FUNCTION =====================================================

    def update(self):
        if self.var_item_price_in_Rs.get()=="" or self.var_item_name.get()=="" :
            messagebox.showerror("Error","Please Enter all details",parent=self.root)
        else:
            con=mysql.connector.connect(host="localhost",user="root",password="Soujatya@2003",database="hostel_management",auth_plugin='mysql_native_password')
            my_cursor=con.cursor()
            
            my_cursor.execute("UPDATE food set item_price_in_Rs=%s WHERE item_name=%s",(
            # UPDATE `hostel_management`.`student` SET `Student_Name` = 'Rahul' WHERE (`Student_ID` = '9972');
            
            self.var_item_price_in_Rs.get(),    
            self.var_item_name.get()
            ))
        

            con.commit()
            self.fetch_data()
            con.close()
            messagebox.showinfo("update","menu details has been updated successfully",parent=self.root)

    
    # ==================================================== DELETE FUNCTION ===============================================
    def stu_delete(self):
        stu_delete=messagebox.askyesno("Hostel Management System","Do you want to delete the records of this food?",parent=self.root)
        if stu_delete>0:
            con=mysql.connector.connect(host="localhost",user="root",password="Soujatya@2003",database="hostel_management",auth_plugin='mysql_native_password')
            my_cursor=con.cursor()
            query="delete from food where item_name=%s"
            value=(self.var_item_name.get(),)
            my_cursor.execute(query,value)
        else:
            if not stu_delete:
                return
        con.commit()
        self.fetch_data()
        con.close()
        messagebox.showinfo("update","menu has been deleted successfully",parent=self.root)

    # ===================================================== RESET FUNCTION =============================================

    def reset(self):
    
        self.var_item_name.set(""),
        self.var_item_price_in_Rs.set("")

    # ================================================== SEARCH FUNCTION ===============================================
    def search(self):

        if self.search_var.get()=="item_name":
            con=mysql.connector.connect(host="localhost",user="root",password="Soujatya@2003",database="hostel_management",auth_plugin='mysql_native_password')
            my_cursor=con.cursor()
            
            my_cursor.execute("select * from food  where item_name LIKE '%" +str(self.txt_search.get())+"%'")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.Student_Details_Table.delete(*self.Student_Details_Table.get_children())
                for i in rows:
                    self.Student_Details_Table.insert("",END,values=i)
                con.commit()
            con.close()

        if self.search_var.get()=="item_price_in_Rs":
            con=mysql.connector.connect(host="localhost",user="root",password="Soujatya@2003",database="hostel_management",auth_plugin='mysql_native_password')
            my_cursor=con.cursor()
            
            my_cursor.execute("select * from food  where item_price_in_Rs LIKE '%" +str(self.txt_search.get())+"%'")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.Student_Details_Table.delete(*self.Student_Details_Table.get_children())
                for i in rows:
                    self.Student_Details_Table.insert("",END,values=i)
                con.commit()
            con.close()

        
        
        

    
        
        
        
        


        


        
        



if __name__== "__main__":
    root=Tk()
    obj=food_details(root)
    root.mainloop()
