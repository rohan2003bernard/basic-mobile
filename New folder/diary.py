from tkinter import*
import csv
import os
import pyttsx3
import random
import datetime

dtk=Tk()

dtk.resizable(False, False)
dtk.geometry('1000x750')

today=datetime.date.today()

diary_back = PhotoImage(file = "diary_back2.png")
back=Label(dtk,image=diary_back,border=0)
back.pack(anchor=CENTER)

mem=Text(dtk,bg='darkslategray1',fg='green',font=["Comic Sans MS",20])
mem.insert(INSERT, '\n')
mem.insert(INSERT, '\n')
mem.place(x=125,y=190,width=750,height=445)

d=int(today.strftime("%d"))
m=int(today.strftime("%m"))
y=int(today.strftime("%Y"))

date_dm=Label(dtk,text=(d,'/',m),fg='green',font=["Comic Sans MS",18])
date_dm.place(x=300,y=120)

date_y=Label(dtk,text=(y),fg='green',font=["Comic Sans MS",18])
date_y.place(x=300,y=150)

days=datetime.datetime.today().strftime("%a")

def ph_open(event=True):
    dtk.destroy()
    os.system("phone.py")

dtk.bind("<Escape>",ph_open)

back=Button(dtk,text="BACK",fg="blue",bg="pink",font=["Comic Sans MS",18],command=ph_open)
back.place(x=0,y=0,width=125,height=50)

day=Label(dtk,text=(days),fg='green',font=["Comic Sans MS",25])
day.place(x=618,y=135)

spe=Entry(dtk,fg="grey",bg='yellow',font=["Comic Sans MS",18],justify="center")
spe.insert(0,"Enter today's special")
spe.place(x=250,y=190,width=500,height=50)

def special(event):
    spe.delete(0, "end")
    spe['fg'] = 'red'
    spe['bg']='yellow'
    spe.unbind("<FocusIn>")
    return None
spe.bind("<FocusIn>", special)

def saving():
    spec=spe.get()
    memo=mem.get("1.0","end-1c")
    memo=memo.replace("\n\n","")
    with open("diary.csv","a") as csvfile:
        mywriter=csv.writer(csvfile,delimiter=',')
        mywriter.writerow([d,m,y,spec,memo])
        
save=Button(dtk,text="SAVE",fg='cyan',bg='green',font=["Comic Sans MS",18,"bold"],command=saving)
save.place(x=885,y=265,width=105,height=70)

def displaying():
    dis=Toplevel()
    dis.resizable(False, False)
    dis.geometry("600x600")
    dis.configure(bg="white")
    date=Entry(dis,font=(None,20))
    date.place(x=110,y=10,width=50,height=50)
    month=Entry(dis,font=(None,20))
    month.place(x=160,y=10,width=50,height=50)
    year=Entry(dis,font=(None,20))
    year.place(x=210,y=10,width=80,height=50)
    date_lab=Label(dis,text="DATE :",font=["Comic Sans MS",20])
    date_lab.place(x=10,y=10)
    dmy=Label(dis,text="DD/MM/YYYY",bg="red",font=(None,20))
    dmy.place(x=110,y=70,width=180,height=50)

    def getting():
        d=int(date.get())
        m=int(month.get())
        y=int(year.get())
        with open("diary.csv",mode="r") as csvfile:
            myreader=csv.reader(csvfile,delimiter=",")
            for row in myreader:
                if len(row)!=0:
                    if int(row[0])==d:
                        if int(row[1])==m:
                            if int(row[2])==y:
                                result=("\nMemories :",row[4])
                                label1=Label(dis,text=("SpecialEvent :",row[3]),bg="white",font=["Comic Sans MS",18])
                                label1.place(x=0,y=130,width=600,height=40)
                                label2=Text(dis,bg="lightblue",fg="red2",font=["Comic Sans MS",25])
                                label2.insert(END,("Memories :",row[4]))
                                label2.place(x=0,y=170,width=600,height=430)
                    
    check=Button(dis,text="check",bg="white",fg="green",font=["Comic Sans MS",25],command=getting)
    check.place(x=300,y=10,width=110,height=110)

    def exiting():
        dis.destroy()
    
    back=Button(dis,text="QUIT",bg="white",fg="green",font=["Comic Sans MS",25],comman=exiting)
    back.place(x=420,y=10,width=110,height=110)
    
display=Button(dtk,text="DISPLAY",fg='cyan',bg='green',font=["Comic Sans MS",16,"bold"],command=displaying)
display.place(x=10,y=265,width=105,height=70)

#Instruction
def instruc(event=True):
    r=random.randint(0,1)
    engine = pyttsx3.init()  
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[r].id)  
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    engine.say("""Welcome to the world of memories.
Here you can maintain your personal diary.
step 1 . In the yellow box enter that day's special event.
step 2 . In the blue box enter your memories of the day.
step 3 . Click save.
If you want to see your old memories click display and it opens a new window,
there you are given three boxes if the first box enter the date, in the second box enter the month, and, in the third box enter the year.
then click ckeck button.
Your memories would be displayed.
Have a great days.""")
    engine.runAndWait()
    
dtk.bind("?",instruc)

instr=Button(dtk,text="""HOW TO
USE (?)""",bg="white",fg="green",font=["Comic Sans MS",16,"bold"],comman=instruc)
instr.place(x=10,y=140,width=105,height=70)

dtk.mainloop()
