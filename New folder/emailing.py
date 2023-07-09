import smtplib
from tkinter import*
from email.message import EmailMessage
import os
import time
import random
import pyttsx3

em=Tk()

em.resizable(False, False)
em.geometry("750x750")

bg_photo=PhotoImage(file="email_bg.png")
bg=Label(em,image=bg_photo)
bg.place(x=0,y=0)

user_id=Entry(em,fg='grey',bg="dodgerblue3",font=("CGill Sans MT",20))
user_id.insert(0,"Enter your friend's email id")
user_id.place(x=80,y=25,width=500,height=50)
    
def clear_user(event):
    user_id.delete(0, "end")
    user_id['fg']='black'
    user_id.unbind("<FocusIn>")
user_id.bind("<FocusIn>", clear_user)

subject=Entry(em,fg='grey',bg="dark turquoise",font=("CGill Sans MT",20))
subject.insert(0,"Subject")
subject.place(x=80,y=100,width=500,height=50)

def clear_subject(event):
    subject.delete(0, "end")
    subject['fg']='black'
    subject.unbind("<FocusIn>")
    
subject.bind("<FocusIn>", clear_subject)

msg_box=Text(em,bg='red',font=("CGill Sans MT",20))
msg_box.place(x=0,y=200,width=750,height=550)

def send():
    u=user_id.get()
    if "@gmail.com" in u:
        None
    else:
        u=u+"@gmail.com"
    s=subject.get()
    message=msg_box.get("1.0", "end-1c")
    m = EmailMessage()
    m["From"] = "basicphone2020@gmail.com"
    m["Subject"] = s
    m["To"] = u
    m.set_content(message)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login('basicphone2020@gmail.com', 'simplyphone')
    s.send_message(m)
    sent_msg=Label(em,text="SENT",bg="yellow",font=("Rockwell",20))
    sent_msg.place(x=335,y=160,width=80)
    em.after(1000,sent_msg.destroy)

send_pic=PhotoImage(file="send.png")
send=Button(em,image=send_pic,command=send)
send.place(x=600,y=25)

def ph_open(event=True):
    em.destroy()
    os.system("phone.py")

def clearing(event=True):
    user_id.delete(0, "end")
    subject.delete(0, "end")
    msg_box.delete('1.0', END)
    
em.bind("<Escape>",clearing)

back=Button(em,text="EXIT",font=("CGill Sans MT",20),bg="deep pink",command=ph_open)
back.place(x=10,y=10,width=60,height=40)

#Instructions
def instruc(event=True):
    r=random.randint(0,1)
    engine = pyttsx3.init()  
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[r].id)  
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    engine.say("""Welcome to world of internet.
Here you can send mail to your friends through gmail.
for that you need to do,
step 1, enter your friends email address, in this you can type with gmail dor com or without gmail dot com,
for example let xyz be the user,
in the username box xyz@gmail.com is valid xyz is also valid.
step 2, Enter the subject of sending this mail.
step 3, Start to type your message.
step 4, click on the send button.
A sent message will be displayed.
Your mail has been sent to your friend.
If you want to send one more email press escape.
If you want to go to main menu click exit button.
Have a great emailing time.""")
    engine.runAndWait()
    
em.bind("?",instruc)

HTU=Button(em,text="""HOW
TO
USE
(?)""",font=("CGill Sans MT",16),bg="sea green",command=instruc)
HTU.place(x=10,y=60,width=60,height=120)

em.mainloop()
