import imp
import profile
from tkinter import *
from turtle import clear
from PIL import Image,ImageTk
from matplotlib import image
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import pymysql
import os
import io
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


class Hotel:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1550x800+0+0")
        self.root.title("Hotel Management System")



        #---------------------------------Logo-------------------------------

        image1 = Image.open("royal_image.jpg")
        image1 = image1.resize((250,150),Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(image=image1)
        label_image1 = Label(self.root,image=self.image1)
        label_image1.place(x=0,y=0)


        '''#---------------------------------Title-------------------------------
        
        label_title = Label(self.root,text="Hotel Management System",font=("times new roman",33,"bold"),background="gray12",fg="yellow")
        label_title.place(x=254,y=0,width=1350,height=50)'''


        #---------------------------------Options-------------------------------

        self.frame1 = Frame(self.root,relief=RIDGE,bd=4,bg="gray14")
        self.frame1.place(x=0,y=150,height=1300,width=254)



        customer_icon = Image.open("home_logo2.jpg")
        customer_icon = customer_icon.resize((60,60),Image.ANTIALIAS)
        self.customer_icon = ImageTk.PhotoImage(image=customer_icon)
        customer_icon_label = Label(self.frame1,image=self.customer_icon,bg="gray14")
        customer_icon_label.place(x=10,y=20)

        button_customer = Button(self.frame1,text="Home",command=self.home,font=("times new roman",15,"bold"),background="gray14",fg="white",bd=0,activebackground="gray14",activeforeground="white",cursor="hand2")
        button_customer.place(x=85,y=35)




        check_in_icon = Image.open("customer_icon.png")
        check_in_icon = check_in_icon.resize((60,60),Image.ANTIALIAS)
        self.check_in_icon = ImageTk.PhotoImage(image=check_in_icon)
        label_check_in_icon = Label(self.frame1,image=self.check_in_icon,bg="gray14")
        label_check_in_icon.place(x=10,y=95)

        check_in_booking = Button(self.frame1,text="Customers",command=self.customer,font=("times new roman",15,"bold"),background="gray14",fg="white",bd=0,activebackground="gray14",activeforeground="white",cursor="hand2")
        check_in_booking.place(x=85,y=107)



        check_out_icon = Image.open("room_logo1.jpg")
        check_out_icon = check_out_icon.resize((60,60),Image.ANTIALIAS)
        self.check_out_icon = ImageTk.PhotoImage(image=check_out_icon)
        label_check_out_icon = Label(self.frame1,image=self.check_out_icon,bg="gray14")
        label_check_out_icon.place(x=10,y=180)

        check_out_booking = Button(self.frame1,text="Room Booking",command=self.room_booking,font=("times new roman",15,"bold"),background="gray14",fg="white",bd=0,activebackground="gray14",activeforeground="white",cursor="hand2")
        check_out_booking.place(x=85,y=192)




        report_icon = Image.open("report2.png")
        report_icon = report_icon.resize((60,60),Image.ANTIALIAS)
        self.report_icon = ImageTk.PhotoImage(image=report_icon)
        label_report_icon = Label(self.frame1,image=self.report_icon,bg="gray14")
        label_report_icon.place(x=10,y=270)

        report_icon_button = Button(self.frame1,text="Room Details",command=self.room_details,font=("times new roman",15,"bold"),background="gray14",fg="white",bd=0,activebackground="gray14",activeforeground="white",cursor="hand2")
        report_icon_button.place(x=85,y=281)



        profile_icon = Image.open("profile.png")
        profile_icon = profile_icon.resize((60,60),Image.ANTIALIAS)
        self.profile_icon = ImageTk.PhotoImage(image=profile_icon)
        label_profile_icon = Label(self.frame1,image=self.profile_icon,bg="gray14")
        label_profile_icon.place(x=10,y=370)

        profile_icon_button = Button(self.frame1,text="Profile",font=("times new roman",15,"bold"),background="gray14",fg="white",bd=0,activebackground="gray14",activeforeground="white",cursor="hand2")
        profile_icon_button.place(x=85,y=381)



        logout_icon = Image.open("logout.jpg")
        logout_icon = logout_icon.resize((60,60),Image.ANTIALIAS)
        self.logout_icon = ImageTk.PhotoImage(image=logout_icon)
        label_logout_icon = Label(self.frame1,image=self.logout_icon,bg="gray14")
        label_logout_icon.place(x=10,y=470)

        logout_icon_button = Button(self.frame1,text="Logout",command=self.logout,font=("times new roman",15,"bold"),background="gray14",fg="white",bd=0,activebackground="gray14",activeforeground="white",cursor="hand2")
        logout_icon_button.place(x=85,y=481)




        exit_icon = Image.open("exit.jpg")
        exit_icon = exit_icon.resize((60,60),Image.ANTIALIAS)
        self.exit_icon = ImageTk.PhotoImage(image=exit_icon)
        label_exit_icon = Label(self.frame1,image=self.exit_icon,bg="gray14")
        label_exit_icon.place(x=10,y=560)

        exit_icon_button = Button(self.frame1,text="Exit",command=self.exit,font=("times new roman",15,"bold"),background="gray14",fg="white",bd=0,activebackground="gray14",activeforeground="white",cursor="hand2")
        exit_icon_button.place(x=85,y=571)


        #---------------------------------Label-------------------------------

        label_title = Label(self.root,text="Profile",font=("times new roman",33,"bold"),background="gray12",fg="yellow")
        label_title.place(x=254,y=2,width=1350,height=50)


        #------------------------------------Variables-------------------------------

        self.var_full_name = StringVar()
        self.var_phone_number = StringVar()
        self.var_gender = StringVar()
        self.var_email_address = StringVar()
        self.var_country = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_address = StringVar()
        self.var_role = StringVar()
        self.var_education = StringVar()
        self.var_percentage = StringVar()
        self.var_salary = StringVar()
        self.var_joining_date = StringVar()
        self.var_exit_date = StringVar()

        #---------------------------------Customer Details-------------------------------

        self.first_label_frame = LabelFrame(self.root,text="Staff Details",bd=4,font=("times new roman",15,"bold"))
        self.first_label_frame.place(x=256,y=52,width=1270,height=470)



        def showimage():
            global image1
            fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select A File",filetype=(("jpeg","*.jpg"),("png","*.png")))
            img = Image.open(fln)
            image1 = img.save("photo1.jpg")
            img.thumbnail((90,90))
            img = ImageTk.PhotoImage(img)
            lbl.config(image=img)
            lbl.image = img


            '''
            conn = pymysql.connect(host="localhost",user="root",password="",database="test")
            cur = conn.cursor()
            query = "insert into staff_details (image) values(%s)"
            with open('photo1.jpg','rb') as file:
                binarydata = file.read()
            cur.execute(query,binarydata)
            conn.commit()
            conn.close()'''
        lbl = Label(self.first_label_frame)
        lbl.place(x=600,y=0)


        btn = Button(self.first_label_frame,text="Browse Image",command=showimage)
        btn.place(x=500,y=20)


        '''def Upload_file():
            fileName = filedialog.askopenfilename(initialdir = "/", title="Select A File",filetype=(("jpeg","*.jpg"),("png","*.png")))
            img= Image.open(fileName)
            img = img.resize((60,60),Image.ANTIALIAS)
            image = ImageTk.PhotoImage(img)
            image1 = Label(self.first_label_frame,image=image)
            image1.place(x=200,y=20)

    
        self.button = ttk.Button(self.first_label_frame, text="Browse Afile", command=Upload_file)
        self.button.grid(row=1,column=1)'''


        #----------------------------------1st Column---------------------------------

        self.firstlabel = Label(self.first_label_frame,text="Full Name",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.firstlabel.place(x=10,y=80)
        self.firstentry = ttk.Entry(self.first_label_frame,font=("Copperplate",13),width=30,textvariable=self.var_full_name)
        self.firstentry.place(x=150,y=95)

        

        
        self.secondlabel = Label(self.first_label_frame,text="Phone Number",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.secondlabel.place(x=10,y=135)
        self.secondentry = ttk.Entry(self.first_label_frame,font=("Copperplate",13),width=30,textvariable=self.var_phone_number)
        self.secondentry.place(x=150,y=155)

        
        self.thirdlabel = Label(self.first_label_frame,text="Gender",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.thirdlabel.place(x=10,y=195)
        self.firstcombo = ttk.Combobox(self.first_label_frame,font=("Copperplate",13,"bold"),width=28,textvariable=self.var_gender)
        self.firstcombo["values"] = ("Male","Female","Other")
        self.firstcombo.current(0)
        self.firstcombo["state"] = ("readonly")
        self.firstcombo.place(x=150,y=215)


        
        self.fourthlabel = Label(self.first_label_frame,text="Email Address",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.fourthlabel.place(x=10,y=255)
        self.fourthentry = ttk.Entry(self.first_label_frame,font=("Copperplate",13),width=30,textvariable=self.var_email_address)
        self.fourthentry.place(x=150,y=275)

        self.sixtheenlabel = Label(self.first_label_frame,text="Country",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.sixtheenlabel.place(x=10,y=315)
        self.sixtheenentry = ttk.Entry(self.first_label_frame,font=("Copperplate",13),width=30,textvariable=self.var_country)
        self.sixtheenentry.place(x=150,y=335)


        #--------------------------------2nd Column-----------------------------


        self.sixthlabel = Label(self.first_label_frame,text="State",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.sixthlabel.place(x=450,y=80)
        self.sixthentry = ttk.Entry(self.first_label_frame,font=("Copperplate",13),width=30,textvariable=self.var_state)
        self.sixthentry.place(x=550,y=95)

        self.seventhlabel = Label(self.first_label_frame,text="City",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.seventhlabel.place(x=450,y=135)
        self.seventhentry = ttk.Entry(self.first_label_frame,font=("Copperplate",13),width=30,textvariable=self.var_city)
        self.seventhentry.place(x=550,y=155)

        self.eightlabel = Label(self.first_label_frame,text="Address",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.eightlabel.place(x=450,y=195)
        self.eightentry = ttk.Entry(self.first_label_frame,font=("Copperplate",13),width=30,textvariable=self.var_address)
        self.eightentry.place(x=550,y=215)

        self.ninthlabel = Label(self.first_label_frame,text="Role",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.ninthlabel.place(x=450,y=255)
        self.ninthentry = ttk.Entry(self.first_label_frame,font=("Copperplate",13),width=30,textvariable=self.var_role)
        self.ninthentry.place(x=550,y=275)


        #----------------------------------3rd Column----------------------------------

        self.tenthlabel = Label(self.first_label_frame,text="Education",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.tenthlabel.place(x=850,y=80)
        self.secondcombo = ttk.Combobox(self.first_label_frame,font=("Copperplate",13,"bold"),width=28,textvariable=self.var_education)
        self.secondcombo["values"] = ("SSC","HSC","Higher Education")
        self.secondcombo.current(0)
        self.secondcombo["state"] = ("readonly")
        self.secondcombo.place(x=970,y=95)

        self.eleventhlabel = Label(self.first_label_frame,text="Percentage",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.eleventhlabel.place(x=850,y=135)
        self.eleventhentry = ttk.Entry(self.first_label_frame,font=("Copperplate",13),width=30,textvariable=self.var_percentage)
        self.eleventhentry.place(x=970,y=155)

        self.twelthlabel = Label(self.first_label_frame,text="Salary",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.twelthlabel.place(x=850,y=195)
        self.twelthentry = ttk.Entry(self.first_label_frame,font=("Copperplate",13),width=30,textvariable=self.var_salary)
        self.twelthentry.place(x=970,y=215)

        self.fourtheenlabel = Label(self.first_label_frame,text="Joining Date",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.fourtheenlabel.place(x=850,y=255)
        self.fourtheenentry = ttk.Entry(self.first_label_frame,font=("Copperplate",13),width=30,textvariable=self.var_joining_date)
        self.fourtheenentry.place(x=970,y=275)

        self.fiftheenlabel = Label(self.first_label_frame,text="Exit Date",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.fiftheenlabel.place(x=850,y=315)
        self.fiftheenentry = ttk.Entry(self.first_label_frame,font=("Copperplate",13),width=30,textvariable=self.var_exit_date)
        self.fiftheenentry.place(x=970,y=335)

        #-------------------------------------Buttons-----------------------------------

        self.button_frame = Frame(self.first_label_frame,bd=0,relief=RIDGE)
        self.button_frame.place(x=370,y=385,width=502,height=50)


        self.Fetchbutton = Button(self.first_label_frame,text="Get Staff Data",font=("Copperplate",13,"bold"),bg="Green",fg="white",width=20,command=self.fetch_data)
        self.Fetchbutton.place(x=550,y=330)

        self.Addbutton = Button(self.button_frame,text="Add",font=("Copperplate",13,"bold"),bg="Green",fg="white",width=8,command=self.Staff_data_add)
        self.Addbutton.place(x=25,y=5)

        self.updatebutton = Button(self.button_frame,text="Update",font=("Copperplate",13,"bold"),bg="Green",fg="white",width=8,command=self.update_data)
        self.updatebutton.place(x=150,y=5)

        self.deletebutton = Button(self.button_frame,text="Delete",font=("Copperplate",13,"bold"),bg="Green",fg="white",width=8,command=self.delete_data)
        self.deletebutton.place(x=278,y=5)

        self.clearbutton = Button(self.button_frame,text="Clear",font=("Copperplate",13,"bold"),bg="Green",fg="white",width=8,command=self.reset)
        self.clearbutton.place(x=404,y=5)

    #---------------------------------View Staff Details-------------------------------

        second_label_frame = LabelFrame(self.root,text="View Staff Details",bd=4,font=("times new roman",15,"bold"))
        second_label_frame.place(x=256,y=522,width=1270,height=360)

        self.search_val = StringVar()

        eleventhlabel = Label(second_label_frame,text="Search By:",font=("Copperplate",14,"bold"),bg="green",fg="white",padx=7)
        eleventhlabel.place(x=90,y=12)
        fifthcombo = ttk.Combobox(second_label_frame,font=("Copperplate",14,"bold"),width=20,textvariable=self.search_val)
        fifthcombo["values"] = ("full_name","Email_Address")
        fifthcombo.current(1)
        fifthcombo["state"] = ("readonly")
        fifthcombo.place(x=40,y=60)


        self.search_txt = StringVar()

        self.fifteenentry = ttk.Entry(second_label_frame,font=("Copperplate",13),width=29,textvariable=self.search_txt)
        self.fifteenentry.place(x=30,y=110,height=29)

        searchbutton = Button(second_label_frame,text="Search",font=("Copperplate",11,"bold"),bg="Green",fg="white",command=self.search)
        searchbutton.place(x=120,y=160)

        showallbutton = Button(second_label_frame,text="Show All",font=("Copperplate",11,"bold"),bg="Green",fg="white",command=self.Staff_data_fetch)
        showallbutton.place(x=115,y=210)

        third_label_frame = Frame(second_label_frame,bd=4)
        third_label_frame.place(x=300,y=10,width=950,height=210)

        x_scroll = ttk.Scrollbar(third_label_frame,orient=HORIZONTAL)
        y_scroll = ttk.Scrollbar(third_label_frame,orient=VERTICAL)

        self.view = ttk.Treeview(third_label_frame,columns=("full_name","phone_number","gender","email_address"),xscrollcommand=x_scroll.set,yscrollcommand=y_scroll.set)

        x_scroll.pack(side=BOTTOM,fill=X)
        y_scroll.pack(side=RIGHT,fill=Y)

        x_scroll.config(command=self.view.xview)
        y_scroll.config(command=self.view.yview)

        self.view.heading("full_name",text="Full Name")
        self.view.heading("phone_number",text="Phone Number")
        self.view.heading("gender",text="Gender")
        self.view.heading("email_address",text="Email Address")
        #self.view.heading("Email",text="Email")


        self.view["show"] = "headings"

        
        self.view.column("full_name",width=120)
        self.view.column("phone_number",width=120)
        self.view.column("gender",width=120)
        self.view.column("email_address",width=120)
        #self.view.column("Email",width=120)

        self.view.pack(fill=BOTH,expand=1)

        self.view.bind("<ButtonRelease-1>",self.show_data)

        self.Staff_data_fetch()

        #---------------------------------Adding  Staff Data In Database-------------------------------

    def Staff_data_add(self):
        if self.var_full_name.get() == "" :
            messagebox.showerror("Error","All Fields Are Required!",parent=self.root)
        else:
            conn = pymysql.connect(host="localhost",user="root",password="",database="test")
            cur = conn.cursor()
            cur.execute("select * from staff_details where email_address=%s",self.var_email_address.get())
            row = cur.fetchone()
            if row != None:
                messagebox.showerror("Error","User Already Exit!")
            else:

                try:
                    conn = pymysql.connect(host="localhost",user="root",password="",database="test")
                    cur = conn.cursor()

                    query = "insert into staff_details(full_name,phone_number,gender,email_address,country,state,city,address,role,education,percentage,salary,joining_date,exit_date,image) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    
                    
                    with open('photo1.jpg','rb') as file:
                        binarydata = file.read()

                    cur.execute(query,
                                        (

                                                    self.var_full_name.get(),
                                                    self.var_phone_number.get(),
                                                    self.var_gender.get(),
                                                    self.var_email_address.get(),
                                                    self.var_country.get(),
                                                    self.var_state.get(),
                                                    self.var_city.get(),
                                                    self.var_address.get(),
                                                    self.var_role.get(),
                                                    self.var_education.get(),
                                                    self.var_percentage.get(),
                                                    self.var_salary.get(),
                                                    self.var_joining_date.get(),
                                                    self.var_exit_date.get(),
                                                    binarydata
                                                                                                
                                                                    ))

                    conn.commit()
                    self.Staff_data_fetch()
                    conn.close()
                    messagebox.showinfo("Success","Customer Has Been Added")
                    self.clear()

                except Exception as Error:
                    messagebox.showerror("Error",f"Error due to {Error}",parent=self.root)



    #---------------------------------Showing Customer Data in Table-------------------------------

    def Staff_data_fetch(self):
        conn = pymysql.connect(host="localhost",user="root",password="",database="test")
        cur = conn.cursor()
        cur.execute("select * from staff_details")
        row = cur.fetchall()
        if row != 0:
            self.view.delete(*self.view.get_children())
            for i in row:
                self.view.insert("",END,values=i)
            conn.commit()
        conn.close()


    def show_data(self,event=""):
        cursor_row = self.view.focus()
        content = self.view.item(cursor_row)
        row = content["values"]

        self.var_full_name.set(row[0])
        self.var_phone_number.set(row[1])
        self.var_gender.set(row[2])
        self.var_email_address.set(row[3])
        self.var_country.set(row[4])
        self.var_state.set(row[5])
        self.var_city.set(row[6])
        self.var_address.set(row[7])
        self.var_role.set(row[8])
        self.var_education.set(row[9])
        self.var_percentage.set(row[10])
        self.var_salary.set(row[11])
        self.var_joining_date.set(row[12])
        self.var_exit_date.set(row[13])


    def update_data(self):
        conn = pymysql.connect(host="localhost",user="root",password="",database="test")
        cur = conn.cursor()
        query = "update staff_details set full_name=%s,phone_number=%s,gender=%s,country=%s,state=%s,city=%s,address=%s,role=%s,education=%s,percentage=%s,salary=%s,joining_date=%s,exit_date=%s,image=%s where email_address=%s"
        
        
        with open('photo1.jpg','rb') as file:
            binarydata = file.read()

        cur.execute(query,
                        (

                                                    self.var_full_name.get(),
                                                    self.var_phone_number.get(),
                                                    self.var_gender.get(),
                                                    self.var_country.get(),
                                                    self.var_state.get(),
                                                    self.var_city.get(),
                                                    self.var_address.get(),
                                                    self.var_role.get(),
                                                    self.var_education.get(),
                                                    self.var_percentage.get(),
                                                    self.var_salary.get(),
                                                    self.var_joining_date.get(),
                                                    self.var_exit_date.get(),
                                                    binarydata,
                                                    self.var_email_address.get(),

        ))

        conn.commit()
        self.Staff_data_fetch()
        conn.close()
        messagebox.showinfo("Updated","Customer Data Has Been Updated")


    def delete_data(self):
        delete_message = messagebox.askyesno("Warning","Do you want to delete this customer",parent=self.root)
        if delete_message>0:
            conn = pymysql.connect(host="localhost",user="root",password="",database="test")
            cur = conn.cursor()
            cur.execute("delete from staff_details where email_address=%s",(self.var_email_address.get()))
        else:
            if not delete_message:
                return
        
        conn.commit()
        self.Staff_data_fetch()
        conn.close()
        self.clear()

    def reset(self):
        self.var_full_name.set("")
        self.var_phone_number.set("")
        self.var_gender.set("")
        self.var_email_address.set("")
        self.var_country.set("")
        self.var_state.set("")
        self.var_city.set("")
        self.var_address.set("")
        self.var_role.set("")
        self.var_education.set("")
        self.var_percentage.set("")
        self.var_salary.set("")
        self.var_joining_date.set("")
        self.var_exit_date.set("")

    
    def fetch_data(self):
        if self.var_email_address.get() == "":
            messagebox.showerror("Error","Enter your email address",parent=self.root)
        else:
            conn = pymysql.connect(host="localhost",user="root",password="",database="test")
            cur = conn.cursor()
            m = cur.execute("select * from staff_details where email_address=%s",self.var_email_address.get())
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error","Data not found")
            else:
                conn.commit()
                conn.close()
                self.root.destroy()
                self.showdataframe = Tk()

                self.showdataframe.geometry("700x430+450+140")


            #-------------------------------------Showing Image from Database--------------------------

                f1 = open('photo3.jpg','wb')

                for i in range(len(row)):
                    print(row[1])
                    f1.write(row[14])
                    break

                image2 = Image.open('photo1.jpg')

                image2 = image2.resize((120,120),Image.ANTIALIAS)
                image2 = ImageTk.PhotoImage(image=image2)
                label_image2 = Label(self.showdataframe,image=image2)
                label_image2.place(x=280,y=0)


                firstlabel = Label(self.showdataframe,text="Full Name",font=("times new roman",13,"bold"),padx=2,pady=2)
                firstlabel.place(x=2,y=130)

                first_data_label = Label(self.showdataframe,text=row[0],font=("times new roman",13,"bold"),padx=2,pady=2)
                first_data_label.place(x=130,y=130)

                secondlabel = Label(self.showdataframe,text="Phone Number",font=("times new roman",13,"bold"),padx=2,pady=2)
                secondlabel.place(x=2,y=165)

                second_data_label = Label(self.showdataframe,text=row[1],font=("times new roman",13,"bold"),padx=2,pady=2)
                second_data_label.place(x=130,y=165)

                thirdlabel = Label(self.showdataframe,text="Gender",font=("times new roman",13,"bold"),padx=2,pady=2)
                thirdlabel.place(x=2,y=200)

                third_data_label = Label(self.showdataframe,text=row[2],font=("times new roman",13,"bold"),padx=2,pady=2)
                third_data_label.place(x=130,y=200)

                fourthlabel = Label(self.showdataframe,text="Email Address",font=("times new roman",13,"bold"),padx=2,pady=2)
                fourthlabel.place(x=2,y=235)

                fourth_data_label = Label(self.showdataframe,text=row[3],font=("times new roman",13,"bold"),padx=2,pady=2)
                fourth_data_label.place(x=130,y=235)

                fifthlabel = Label(self.showdataframe,text="Country",font=("times new roman",13,"bold"),padx=2,pady=2)
                fifthlabel.place(x=2,y=270)

                fifth_data_label = Label(self.showdataframe,text=row[4],font=("times new roman",13,"bold"),padx=2,pady=2)
                fifth_data_label.place(x=130,y=270)

                sixthlabel = Label(self.showdataframe,text="State",font=("times new roman",13,"bold"),padx=2,pady=2)
                sixthlabel.place(x=2,y=305)

                sixth_data_label = Label(self.showdataframe,text=row[5],font=("times new roman",13,"bold"),padx=2,pady=2)
                sixth_data_label.place(x=130,y=305)

                seventhlabel = Label(self.showdataframe,text="City",font=("times new roman",13,"bold"),padx=2,pady=2)
                seventhlabel.place(x=2,y=340)

                seventh_data_label = Label(self.showdataframe,text=row[6],font=("times new roman",13,"bold"),padx=2,pady=2)
                seventh_data_label.place(x=130,y=340)

                eightlabel = Label(self.showdataframe,text="Address",font=("times new roman",13,"bold"),padx=2,pady=2)
                eightlabel.place(x=400,y=130)

                eight_data_label = Label(self.showdataframe,text=row[7],font=("times new roman",13,"bold"),padx=2,pady=2)
                eight_data_label.place(x=510,y=130)


                ninthlabel = Label(self.showdataframe,text="Role",font=("times new roman",13,"bold"),padx=2,pady=2)
                ninthlabel.place(x=400,y=165)

                ninth_data_label = Label(self.showdataframe,text=row[8],font=("times new roman",13,"bold"),padx=2,pady=2)
                ninth_data_label.place(x=510,y=165)


                tenthlabel = Label(self.showdataframe,text="Education",font=("times new roman",13,"bold"),padx=2,pady=2)
                tenthlabel.place(x=400,y=200)

                tenth_data_label = Label(self.showdataframe,text=row[9],font=("times new roman",13,"bold"),padx=2,pady=2)
                tenth_data_label.place(x=510,y=200)

                eleventhlabel = Label(self.showdataframe,text="Percentage",font=("times new roman",13,"bold"),padx=2,pady=2)
                eleventhlabel.place(x=400,y=235)

                eleventh_data_label = Label(self.showdataframe,text=row[10],font=("times new roman",13,"bold"),padx=2,pady=2)
                eleventh_data_label.place(x=510,y=235)

                twelthlabel = Label(self.showdataframe,text="Salary",font=("times new roman",13,"bold"),padx=2,pady=2)
                twelthlabel.place(x=400,y=270)

                twelth_data_label = Label(self.showdataframe,text=row[11],font=("times new roman",13,"bold"),padx=2,pady=2)
                twelth_data_label.place(x=510,y=270)

                thirteenthlabel = Label(self.showdataframe,text="Joining Date",font=("times new roman",13,"bold"),padx=2,pady=2)
                thirteenthlabel.place(x=400,y=305)

                thirteenth_data_label = Label(self.showdataframe,text=row[12],font=("times new roman",13,"bold"),padx=2,pady=2)
                thirteenth_data_label.place(x=510,y=305)

                fourteenthlabel = Label(self.showdataframe,text="Exit Date",font=("times new roman",13,"bold"),padx=2,pady=2)
                fourteenthlabel.place(x=400,y=340)

                fourteenth_data_label = Label(self.showdataframe,text=row[13],font=("times new roman",13,"bold"),padx=2,pady=2)
                fourteenth_data_label.place(x=510,y=340)

                def staff_profile():
                    self.showdataframe.destroy()
                    import profile

                self.Profilebutton = Button(self.showdataframe,text="Profile",font=("Copperplate",13,"bold"),bg="Green",fg="white",width=8,command=staff_profile)
                self.Profilebutton.place(x=300,y=380)

                self.showdataframe.mainloop()








    #---------------------------------Searching Staff Data By Email Address-----------------------------


    def search(self):
        conn = pymysql.connect(host="localhost",user="root",password="",database="test")
        cur = conn.cursor()

        cur.execute("select full_name,phone_number,gender,email_address from staff_details where " + str(self.search_val.get())+ " LIKE '%"+str(self.search_txt.get())+"%'")
        row = cur.fetchall()
        if len(row)!=0:
            self.view.delete(*self.view.get_children())
            for i in row:
                self.view.insert("",END,values=i)

            self.clear()
            conn.commit()
        conn.close()
        



    def clear(self):
        self.firstentry.delete(0,END)
        self.secondentry.delete(0,END)
        self.eightentry.delete(0,END)
        self.fourthentry.delete(0,END)
        self.ninthentry.delete(0,END)
        self.sixthentry.delete(0,END)
        self.eleventhentry.delete(0,END)
        self.twelthentry.delete(0,END)
        self.seventhentry.delete(0,END)
        self.fiftheenentry.delete(0,END)


    


    def customer(self):
        self.root.destroy()
        import cust_details

    def room_booking(self):
        self.root.destroy()
        import roombooking

    def room_details(self):
        self.root.destroy()
        import room_details

    def home(self):
        self.root.destroy()
        import home

    def logout(self):
        self.root.destroy()
        import login

    def exit(self):
        self.root.destroy()


    
        

        




root = Tk()
obj = Hotel(root)
root.mainloop()