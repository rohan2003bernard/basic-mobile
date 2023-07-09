import requests
from tkinter import*
import random
import pyttsx3
import os

msg=Tk()

msg.geometry("750x750")
msg.resizable(False, False)

sms_bg=PhotoImage(file="sms_bg.png")
bg=Label(msg,image=sms_bg)
bg.pack()

num=Entry(msg,fg='grey',bg="darkgoldenrod1",font=("CGill Sans MT",20))
num.insert(0,"Enter the number")
num.place(x=90,y=50,width=500,height=50)

msg_box=Text(msg,bg='medium blue',font=("CGill Sans MT",20))
msg_box.insert(END,"Enter you message")
msg_box.place(x=0,y=200,width=750,height=550)

def clear_num(event):
    num.delete(0, "end")
    num['fg']='black'
    num.unbind("<FocusIn>")
num.bind("<FocusIn>", clear_num)

def send(event=True):
    number=num.get()
    mes=msg_box.get("1.0", "end-1c")
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS&language=english&route=p&message=&numbers="
    mes="message="+mes
    number="numbers="+number
    payload = payload.replace("message=",mes)
    payload = payload.replace("numbers=",number)
    headers = {
    'authorization': "Gn1kiNRhTIqYVrHfuz0mB7e32yM8dEjgZXP5LWtJ4xF6wsbvOcOwmHpyPNRgl897nBWK1UjAuFQk2rTS",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    }
    sent_msg=Label(msg,text="SENT",bg="purple",font=("Rockwell",20))
    sent_msg.place(x=335,y=120,width=80)
    msg.after(1000,sent_msg.destroy)
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)

def clear_mes(event):
    msg_box.delete("1.0","end")
    msg_box['fg']='black'
    msg_box.unbind("<FocusIn>")
msg_box.bind("<FocusIn>", clear_mes)

sendpic=PhotoImage(file="msg_send.png")
send=Button(msg,image=sendpic,bg="lime green",command=send)
send.place(x=600,y=25,width=150,height=150)

msg.bind("<Return>",send)

heading=Label(msg,text="MESSAGE",bg="blue",fg="green2",font=(None,20))
heading.place(x=300,y=10)

def ph_open(event=True):
    msg.destroy()
    os.system("phone.py")

msg.bind("<Escape>",ph_open)

back=Button(msg,text="EXIT",font=("CGill Sans MT",20),bg="green4",command=ph_open)
back.place(x=10,y=10,width=60,height=40)

#Instruction
def instruc(event=True):
    r=random.randint(0,1)
    engine = pyttsx3.init()  
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[r].id)  
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    engine.say("""Welcome to the place for sms. In this app you can message any of your friends.
step 1, Enter your friend's number.
step 2, Enter your message to your friend.
step 3, Click on the send button or press enter key.
A message sent will be displayed.
Your message has been sent.
If you want to go to main menu click exit.
Have a great messaging time.""")
    engine.runAndWait()
    
msg.bind("?",instruc)

HTU=Button(msg,text="""HOW
TO
USE
(?)""",font=("CGill Sans MT",16),bg="saddle brown",command=instruc)
HTU.place(x=10,y=60,width=60,height=120)

msg.mainloop()
