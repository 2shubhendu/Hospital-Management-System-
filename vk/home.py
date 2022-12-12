from tkinter import *
from PIL import Image,ImageTk
from matplotlib import image


class Hotel:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1550x800+0+0")
        self.root.title("Hotel Management System")

        #---------------------------------Background Image-------------------------------

        image2 = Image.open("hotel4.jpg")
        image2 = image2.resize((1550,800),Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(image=image2)
        label_image2 = Label(self.root,image=self.image2)
        label_image2.place(x=0,y=0)



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

        button_customer = Button(self.frame1,text="Home",font=("times new roman",15,"bold"),background="gray14",fg="white",bd=0,activebackground="gray14",activeforeground="white",cursor="hand2")
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


    def customer(self):
        self.root.destroy()
        import cust_details

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