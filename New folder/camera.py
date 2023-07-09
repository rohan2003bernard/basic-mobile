import tkinter
import cv2
import os
import PIL.Image, PIL.ImageTk
import random
import time
import pyttsx3
 
class App:
    def __init__(self, cam,window_title, video_source=0):
        self.cam = cam
        self.cam.title(window_title)
        self.cam.geometry("750x750")
        self.cam.resizable(False, False)
        self.cam.attributes('-topmost', True)
        self.cam.update()
        self.cam.attributes('-topmost', False)
        self.video_source = video_source
        self.vid = MyVideoCapture(self.video_source)

        self.cambg=tkinter.PhotoImage(file="cam_bg.png")
        self.bg=tkinter.Label(cam,image=self.cambg)
        self.bg.pack()
        
        self.canvas =tkinter.Canvas(cam, width = self.vid.width, height = self.vid.height,bg='cyan2',border=0)
        self.canvas.place(x=55,y=30)

        def message(event=True):
            self.flash_pic=tkinter.PhotoImage(file="flash.png")
            self.flash=tkinter.Label(cam,image=self.flash_pic)
            self.flash.place(x=55,y=30)
            self.flash.after(500,self.flash.destroy)
            
            self.msg=tkinter.Label(cam,text="CAPTURED",bg='lawn green',font=("Berlin Sans FB Demi",80),fg='blue')
            self.msg.place(x=55,y=200,width=640)
            self.cam.after(1000,self.msg.destroy)
            
        self.ins=tkinter.Label(cam,text="""Press 'c' to take a pic
and
Press 'esc' to return back""",anchor="e",bg='cyan2',font=("Berlin Sans FB Demi",30),fg='brown')
        self.ins.place(x=55,y=550,width=640)
        cam.bind('c',self.snapshot)
        self.btn_snapshot=tkinter.Button(cam, text="Snapshot",width=24,font=("Castellar",12,"bold"),bg='cyan2',
                                         activebackground='green', command=lambda:[self.snapshot(),message()])
        self.btn_snapshot.place(x=375,y=510,width=320,height=40)

        cam.bind("<Escape>",self.back)
        self.btn_back=tkinter.Button(cam,text="EXIT",font=("Castellar",12,"bold"),bg='cyan2',command=self.back)
        self.btn_back.place(x=55,y=510,width=320,height=40)
        self.emoji_pic=tkinter.PhotoImage(file="selfie.png")
        self.emoji=tkinter.Label(cam,image=self.emoji_pic,border=0)
        self.emoji.place(x=55,y=550)

        #Instructions
        def instruc(event=True):
            r=random.randint(0,1)
            engine = pyttsx3.init()  
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[r].id)  
            rate = engine.getProperty('rate')
            engine.setProperty('rate', rate-60)
            engine.say("""Welcome to the world of pictures.
Here you can take selfie of your or with your friends.
If you want to selfie click on the button snapshot or press C.
If you want to return to the main menu click on the button exit or press escape in your device.
Help other with a smile.""")
            engine.runAndWait()
        cam.bind("?",instruc)
        self.HTU=tkinter.Button(cam,text="""HOW TO USE""",border=0,bg='cyan2',fg="green",font=("Berlin Sans FB Demi",30),command=instruc)
        self.HTU.place(x=225,y=690,width=250,height=60)

        self.delay = 15
        self.update()
        self.cam.mainloop()
    def back(self,event=True):
        self.cam.destroy()
        os.system("phone.py")
 
    def snapshot(self,event=True):
        
        ret, frame = self.vid.get_frame()

        if ret:
            cv2.imwrite("capture-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
     
    def update(self):
        
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)

        self.cam.after(self.delay, self.update)


class MyVideoCapture:
    def __init__(self, video_source=0):

        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
           return (ret, None)

    def __del__(self):
       if self.vid.isOpened():
            self.vid.release()
            
App(tkinter.Tk(), "CAMERA")
