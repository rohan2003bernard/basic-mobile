from tkinter import *
import pyttsx3
import webbrowser
import random
import os

ggl=Tk()

ggl.geometry("750x750")
ggl.config(bg='white')
ggl.resizable(False, False)

search=Entry(ggl,font=('Eras Bold ITC',20),fg="gray")
search.insert(0,"Enter your search")
search.place(x=125,y=300,width=500,height=50)

def clear_search(event):
    search.delete(0, END)
    search['fg'] = 'black'
    search.unbind("<FocusIn>")
    return None
search.bind("<FocusIn>", clear_search)

def getting(event=True):
    val=search.get()
    webbrowser.open("https://www.google.com/search?q=" + val)
    search.delete(0,END)
    
ser=Button(ggl,text="SEARCH",bg='firebrick1',font=('times',20,"bold"),command=getting)
ser.place(x=300,y=400,width=150,height=50)

ggl.bind("<Return>",getting)

ggl_pic=PhotoImage(file="google_txt.png")
ggl_label=Label(ggl,image=ggl_pic,bg='white')
ggl_label.place(x=50,y=50)

def ph_open(event=True):
    ggl.destroy()
    os.system("phone.py")
    
back=Button(ggl,text="BACK",font=("Copperplate Gothic Bold",28),bg='PaleVioletRed2',command=ph_open)
back.place(x=100,y=500,width=200,height=200)

ggl.bind("<Escape>",ph_open)

#Instructions
def instruc(event=True):
    r=random.randint(0,1)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[r].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    engine.say("""Welcome to google. In this app you can use it as google search.
step 1, in the search box, enter you search.
step 2, click on the search button or press enter key. You will be directed to the google page.
If you want to got to main menu click on the quit button or press escape key.
Have a nice day.""")
    engine.runAndWait()
    
ggl.bind("?",instruc)

HTU=Button(ggl,text="""HOW TO
USE (?)""",font=("Copperplate Gothic Bold",28),bg='cornflower blue',command=instruc)
HTU.place(x=450,y=500,width=200,height=200)

ggl.mainloop()
