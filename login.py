from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox
from hostel_management2 import HostelManagementSystem

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        bg=Image.open(r"C:\Users\HP\Desktop\Computer Science\Computer Programs\Python\Projects\login1.PNG")
        bg=bg.resize((1550,800),Image.ANTIALIAS)
        self.bg=ImageTk.PhotoImage(bg)

        lblimg = Label(self.root,image=self.bg,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=800)

        frame=Frame(self.root,bg="black")
        frame.place(x=450,y=170,width=360,height=360)

        img1=Image.open(r"C:\Users\HP\Desktop\Computer Science\Computer Programs\Python\Projects\login2.PNG")
        img1=img1.resize((360,120),Image.ANTIALIAS)
        self.img1=ImageTk.PhotoImage(img1)

        lblimg1 = Label(self.root,image=self.img1,bd=4,relief=RIDGE,borderwidth=0,bg="black")
        lblimg1.place(x=450,y=170,width=360,height=150)

        # ================================================ TITLE ====================================================
        lbl_title = Label(lblimg1,text = "LOGIN WINDOW",font=("times new roman",20,"bold"), bg="red",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=360,height=50)

        get_str=Label(frame,text="Get Started",font=("times new roman",18,"bold"),fg="white",bg="black")
        get_str.place(x=110,y=144)

        # label
        username=Label(frame,text="username",font=("times new roman",16,"bold"),fg="gold",bg="black")
        username.place(x=95,y=174)

        self.txtuser=ttk.Entry(frame,font=("times new roman",11,"bold"))
        self.txtuser.place(x=70,y=200,width=210)

        password=Label(frame,text="password",font=("times new roman",16,"bold"),fg="gold",bg="black")
        password.place(x=95,y=230)

        self.txtpass=ttk.Entry(frame,font=("times new roman",11,"bold"))
        self.txtpass.place(x=70,y=260,width=210)

        # ==================================================== ICON IMAGES =============================================
        img2=Image.open(r"C:\Users\HP\Desktop\Computer Science\Computer Programs\Python\Projects\login3.PNG")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.img2=ImageTk.PhotoImage(img2)

        lblimg2 = Label(image=self.img2,bd=4,relief=RIDGE,borderwidth=0,bg="black")
        lblimg2.place(x=520,y=348,width=22,height=22)

        img3=Image.open(r"C:\Users\HP\Desktop\Computer Science\Computer Programs\Python\Projects\login4.PNG")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.img3=ImageTk.PhotoImage(img3)

        lblimg3 = Label(image=self.img3,bd=4,relief=RIDGE,borderwidth=0,bg="black")
        lblimg3.place(x=520,y=409,width=22,height=22)

        # ==================================================== LOGIN BUTTON ============================================
        loginbtn=Button(frame,text="Login",command=self.Login,font=("times new roman",11,"bold"),bd=3,relief=RIDGE,fg="yellow",bg="sky blue",cursor="hand2",activeforeground="yellow",activebackground="sky blue")
        loginbtn.place(x=120,y=290,width=120,height=25)
        
        # ===================================================== REGISTER BUTTON ========================================
        registerbtn=Button(frame,text="New User Register",font=("times new roman",8,"bold"),bd=0,fg="white",bg="black",cursor="hand2",activeforeground="white",activebackground="black")
        registerbtn.place(x=120,y=320,width=120,height=15)

        # ====================================================== FORGOT PASSWORD ========================================

        forgotbtn=Button(frame,text="Forgot Password",font=("times new roman",8,"bold"),bd=0,fg="white",bg="black",cursor="hand2",activeforeground="white",activebackground="black")
        forgotbtn.place(x=120,y=340,width=120,height=15)

    def Login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="" :
            messagebox.showerror("Error","All fields are required")
        elif self.txtuser.get()=="Soujatya" and self.txtpass.get()=="@15":
            messagebox.showinfo("Succes","Login Successful")
            self.new_window=Toplevel(self.root)
            self.app=HostelManagementSystem(self.new_window)
        else:
            messagebox.showerror("Invalid","Invalid username or password")

            
                
        






        




    

if __name__== "__main__":
    root=Tk()
    app=Login_Window(root)
    root.mainloop()

