import pygame, time, os, subprocess
from pygame.locals import *
pygame.init()

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=1024)
Text30 = pygame.font.Font('img/chintzy.ttf', 30)
Text50 = pygame.font.Font('img/chintzy.ttf', 50)

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
    
def affiche():
    fenetre.blit(fond, (0,0))

    #Boutons pour la variation des Hertz
    fenetre.blit(Plus1, (325,80))
    fenetre.blit(Plus10, (250,80))
    fenetre.blit(Plus100, (175,80))
    fenetre.blit(Moins1, (425,80))
    fenetre.blit(Moins10, (500,80))
    fenetre.blit(Moins100, (575,80))
    #Boutons pour la variation des kiloHertz
    fenetre.blit(Plus1, (325,135))
    fenetre.blit(Plus10, (250,135))
    fenetre.blit(Plus100, (175,135))
    fenetre.blit(Moins1, (425,135))
    fenetre.blit(Moins10, (500,135))
    fenetre.blit(Moins100, (575,135))
    #Boutons pour la variation des MegaHertz
    fenetre.blit(Plus1, (325,190))
    fenetre.blit(Plus10, (250,190))
    fenetre.blit(Plus100, (175,190))
    fenetre.blit(Moins1, (425,190))
    fenetre.blit(Moins1, (425,190))
    fenetre.blit(Moins10, (500,190))
    fenetre.blit(Moins100, (575,190))
    #Boutons Modes
    fenetre.blit(AM, (175,245))
    fenetre.blit(FM, (250,245))
    fenetre.blit(wFM, (325,245))
    fenetre.blit(LSB, (425,245))
    fenetre.blit(USB, (500,245))
    fenetre.blit(RAW, (575,245))
    #Boutons Prédefinis
    fenetre.blit(CB, (100,540))
    fenetre.blit(Avion, (250,540))
    fenetre.blit(Talkie, (400,540))
    fenetre.blit(Predef, (550,540))
    ##POUR LA QUALITE D'ECOUTE
    #Boutons pour la variation des Hertz
    fenetre.blit(Plus1, (325,355))
    fenetre.blit(Plus10, (250,355))
    fenetre.blit(Plus100, (175,355))
    fenetre.blit(Moins1, (425,355))
    fenetre.blit(Moins10, (500,355))
    fenetre.blit(Moins100, (575,355))
    #Boutons pour la variation des kiloHertz
    fenetre.blit(Plus1, (325,410))
    fenetre.blit(Plus10, (250,410))
    fenetre.blit(Plus100, (175,410))
    fenetre.blit(Moins1, (425,410))
    fenetre.blit(Moins10, (500,410))
    fenetre.blit(Moins100, (575,410))
    #Boutons pour la variation des MegaHertz
    fenetre.blit(Plus1, (325,465))
    fenetre.blit(Plus10, (250,465))
    fenetre.blit(Plus100, (175,465))
    fenetre.blit(Moins1, (425,465))
    fenetre.blit(Moins10, (500,465))
    fenetre.blit(Moins100, (575,465))





#Programme principal

#Limitation de vitesse de la boucle
#30 frames par secondes suffisent
pygame.time.Clock().tick(30)

##Definition des boutons et images
fenetre = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Frequence')
fond=pygame.image.load("img/fond.png").convert_alpha()
Plus1 = pygame.image.load("img/+1.png").convert_alpha()
Plus10 = pygame.image.load("img/+10.png").convert_alpha()
Plus100= pygame.image.load("img/+100.png").convert_alpha()
Moins1= pygame.image.load("img/-1.png").convert_alpha()
Moins10= pygame.image.load("img/-10.png").convert_alpha()
Moins100= pygame.image.load("img/-100.png").convert_alpha()
CB=pygame.image.load("img/CB.png").convert_alpha()
Avion=pygame.image.load("img/Avion.png").convert_alpha()
Talkie=pygame.image.load("img/Talkie.png").convert_alpha()
Predef=pygame.image.load("img/Predef.png").convert_alpha()
AM=pygame.image.load("img/AM.png").convert_alpha()
FM=pygame.image.load("img/FM.png").convert_alpha()
wFM=pygame.image.load("img/wFM.png").convert_alpha()
LSB=pygame.image.load("img/LSB.png").convert_alpha()
USB=pygame.image.load("img/USB.png").convert_alpha()
RAW=pygame.image.load("img/RAW.png").convert_alpha()


affiche()

#Variables 
i=0
continuer = 1
L=0
C=0
f=88000000
f2=190000
mode='wbfm'
str_f=affiche_f(f)
str_f2=affiche_f(f2)
run=subprocess.Popen(["sudo rtl_fm -f "+str(f)+" -M "+mode+" -g 50 -r 48k -s "+str(f2)+"|sudo aplay -r 48k -f S16_LE -D plughw:1,0"], shell=True)
print('On lance la fréquence '+str(f)+' Hz')
print("sudo rtl_fm -f "+str(f)+" -M "+mode+" -g 50 -r 48k -s "+str(f2)+"|sudo aplay -r 48k -f S16_LE -D plughw:1,0")
run.wait()
#Boucle infinie
while continuer:
    
    #Affichage des caracteres des frequences
    text_freq= Text50.render(str_f, 0, (255,255,255))
    text_freq2= Text50.render(str_f2, 0, (255,255,255))
    fenetre.blit(text_freq, (300,10))
    fenetre.blit(text_freq2, (275,300))
    
    for event in pygame.event.get():
        
        if event.type == QUIT:
            continuer = 0

        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            #Separation suivant x
            if 0 <event.pos[1] < 130 :
                L=1
            if 129 <event.pos[1] < 185 :
                L=2
            if 184 <event.pos[1] < 240 :
                L=3
            if 239 <event.pos[1] < 330 :
                L=4
            if 329 <event.pos[1] < 405 :
                L=5
            if 404 <event.pos[1] < 463 :
                L=6
            if 462 <event.pos[1] < 525 :
                L=7
            if 524 <event.pos[1] :
                L=8


            if 0 <event.pos[0] < 235 :
                C=1
            if 234 <event.pos[0] < 310 :
                C=2
            if 309 <event.pos[0] < 400 :
                C=3
            if 399 <event.pos[0] < 485 :
                C=4
            if 484 <event.pos[0] < 560 :
                C=5
            if 559 <event.pos[0] :
                C=6
                
            print('Ligne : '+str(L))
            print('Colonne : '+str(C))
            delta=0
            if C==1: delta=100
            if C==2: delta=10
            if C==3: delta=1
            if C==4: delta=-1
            if C==5: delta=-10
            if C==6: delta=-100
            if L==1: f=f+delta
            if L==2:f=f+delta*1000
            if L==3:f=f+delta*1000000
            if L==4:
                print('Changement de mode')
                if C==1: mode='AM'
                if C==2: mode='FM'
                if C==3: mode='wbfm'
                if C==4: mode='lsb'
                if C==5: mode='usb'
                if C==6: mode='raw'
            if L==1 or L==2 or L==3 : delta=0
            if L==5:f2=f2+delta
            if L==6:f2=f2+delta*1000
            if L==7:f2=f2+delta*1000000
            str_f=affiche_f(f)
            str_f2=affiche_f(f2)
            affiche()
            kill=subprocess.Popen(["sudo pkill -f rtl_fm && sudo pkill -f aplay"], shell=True)
            kill.wait()
            print('Everybody dies')
            run=subprocess.Popen(["sudo rtl_fm -f "+str(f)+" -M "+mode+" -g 50 -r 48k -s "+str(f2)+"|sudo aplay -r 48k -f S16_LE -D plughw:1,0"], shell=True)
            run.wait()
            print('Everybody is back')
#sudo pkill -f rtl_fm
#sudo pkill -f aplay
#sudo rtl_fm -f %frequence -M %mode -g 50 -r 48k -s %freq2|sudo aplay -r 48k -f S16_LE -D plughw:1,0
#os.popen(" ")
    pygame.display.flip()

