

from tkinter import *
from numpy import delete 
import pymysql
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox


class Hotel:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1550x800+0+0")
        self.root.title("Hotel Management System")



        self.var_fname = StringVar()
        self.var_mname = StringVar()
        self.var_lname = StringVar()
        self.var_gender = StringVar()
        self.var_mobileno = StringVar()
        self.var_country = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_address = StringVar()
        self.var_email = StringVar()

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

        check_in_booking = Button(self.frame1,text="Customers",font=("times new roman",15,"bold"),background="gray14",fg="white",bd=0,activebackground="gray14",activeforeground="white",cursor="hand2")
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

        profile_icon_button = Button(self.frame1,text="Profile",command=self.staff_details,font=("times new roman",15,"bold"),background="gray14",fg="white",bd=0,activebackground="gray14",activeforeground="white",cursor="hand2")
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

        label_title = Label(self.root,text="Add Customer Details",font=("times new roman",33,"bold"),background="gray12",fg="yellow")
        label_title.place(x=254,y=2,width=1350,height=50)


        #---------------------------------Customer Details-------------------------------

        self.first_label_frame = LabelFrame(self.root,text="Customer Details",bd=0,font=("times new roman",15,"bold"))
        self.first_label_frame.place(x=256,y=52,width=1270,height=400)


        self.firstlabel = Label(self.first_label_frame,text="First Name",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.firstlabel.grid(row=0,column=0)
        self.firstentry = ttk.Entry(self.first_label_frame,font=("Copperplate",13),width=30,textvariable=self.var_fname)
        self.firstentry.grid(row=0,column=1)

        


        self.secondlabel = Label(self.first_label_frame,text="Middle Name",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.secondlabel.grid(row=1,column=0)
        self.secondentry = ttk.Entry(self.first_label_frame,font=("Copperplate",13),width=30,textvariable=self.var_mname)
        self.secondentry.grid(row=1,column=1)


        self.thirdlabel = Label(self.first_label_frame,text="Last Name",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.thirdlabel.grid(row=2,column=0)
        self.thirdentry = ttk.Entry(self.first_label_frame,font=("Copperplate",13),width=30,textvariable=self.var_lname)
        self.thirdentry.grid(row=2,column=1)


        self.fourthlabel = Label(self.first_label_frame,text="Phone Number",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.fourthlabel.grid(row=3,column=0)
        self.fourthentry = ttk.Entry(self.first_label_frame,font=("Copperplate",13),width=30,textvariable=self.var_mobileno)
        self.fourthentry.grid(row=3,column=1)


        self.fifthlabel = Label(self.first_label_frame,text="Gender",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.fifthlabel.grid(row=4,column=0)
        self.firstcombo = ttk.Combobox(self.first_label_frame,font=("Copperplate",13,"bold"),width=28,textvariable=self.var_gender)
        self.firstcombo["values"] = ("Male","Female","Other")
        self.firstcombo.current(0)
        self.firstcombo["state"] = ("readonly")
        self.firstcombo.grid(row=4,column=1)



        self.sixthlabel = Label(self.first_label_frame,text="Address",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.sixthlabel.grid(row=4,column=3)
        self.sixthentry = ttk.Entry(self.first_label_frame,font=("Copperplate",13),width=30,textvariable=self.var_address)
        self.sixthentry.grid(row=4,column=4)


        self.seventhlabel = Label(self.first_label_frame,text="State",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.seventhlabel.grid(row=1,column=3)
        self.secondcombo = ttk.Combobox(self.first_label_frame,font=("Copperplate",13,"bold"),width=28,textvariable=self.var_state)
        self.secondcombo["values"] = ("Delhi","Maharashtra","Madya Pradesh","Hariyana","Gujrat","Punjab","Jammu and Kashmir","Sikkim","Manipur","Meghalaya","Telanga","Kerala","Tamilnadu","Goa","Karnata","Andra Pradesh")
        self.secondcombo.current(1)
        self.secondcombo["state"] = ("readonly")
        self.secondcombo.grid(row=1,column=4)


        self.eightlabel = Label(self.first_label_frame,text="City",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.eightlabel.grid(row=2,column=3)
        self.thirdcombo = ttk.Combobox(self.first_label_frame,font=("Copperplate",13,"bold"),width=28,textvariable=self.var_city)
        self.thirdcombo["values"] = ("Pune","Mumbai","Solapur","Nashik","Nagpur","Navi Mumbai","Thane","kolhapur","Nandhed","Latur","Yavantmal","Amravti","Aurangabad")
        self.thirdcombo.current(0)
        self.thirdcombo["state"] = ("readonly")
        self.thirdcombo.grid(row=2,column=4)


        self.tenthlabel = Label(self.first_label_frame,text="Country",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.tenthlabel.grid(row=0,column=3)
        self.fourthcombo = ttk.Combobox(self.first_label_frame,font=("Copperplate",13,"bold"),width=28,textvariable=self.var_country)
        self.fourthcombo["values"] = ("India","Russia","Japan","France","America","South Africa","Bangladesh","Israel","Ukrain","Nepal","Sri Lanka","China","South Korea","North Korea","Myanmar","North Korea","Germany","Swedan")
        self.fourthcombo.current(0)
        self.fourthcombo["state"] = ("readonly")
        self.fourthcombo.grid(row=0,column=4)



        self.ninthlabel = Label(self.first_label_frame,text="Email",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.ninthlabel.grid(row=3,column=3)
        self.ninthentry = ttk.Entry(self.first_label_frame,font=("Copperplate",13),width=30,textvariable=self.var_email)
        self.ninthentry.grid(row=3,column=4)


        self.button_frame = Frame(self.first_label_frame,bd=0,relief=RIDGE)
        self.button_frame.place(x=150,y=305,width=502,height=50)

        self.Addbutton = Button(self.button_frame,text="Add",font=("Copperplate",13,"bold"),bg="Green",fg="white",width=8,command=self.Customer_add)
        self.Addbutton.place(x=25,y=5)

        self.updatebutton = Button(self.button_frame,text="Update",font=("Copperplate",13,"bold"),bg="Green",fg="white",width=8,command=self.update_data)
        self.updatebutton.place(x=150,y=5)

        self.deletebutton = Button(self.button_frame,text="Delete",font=("Copperplate",13,"bold"),bg="Green",fg="white",width=8,command=self.delete_data)
        self.deletebutton.place(x=278,y=5)

        self.clearbutton = Button(self.button_frame,text="Clear",font=("Copperplate",13,"bold"),bg="Green",fg="white",width=8,command=self.reset)
        self.clearbutton.place(x=404,y=5)



        #---------------------------------View Images-------------------------------

        third_frame = Frame(self.first_label_frame,bd=0,relief=RIDGE)
        third_frame.place(x=795,y=1,width=460,height=380)


        image2 = Image.open("view.jpg")
        image2 = image2.resize((225,170),Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(image=image2)
        label_image2 = Label(third_frame,image=self.image2,bg="black",bd=0).place(x=2,y=2)


        
        image3 = Image.open("view1.jpg")
        image3 = image3.resize((225,170),Image.ANTIALIAS)
        self.image3 = ImageTk.PhotoImage(image=image3)
        label_image3 = Label(third_frame,image=self.image3,bg="black",bd=0).place(x=250,y=2)


        image4 = Image.open("view3.jpg")
        image4 = image4.resize((225,170),Image.ANTIALIAS)
        self.image4 = ImageTk.PhotoImage(image=image4)
        label_image4 = Label(third_frame,image=self.image4,bg="black",bd=0).place(x=2,y=190)


        image5 = Image.open("view4.jpg")
        image5 = image5.resize((225,170),Image.ANTIALIAS)
        self.image5 = ImageTk.PhotoImage(image=image5)
        label_image5 = Label(third_frame,image=self.image5,bg="black",bd=0).place(x=250,y=190)


        #---------------------------------View Customer Details-------------------------------

        second_label_frame = LabelFrame(self.root,text="View Customer Details",bd=4,font=("times new roman",15,"bold"))
        second_label_frame.place(x=256,y=432,width=1270,height=360)

        self.search_val = StringVar()

        eleventhlabel = Label(second_label_frame,text="Search By:",font=("Copperplate",14,"bold"),bg="green",fg="white",padx=7)
        eleventhlabel.place(x=200,y=12)
        fifthcombo = ttk.Combobox(second_label_frame,font=("Copperplate",14,"bold"),width=20,textvariable=self.search_val)
        fifthcombo["values"] = ("first_name","Email")
        fifthcombo.current(1)
        fifthcombo["state"] = ("readonly")
        fifthcombo.place(x=340,y=12)

        self.search_txt = StringVar()

        self.fifteenentry = ttk.Entry(second_label_frame,font=("Copperplate",13),width=30,textvariable=self.search_txt)
        self.fifteenentry.place(x=594,y=10,height=29)


        searchbutton = Button(second_label_frame,text="Search",font=("Copperplate",11,"bold"),bg="Green",fg="white",command=self.search)
        searchbutton.place(x=890,y=9)

        showallbutton = Button(second_label_frame,text="Show All",font=("Copperplate",11,"bold"),bg="Green",fg="white",command=self.Customer_data_fetch)
        showallbutton.place(x=970,y=9)


        third_label_frame = Frame(second_label_frame,bd=30)
        third_label_frame.place(x=0,y=45,width=1280,height=310)

        x_scroll = ttk.Scrollbar(third_label_frame,orient=HORIZONTAL)
        y_scroll = ttk.Scrollbar(third_label_frame,orient=VERTICAL)

        self.view = ttk.Treeview(third_label_frame,columns=("First Name","Middle Name","Last Name","Gender","Mobile Number","Country","State","City","Address","Email"),xscrollcommand=x_scroll.set,yscrollcommand=y_scroll.set)

        x_scroll.pack(side=BOTTOM,fill=X)
        y_scroll.pack(side=RIGHT,fill=Y)

        x_scroll.config(command=self.view.xview)
        y_scroll.config(command=self.view.yview)

        self.view.heading("First Name",text="First Name")
        self.view.heading("Middle Name",text="Middle Name")
        self.view.heading("Last Name",text="Last Name")
        self.view.heading("Gender",text="Gender")
        self.view.heading("Mobile Number",text="Mobile Number")
        self.view.heading("Country",text="Country")
        self.view.heading("State",text="State")
        self.view.heading("City",text="City")
        self.view.heading("Address",text="Address")
        self.view.heading("Email",text="Email")


        self.view["show"] = "headings"

        
        self.view.column("First Name",width=120)
        self.view.column("Middle Name",width=120)
        self.view.column("Last Name",width=120)
        self.view.column("Gender",width=120)
        self.view.column("Mobile Number",width=120)
        self.view.column("Country",width=120)
        self.view.column("State",width=120)
        self.view.column("City",width=120)
        self.view.column("Address",width=120)
        self.view.column("Email",width=120)

        self.view.pack(fill=BOTH,expand=1)

        self.view.bind("<ButtonRelease-1>",self.show_data)

        self.Customer_data_fetch()


    #---------------------------------Adding  Customer Data In Database-------------------------------

    def Customer_add(self):
        if self.var_fname.get() == "" or self.var_mname.get() == "" or self.var_lname.get() == "" or self.var_gender.get() == "" or self.var_mobileno.get() == "" or self.var_country.get() == "" or self.var_state.get() == "" or self.var_city.get() == "" or self.var_address.get() == "" or self.var_email.get() == "":
            messagebox.showerror("Error","All Fields Are Required!",parent=self.root)
        else:
            conn = pymysql.connect(host="localhost",user="root",password="",database="test")
            cur = conn.cursor()
            cur.execute("select * from customer where email=%s",self.var_email.get())
            row = cur.fetchone()
            if row != None:
                messagebox.showerror("Error","User Already Exit!")
            else:

                try:
                    conn = pymysql.connect(host="localhost",user="root",password="",database="test")
                    cur = conn.cursor()

                    cur.execute("insert into customer(first_name,middle_name,last_name,gender,mobile_no,country,state,city,address,email) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                    self.var_fname.get(),
                            
                                                    self.var_mname.get(),
                                                    self.var_lname.get(),
                                                    self.var_gender.get(),
                                                    self.var_mobileno.get(),
                                                    self.var_country.get(),
                                                    self.var_state.get(),
                                                    self.var_city.get(),
                                                    self.var_address.get(),
                                                    self.var_email.get(),
                                                    
                                                                    ))

                    conn.commit()
                    self.Customer_data_fetch()
                    conn.close()
                    messagebox.showinfo("Success","Customer Has Been Added")
                    self.clear()

                except Exception as Error:
                    messagebox.showerror("Error",f"Error due to {Error}",parent=self.root)


    def clear(self):
        self.firstentry.delete(0,END)
        self.secondentry.delete(0,END)
        self.thirdentry.delete(0,END)
        self.fourthentry.delete(0,END)
        self.ninthentry.delete(0,END)
        self.sixthentry.delete(0,END)

        #---------------------------------Showing Customer Data in Table-------------------------------

    def Customer_data_fetch(self):
        conn = pymysql.connect(host="localhost",user="root",password="",database="test")
        cur = conn.cursor()
        cur.execute("select first_name,middle_name,last_name,gender,mobile_no,country,state,city,address,email from customer")
        row = cur.fetchall()
        if row != 0:
            self.view.delete(*self.view.get_children())
            for i in row:
                self.view.insert("",END,values=i)
            conn.commit()
        conn.close()

    
        #---------------------------------showing Customer Data by selecting the row in Table-------------------------------


    def show_data(self,event=""):
        cursor_row = self.view.focus()
        content = self.view.item(cursor_row)
        row = content["values"]

        self.var_fname.set(row[0])
        self.var_mname.set(row[1])
        self.var_lname.set(row[2])
        self.var_gender.set(row[3])
        self.var_mobileno.set(row[4])
        
        self.var_country.set(row[5])
        self.var_state.set(row[6])
        self.var_city.set(row[7])
        self.var_address.set(row[8])
        self.var_email.set(row[9])

    def update_data(self):
        conn = pymysql.connect(host="localhost",user="root",password="",database="test")
        cur = conn.cursor()
        cur.execute("update customer set first_name=%s,middle_name=%s,last_name=%s,mobile_no=%s,gender=%s,country=%s,state=%s,city=%s,address=%s where email=%s",(

                                                self.var_fname.get(),
                                                self.var_mname.get(),
                                                self.var_lname.get(),
                                                self.var_mobileno.get(),
                                                self.var_gender.get(),
                                                self.var_country.get(),
                                                self.var_state.get(),
                                                self.var_city.get(),
                                                self.var_address.get(),
                                                self.var_email.get(),

        ))

        conn.commit()
        self.Customer_data_fetch()
        conn.close()
        messagebox.showinfo("Updated","Customer Data Has Been Updated")

    def delete_data(self):
        delete_message = messagebox.askyesno("Warning","Do you want to delete this customer",parent=self.root)
        if delete_message>0:
            conn = pymysql.connect(host="localhost",user="root",password="",database="test")
            cur = conn.cursor()
            cur.execute("delete from customer where email=%s",(self.var_email.get()))
        else:
            if not delete_message:
                return
        
        conn.commit()
        self.Customer_data_fetch()
        conn.close()
        self.clear()

    def reset(self):
        self.var_fname.set("")
        self.var_mname.set("")
        self.var_lname.set("")
        self.var_mobileno.set("")
        self.var_address.set("")
        self.var_email.set("")

    def search(self):
        conn = pymysql.connect(host="localhost",user="root",password="",database="test")
        cur = conn.cursor()

        cur.execute("select first_name,middle_name,last_name,gender,mobile_no,country,state,city,address,email from customer where " + str(self.search_val.get())+ " LIKE '%"+str(self.search_txt.get())+"%'")
        row = cur.fetchall()
        if len(row)!=0:
            self.view.delete(*self.view.get_children())
            for i in row:
                self.view.insert("",END,values=i)

            conn.commit()
        conn.close()

    
    #----------------------------------Redirecting to menu options------------------------------

    def home(self):
        self.root.destroy()
        import home

    def room_booking(self):
        self.root.destroy()
        import roombooking

    def room_details(self):
        self.root.destroy()
        import room_details

    def staff_details(self):
        self.root.destroy()
        import profile

    def logout(self):
        self.root.destroy()
        import login

    def exit(self):
        self.root.destroy()

        




root = Tk()
obj = Hotel(root)
root.mainloop()




