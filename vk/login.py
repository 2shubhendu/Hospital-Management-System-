
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql


class login:
    def __init__(self,root):
        self.root = root
        
        self.root.geometry("1550x800+0+0")
        self.root.title("Login Form")

        self.var_username = StringVar()
        self.var_password = StringVar()
    


        def login():
            if self.var_username.get() == "" or self.var_password.get()=="":
                messagebox.showerror("Error","All Fields Required")

            else:
                try:
                    conn = pymysql.connect(host="localhost",user="root",password="",database="test")
                    cur = conn.cursor()
                    cur.execute("select * from users where email=%s and password=%s",(self.var_username.get(),self.var_password.get()))
                    row = cur.fetchone()

                    if row == None:
                        messagebox.showerror("Error","Invalid Username Or Password")
                    else:
                        self.root.destroy()
                        import home
                        
                
                except Exception as Error:
                    messagebox.showerror("Error",f"Error due to {Error}")

        def For_register_window():
            self.root.destroy()
            import register
            

        def Forget_password():
            self.root2 = Toplevel()
            self.root2.title("Forget Password")
            self.root2.geometry("300x350+550+200")
            self.root2.focus_force()
            self.root2.grab_set()
            self.root2.config(bg="white")

            self.var_reset = StringVar()



            

            def reset():

                if self.var_reset.get() == "":
                    messagebox.showerror("Error","Enter your email")
                else:
                    conn = pymysql.connect(host="localhost",user="root",password="",database="test")
                    cur = conn.cursor()
                    cur.execute("select password from users where email=%s",self.var_reset.get())
                    row = cur.fetchone()
                    password = row

                    if row == None:
                        messagebox.showerror("Error","First Register Yourself")
                    else:
                        print(self.var_reset.get())
                        print(row)
                        #Pass_reset()

                        import smtplib
                        import random
                        

                        password = str(row)
                        receiver_email = (self.var_reset.get())

                        s = smtplib.SMTP("smtp.gmail.com" , 587)
                        s.starttls()

                        s.login("ncerpune12345@gmail.com" , "Ncer@123")
                        s.sendmail("ncerpune12345@gmail.com", receiver_email, password)
                        messagebox.showinfo("Success","Password sent successfully on your registered email")
                    
                        self.root2.destroy()


            image6 = Image.open("forget_password.jpg")
            image6 = image6.resize((270,140),Image.ANTIALIAS)
            self.image6 = ImageTk.PhotoImage(image=image6)
            label_image6 = Label(self.root2,image=self.image6,bg="white").place(x=10,y=5)

            info_label = Label(self.root2,text="Email Address",font=("times new roman",15,"bold"),bg="white",fg="black")
            info_label.place(x=10,y=150)

            self.txtemail = ttk.Entry(self.root2,font=("tiems new roman",15,"bold"),textvariable=self.var_reset)
            self.txtemail.place(x=10,y=185,height=30,width=280)


            # reset_password icon
            
            '''image7 = Image.open("reset_password.png")
            image7 = image7.resize((280,40),Image.ANTIALIAS)
            self.image7 = ImageTk.PhotoImage(image=image7)
            label_image7 = Label(self.root2,image=self.image7,bg="white").place(x=10,y=240)'''

            


            self.reset_button = Button(self.root2,command=reset,text="Reset Password",bg="Green")
            self.reset_button.place(x=10,y=240,height=40,width=280)




        self.image = ImageTk.PhotoImage(file="hotel.jpg")
        label_image = Label(self.root,image=self.image).place(x=0,y=0,relheight=1,relwidth=1)

        frame = Frame(self.root,bg="black")
        frame.place(x=80,y=200,width=340,height=470)

        img1 = Image.open("logo3.jpg")
        img1 = img1.resize((100,100),Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(image=img1)
        label_image2 = Label(frame,image=self.image2,bg="black",bd=0).place(x=120,y=20,width=100,height=100)

        self.username = Label(frame,text="Username",font=("tiems new roman",15,"bold"),fg="white",bg="black")
        self.username.place(x=60,y=150)

        self.txtuser = ttk.Entry(frame,font=("tiems new roman",15,"bold"),textvariable=self.var_username)
        self.txtuser.place(x=20,y=190,width=270)


        self.password = Label(frame,text="Password",font=("tiems new roman",15,"bold"),fg="white",bg="black")
        self.password.place(x=60,y=240 )

        self.txtpass = ttk.Entry(frame,show="*",font=("tiems new roman",15,"bold"),textvariable=self.var_password)
        self.txtpass.place(x=20,y=280,width=270)

        img2 = Image.open("user_icon.png")
        img2 = img2.resize((30,30),Image.ANTIALIAS)
        self.image3 = ImageTk.PhotoImage(image=img2)
        label_image3 = Label(frame,image=self.image3,bg="black").place(x=20,y=150)

        img3 = Image.open("pass_icon.png")
        img3 = img3.resize((30,30),Image.ANTIALIAS)
        self.image4 = ImageTk.PhotoImage(image=img3)
        label_image4 = Label(frame,image=self.image4,bg="black").place(x=20,y=240)

        #button = Button(self.root).place(x=140,y=530,width=200,height=44)

        img4 = Image.open("login_button.jpg")
        img4 = img4.resize((147,57),Image.ANTIALIAS)
        self.image5 = ImageTk.PhotoImage(image=img4)
        label_image5 = Label(self.root,image=self.image5,bg="black").place(x=120,y=530,width=290,height=40)

        self.button = Button(self.root,image=self.image5,background="black",bd=0,activebackground="black",command=login).place(x=140,y=530,width=200,height=44)

        # Registration Link

        self.reg_button = Button(frame,text="New User Register",command=For_register_window,font=("times new roman",12,"bold"),fg="white",bd=0,bg="black",activebackground="black")
        self.reg_button.place(x=20,y=390)

        # Forgot Password Link

        self.fp_button = Button(frame,text="Forget Password",command=Forget_password,font=("times new roman",12,"bold"),fg="white",bd=0,bg="black",activebackground="black")
        self.fp_button.place(x=20,y=419)

        #Condition For Login

        '''
        def login():
            if txtuser.get() == "" or txtpass.get()=="":
                messagebox.showerror("Error","All Fields Required")

            elif txtuser.get()=="Shubhendu" and txtpass.get()=="12345":
                messagebox.showinfo("Success","Login Successful")

            else:
                messagebox.showerror("Error","Invalid Username or Password")

                '''


root = Tk()
obj = login(root)
root.mainloop()


    