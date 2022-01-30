
import tkinter
from tkinter import *
from PIL import Image,ImageTk  # pip install pillow
from student import student_details
from room import room_details
from wtng_list import waiting_list
from food_facilities import food_details


class HostelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hostel Management System")
        self.root.geometry("1550x800+0+0")

# ================================================ TOP IMAGE =====================================================
        img1=Image.open(r"C:\Users\HP\Desktop\Computer Science\Computer Programs\Python\Projects\hostel.PNG")
        img1=img1.resize((1500,140),Image.ANTIALIAS)
   
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg = Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

# ================================================ LOGO =========================================================
        img2=Image.open(r"C:\Users\HP\Desktop\Computer Science\Computer Programs\Python\Projects\logo2.PNG")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=200,height=140)

# ================================================ TITLE ===================================================
        lbl_title = Label(self.root,text = "HOSTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="silver",fg="red",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1420,height=50)

# ================================================ MAIN FRAME ================================================
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

# ================================================ DASHBOARD ==================================================
        lbl_dashboard = Label(main_frame,text = "Dashboard",font=("times new roman",25,"bold"), bg="pink",fg="green",bd=4,relief=RIDGE)
        lbl_dashboard.place(x=0,y=0,width=230)
# ================================================ Button Frame ===============================================
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=40,width=228,height=230)

        student_btn=Button(btn_frame, text="Student Details",command=self.stud_details,width=20,font=("times new roman",14,"bold"), bg="black",fg="gold",bd=0,cursor="hand2")
        student_btn.grid(row=0,column=0,pady=1)

        rooms_btn=Button(btn_frame, text="Room Status",command=self.room_status,width=20,font=("times new roman",14,"bold"), bg="black",fg="gold",bd=0,cursor="hand2")
        rooms_btn.grid(row=1,column=0,pady=1)

        waitlist_btn=Button(btn_frame, text="Waiting List",command=self.wait_list,width=20,font=("times new roman",14,"bold"), bg="black",fg="gold",bd=0,cursor="hand2")
        waitlist_btn.grid(row=2,column=0,pady=1)

        foodfacilities_btn=Button(btn_frame, text="Food Facilities",command=self.food,width=20,font=("times new roman",14,"bold"), bg="black",fg="gold",bd=0,cursor="hand2")
        foodfacilities_btn.grid(row=3,column=0,pady=1)

        

        
# ============================================= Large Image =======================================
        img3=Image.open(r"C:\Users\HP\Desktop\Computer Science\Computer Programs\Python\Projects\hostel_final.PNG")
        img3=img3.resize((1310,480),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg = Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=225,y=0,width=1310,height=480)

# ============================================= Leftside Images =========================================
        

        img5=Image.open(r"C:\Users\HP\Desktop\Computer Science\Computer Programs\Python\Projects\left_image_final.PNG")
        img5=img5.resize((229,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg = Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=270,width=229,height=200)


    def stud_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student_details(self.new_window)
        

    def room_status(self):
        self.new_window=Toplevel(self.root)
        self.app=room_details(self.new_window)

    def wait_list(self):
        self.new_window=Toplevel(self.root)
        self.app=waiting_list(self.new_window)

    def food(self):
        self.new_window=Toplevel(self.root)
        self.app=food_details(self.new_window)
        

if __name__== "__main__":
        root=Tk()
        obj=HostelManagementSystem(root)
        root.mainloop()