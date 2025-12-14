from pygame import *
from time import sleep
mixer.init()
font.init()
#подгоняем под экран
display.init()
display.set_caption('PING-PONG')
shet=0
window = display.set_mode((0, 0), FULLSCREEN)
infoObject = display.Info()
w=infoObject.current_w
h=infoObject.current_h

ball_w=w/15
ball_h=w/15
ball_x=h/10*7
ball_y=500
speed_x=w/400
speed_y=w/400

r_w=w/50
r_h=h/3
r_x=w/40
r_x2=(w/100)*90
r_y=w/2.5
r_speed=w/33


text_lose=font.Font(None,int(w/20)).render('Поражение!',1,(255,255,255))

background=transform.scale(image.load('фон.jpg'),(w, h))

clock=time.Clock()

mixer.music.load('Rainy Day Games YouTube Audio Library.mp3')
mixer.music.set_volume(0.1)
mixer.music.play()
tolchek=mixer.Sound('otskok.mp3')
#классы
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,width,hight,player_x,player_y,player_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(width,hight))
        self.player_speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Rocketka(GameSprite):
    def update_l(self):
        keys=key.get_pressed()
        if keys[K_w] and self.rect.y>5:
            self.rect.y -= self.player_speed
        if keys[K_s] and self.rect.y<w-r_h:
            self.rect.y += self.player_speed
    def update_r(self):
        keys=key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y -= self.player_speed
        if keys[K_DOWN] and self.rect.y<w-r_h:
            self.rect.y += self.player_speed
#спрайты
ball=GameSprite('tennis.png',ball_w,ball_h,ball_x,ball_y,0)
r1=Rocketka('черный.jpg',r_w,r_h,r_x,r_y,r_speed)
r2=Rocketka('черный.jpg',r_w,r_h,r_x2,r_y,r_speed)
#игровой цикл
game=True
end=False
while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
    if not end:
        window.blit(background,(0,0))
        ball.reset()
        ball.update(speed_y)
        text_chet=font.Font(None,int(w/20)).render('Счёт:'+str(shet),1,(255,255,255))
        r1.reset()
        r1.update_l()
        r2.reset()
        r2.update_r()
        ball.rect.x+=speed_x
        ball.rect.y+=speed_y
        window.blit(text_chet,(0,w/20))
        if ball.rect.y<5:
            speed_y*=-1
            tolchek.play()
        if ball.rect.y>h:
            speed_y*=-1
            tolchek.play()
        if sprite.collide_rect(ball,r1):
            shet+=1
            speed_x*=-1
            speed_x+=3
            speed_y+=3
            tolchek.play()
        if sprite.collide_rect(ball,r2):
            shet+=1
            speed_x*=-1
            speed_x-=3
            speed_y-=3
            tolchek.play()
        if ball.rect.x<=5 or ball.rect.x >= w:
            window.blit(text_lose,(h/2,w/2))
            end=True
        

    display.update()
    clock.tick(60)