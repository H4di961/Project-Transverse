from pygame import*
from math import*
from random import*
from pygame import mixer
init() 
fenetre = display.set_mode((600,600), RESIZABLE)

#musique

music_fond=mixer.Sound("Megalovania.mp3")
music_fond.set_volume(2.0)
music_fond.play(-1)

explosion_bombe= mixer.Sound("mixkit-8-bit-bomb-explosion-2811.wav")
explosion_bombe.set_volume(0.2)


fond = image.load("bomberman_background.png").convert()
boots=image.load("boots.png").convert_alpha() #5 dans la matrice
for x in range (boots.get_size()[0]):
    for y in range (boots.get_size()[1]):
        (r,v,b,t)=boots.get_at((x,y))
        if r+b+v>700:
            boots.set_at((x,y),(r,v,b,0))
a1=image.load("a1.png").convert_alpha() #5 dans la matrice
for x in range (a1.get_size()[0]):
    for y in range (a1.get_size()[1]):
        (r,v,b,t)=a1.get_at((x,y))
        if r+b+v>700:
            a1.set_at((x,y),(r,v,b,0))
a2=image.load("a2.png").convert_alpha() #5 dans la matrice
for x in range (a2.get_size()[0]):
    for y in range (a2.get_size()[1]):
        (r,v,b,t)=a2.get_at((x,y))
        if r+b+v>700:
            a2.set_at((x,y),(r,v,b,0))
a3=image.load("a3.png").convert_alpha() #5 dans la matrice
for x in range (a3.get_size()[0]):
    for y in range (a3.get_size()[1]):
        (r,v,b,t)=a3.get_at((x,y))
        if r+b+v>700:
            a3.set_at((x,y),(r,v,b,0))
a4=image.load("a4.png").convert_alpha() #5 dans la matrice
for x in range (a4.get_size()[0]):
    for y in range (a4.get_size()[1]):
        (r,v,b,t)=a4.get_at((x,y))
        if r+b+v>700:
            a4.set_at((x,y),(r,v,b,0))
a5=image.load("a5.png").convert_alpha() #5 dans la matrice
for x in range (a5.get_size()[0]):
    for y in range (a5.get_size()[1]):
        (r,v,b,t)=a5.get_at((x,y))
        if r+b+v>700:
            a5.set_at((x,y),(r,v,b,0))
perso1=image.load("perso1.png").convert_alpha()
for x in range (perso1.get_size()[0]):
    for y in range (perso1.get_size()[1]):
        (r,v,b,t)=perso1.get_at((x,y))
        if r+b+v>700:
            perso1.set_at((x,y),(r,v,b,0))
perso2=image.load("perso2.png").convert_alpha()
for x in range (perso2.get_size()[0]):
    for y in range (perso2.get_size()[1]):
        (r,v,b,t)=perso2.get_at((x,y))
        if r+b+v>700:
            perso2.set_at((x,y),(r,v,b,0))
block=image.load("block.png").convert()  # 2 dans la matrice
bombe=image.load("bombe.png").convert_alpha()#3 dans la matrice
for x in range (bombe.get_size()[0]):
    for y in range (bombe.get_size()[1]):
        (r,v,b,t)=bombe.get_at((x,y))
        if r+b+v>700:
            bombe.set_at((x,y),(r,v,b,0))
flamme=image.load("flame1.png").convert_alpha()
for x in range (flamme.get_size()[0]):
    for y in range (flamme.get_size()[1]):
        (r,v,b,t)=flamme.get_at((x,y))
        if r+b+v>760:
            flamme.set_at((x,y),(r,v,b,0))# 4 dans la matrice
liste_im=[block,bombe,flamme,boots]
fin1=image.load("ecrandefin.png").convert()
fin2=image.load("ecrandefin1.png").convert()
lafin=[fin2,fin1]


#matrice
matrice=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
         [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
         [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
         [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
         [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
         [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
         [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

#apparition au hasard des blocs:
for l in range(len(matrice)):
    for c in range(len(matrice[0])):
        if l+c>=4 and l+c<=24:
            if matrice[l][c]==0:
                if randint(1,10)>=6:
                    matrice[l][c]=2
                    

xp=80
yp=40
xp2=520
yp2=520
collision=1
continuer=0
liste_bombes=[]
liste_f=[]
vie1=1
vie2=1
fin=1
anim=[a1,a2,a3,a4,a5]
chance_b_f=3
vitesse1=1
vitesse2=1

while True:
    time.Clock().tick(230)
    for evenements in event.get(): 
        if evenements.type == QUIT: quit()
        
# affichages
    fenetre.blit(fond,(0,0))
    
    fenetre.blit(perso1,(xp,yp))
    fenetre.blit(perso2,(xp2,yp2)) # affichage des elements 
    for ligne in range(13):
        for col in range(13):
            if matrice[1+ligne][1+col] >=2:
                fenetre.blit(liste_im[int(matrice[1+ligne][1+col])-2],(col*40+40,ligne*40+40)) # apparition des differents blocs
    display.flip()
 
            

#attaque:

    keyb=key.get_pressed()
    if keyb[K_e]:
        matrice[int((yp2+20)//40)][int((xp2+20)//40)]=3.5 #bombe invisible
        liste_bombes.append([int((xp2+20)//40),int((yp2+20)//40),300]) # gestion d'une bombe
    if keyb[K_RSHIFT]:
        matrice[int((yp+20)//40)][int((xp+20)//40)]=3.5
        liste_bombes.append([int((xp+20)//40),int((yp+20))//40,300])
   
# gestion des bombes
    for bombes in liste_bombes:
        bombes[2]-=1 #gestion vie bombe
        if bombes[2]==150:matrice[bombes[1]][bombes[0]]=3 #vraie bombe
        if bombes[2]==0: #fin de vie 
            matrice[bombes[1]][bombes[0]]=0
            liste_bombes.remove(bombes)
            matrice[bombes[1]][bombes[0]]=4 #flamme
            feu=[59,(bombes[0],bombes[1],0)] # gestion de flamme
            for i in range (1,3):
                if matrice[bombes[1]-i][bombes[0]]==2:
                    matrice[bombes[1]-i][bombes[0]]=4
                    feu.append((bombes[0],bombes[1]-i,int(randint(1,chance_b_f)==1)))
                    explosion_bombe.play()
                    
                    break
                elif matrice[bombes[1]-i][bombes[0]]==0: 
                    matrice[bombes[1]-i][bombes[0]]=4
                    feu.append((bombes[0],bombes[1]-i,0))
                    explosion_bombe.play()
                elif matrice[bombes[1]-i][bombes[0]]in[3,3.5]: #declenchement des bombes si touchees 
                    for bombe2 in liste_bombes:
                        if bombe2[0]==bombes[0] and bombes[1]-i==bombe2[1]:
                            bombe2[2]=1
                            explosion_bombe.play()
                            break
                elif matrice[bombes[1]+i][bombes[0]]in[3,3.5]: #declenchement des bombes si touchees 
                    for bombe2 in liste_bombes:
                        if bombe2[0]==bombes[0] and bombes[1]+i==bombe2[1]:
                            bombe2[2]=1
                            explosion_bombe.play()
                            break
                elif matrice[bombes[1]][bombes[0]-i]in[3,3.5]: #declenchement des bombes si touchees 
                    for bombe2 in liste_bombes:
                        if [bombe2[0]-i]==bombes[0] and bombes[1]==bombe2[1]:
                            bombe2[2]=1
                            explosion_bombe.play()
                            break
                elif matrice[bombes[1]][bombes[0]+i]in[3,3.5]: #declenchement des bombes si touchees 
                    for bombe2 in liste_bombes:
                        if [bombe2[0]+i]==bombes[0] and bombes[1]==bombe2[1]:
                            bombe2[2]=1
                            explosion_bombe.play()
                            break
                else : break
                
            for i in range (1,3):
                if matrice[bombes[1]+i][bombes[0]]==2: 
                    matrice[bombes[1]+i][bombes[0]]=4
                    feu.append((bombes[0],bombes[1]+i,int(randint(1,chance_b_f)==1)))
                    explosion_bombe.play()
                    break
                if matrice[bombes[1]+i][bombes[0]]==0: 
                    matrice[bombes[1]+i][bombes[0]]=4
                    feu.append((bombes[0],bombes[1]+i,0))
                    explosion_bombe.play()
                else : break
            for i in range (1,3):
                if matrice[bombes[1]][bombes[0]+i]==2: 
                    matrice[bombes[1]][bombes[0]+i]=4
                    feu.append((bombes[0]+i,bombes[1],int(randint(1,chance_b_f)==1)))
                    explosion_bombe.play()
                    break
                if matrice[bombes[1]][bombes[0]+i]==0: 
                    matrice[bombes[1]][bombes[0]+i]=4
                    feu.append((bombes[0]+i,bombes[1],0))
                    explosion_bombe.play()
                else : break
            for i in range (1,3):
                if matrice[bombes[1]][bombes[0]-i]==2: 
                    matrice[bombes[1]][bombes[0]-i]=4
                    feu.append((bombes[0]-i,bombes[1],int(randint(1,chance_b_f)==1)))
                    explosion_bombe.play()
                    break
                if matrice[bombes[1]][bombes[0]-i]==0: 
                    matrice[bombes[1]][bombes[0]-i]=4
                    feu.append((bombes[0]-i,bombes[1],0))
                    explosion_bombe.play()
                else : break
            liste_f.append(feu)
            
#gestion des bonus
    if matrice[int((yp+20)//40)][int((xp+20)//40)]==5:
        vitesse1*=1.25
        matrice[int((yp+20)//40)][int((xp+20)//40)]=0
    if matrice[int((yp2+20)//40)][int((xp2+20)//40)]==5:
        vitesse2*=1.25
        matrice[int((yp2+20)//40)][int((xp2+20)//40)]=0
#            
#gestion des flammes          
    for feu in liste_f: 
        feu[0]-=1 #gestion vie 
        if feu[0]==0:
            for couple in feu[1:]:
                matrice[couple[1]][couple[0]]=couple[2]*5
            liste_f.remove(feu)
                    
#gestion de la vie:
    if matrice[int((yp+20)//40)][int((xp+20)//40)]==4:#si le feu est touche
        vie1-=1
    if matrice[int((yp2+20)//40)][int((xp2+20)//40)]==4:
        vie2-=1

    if vie1<1:   
        fin=0 #fin du jeu 
    if vie2<1:
        
        fin=-1

    
    
#delacement:
    
    
        #perso 1
    keyb=key.get_pressed()
    if keyb[K_UP]:
        if matrice [int((yp+0)//40)][int((xp+20)//40)]in [0,3.5,5]:
            yp-=vitesse1
            if xp%40<=20 and xp%40!=0:xp-=1
            if xp%40>20 and xp%40!=0:xp+=1
    if keyb[K_DOWN]:
        if matrice [int((yp+40)//40)][int((xp+20)//40)]in [0,3.5,5]:
            yp+=vitesse1
            if xp%40<=20 and xp%40!=0:xp-=1
            if xp%40>20 and xp%40!=0:xp+=1
    if keyb[K_LEFT]:
        if matrice[int((yp+20)//40)][int((xp+0)//40)]in [0,3.5,5]:
            xp-=vitesse1
            if yp%40<=20 and yp%40!=0:yp-=1
            if yp%40>20 and yp%40!=0:yp+=1
    if keyb[K_RIGHT]:
        if matrice[int((yp+20)//40)][int((xp+40)//40)]in [0,3.5,5]:
            xp+=vitesse1
            if yp%40<=20 and yp%40!=0:yp-=1
            if yp%40>20 and yp%40!=0:yp+=1
            
            #perso 2
    keyb=key.get_pressed()
    if keyb[K_z]:
        if matrice [int((yp2+0)//40)][int((xp2+20)//40)]in [0,3.5,5]:
            yp2-=vitesse2
            if xp2%40<=20 and xp2%40!=0:xp2-=1
            if xp2%40>20 and xp2%40!=0:xp2+=1
    if keyb[K_s]:
        if matrice [int((yp2+40)//40)][int((xp2+20)//40)]in [0,3.5,5]:
            yp2+=vitesse2
            if xp2%40<=20 and xp2%40!=0:xp2-=1
            if xp2%40>20 and xp2%40!=0:xp2+=1
    if keyb[K_d]:
        if matrice[int((yp2+20))//40][int((xp2+40)//40)]in [0,3.5,5]:
            xp2+=vitesse2
            if yp2%40<=20 and yp2%40!=0:yp2-=1
            if yp2%40>20 and yp2%40!=0:yp2+=1
    if keyb[K_q]:
        if matrice[int((yp2+20)//40)][int((xp2+0)//40)]in [0,3.5,5]:
            xp2-=vitesse2
            if yp2%40<=20 and yp2%40!=0:yp2-=1
            if yp2%40>20 and yp2%40!=0:yp2+=1
            
    if vie1<1:vie1-=1
    if vie2<1:vie2-=1 
    if vie1<=-30 or vie2<=-30:
        if vie1<=0:
            for i in range(5):
                fenetre.blit(anim[i],(xp,yp))
                display.flip()
                time.wait(100)
        if vie2<=0:
            for i in range(5):
                fenetre.blit(anim[i],(xp2,yp2))
                display.flip()
                time.wait(100)
    
        
        while True : #affichage et reinitialisation du jeu
            
            fenetre.blit(lafin[-fin],(0,0))
            display.flip()
            for evenements in event.get(): pass
            keyb=key.get_pressed()
            if keyb[K_SPACE]:
                matrice=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                         [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
                         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                         [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
                         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                         [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
                         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                         [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
                         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                         [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
                         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                         [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
                         [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
                xp=80
                yp=40
                xp2=520
                yp2=520
                collision=1
                continuer=0
                liste_bombes=[]
                liste_f=[]
                vie1=1
                vie2=1
                fin=1
                anim=[a1,a2,a3,a4,a5]
                chance_b_f=3
                vitesse1=1
                vitesse2=1
                for l in range(len(matrice)):
                    for c in range(len(matrice[0])):
                        if l+c>=4 and l+c<=24:
                            if matrice[l][c]==0:
                                if randint(1,10)>=6:
                                    matrice[l][c]=2
                    
                break


 
