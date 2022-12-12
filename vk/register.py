
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
from pyparsing import Regex
import re

class Register:
    def __init__(self,root):
        self.root = root

        self.root.title("Registration Form")
        self.root.geometry("1550x785+0+0")



        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_email = StringVar()
        self.var_password = StringVar()
        self.var_cpassword = StringVar()
        self.var_check = IntVar()



        def For_login_window():
            self.root.destroy()
            import login
            
        

        # Conditions

        def Register_data():

        
            if self.var_fname.get() == "" or self.var_lname.get() == "" or self.var_email.get() == "" or self.var_password.get() == "" or self.var_cpassword.get() == "":
                messagebox.showerror("Error","All Fields Are Required!")

            elif self.var_check.get() == 0:
                messagebox.showerror("Error","Accept The Terms And Conditions")

            
            elif len(self.var_password.get()) < 8 :
                messagebox.showerror("Error","Password must be more than 8 character")

            elif self.var_password.get() != self.var_cpassword.get():
                messagebox.showerror("Error","Password not match!")

            else:

                try:
                    conn = pymysql.connect(host="localhost",user="root",password="",database="test")
                    cur = conn.cursor()
                    cur.execute("select * from users where email=%s",self.var_email.get())
                    row = cur.fetchone()
                    if row != None:
                        messagebox.showerror("Error","User Already Exit!")
                    else:

                        cur.execute("insert into users(first_name,last_name,email,password) values(%s,%s,%s,%s)",(
                                    self.var_fname.get(),
                                    self.var_lname.get(),
                                    self.var_email.get(),
                                    self.var_password.get()
                                    ))

                        conn.commit()
                        conn.close()
                        messagebox.showinfo("Success","Register Successfull")
                        clear()
                    

                except Exception as error:
                    messagebox.showerror("Error",f"Error due to {error}")


        def clear():
            self.txt_fname.delete(0,END)
            self.txt_lname.delete(0,END)
            self.txt_email.delete(0,END)
            self.txt_password.delete(0,END)
            self.txt_cpassword.delete(0,END)



        # Background Image

        image = Image.open("hotel3.jpg")
        self.bg = ImageTk.PhotoImage(file="hotel3.jpg")
        image1 = Label(self.root,image=self.bg)
        image1.place(x=0,y=0,relheight=1,relwidth=1)

        

        self.frame1 = Frame(self.root,bg="black")
        self.frame1.place(x=450,y=130,width=570,height=650)

        title = Label(self.frame1,text="Sign Up",font=("times new roman",20,"bold"),fg="green",bg="black").place(x=50,y=30)

        
        #-------------------------First Row-------------------------------------------

        self.fname=Label(self.frame1,text="First Name",font=("times new roman",13),bg="black",fg="white").place(x=50,y=100)
        self.txt_fname = Entry(self.frame1,font=("times new roman",13),textvariable=self.var_fname,borderwidth=3,bg="lightgray")
        self.txt_fname.place(x=50,y=130,height=32)

        self.lname=Label(self.frame1,text="Last Name",font=("times new roman",13),bg="black",fg="white").place(x=300,y=100)
        self.txt_lname = Entry(self.frame1,font=("times new roman",13),borderwidth=3,bg="lightgray",textvariable=self.var_lname)
        self.txt_lname.place(x=300,y=130,height=32)

        

        #-------------------------Second Row-------------------------------------------
        
        self.email=Label(self.frame1,text="Email Address",font=("times new roman",13),bg="black",fg="white").place(x=50,y=180)
        self.txt_email = Entry(self.frame1,font=("times new roman",13),borderwidth=3,bg="lightgray",textvariable=self.var_email)
        self.txt_email.place(x=50,y=210,height=32,width=439)

        

        self.password=Label(self.frame1,text="Password",font=("times new roman",13),bg="black",fg="white").place(x=50,y=260)
        self.txt_password = Entry(self.frame1,show="*",font=("times new roman",13),borderwidth=3,bg="lightgray",textvariable=self.var_password)
        self.txt_password.place(x=50,y=300,height=32,width=439)

        self.cpassword=Label(self.frame1,text="Confirm Password",font=("times new roman",13),bg="black",fg="white").place(x=50,y=340)
        self.txt_cpassword = Entry(self.frame1,show="*",font=("times new roman",13),borderwidth=3,bg="lightgray",textvariable=self.var_cpassword)
        self.txt_cpassword.place(x=50,y=380,height=32,width=439)



        self.check=Checkbutton(self.frame1,bg="black",onvalue=1,offvalue=0,activebackground="black",variable=self.var_check).place(x=50,y=430)
        self.txt_check=Label(self.frame1,text="Accept The Terms and Conditions",font=("times new roman",13),bg="black",fg="white")
        self.txt_check.place(x=70,y=430)
        

        self.button=Button(self.frame1,text="Sign Up",font=("times new roman",13,"bold"),bg="Green",command=Register_data,activebackground="white").place(x=50,y=470)

        # For Login Link

        self.label = Label(self.frame1,text="Already have an account?",font=("times new roman",12,"bold"),bg="black",fg="white")
        self.label.place(x=50,y=520)

        self.l_button = Button(self.frame1,text="Sign In",command=For_login_window,font=("times new roman",12,"bold"),bd=0,bg="black",fg="blue",activebackground="black")
        self.l_button.place(x=226,y=519)

        




root = Tk()
obj = Register(root)
root.mainloop()

