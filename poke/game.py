import pygame
import time

pygame.init()

moveset={

    "Charmander":{"SCRATCH":[5,1],"EMBER":[15,5],"INFERNO":[20,7],"SLASH":[10,3]},
    "Bulbasaur":{"TACKLE":[5,1],"RAZOR LEAF":[10,3],"FRENZYPLANT":[20,7],"TAKE DOWN":[15,5]},
    "Squirtle":{"TACKLE":[5,1],"HYDROCANNON":[20,7],"BUBBLE BEAM":[15,5],"HEADBUTT":[10,3]},
    "Pikachu":{"THUNDERSHOCK":[5,1],"SLAM":[10,3],"THUNDERBOLT":[15,5],"THUNDER":[20,7]}

}

def pokemake(a,x,y):
    
    im=pygame.image.load(a)
    im=pygame.transform.scale(im,(x,y))
    return im

p1mv={}
p2mv={}
p1m=[]
p1mc=[]
p2m=[]
p2mc=[]

hp1=80
pp1=50
hp2=80
pp2=50

attack=""
win=""
running=1
inforect=0
msgRect=0
w,h=(1366,768)
bg_color=(255,255,255)
image=pygame.image.load('logo.jpg')
ball=pokemake('Pokeball.PNG',30,30)
point=pokemake('finger.png',30,30)
charm=pokemake('charmander.png',200,200)
bulb=pokemake('bulbasaur.jpg',240,200)
squi=pokemake('squirtle.png',200,200)
pika=pokemake('pikachu.png',200,200)
chab=pokemake('char1.png',200,200)
chaf=pokemake('char2.png',200,200)
bulbb=pokemake('bulb1.png',240,200)
bulbf=pokemake('bulb2.png',240,200)
squib=pokemake('squi1.png',200,200)
squif=pokemake('squi2.png',180,200)
pikab=pokemake('pika1.png',180,200)
pikaf=pokemake('pika2.png',200,200)
bgm='bgm.ogg'
vic='victory.ogg'
bat='battle.ogg'
bgi=pokemake('bg.png',1366,768)
rectn=pokemake('rect.png',1050,260)
selc=pokemake('ptr.png',40,40)
bgw=pokemake('winner.png',1366,768)

pygame.mixer.init()
    

def set_text(string,_font,_size,x,y,color,textRect,fill):
    global w,h,bg_color
	
    font = pygame.font.Font(_font, _size)
    text = font.render(string, True, color, (256,256,256))
    textRect = text.get_rect()
    textRect.center = (x,y)
    if(fill==1):
        screen.fill(bg_color)
    screen.blit(text,textRect)
    

def homescreen():
    global w,h,bg_color,image,bgm
    alive=1
    pygame.mixer.music.load(bgm)    

    pygame.mixer.music.play() 
    while(alive):
   

            
            welcRect=0
            set_text('Press Enter to Continue','pf.ttf',20,w/2,h/2+200,(100,100,0),welcRect,1)    

            screen.blit(image,(w/4,h/4-250))
            pygame.display.update()

        
        
            for event in pygame.event.get():
                if(event.type == pygame.KEYDOWN):
                    if event.key == pygame.K_RETURN:
                        alive=0
                elif(event.type == pygame.QUIT):
                    pygame.quit()
                    quit() 
        
    pygame.mixer.music.stop()

def select_cons(player):
    
    global ball,point
    msgRect=0
    set_text('Choose your Pokemon, '+player,'df.ttf',30,w/2,100,(20,20,20),msgRect,1)
    screen.blit(ball,(300,250))
    screen.blit(ball,(300,300))
    screen.blit(ball,(300,350))
    screen.blit(ball,(300,400))

def show_poke(image,name,desc):
    
    screen.blit(image,(800,250))
    
    
    tRect1,tRect2=0,0
    set_text(name,'df.ttf',35,880,500,(20,20,20),tRect1,0)
    set_text(desc,'df.ttf',35,880,550,(20,20,20),tRect1,0)


def select(player):  
    
    ptr=250

    alive=1
    while(alive):
            
        select_cons(player)
        screen.blit(point,(250,ptr))
        
        if(ptr==250):
            desc="The flame that burns at the tip of its tail is an indication of its emotions."
            show_poke(charm,'Charmander',desc)
        elif(ptr==300):
            desc="By soaking up the sun\'s rays, the seed grows progressively larger."
            show_poke(bulb,'Bulbasaur',desc)
        elif(ptr==350):
            desc="Squirtle's shell is not merely used for protection."
            show_poke(squi,'Squirtle',desc)
        elif(ptr==400):
            desc="Whenever Pikachu comes across something new, it blasts it with a jolt of electricity."
            show_poke(pika,'Pikachu',desc)        
        

        pygame.display.update()
        for event in pygame.event.get():
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_UP):
                    ptr-=50
                    if(ptr<250):
                        ptr=250              
                elif(event.key == pygame.K_DOWN):
                    ptr+=50
                    if(ptr>400):
                        ptr=400
                elif(event.key == pygame.K_RETURN):
                    alive=0
                else:
                    pass

            elif(event.type == pygame.QUIT):
                pygame.quit()
                quit()

    print(ptr)
                
    if(ptr==250):
        return ("Charmander",(255,165,0))     
    elif(ptr==300):
        return ("Bulbasaur",(0,230,0))
    elif(ptr==350):
        return ("Squirtle",(173,216,230))
    elif(ptr==400): 
        return ("Pikachu",(255,255,0))
    

def draw(poke1,poke2,turn):
    
    m1rect,m2rect,m3rect,m4rect=0,0,0,0
    global moveset,rectn,p1m,p1mc,p2m,p2mc,p1mv,p2mv,running,win
    black=(250,250,250)

    screen.blit(rectn,(350,500))

    if(poke1=="Charmander"):
        p1back=chab
        p1front=chaf
    elif(poke1=="Bulbasaur"):
        p1back=bulbb
        p1front=bulbf
    elif(poke1=="Squirtle"):
        p1back=squib
        p1front=squif
    elif(poke1=="Pikachu"):
        p1back=pikab    
        p1front=pikaf
    
    p1mv=moveset.get(poke1)
    p1m=list(p1mv.keys())
    p1mc=[]
    for i in range(len(p1m)):
        cost=p1mv.get(p1m[i])
        p1mc.append(cost)

    if(poke2=="Charmander"):
        p2back=chab
        p2front=chaf
    elif(poke2=="Bulbasaur"):
        p2back=bulbb
        p2front=bulbf
    elif(poke2=="Squirtle"):
        p2back=squib
        p2front=squif
    elif(poke2=="Pikachu"):
        p2back=pikab    
        p2front=pikaf
    
    p2mv=moveset.get(poke2) 
    p2m=list(p2mv.keys())
    p2mc=[]
    for i in range(len(p2m)):
        cost=p2mv.get(p2m[i])
        p2mc.append(cost)

    if(turn%2==0):
        screen.blit(p2front,(1020,200))
        screen.blit(p1back,(150,350))
        set_text(p1m[0]+" "+str(p1mc[0]),'nf.ttf',20,700,570,black,m1rect,0)
        set_text(p1m[1]+" "+str(p1mc[1]),'nf.ttf',20,1100,570,black,m1rect,0)
        set_text(p1m[2]+" "+str(p1mc[2]),'nf.ttf',20,700,670,black,m1rect,0)
        set_text(p1m[3]+" "+str(p1mc[3]),'nf.ttf',20,1100,670,black,m1rect,0)

        
    else:  
        screen.blit(p2back,(150,350))
        screen.blit(p1front,(1020,200))
        set_text(p2m[0]+" "+str(p2mc[0]),'nf.ttf',20,700,570,black,m1rect,0)
        set_text(p2m[1]+" "+str(p2mc[1]),'nf.ttf',20,1100,570,black,m1rect,0)
        set_text(p2m[2]+" "+str(p2mc[2]),'nf.ttf',20,700,670,black,m1rect,0)
        set_text(p2m[3]+" "+str(p2mc[3]),'nf.ttf',20,1100,670,black,m1rect,0)    


def use_attack(move,turn):

    global p1mv,p2mv,hp1,hp2,pp1,pp2,running,win,poke1,poke2,attack

    if(turn%2==0):
        stat=p1mv.get(move)
        if(pp1-stat[1]<0):
            attack="No PP left for this move. \'S\' to struggle"
            turn-=1  
        else:
            hp2-=stat[0]
            pp1-=stat[1]
            attack=poke1+" used "+move
            if(hp2<=0):
                running=0
                win=poke1
    else:
        stat=p2mv.get(move)
        if(pp2-stat[1]<0):
            attack="No PP left for this move. \'S\' to struggle"
            turn-=1   
        else:
            hp1-=stat[0]
            pp2-=stat[1]
            attack=poke2+" used "+move
            if(hp1<=0):
                running=0
                win=poke1
              
    return turn


def game(poke1,poke2,turn):
        
    global bg_color,rectn,attack,inforect,hp1,hp2,pp1,pp2
    black=(250,250,250)

    hprect1,pprect1=0,0
    hprect2,pprect2=0,0    

    prx=450
    pry=550

    struggle=0
    alive=1
    while(alive):

        screen.fill(bg_color)
        
        screen.blit(bgi,(0,0))

        draw(poke1,poke2,turn)
 
        screen.blit(selc,(prx,pry))
    
        if(turn%2==0):
            set_text('HP: '+str(hp1),'nf.ttf',20,130,660,black,hprect1,0)
            set_text('PP: '+str(pp1),'nf.ttf',20,130,690,black,hprect1,0)
            set_text('HP: '+str(hp2),'nf.ttf',20,1220,70,black,hprect1,0)
            set_text('PP: '+str(pp2),'nf.ttf',20,1220,100,black,hprect1,0)
        else:
            set_text('HP: '+str(hp1),'nf.ttf',20,1220,70,black,hprect1,0)
            set_text('PP: '+str(pp1),'nf.ttf',20,1220,100,black,hprect1,0)
            set_text('HP: '+str(hp2),'nf.ttf',20,130,660,black,hprect1,0)
            set_text('PP: '+str(pp2),'nf.ttf',20,130,690,black,hprect1,0)
    
        set_text(attack,'nf.ttf',15,400,100,black,inforect,0)
   
        pygame.display.update()

        for event in pygame.event.get():
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_RETURN):
                    alive=0
                elif(event.key == pygame.K_DOWN):
                    pry+=100
                    if(pry>650):
                        pry=650
                elif(event.key == pygame.K_UP):
                    pry-=100
                    if(pry<550):
                        pry=550
                elif(event.key == pygame.K_LEFT):
                    prx-=450
                    if(prx<450):      
                        prx=450
                elif(event.key == pygame.K_RIGHT):
                    prx+=450
                    if(prx>900):
                        prx=900
                elif(event.key == pygame.K_s):
                    alive=0
                    struggle=1                
    

            elif(event.type == pygame.QUIT):
                pygame.quit()
                quit()    
                
    if(turn%2==0):
        if(struggle==0):
            if((prx,pry)==(450,550)):
                turn=use_attack(p1m[0],turn)
            elif((prx,pry)==(900,550)):
                turn=use_attack(p1m[1],turn)
            elif((prx,pry)==(450,650)):
                turn=use_attack(p1m[2],turn)
            elif((prx,pry)==(900,650)):
                turn=use_attack(p1m[3],turn)
        else:
            hp2-=1
            attack=poke1+" struggled"    
    else:
        if(struggle==0):        
            if((prx,pry)==(450,550)):
                turn=use_attack(p2m[0],turn)
            elif((prx,pry)==(900,550)):
                turn=use_attack(p2m[1],turn)
            elif((prx,pry)==(450,650)):
                turn=use_attack(p2m[2],turn)
            elif((prx,pry)==(900,650)):
                turn=use_attack(p2m[3],turn)             
        else:
            hp1-=1
            attack=poke2+" struggled"  


    
    return turn
    

def winner(win):
    global bgw,w,h,chaf,bulbf,squif,pikaf
    
    winrect=0    
    
    pygame.mixer.music.load(vic)
    pygame.mixer.music.play()

    screen.blit(bgw,(0,0))
    
    if(win == "Charmander"):
        wset = chaf
    elif(win == "Bulbasaur"):
        wset = bulbf
    elif(win == "Squirtle"):
        wset = squif
    elif(win == "Pikachu"):
        wset = pikaf

    screen.blit(wset,(600,300))   
    set_text(win+" is the Winner!",'pf.ttf',30,w/2,600,(255,255,255),winrect,0)
    
    pygame.display.update()    
    
    alive=1
    while(alive):
        for event in pygame.event.get():
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_RETURN):
                    alive=0
            
            elif(event.type == pygame.QUIT):
                pygame.quit()
                quit()   

    pygame.mixer.music.stop()

screen = pygame.display.set_mode((w,h))
pygame.display.set_caption('Poke\'mon')


homescreen()

poke1,col=select('Player 1')
set_text('Player 1 selected '+poke1,'pf.ttf',30,w/2,h/2,col,msgRect,1)
pygame.display.update()
time.sleep(2)
    
poke2,col=select('Player 2')
set_text('Player 2 selected '+poke2,'pf.ttf',30,w/2,h/2,col,msgRect,1)
pygame.display.update()
time.sleep(2)

turn=0
    
pygame.mixer.music.load(bat)
pygame.mixer.music.play()
    
while(running):
    turn=game(poke1,poke2,turn)
    turn+=1

pygame.mixer.music.stop()

winner(win)
time.sleep(4)
