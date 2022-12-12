import smtplib
import random
from tkinter import messagebox

password = "kali"

s = smtplib.SMTP("smtp.gmail.com" , 587)
s.starttls()

s.login("ncerpune12345@gmail.com" , "Ncer@123")
s.sendmail("ncerpune12345@gmail.com", "khetavatvishal14@gmail.com", password)
messagebox.showinfo("Success","Password sent successfully on your registered email")