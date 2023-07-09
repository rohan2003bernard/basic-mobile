import pygame
from pygame import mixer
import random
import os
import time
import playsound

pygame.init()

w=1200
h=700

Qx=1050
Qy=640

black = (0,0,0)
white = (255,255,255)

red = (200,0,0)
green = (0,200,0)
blue = (0,0,205)

bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue = (0,128,255)

shin_width = 149
shin_height = 200

gameDisplay = pygame.display.set_mode((w,h))
pygame.display.set_caption('ShinChan Game')
clock = pygame.time.Clock()

#Images
background=pygame.image.load('sc_bg.png')
shinImg =pygame.image.load('shinchan.png')
kamenin=pygame.image.load('action kamen.png')
menu_bg=pygame.image.load("menu.png")
lost=pygame.image.load("beated.png")
lost_bg=pygame.image.load("hell.png")
misae=pygame.image.load("misae.png")
dialouge=pygame.image.load("misae dia.png")
lt=pygame.image.load("arr_left.png")
rt=pygame.image.load("arr_right.png")
ins_bg=pygame.image.load("ins_bg.png")

#Sounds
drop_sound=mixer.Sound("end beat.mp3")
catch=mixer.Sound("catch.mp3")

def shin_score(count):
    font = pygame.font.SysFont("Eras Bold ITC", 80)
    text = font.render("score: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def dropcount(drop_count):
    drop_font = pygame.font.SysFont("Eras Bold ITC", 80)
    drop_text= drop_font.render("DROPPED: "+str(drop_count), True, black)
    gameDisplay.blit(drop_text,(w-350,0))

def things(kamenx, kameny, thingw, thingh):
    gameDisplay.blit(kamenin,(kamenx,kameny))

def shin(x,y):
    gameDisplay.blit(shinImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((w/2),(h/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def button(msg,Bx,By,Bw,Bh,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if Bx+Bw > mouse[0] > Bx and By+Bh > mouse[1] > By:
        pygame.draw.rect(gameDisplay, ac,(Bx,By,Bw,Bh))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(Bx,By,Bw,Bh))
    Button_Text = pygame.font.SysFont("Eras Bold ITC",50)
    textSurf, textRect = text_objects(msg, Button_Text)
    textRect.center = ( (Bx+100), (By+70) )
    gameDisplay.blit(textSurf, textRect)
    
def droped():
    gameDisplay.blit(lost_bg,(0,0))
    message_display('You lost')
    gameDisplay.blit(misae,(510,50))
    gameDisplay.blit(dialouge,(750,0))
    gameDisplay.blit(lost,((w/2-100),(h/2+50)))
    mixer.Sound.play(drop_sound)
    mixer.music.stop()
    pygame.display.update()

    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        button("Play Again",200,450,200,150,green,bright_green,game_loop)
        button("Quit",800,450,200,150,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(60)

def instruc(text,x,y):
    font = pygame.font.SysFont("Eras Bold ITC", 50)
    Text= font.render(text, True, blue)
    gameDisplay.blit(Text,(x,y))
    
def inst():
    gameDisplay.blit(ins_bg,(0,0))
    mixer.music.load("music.mp3")
    mixer.music.play(-1)
    ins=True
    while ins:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        instruc("Shin Chan has to clean his room. ",10,20)
        instruc("So kindly help him.",10,65)
        instruc("He has to catch the falling toys and",10,100)
        instruc("if he catches one toy he gets one point.",10,135)
        instruc("or else if he drop, drop point increases",10,170)
        instruc("toys can be catched only using hands",10,205)
        instruc("press left arrow key to move left",10,240)
        instruc("press right arrow key to move right",10,275)
        gameDisplay.blit(lt,(10,380))
        gameDisplay.blit(rt,(150,380))
        button("PLAY",100,500,220,150,green,bright_green,game_loop)
        pygame.display.update()
        
def quitgame():
    pygame.quit()
    os.system("phone.py")

def menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.blit(menu_bg,(0,0))
        largeText = pygame.font.SysFont("Eras Bold ITC",115)
        TextSurf, TextRect = text_objects("""Shin Chan's Catch the toys""", largeText)
        TextRect.center = ((w/2),100)
        gameDisplay.blit(TextSurf, TextRect)

        button("PLAY",50,500,200,150,green,bright_green,game_loop)
        button("HOW TO",270,500,200,150,blue,bright_blue,inst)
        button("Quit",500,500,200,150,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(15)
        
def game_loop():
    playsound.playsound("start play.mp3")
    x = (w * 0.5)-shin_width*0.5
    y = h-shin_height
    mixer.music.load("intro.mp3")
    mixer.music.play(-1)
    x_change = 0
    oppos = 10
    kamenw = 120
    kamenh = 200
    kamen_startx = random.randrange(0, w-kamenw)
    kamen_starty = 0-kamenh
    thingCount = 1
    score = 0
    drop=5
    gameExit = False

    while not gameExit:
        gameDisplay.blit(background,(0,0))
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                if event.key == pygame.K_RIGHT:
                    x_change = 10
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos=event.pos
                if Qbut.collidepoint(mouse_pos):
                    gameExit = False
                    os.system("phone.py")

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        things(kamen_startx, kamen_starty, kamenw, kamenh)
        kamen_starty += oppos
        shin(x,y)
        shin_score(score)
        dropcount(drop)

        if x+shin_width > w :
            x=0+shin_width

        if x < 0:
            x=w-shin_width

        if kamen_starty > h:
            kamen_starty = 0 - kamenh
            kamen_startx = random.randrange(0,w-kamenw)
            drop -= 1

        if y < kamen_starty+kamenh :
            if x > kamen_startx and x < kamen_startx + kamenw or x+shin_width > kamen_startx and x + shin_width < kamen_startx+kamenw:
                score+=1
                kamen_starty = 0 - kamenh
                kamen_startx = random.randrange(0,w-kamenw)
                mixer.Sound.play(catch)

        if drop==0:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos=event.pos
                    if EQbut.collidepoint(mouse_pos):
                        gameloop()
            droped()
        pygame.display.update()
        clock.tick(60)

menu()
game_loop()
pygame.quit()

quit()
