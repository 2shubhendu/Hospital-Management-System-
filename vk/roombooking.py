from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from numpy import pad
import pymysql
from pyparsing import Regex
import re
from time import strftime
from datetime import date, datetime


class RoomBooking:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1550x800+0+0")
        self.root.title("Hotel Management System")

        self.frame1 = Frame(self.root,relief=RIDGE,bd=4,bg="gray14")
        self.frame1.place(x=0,y=150,height=1300,width=254)


        #-----------------------------Logo-------------------------

        image1 = Image.open("royal_image.jpg")
        image1 = image1.resize((250,150),Image.ANTIALIAS)
        self.image1 = ImageTk.PhotoImage(image=image1)
        label_image1 = Label(self.root,image=self.image1)
        label_image1.place(x=0,y=0)

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

        check_in_booking = Button(self.frame1,text="Customers",command=self.customers,font=("times new roman",15,"bold"),background="gray14",fg="white",bd=0,activebackground="gray14",activeforeground="white",cursor="hand2")
        check_in_booking.place(x=85,y=107)



        check_out_icon = Image.open("room_logo1.jpg")
        check_out_icon = check_out_icon.resize((60,60),Image.ANTIALIAS)
        self.check_out_icon = ImageTk.PhotoImage(image=check_out_icon)
        label_check_out_icon = Label(self.frame1,image=self.check_out_icon,bg="gray14")
        label_check_out_icon.place(x=10,y=180)

        check_out_booking = Button(self.frame1,text="Room Booking",font=("times new roman",15,"bold"),background="gray14",fg="white",bd=0,activebackground="gray14",activeforeground="white",cursor="hand2")
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


        #------------------------------Variables-----------------------------

        self.var_email = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_proof_no = StringVar()
        self.var_check_in = StringVar()
        self.var_check_out = StringVar()
        self.var_room_type = StringVar()
        self.var_available_room = StringVar()
        self.var_no_of_days = StringVar()
        self.var_room_price = StringVar()
        self.var_gst = StringVar()
        self.var_total_price = StringVar()




        #---------------------------------Label-------------------------------

        label_title = Label(self.root,text="RoomBooking Details",font=("times new roman",33,"bold"),background="gray12",fg="yellow")
        label_title.place(x=254,y=2,width=1350,height=50)

        #---------------------------------Check_in Details---------------------

        self.first_label_frame = LabelFrame(self.root,text="RoomBooking Detail",bd=4,font=("times new roman",15,"bold"))
        self.first_label_frame.place(x=256,y=52,width=1270,height=400)

        #--------------------------------Entry Fields---------------------------

        self.firstlabel = Label(self.first_label_frame,text="Email",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.firstlabel.grid(row=0,column=0)
        self.firstentry = ttk.Entry(self.first_label_frame,font=("Copperplate",13),width=30,textvariable=self.var_email)
        self.firstentry.grid(row=0,column=1)



        self.tenthlabel = Label(self.first_label_frame,text="ID Proof",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.tenthlabel.grid(row=1,column=0)
        self.fourthcombo = ttk.Combobox(self.first_label_frame,font=("Copperplate",13,"bold"),width=28,textvariable=self.var_id_proof)
        self.fourthcombo["values"] = ("Aadhar Card","Pan Card","Passport")
        self.fourthcombo.current(0)
        self.fourthcombo["state"] = ("readonly")
        self.fourthcombo.grid(row=1,column=1)

        self.eleventhlabel = Label(self.first_label_frame,text="ID Proof Number",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.eleventhlabel.grid(row=2,column=0)
        self.ninthentry = ttk.Entry(self.first_label_frame,font=("Copperplate",13),width=30,textvariable=self.var_id_proof_no)
        self.ninthentry.grid(row=2,column=1)


        self.secondlabel = Label(self.first_label_frame,text="Room",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.secondlabel.grid(row=3,column=0)
        self.firstcombo = ttk.Combobox(self.first_label_frame,font=("Copperplate",13,"bold"),width=28,textvariable=self.var_room_type)
        self.firstcombo["values"] = ("Single","Double")
        self.firstcombo.current(0)
        self.firstcombo["state"] = ("readonly")
        self.firstcombo.grid(row=3,column=1)


        self.secondlabel = Label(self.first_label_frame,text="Check In Date",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.secondlabel.grid(row=4,column=0)
        self.secondentry = ttk.Entry(self.first_label_frame,font=("Copperplate",13),width=30,textvariable=self.var_check_in)
        self.secondentry.grid(row=4,column=1)


        self.fourthlabel = Label(self.first_label_frame,text="Check Out Date",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.fourthlabel.grid(row=0,column=4)
        self.fourthentry = ttk.Entry(self.first_label_frame,font=("Copperplate",13),width=30,textvariable=self.var_check_out)
        self.fourthentry.grid(row=0,column=5)

        self.twelthlabel = Label(self.first_label_frame,text="Available Room",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.twelthlabel.grid(row=1,column=4)

        #-----------------------------------Fetching room_number from room_details tabel--------------------

        conn = pymysql.connect(host="localhost",user="root",password="",database="test")
        cur = conn.cursor()
        cur.execute("select room_number from room_details")
        row = cur.fetchall()

        self.firstcombo = ttk.Combobox(self.first_label_frame,font=("Copperplate",13,"bold"),width=28,textvariable=self.var_available_room)
        self.firstcombo["values"] = row
        self.firstcombo.current(0)
        self.firstcombo["state"] = ("readonly")
        self.firstcombo.grid(row=1,column=5)


        self.fifthlabel = Label(self.first_label_frame,text="Room Price",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.fifthlabel.grid(row=2,column=4)
        self.seventhentry = ttk.Entry(self.first_label_frame,font=("Copperplate",13),width=30,textvariable=self.var_room_price)
        self.seventhentry.grid(row=2,column=5)

        self.sixthlabel = Label(self.first_label_frame,text="GST",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.sixthlabel.grid(row=3,column=4)
        self.eightentry = ttk.Entry(self.first_label_frame,font=("Copperplate",13),width=30,textvariable=self.var_gst)
        self.eightentry.grid(row=3,column=5)

        self.tenthlabel = Label(self.first_label_frame,text="Total Price",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.tenthlabel.grid(row=4,column=4)
        self.tenthentry = ttk.Entry(self.first_label_frame,font=("Copperplate",13),width=30,textvariable=self.var_total_price)
        self.tenthentry.grid(row=4,column=5)





        #---------------------------Buttons--------------------------------
        self.button_frame = Frame(self.first_label_frame,bd=0,relief=RIDGE)
        self.button_frame.place(x=80,y=305,width=792,height=50)

        self.Fetch_data_button = Button(self.button_frame,text="Fetch Customer Details",font=("Copperplate",13,"bold"),bg="Green",fg="white",width=25,command=self.fetch_data)
        self.Fetch_data_button.place(x=450,y=5)

        self.Billbutton = Button(self.button_frame,text="Bill",font=("Copperplate",13,"bold"),bg="Green",fg="white",width=8,command=self.total_days_and_bill)
        self.Billbutton.place(x=0,y=5)

        self.Clearbutton = Button(self.button_frame,text="Clear",font=("Copperplate",13,"bold"),bg="Green",fg="white",width=8,command=self.clear)
        self.Clearbutton.place(x=145,y=5)

        self.Bookbutton = Button(self.button_frame,text="Book",font=("Copperplate",13,"bold"),bg="Green",fg="white",width=8,command=self.room_add)
        self.Bookbutton.place(x=290,y=5)


        #---------------------------------View Images-------------------------------

        third_frame = Frame(self.first_label_frame,bd=0,relief=RIDGE)
        third_frame.place(x=870,y=1,width=380,height=350)


        image2 = Image.open("hote_room.jpg")
        image2 = image2.resize((380,160),Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(image=image2)
        label_image2 = Label(third_frame,image=self.image2,bg="black",bd=0).place(x=1,y=10)


        '''
        image3 = Image.open("hotel_room1.jpg")
        image3 = image3.resize((380,140),Image.ANTIALIAS)
        self.image3 = ImageTk.PhotoImage(image=image3)
        label_image3 = Label(third_frame,image=self.image3,bg="black",bd=0).place(x=190,y=10)'''

        
        image4 = Image.open("hotel_room2.jpg")
        image4 = image4.resize((380,160),Image.ANTIALIAS)
        self.image4 = ImageTk.PhotoImage(image=image4)
        label_image4 = Label(third_frame,image=self.image4,bg="black",bd=0).place(x=1,y=180)

        '''
        image5 = Image.open("hotel_room3.jpg")
        image5 = image5.resize((180,140),Image.ANTIALIAS)
        self.image5 = ImageTk.PhotoImage(image=image5)
        label_image5 = Label(third_frame,image=self.image5,bg="black",bd=0).place(x=190,y=180)'''




        #---------------------------------View Customer staying Details-------------------------------

        second_label_frame = LabelFrame(self.root,text="View Room Details",bd=4,font=("times new roman",15,"bold"))
        second_label_frame.place(x=256,y=432,width=1270,height=360)

        self.search_val = StringVar()
        self.search_txt = StringVar()

        eleventhlabel = Label(second_label_frame,text="Search By:",font=("Copperplate",14,"bold"),bg="green",fg="white",padx=7)
        eleventhlabel.place(x=200,y=12)
        fifthcombo = ttk.Combobox(second_label_frame,font=("Copperplate",14,"bold"),width=20,textvariable=self.search_val)
        fifthcombo["values"] = ("ID Proof Number","Email")
        fifthcombo.current(1)
        fifthcombo["state"] = ("readonly")
        fifthcombo.place(x=340,y=12)

    

        self.fifteenentry = ttk.Entry(second_label_frame,font=("Copperplate",13),width=30,textvariable=self.search_txt)
        self.fifteenentry.place(x=594,y=10,height=29)

    

        searchbutton = Button(second_label_frame,text="Search",font=("Copperplate",11,"bold"),bg="Green",fg="white",command=self.search)
        searchbutton.place(x=890,y=9)

        showallbutton = Button(second_label_frame,text="Show All",font=("Copperplate",11,"bold"),bg="Green",fg="white",command=self.room_data_fetch)
        showallbutton.place(x=970,y=9)


        third_label_frame = Frame(second_label_frame,bd=30)
        third_label_frame.place(x=0,y=45,width=1280,height=310)

        x_scroll = ttk.Scrollbar(third_label_frame,orient=HORIZONTAL)
        y_scroll = ttk.Scrollbar(third_label_frame,orient=VERTICAL)

        self.room = ttk.Treeview(third_label_frame,columns=("email","id proof","id proof number","check_in","check_out","room_type","available_room"),xscrollcommand=x_scroll.set,yscrollcommand=y_scroll.set)

        x_scroll.pack(side=BOTTOM,fill=X)
        y_scroll.pack(side=RIGHT,fill=Y)

        x_scroll.config(command=self.room.xview)
        y_scroll.config(command=self.room.yview)


        self.room.heading("email",text="Email Address")
        self.room.heading("id proof",text="ID Proof")
        self.room.heading("id proof number",text="ID Proof Number")
        self.room.heading("check_in",text="Check_In")
        self.room.heading("check_out",text="Check_Out")
        self.room.heading("room_type",text="Room Type")
        self.room.heading("available_room",text="Room No")
        #self.room.heading("no_of_days",text="No_Of_Days")
        


        self.room["show"] = "headings"

        
        self.room.column("email",width=120)
        self.room.column("id proof",width=120)
        self.room.column("id proof number",width=120)
        self.room.column("check_in",width=120)
        self.room.column("check_out",width=120)
        self.room.column("room_type",width=120)
        self.room.column("available_room",width=120)
        #self.room.column("no_of_days",width=120)
        

        self.room.pack(fill=BOTH,expand=1)

        self.room.bind("<ButtonRelease-1>",self.show_data)
        self.room_data_fetch()

    def fetch_data(self):
        if self.var_email.get() == "":
            messagebox.showerror("Error","Enter your email address",parent=self.root)
        else:
            conn = pymysql.connect(host="localhost",user="root",password="",database="test")
            cur = conn.cursor()
            cur.execute("select first_name,middle_name,last_name,gender,mobile_no,country,state,city,address,email from customer where email=%s",self.var_email.get())
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error","Data not found")
            else:
                conn.commit()
                conn.close()

                showdataframe = Frame(self.first_label_frame,bd=10,relief=RIDGE)
                showdataframe.place(x=870,y=1,width=380,height=350)

                firstlabel = Label(showdataframe,text="First Name",font=("times new roman",13,"bold"),padx=2,pady=2)
                firstlabel.place(x=2,y=0)

                first_data_label = Label(showdataframe,text=row[0],font=("times new roman",13,"bold"),padx=2,pady=2)
                first_data_label.place(x=130,y=0)

                secondlabel = Label(showdataframe,text="Middle Name",font=("times new roman",13,"bold"),padx=2,pady=2)
                secondlabel.place(x=2,y=30)

                second_data_label = Label(showdataframe,text=row[1],font=("times new roman",13,"bold"),padx=2,pady=2)
                second_data_label.place(x=130,y=30)

                thirdlabel = Label(showdataframe,text="Last Name",font=("times new roman",13,"bold"),padx=2,pady=2)
                thirdlabel.place(x=2,y=65)

                third_data_label = Label(showdataframe,text=row[2],font=("times new roman",13,"bold"),padx=2,pady=2)
                third_data_label.place(x=130,y=65)

                fourthlabel = Label(showdataframe,text="Gender",font=("times new roman",13,"bold"),padx=2,pady=2)
                fourthlabel.place(x=2,y=95)

                fourth_data_label = Label(showdataframe,text=row[3],font=("times new roman",13,"bold"),padx=2,pady=2)
                fourth_data_label.place(x=130,y=95)

                fifthlabel = Label(showdataframe,text="Mobile Number",font=("times new roman",13,"bold"),padx=2,pady=2)
                fifthlabel.place(x=2,y=125)

                fifth_data_label = Label(showdataframe,text=row[4],font=("times new roman",13,"bold"),padx=2,pady=2)
                fifth_data_label.place(x=130,y=125)

                sixthlabel = Label(showdataframe,text="Country",font=("times new roman",13,"bold"),padx=2,pady=2)
                sixthlabel.place(x=2,y=155)

                sixth_data_label = Label(showdataframe,text=row[5],font=("times new roman",13,"bold"),padx=2,pady=2)
                sixth_data_label.place(x=130,y=155)

                seventhlabel = Label(showdataframe,text="State",font=("times new roman",13,"bold"),padx=2,pady=2)
                seventhlabel.place(x=2,y=185)

                seventh_data_label = Label(showdataframe,text=row[6],font=("times new roman",13,"bold"),padx=2,pady=2)
                seventh_data_label.place(x=130,y=185)

                eightlabel = Label(showdataframe,text="City",font=("times new roman",13,"bold"),padx=2,pady=2)
                eightlabel.place(x=2,y=215)

                eight_data_label = Label(showdataframe,text=row[7],font=("times new roman",13,"bold"),padx=2,pady=2)
                eight_data_label.place(x=130,y=215)


                ninthlabel = Label(showdataframe,text="Address",font=("times new roman",13,"bold"),padx=2,pady=2)
                ninthlabel.place(x=2,y=245)

                ninth_data_label = Label(showdataframe,text=row[8],font=("times new roman",13,"bold"),padx=2,pady=2)
                ninth_data_label.place(x=130,y=245)


                tenthlabel = Label(showdataframe,text="Email Address",font=("times new roman",13,"bold"),padx=2,pady=2)
                tenthlabel.place(x=2,y=275)

                tenth_data_label = Label(showdataframe,text=row[9],font=("times new roman",13,"bold"),padx=2,pady=2)
                tenth_data_label.place(x=130,y=275)


    #---------------------------------Adding  Customer Data In Database-------------------------------

    def room_add(self):
        if self.var_email.get() == "":
            messagebox.showerror("Error","All Fields Are Required!",parent=self.root)
        else:
            conn = pymysql.connect(host="localhost",user="root",password="",database="test")
            cur = conn.cursor()
            cur.execute("select * from customer where email=%s",self.var_email.get())      
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error","User Data Is Not Added")
            else:

                try:
                    conn = pymysql.connect(host="localhost",user="root",password="",database="test")
                    cur = conn.cursor()

                    cur.execute("insert into room(email,id_proof,id_proof_no,check_in,check_out,room_type,available_room) values(%s,%s,%s,%s,%s,%s,%s)",(

                                                    self.var_email.get(),
                                                    self.var_id_proof.get(),
                                                    self.var_id_proof_no.get(),
                                                    self.var_check_in.get(),
                                                    self.var_check_out.get(),
                                                    self.var_room_type.get(),
                                                    self.var_available_room.get()
                                                    
                                                                                                
                                                                    ))

                    conn.commit()
                    self.room_data_fetch()
                    conn.close()
                    messagebox.showinfo("Success","Room Has Been Booked")
                    self.clear()

                except Exception as Error:
                    messagebox.showerror("Error",f"Error due to {Error}",parent=self.root)


        #---------------------------------Showing Customer Data in Table-------------------------------

    def room_data_fetch(self):
        conn = pymysql.connect(host="localhost",user="root",password="",database="test")
        cur = conn.cursor()
        cur.execute("select * from room")
        row = cur.fetchall()
        if row != 0:
            self.room.delete(*self.room.get_children())
            for i in row:
                self.room.insert("",END,values=i)
            conn.commit()
        conn.close()


            #---------------------------------showing Customer Data by selecting the row in Table-------------------------------


    def show_data(self,event=""):
        cursor_row = self.room.focus()
        content = self.room.item(cursor_row)
        row = content["values"]

        self.var_email.set(row[0])
        self.var_id_proof.set(row[1])
        self.var_id_proof_no.set(row[2])
        self.var_check_in.set(row[3])
        self.var_check_out.set(row[4])
        self.var_room_type.set(row[5])
        self.var_available_room.set(row[6])


    #---------------------------------------------Clearing the data in room tabl-----------------------

    def clear(self):
        self.firstentry.delete(0,END)
        self.secondentry.delete(0,END)
        self.tenthentry.delete(0,END)
        self.fourthentry.delete(0,END)
        self.ninthentry.delete(0,END)
        self.seventhentry.delete(0,END)
        self.eightentry.delete(0,END)

    

    #----------------------------------Searching the data by specific email------------------------------

    def search(self):
        conn = pymysql.connect(host="localhost",user="root",password="",database="test")
        cur = conn.cursor()

        cur.execute("select * from room where " + str(self.search_val.get())+ " LIKE '%"+str(self.search_txt.get())+"%'")
        row = cur.fetchall()
        if len(row)!=0:
            self.room.delete(*self.room.get_children())
            for i in row:
                self.room.insert("",END,values=i)

            conn.commit()
        conn.close()


    #-----------------------------------------Calculating no_of_days and Bill-----------------------------


    def total_days_and_bill(self):
        entrydate = self.var_check_in.get()
        exitdate = self.var_check_out.get()

        entrydate = datetime.strptime(entrydate,"%d/%m/%Y")
        exitdate = datetime.strptime(exitdate,"%d/%m/%Y")

        self.var_no_of_days.set(abs(entrydate-exitdate).days)


        if self.var_room_type.get() == "Single":
            single_room_price = float(1200)
            no_of_days = float(self.var_no_of_days.get())
            total_price = float(single_room_price*no_of_days)

            GST = "Rs."+str("%.2f"%((total_price)*0.1))
            final_price = "Rs."+str("%.2f"%(total_price+((total_price)*0.1)))

            self.var_room_price.set(single_room_price)
            self.var_gst.set(GST)
            self.var_total_price.set(final_price)

        elif self.var_room_type.get() == "Double":
            single_room_price = float(1500)
            no_of_days = float(self.var_no_of_days.get())
            total_price = float(single_room_price*no_of_days)

            GST = "Rs."+str("%.2f"%((total_price)*0.1))
            final_price = "Rs."+str("%.2f"%(total_price+((total_price)*0.1)))

            self.var_room_price.set(single_room_price)
            self.var_gst.set(GST)
            self.var_total_price.set(final_price)

        else:
            pass


        #----------------------------------Redirecting to menu options------------------------------

    def home(self):
        self.root.destroy()
        import home

    def customers(self):
        self.root.destroy()
        import cust_details

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
obj = RoomBooking(root)
root.mainloop()

