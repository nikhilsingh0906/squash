import pygame,time,random

pygame.mixer.pre_init(44100,16,2,4096)

pygame.init()
display=pygame.display.set_mode((441,600))
pygame.display.set_caption('squash')
clock=pygame.time.Clock()

pygame.mixer.music.load("Dame2.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

display_w=441
display_h=600

#ball_vel_min=2
#ball_vel_max=10

linel=pygame.draw.line(display,(0,0,0),(0,0),(441,600),1)

rt1=pygame.image.load('racket 1.jpg').convert()
rt2=pygame.image.load('racket 2.jpg').convert()
img=pygame.image.load('Squash.jpg').convert()
ball=pygame.image.load('ball1.png').convert()



def Ball(ball_x,ball_y):
    display.blit(ball,(ball_x,ball_y))

def back(x,y):                                                  #back image
    display.blit(img,(x,y))
def racket1(xr1,yr1):                                           #racket
    display.blit(rt1,(xr1,yr1))
def racket2(xr2,yr2):
    display.blit(rt2,(xr2,yr2))

def things_P1(count):                                            #scorecard
    font=pygame.font.Font(None,70)
    text=font.render("P1:"+str(count),True,(0,0,0))
    display.blit(text,(0,0))
def things_P2(count):                                            #scorecard
    font=pygame.font.Font(None,70)
    text=font.render("P2:"+str(count),True,(0,0,0))
    display.blit(text,(display_w-130,0))

x=0
y=0
xr1=display_w-139
yr1=display_h-50
xr1_change=0
yr1_change=0
xr2=35
yr2=display_h-50
xr2_change=0
yr2_change=0

P1 = 0                      #score
P2 = 0

ball_x = 35 #random.randrange(0, display_w)
ball_y = 50
ball_xspeed =1
ball_yspeed =1

stop=False
while not stop:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            stop=True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xr1_change = -5
            elif event.key == pygame.K_RIGHT:
                xr1_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xr1_change = 0


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                yr1_change = -5
            elif event.key == pygame.K_DOWN:
                yr1_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                yr1_change = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                xr2_change = -5
            elif event.key == pygame.K_d:
                xr2_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                xr2_change = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                yr2_change = -5
            elif event.key == pygame.K_s:
                yr2_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                yr2_change = 0

    xr1 += xr1_change
    yr1 += yr1_change
    xr2 += xr2_change
    yr2 += yr2_change

    display.blit(img,(0,0))
    back(x,y)
    linel = pygame.draw.line(display, (0, 0, 0), (35, 0), (0, 600), 1)
    liner = pygame.draw.line(display, (0, 0, 0), (441-39, 0), (441, 600), 1)
    linet = pygame.draw.line(display, (0, 0, 0), (35, 50), (441-39, 50), 1)
    racket1(xr1,yr1)
    racket2(xr2,yr2)

    Ball(ball_x,ball_y)                        #ball motion
    ball_x +=ball_xspeed
    ball_y +=ball_yspeed

    things_P1(P1)                              #scorecard call
    things_P2(P2)

    if xr1 > 441-100:                          #racket1 strict
        xr1_change= -1
    if xr1 < 0:
        xr1_change= +1

    if yr1 > display_h-34:
        yr1_change= -1
    if yr1 < 50:
        yr1_change= +1

    if xr2 > display_w - 100:                   #racket2 strict
        xr2_change = -1
    if xr2 <0:
        xr2_change = +1

    if yr2 > display_h - 31:
        yr2_change = -1
    if yr2 < 50:
        yr2_change = +1

    if ball_x >display_w-20:                                     #ball restrict
        ball_xspeed = -(ball_xspeed + 0.2)
        ball_yspeed += 0.2
        print("new speeds %f %f",ball_xspeed,ball_yspeed)

    if ball_x < 35:                                             # ball restrict
            ball_xspeed = -(ball_xspeed - 0.2)
            ball_yspeed -= 0.2
            print("new speeds %f %f", ball_xspeed, ball_yspeed)

    if ball_y > display_h:
        if P1>P2:
            font = pygame.font.Font(None, 70)
            text = font.render("P1 WINS", True, (255, 0, 0))
            display.blit(text, ((display_w/2)-100, display_h/2))

        if P2>P1:
            font = pygame.font.Font(None, 70)
            text = font.render("P2 WINS", True, (255, 0, 0))
            display.blit(text, ((display_w/2)-50,display_h/2))

        if P2==P1:
            font = pygame.font.Font(None, 70)
            text = font.render("DRAW", True, (255, 0, 0))
            display.blit(text, ((display_w/2)-50,display_h/2))
        pygame.display.update()
        time.sleep(2)
        stop=True
        #ball_yspeed = -(ball_yspeed + 0.1)
        #ball_xspeed -= 0.5
        #print("new speeds %f %f",ball_xspeed,ball_yspeed)

    if ball_y < 50:
        ball_yspeed = -(ball_yspeed - 0.2)
        ball_xspeed += 0.2
        print("new speeds %f %f",ball_xspeed,ball_yspeed)

    if (xr1<=ball_x<=xr1+80) and (yr1<=ball_y<=yr1+14):
        ball_yspeed = -(ball_yspeed + 0.2)
        ball_xspeed -= 0.2
        print("new speeds %f %f", ball_xspeed, ball_yspeed)
        P1 += 1                                                         #scorechange

    if (xr2<=ball_x<=xr2+80) and (yr2<=ball_y<=yr1+17):
        ball_yspeed = -(ball_yspeed + 0.2)
        ball_xspeed -= 0.2
        print("new speeds %f %f", ball_xspeed, ball_yspeed)
        P2 += 1                                                         #scorechange


    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()
