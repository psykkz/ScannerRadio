import time, os, subprocess
from tkinter import *

def clic(event):
    global f
    global f2
    global str_f
    global str_f2
    global mode
    global text_freq
    global text_freq2
    f3=-1
    f4=-1
    if 0 <event.y < 130 : L=1
    if 129 <event.y< 185 : L=2
    if 184 <event.y< 240 : L=3
    if 239 <event.y< 330 : L=4
    if 329 <event.y < 405 : L=5
    if 404 <event.y < 463 : L=6
    if 462 <event.y < 525 : L=7
    if 524 <event.y : L=8

    if 0 <event.x < 235 : C=1
    if 234 <event.x < 310 : C=2
    if 309 <event.x < 400 : C=3
    if 399 <event.x < 485 : C=4
    if 484 <event.x < 560 : C=5
    if 559 <event.x :C=6
                
    print('Ligne : '+str(L))
    print('Colonne : '+str(C))
    delta=0
    if C==1: delta=100
    if C==2: delta=10
    if C==3: delta=1
    if C==4: delta=-1
    if C==5: delta=-10
    if C==6: delta=-100
    if L==1: f3=f+delta
    if L==2: f3=f+delta*1000
    if L==3: f3=f+delta*1000000
    if L==4:
        print('Changement de mode')
        if C==1: mode='AM'
        if C==2: mode='FM'
        if C==3: mode='wbfm'
        if C==4: mode='lsb'
        if C==5: mode='usb'
        if C==6: mode='raw'
    if L==1 or L==2 or L==3 : delta=0
    if L==5:f4=f2+delta
    if L==6:f4=f2+delta*1000
    if L==7:f4=f2+delta*1000000
    if f3>0 : f=f3
    if f4>0 : f2=f4
    str_f=affiche_f(f)
    print(f)
    str_f2=affiche_f(f2)
    print(f2)
    canvas.delete(text_freq)
    canvas.delete(text_freq2)
    text_freq= canvas.create_text(485, 33, text=str_f, font=("Arial", "48"), fill="blue")
    text_freq2= canvas.create_text(445, 327, text=str_f2, font=("Helvetica", "48"), fill="blue")
    canvas.pack()
    ##
    ###affiche()
    ##
    kill=subprocess.Popen(["sudo pkill -f rtl_fm && sudo pkill -f aplay"], shell=True)
    kill.wait()
    print('Everybody dies')
    run=subprocess.Popen(["sudo rtl_fm -f "+str(f)+" -M "+mode+" -g 50 -r 48k -s "+str(f2)+"|sudo aplay -r 48k -f S16_LE -D plughw:1,0"], shell=True)
    run.wait()
    print('Everybody is back')

def affiche_f(valeur):
    nombre=[]
    for c in str(valeur):
        nombre.append(int(c))
    taille=len(nombre)
    for d in range(0,9):
        if taille<(9-d) : nombre.insert(0,0)
    variable=''
    variable=str(nombre[0])+str(nombre[1])+str(nombre[2])+' '+str(nombre[3])+str(nombre[4])+str(nombre[5])+' '+str(nombre[6])+str(nombre[7])+str(nombre[8])
    return variable
    

## Programme PRINCIPAL
#On définit les Variables
blanc='                                  '
L=0
C=0
f=102000000
f2=500000
mode='wbfm'
#On lance la premiere ecoute
str_f=affiche_f(f)
str_f2=affiche_f(f2)
run=subprocess.Popen(["sudo rtl_fm -f "+str(f)+" -M "+mode+" -g 50 -r 48k -s "+str(f2)+"|sudo aplay -r 48k -f S16_LE -D plughw:1,0"], shell=True)
run.wait()

#On place la fenetre et le canvas
fenetre = Tk()
fenetre.title("Scanner")
fond = PhotoImage(file='img/fond2.png')
canvas = Canvas(fenetre, width=800, height=600, background='red')
canvas.create_image(400,300, image=fond)
text_freq= canvas.create_text(485, 33, text=str_f, font=("Arial", "48"), fill="blue")
text_freq2= canvas.create_text(445, 327, text=str_f2, font=("Helvetica", "48"), fill="blue")

canvas.pack()
canvas.bind('<Button-1>', clic)
fenetre.mainloop()

