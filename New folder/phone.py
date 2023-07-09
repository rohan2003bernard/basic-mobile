from tkinter import *
import os
import random
from datetime import*
import pyttsx3
import time

ph=Tk()

ph.geometry("298x650")
ph.resizable(False, False)
ph.title("phone")

#cover
ph_photo = PhotoImage(file = "phone image.png")
phone=Label(ph,image=ph_photo,border=0)
phone.pack()

def power_off(event=True):
    ph.destroy()

ph.bind("<Escape>",power_off)

exit_photo=PhotoImage(file="exit.png")
exit_but=Button(ph,image=exit_photo,border=0,command=power_off)
exit_but.place(x=195,y=432)

call_photo=PhotoImage(file="call.png")
call=Button(ph,image=call_photo,border=0)
call.place(x=28,y=432)

#Instruction
def instruc(event=True):
    r=random.randint(0,1)
    engine = pyttsx3.init()  
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[r].id)  
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-60)
    engine.say("""welcome. This is a basic model virtual phone.
This phone contains automatic online class attender, calculator, camera, diary, emailing facility, google, shin chan game, sms and wikipedia.
If you click any of the app it will direct you to the app's window.
If you want to exit click back button or press escape.
Enjoy your virtual phone.
Handle with care.""")
    engine.runAndWait()
    
ph.bind("?",instruc)

HTU_but=Button(ph,text="""HOW TO
USE.
(Press (?))""",border=0,bg="red2",fg="blue2",font=("Arial Black",11),command=instruc)
HTU_but.place(x=112,y=394,width=69,height=69)

back_photo=PhotoImage(file='back.png')
back=Button(ph,image=back_photo,border=0)
back.place(x=195,y=393)

opt_photo=PhotoImage(file='opt.png')
opt=Button(ph,image=opt_photo,border=0)
opt.place(x=28,y=393)

#calculator
def open_calc():
    ph.destroy()
    os.system('calculator.py')
    
calc_photo=PhotoImage(file = "calc.png")
calc=Button(ph,image=calc_photo,border=0,command=open_calc)
calc.place(x=120,y=145)

#class
def open_class():
    ph.destroy()
    os.system('class.py')
    
cal_photo=PhotoImage(file = "oc.png")
cal=Button(ph,image=cal_photo,border=0,command=open_class)
cal.place(x=45,y=145)

#diary
def open_diary(event=True):
    ph.destroy()
    os.system("diary.py")
    
diary_photo=PhotoImage(file='diary.png')
diary=Button(ph,image=diary_photo,border=0,command=open_diary)
diary.place(x=45,y=220)

#google
def open_web():
    ph.destroy()
    os.system("google.py")
    
google_photo=PhotoImage(file='google.png')
google=Button(ph,image=google_photo,border=0,command=open_web)
google.place(x=195,y=220)

#wikipedia
def open_wiki():
    ph.destroy()
    os.system("wiki.py")
    
wiki_photo=PhotoImage(file='wiki_image.png')
wiki=Button(ph,image=wiki_photo,border=0,command=open_wiki,bg="lime green")
wiki.place(x=195,y=295)

#camera
def open_cam():
    ph.destroy()
    os.system("camera.py")
    
cam_photo=PhotoImage(file='camera.png')
cam=Button(ph,image=cam_photo,border=0,command=open_cam)
cam.place(x=195,y=145)

# shin chan
def open_shin():
    ph.destroy()
    os.system('shin_game.py')
    
shin_photo=PhotoImage(file="shin_pic.png")
shin_chan=Button(ph,image=shin_photo,border=0,command=open_shin,bg="lime green")
shin_chan.place(x=45,y=295)

# Emailing
def open_email():
    ph.destroy()
    os.system("emailing.py")
    
email_photo=PhotoImage(file="mail.png")
email=Button(ph,image=email_photo,border=0,command=open_email)
email.place(x=120,y=220)

#Power off
def open_sms():
    ph.destroy()
    os.system("sms.py")
    
sms_photo=PhotoImage(file="sms.png")
sms=Button(ph,image=sms_photo,border=0,command=open_sms)
sms.place(x=120,y=295)

#date
today=time.strftime("%d/%m/%Y")
date=Label(ph,text=today,fg='black',font=('times', 16, 'bold'),bg="chocolate1")
date.place(x=74,y=106,width=150,height=28)

#time
time1 = ''
clock = Label(ph, font=('times', 18, 'bold'),bg="chocolate1")
clock.place(x=92,y=78,width=111,height=28)

def tick():
    global time1
    time2 = time.strftime('%H:%M')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200, tick)
tick()

#numbers
one=Button(ph,text="1",bg="red2",fg="blue2",border=0,font=("Arial Black",20))
one.place(x=28,y=474,width=70,height=22)

two=Button(ph,text="2",bg="red2",fg="blue2",border=0,font=("Arial Black",20))
two.place(x=112,y=474,width=70,height=22)

three=Button(ph,text="3",bg="red2",fg="blue2",border=0,font=("Arial Black",20))
three.place(x=196,y=474,width=70,height=22)

four=Button(ph,text="4",bg="red2",fg="blue2",border=0,font=("Arial Black",20))
four.place(x=28,y=512,width=70,height=22)

five=Button(ph,text="5",bg="red2",fg="blue2",border=0,font=("Arial Black",20))
five.place(x=112,y=512,width=70,height=22)

six=Button(ph,text="6",bg="red2",fg="blue2",border=0,font=("Arial Black",20))
six.place(x=196,y=512,width=70,height=22)

seven=Button(ph,text="7",bg="red2",fg="blue2",border=0,font=("Arial Black",20))
seven.place(x=28,y=548,width=70,height=23)

eight=Button(ph,text="8",bg="red2",fg="blue2",border=0,font=("Arial Black",20))
eight.place(x=112,y=548,width=70,height=23)

nine=Button(ph,text="9",bg="red2",fg="blue2",border=0,font=("Arial Black",20))
nine.place(x=196,y=548,width=70,height=23)

zero=Button(ph,text="0",bg="red2",fg="blue2",border=0,font=("Arial Black",20))
zero.place(x=112,y=586,width=70,height=29)

ash=Button(ph,text="#",bg="red2",fg="blue2",border=0,font=("Arial Black",20))
ash.place(x=196,y=586,width=70,height=29)

star=Button(ph,text="*",bg="red2",fg="blue2",border=0,font=("Arial Black",20))
star.place(x=28,y=586,width=70,height=29)

made=Label(ph,text="""M
A
D
E

I
N

I
N
D
I
A""",font=(None,9),bg="black",fg="white")
made.place(x=280,y=100)

ph.mainloop()
