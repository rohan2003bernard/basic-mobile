from tkinter import*
import math
import os
import pyttsx3
import random

calc = Tk()

calc.resizable(False, False)

ph_photo = PhotoImage(file = "phone image.png")
phone=Label(calc,image=ph_photo,border=0)
phone.pack()

call_photo=PhotoImage(file="call.png")
call=Button(calc,image=call_photo,border=0)
call.place(x=28,y=432)

#Instruction
def instruc(event=True):
    engine = pyttsx3.init()
    r=random.randint(0,1)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[r].id)  
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-60)
    engine.say("""welcome to the world of calculations. In this app you can do the mathematic calculations.
For that you need to do,
step 1, enter the calculations. Example, 2+3. you can type in your device or else click the buttons provided.
step 2, press the equal to button in the phone or enter key in your device to see the result.
step 3, if you want to continue with that result click or press the any symbol key and give your numbers. 
If you to clear you can click on the AC button or C button or else press escape key in your device.
If you want to go back to the main menu click on the back button.
Enjoy your calculations""")
    engine.runAndWait()
    
start_but=Button(calc,text="""HOW TO
USE""",border=0,bg="red2",fg="green",font=("Arial Black",11),command=instruc)
start_but.place(x=112,y=394,width=69,height=69)

back_photo=PhotoImage(file='back.png')
back=Button(calc,image=back_photo,border=0)
back.place(x=195,y=393)

opt_photo=PhotoImage(file='opt.png')
opt=Button(calc,image=opt_photo,border=0)
opt.place(x=28,y=393)

def open_ph(event=True):
    calc.destroy()
    os.system("phone.py")
    
exit_photo=PhotoImage(file="exit.png")
exit_but=Button(calc,image=exit_photo,border=0,command=open_ph)
exit_but.place(x=195,y=432)

class Calc:
    
    def getandreplace(self):
        self.txt = self.e.get()
        self.txt = self.txt.replace('÷', '/')
        self.txt = self.txt.replace('x', '*')
        self.txt = self.txt.replace('%', '/100')

    def evaluation(self, specfunc):
        self.getandreplace()
        
        try:
            self.txt = eval(str(self.txt))
            
        except SyntaxError:
            self.displayinvalid()
            
        else:
            if any([specfunc == 'sqph', specfunc == 'power']):
                self.txt = self.evalspecialfunctions(specfunc)

            self.refreshtext()

    def displayinvalid(self):
        self.e.delete(0, END)
        self.e.insert(0, 'Invalid Input!')

    def refreshtext(self):
        self.e.delete(0, END)
        self.e.insert(0, self.txt)

    def evalspecialfunctions(self, specfunc):
        
        if specfunc == 'sqph':
            return math.sqrt(float(self.txt))
        
        elif specfunc == 'power':
            return math.pow(float(self.txt), 2)

    def clearall(self):
        self.e.delete(0, END)
        self.e.insert(0, '0')

    def clear1(self, event=None):
        
        if event is None:
            self.txt = self.e.get()[:-1]
            
        else:
            self.txt = self.getvalue()

            self.refreshtext()

    def action(self, argi: object):
        self.txt = self.getvalue()
        self.stripfirstchar()
        self.e.insert(END, argi)

    def keyaction(self, event=None):
        self.txt = self.getvalue()

        if any([event.char.isdigit(), event.char in '/*-+%().']):
            self.stripfirstchar()
            
        elif event.char == '\x08':
            self.clear1(event)
            
        elif event.char == '\x1b':
            self.clearall()
            
        elif event.char == '\r':
            self.evaluation('eq')
            
        else:
            self.displayinvalid()
            return 'break'

    def stripfirstchar(self):
        if self.txt[0] == '0':
            self.e.delete(0, 1)

    def getvalue(self): 
        return self.e.get()

    def __init__(self,master):
        self.txt = 'o'
        
        master.title('Calulator')
        master.geometry('235x512')
        
        self.e = Entry(master,bg="lightgreen",fg="blue",font=('times',20,"bold"),border=5)
        self.e.place(x=34, y=78,width=228,height=50)
        
        self.e.insert(0, '0')
        self.e.focus_set()

        Button(master, text="=", width=21,bg='green',font=("Arial Black",20), command=lambda: self.evaluation('eq')).place(x=33, y=310,width=232,height=50)
        Button(master, text='AC',  bg='green',font=("Arial Black",20), command=lambda: self.clearall()).place(x=151, y=260,width=56,height=50)
        Button(master, text='C',  bg='green',font=("Arial Black",20), command=lambda: self.clear1()).place(x=210, y=260,width=56,height=50)
        Button(master, text="+",  bg='white',font=("Arial Black",20), command=lambda: self.action('+')).place(x=33, y=160,width=56,height=50)
        Button(master, text="x",  bg='white',font=("Arial Black",20), command=lambda: self.action('x')).place(x=151, y=160,width=56,height=50)
        Button(master, text="-",  bg='white',font=("Arial Black",20), command=lambda: self.action('-')).place(x=92, y=160,width=56,height=50)
        Button(master, text="÷",  bg='white',font=("Arial Black",20), command=lambda: self.action('÷')).place(x=210, y=160,width=56,height=50)
        Button(master, text="%",  bg='white',font=("Arial Black",20), command=lambda: self.action('%')).place(x=210, y=210,width=56,height=50)
        Button(master, text="#",bg="red2",fg="green",font=("Arial Black",20),border=0,command=lambda: self.action('#')).place(x=196,y=586,width=70,height=29)
        Button(master, text="*",bg="red2",fg="green",font=("Arial Black",20),border=0,command=lambda: self.action('*')).place(x=28,y=586,width=70,height=29)
        Button(master, text="7",bg="red2",fg="green",font=("Arial Black",20),border=0,command=lambda: self.action('7')).place(x=28,y=548,width=70,height=23)
        Button(master, text="8",bg="red2",fg="green",font=("Arial Black",20),border=0,command=lambda: self.action('8')).place(x=112,y=548,width=70,height=23)
        Button(master, text="9",bg="red2",fg="green",font=("Arial Black",20),border=0,command=lambda: self.action('9')).place(x=196,y=548,width=70,height=23)
        Button(master, text="4",bg="red2",fg="green",font=("Arial Black",20),border=0,command=lambda: self.action('4')).place(x=28,y=512,width=70,height=22)
        Button(master, text="5",bg="red2",fg="green",font=("Arial Black",20),border=0,command=lambda: self.action('5')).place(x=112,y=512,width=70,height=22)
        Button(master, text="6",bg="red2",fg="green",font=("Arial Black",20),border=0,command=lambda: self.action('6')).place(x=196,y=512,width=70,height=22)
        Button(master, text="1",bg="red2",fg="green",font=("Arial Black",20),border=0,command=lambda: self.action('1')).place(x=28,y=474,width=70,height=22)
        Button(master, text="2",bg="red2",fg="green",font=("Arial Black",20),border=0,command=lambda: self.action('2')).place(x=112,y=474,width=70,height=22)
        Button(master, text="3",bg="red2",fg="green",font=("Arial Black",20),border=0,command=lambda: self.action('3')).place(x=196,y=474,width=70,height=22)
        Button(master, text="0", bg="red2",fg="green",font=("Arial Black",20),border=0, command=lambda: self.action('0')).place(x=112,y=586,width=70,height=29)
        Button(master, text=".",  bg='white',font=("Arial Black",20), command=lambda: self.action('.')).place(x=33, y=210,width=56,height=50)
        Button(master, text="(",bg='green',font=("Arial Black",20), command=lambda: self.action('(')).place(x=33, y=260,width=56,height=50)
        Button(master, text=")",  bg='green',font=("Arial Black",20), command=lambda: self.action(')')).place(x=92, y=260,width=56,height=50)
        Button(master, text="√",  bg='white',font=("Arial Black",20), command=lambda: self.evaluation('sqph')).place(x=151, y=210,width=56,height=50)
        Button(master, text="x²",  bg='white',font=("Arial Black",20), command=lambda: self.evaluation('power')).place(x=92, y=210,width=56,height=50)

        self.e.bind('<Key>', lambda evt: self.keyaction(evt))

obj=Calc(calc)

calc.geometry("298x650")

calc.mainloop()
