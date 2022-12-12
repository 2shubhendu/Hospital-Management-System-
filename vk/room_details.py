from cgi import test
from tkinter import *
from PIL import Image,ImageTk
from matplotlib import image
from matplotlib.pyplot import text
from tkinter import ttk
from tkinter import messagebox
import pymysql


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

        report_icon_button = Button(self.frame1,text="Room Details",font=("times new roman",15,"bold"),background="gray14",fg="white",bd=0,activebackground="gray14",activeforeground="white",cursor="hand2")
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

        label_title = Label(self.root,text="Room Details",font=("times new roman",33,"bold"),background="gray12",fg="yellow")
        label_title.place(x=254,y=2,width=1350,height=50)





        #----------------------------------variables--------------------------

        self.var_floor_no = StringVar()
        self.var_room_no = StringVar()
        self.var_room_type = StringVar()

        self.var_total_floors = StringVar()
        self.var_total_rooms = StringVar()
        self.var_total_single_rooms = StringVar()
        self.var_total_double_rooms = StringVar()

        #self.var_total_floors = self.var_floor_no.get()


        

        #--------------------------------Room Details------------------------

        self.first_label_frame = LabelFrame(self.root,text="Room Details",bd=0,font=("times new roman",15,"bold"))
        self.first_label_frame.place(x=620,y=52,width=570,height=400)

        self.firstlabel = Label(self.first_label_frame,text="Total Floors",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.firstlabel.grid(row=0,column=0)
        self.firstentry = Label(self.first_label_frame,text = "10",font=("Copperplate",13),textvariable=self.var_total_floors)
        self.firstentry.grid(row=0,column=1)

        self.secondlabel = Label(self.first_label_frame,text="Total Rooms",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.secondlabel.grid(row=1,column=0)
        self.secondentry = Label(self.first_label_frame,font=("Copperplate",13),text="300",textvariable=self.var_total_rooms)
        self.secondentry.grid(row=1,column=1)


        self.thirdlabel = Label(self.first_label_frame,text="Total Single Rooms",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.thirdlabel.grid(row=2,column=0)
        self.thirdentry = Label(self.first_label_frame,font=("Copperplate",13),text="150",textvariable=self.var_total_single_rooms)
        self.thirdentry.grid(row=2,column=1)


        self.fourthlabel = Label(self.first_label_frame,text="Total Double Rooms",font=("Copperplate",13,"bold"),padx=10,pady=19)
        self.fourthlabel.grid(row=3,column=0)
        self.fourthentry = Label(self.first_label_frame,font=("Copperplate",13),text="150",textvariable=self.var_total_double_rooms)
        self.fourthentry.grid(row=3,column=1)


        self.fifthlabel = Label(self.first_label_frame,text="Floor",font=("Copperplate",13,"bold"),padx=10,pady=5)
        self.fifthlabel.place(x=262,y=33)
        self.fifthentry = ttk.Entry(self.first_label_frame,font=("Copperplate",13),width=20,textvariable=self.var_floor_no)
        self.fifthentry.place(x=352,y=35)

        self.sixthlabel = Label(self.first_label_frame,text="Room No",font=("Copperplate",13,"bold"),padx=10,pady=5)
        self.sixthlabel.place(x=242,y=103)
        self.sixthentry = ttk.Entry(self.first_label_frame,font=("Copperplate",13),width=20,textvariable=self.var_room_no)
        self.sixthentry.place(x=352,y=105)


        self.seventh = Label(self.first_label_frame,text="Room Type",font=("Copperplate",13,"bold"),padx=10,pady=5)
        self.seventh.place(x=242,y=168)
        self.seventhentry = ttk.Entry(self.first_label_frame,font=("Copperplate",13),width=20,textvariable=self.var_room_type)
        self.seventhentry.place(x=352,y=170)

        #---------------------------------Images-----------------------------
        third_frame = Frame(self.root,bd=0,relief=RIDGE)
        third_frame.place(x=260,y=55,width=330,height=350)


        image2 = Image.open("room1.jpg")
        image2 = image2.resize((330,160),Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(image=image2)
        label_image2 = Label(third_frame,image=self.image2,bg="black",bd=0).place(x=1,y=10)


        
        image3 = Image.open("room2.jpg")
        image3 = image3.resize((330,160),Image.ANTIALIAS)
        self.image3 = ImageTk.PhotoImage(image=image3)
        label_image3 = Label(third_frame,image=self.image3,bg="black",bd=0).place(x=1,y=185)

        fifth_frame = Frame(self.root,bd=0,relief=RIDGE)
        fifth_frame.place(x=1190,y=55,width=330,height=350)

        image4 = Image.open("room3.webp")
        image4 = image4.resize((330,160),Image.ANTIALIAS)
        self.image4 = ImageTk.PhotoImage(image=image4)
        label_image4 = Label(fifth_frame,image=self.image4,bg="black",bd=0).place(x=1,y=10)


        
        image5 = Image.open("room4.jpg")
        image5 = image5.resize((330,160),Image.ANTIALIAS)
        self.image5 = ImageTk.PhotoImage(image=image5)
        label_image5 = Label(fifth_frame,image=self.image5,bg="black",bd=0).place(x=1,y=185)


        #------------------------------------Buttons-------------------------------

        self.button_frame = Frame(self.first_label_frame,bd=0,relief=RIDGE)
        self.button_frame.place(x=10,y=275,width=502,height=50)

        self.Addbutton = Button(self.button_frame,text="Add",font=("Copperplate",13,"bold"),bg="Green",fg="white",width=8,command=self.Room_add)
        self.Addbutton.place(x=25,y=5)

        self.updatebutton = Button(self.button_frame,text="Update",font=("Copperplate",13,"bold"),bg="Green",fg="white",width=8,command=self.update_data)
        self.updatebutton.place(x=150,y=5)

        self.deletebutton = Button(self.button_frame,text="Delete",font=("Copperplate",13,"bold"),bg="Green",fg="white",width=8,command=self.delete_data)
        self.deletebutton.place(x=278,y=5)

        self.clearbutton = Button(self.button_frame,text="Clear",font=("Copperplate",13,"bold"),bg="Green",fg="white",width=8,command=self.clear)
        self.clearbutton.place(x=404,y=5)

        #-----------------------------------View Customer Details-------------------------------

        second_label_frame = LabelFrame(self.root,text="Room Details",bd=4,font=("times new roman",15,"bold"))
        second_label_frame.place(x=256,y=432,width=1270,height=360)

        self.search_val = StringVar()

        eleventhlabel = Label(second_label_frame,text="Search By:",font=("Copperplate",14,"bold"),bg="green",fg="white",padx=7)
        eleventhlabel.place(x=200,y=12)
        fifthcombo = ttk.Combobox(second_label_frame,font=("Copperplate",14,"bold"),width=20)
        fifthcombo["values"] = ("first_name","Email")
        fifthcombo.current(1)
        fifthcombo["state"] = ("readonly")
        fifthcombo.place(x=340,y=12)

        self.search_txt = StringVar()

        self.fifteenentry = ttk.Entry(second_label_frame,font=("Copperplate",13),width=30)
        self.fifteenentry.place(x=594,y=10,height=29)


        searchbutton = Button(second_label_frame,text="Search",font=("Copperplate",11,"bold"),bg="Green",fg="white")
        searchbutton.place(x=890,y=9)

        showallbutton = Button(second_label_frame,text="Show All",font=("Copperplate",11,"bold"),bg="Green",fg="white")
        showallbutton.place(x=970,y=9)


        third_label_frame = Frame(second_label_frame,bd=30)
        third_label_frame.place(x=0,y=45,width=1280,height=310)

        x_scroll = ttk.Scrollbar(third_label_frame,orient=HORIZONTAL)
        y_scroll = ttk.Scrollbar(third_label_frame,orient=VERTICAL)

        self.view = ttk.Treeview(third_label_frame,columns=("floor_number","room_number","room_type"),xscrollcommand=x_scroll.set,yscrollcommand=y_scroll.set)

        x_scroll.pack(side=BOTTOM,fill=X)
        y_scroll.pack(side=RIGHT,fill=Y)

        x_scroll.config(command=self.view.xview)
        y_scroll.config(command=self.view.yview)

        self.view.heading("floor_number",text="Floor Number")
        self.view.heading("room_number",text="Room Number")
        self.view.heading("room_type",text="Room Type")


        self.view["show"] = "headings"

        
        self.view.column("floor_number",width=120)
        self.view.column("room_number",width=120)
        self.view.column("room_type",width=120)

        self.view.pack(fill=BOTH,expand=1)

        self.view.bind("<ButtonRelease-1>",self.show_data)

        self.Room_data_fetch()




    #---------------------------------Adding  Rooms Data In Database-------------------------------

    def Room_add(self):
        if self.var_floor_no.get() == "" or self.var_room_no.get() == "" or self.var_room_type.get() == "":
            messagebox.showerror("Error","All Fields Are Required!",parent=self.root)
        else:
            conn = pymysql.connect(host="localhost",user="root",password="",database="test")
            cur = conn.cursor()
            cur.execute("select * from room_details where room_number=%s",self.var_room_no.get())
            row = cur.fetchone()
            if row != None:
                messagebox.showerror("Error","Room Already Exit!")
            else:

                try:
                    conn = pymysql.connect(host="localhost",user="root",password="",database="test")
                    cur = conn.cursor()

                    cur.execute("insert into room_details(floor_number,room_number,room_type) values(%s,%s,%s)",(

                                                    self.var_floor_no.get(),
                            
                                                    self.var_room_no.get(),
                                                    self.var_room_type.get()
                                                    
                                                                    ))

                    conn.commit()
                    self.Room_data_fetch()
                    conn.close()
                    messagebox.showinfo("Success","Room Has Been Added")
                    self.clear()

                except Exception as Error:
                    messagebox.showerror("Error",f"Error due to {Error}",parent=self.root)


    def clear(self):
        self.fifthentry.delete(0,END)
        self.seventhentry.delete(0,END)
        self.sixthentry.delete(0,END)


    #---------------------------------Showing Room Data in Table-------------------------------

    def Room_data_fetch(self):
        conn = pymysql.connect(host="localhost",user="root",password="",database="test")
        cur = conn.cursor()
        cur.execute("select * from room_details")
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

        self.var_floor_no.set(row[0])
        self.var_room_no.set(row[1])
        self.var_room_type.set(row[2])


    def update_data(self):
        conn = pymysql.connect(host="localhost",user="root",password="",database="test")
        cur = conn.cursor()
        cur.execute("update room_details set floor_number=%s,room_type=%s where room_number=%s",(

                                                self.var_floor_no.get(),
                                                self.var_room_type.get(),
                                                self.var_room_no.get(),

        ))


        conn.commit()
        self.Room_data_fetch()
        conn.close()
        messagebox.showinfo("Updated","Customer Data Has Been Updated")

    def delete_data(self):
        delete_message = messagebox.askyesno("Warning","Do you want to delete this room",parent=self.root)
        if delete_message>0:
            conn = pymysql.connect(host="localhost",user="root",password="",database="test")
            cur = conn.cursor()
            cur.execute("delete from room_details where room_number=%s",(self.var_room_no.get()))
        else:
            if not delete_message:
                return
        
        conn.commit()
        self.Room_data_fetch()
        conn.close()
        self.clear()

    


    def home(self):
        self.root.destroy()
        import home

    def customer(self):
        self.root.destroy()
        import cust_details

    def room_booking(self):
        self.root.destroy()
        import roombooking

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