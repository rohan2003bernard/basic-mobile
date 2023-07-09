import datetime
import webbrowser
import tkinter
from pynput.mouse import Button, Controller
import pynput
import random
import os
import pyttsx3
import time

mouse = Controller()
key=pynput.keyboard.Controller()

cl=tkinter.Tk()

cl.geometry("750x750")
cl.resizable(False, False)

bg_pic=tkinter.PhotoImage(file="oc_bg.png")
clbg=tkinter.Label(cl,image=bg_pic)
clbg.pack()

pic=tkinter.PhotoImage(file="oc_img.png")
bgpic=tkinter.Label(cl,image=pic,bg="antique white")
bgpic.place(x=70,y=10)

link=tkinter.Entry(cl,fg="gray",font=('Copperplate Gothic Bold',25))
link.insert(0,"Enter the class link")
link.place(x=80,y=400,width=600,height=50)

def clear_link(event):
    link.delete(0, 'end')
    link['fg'] = 'black'
    link.unbind("<FocusIn>")
    return None
link.bind("<FocusIn>", clear_link)

def meet():
    l=link.get()
    if l=="Enter the class link":
        None
    else:
        global mouse
        global key
        webbrowser.open(l)
        time.sleep(10)

        ##MAXIMIZE
        key.press(pynput.keyboard.Key.alt)
        key.press(pynput.keyboard.Key.space)
        key.release(pynput.keyboard.Key.space)
        key.release(pynput.keyboard.Key.alt)
        time.sleep(2)
        key.press('x')
        key.release('x')
        time.sleep(2)
        ##mute mic
        mouse.position = (494,655)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(3)
        ##mute camera
        mouse.position = (577,655)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(3)
        ##Join
        mouse.position = (1127,492)
        mouse.press(Button.left)
        mouse.release(Button.left)
        time.sleep(3)

start=tkinter.Button(cl,text="JOIN",bg="dark violet",font=("Copperplate Gothic Bold",24),command=meet)
start.place(x=325,y=470,width=100,height=50)

cl.bind('<Return>',meet)

def ph_open(event=True):
    cl.destroy()
    os.system("phone.py")

back=tkinter.Button(cl,text="EXIT",bg="DarkGoldenrod2",font=("Copperplate Gothic Bold",24),command=ph_open)
back.place(x=100,y=550,width=150,height=150)

cl.bind('<Escape>',ph_open)

#Instruction
def instruc(event=True):
    r=random.randint(0,1)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[r].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    engine.say("""Welcome to online class. In this app you need to give the class link and sit back and see the automatic class joining function.
You need to do,
Step 1, Paste your class link the space provided.
Step 2, Click join button or press enter key.
stay relaxed and see the system joining itself without any disturbance.
Have a nice day.""")
    engine.runAndWait()
    
HTU=tkinter.Button(cl,text="""HOW TO
USE
press (?)""",bg="SeaGreen3",font=("Copperplate Gothic Bold",24),command=instruc)
HTU.place(x=500,y=550,width=150,height=150)

cl.mainloop()
