import pygame
import sys
from random import randint
window = pygame.display.set_mode((1280,720)) #створення вікна з розмірами
window.fill((255,255,255))
pygame.display.set_caption("ping-pong")
score1=0
score2=0
pygame.font.init()
font1=pygame.font. SysFont("Arial",30)
win1=font1.render("player1 win!!!", True, (160, 160, 160))
win2=font1.render("player2 win!!!", True, (160,160,160))
black=pygame.transform.scale(pygame.image.load("black.jpg"), (2000,1000))
class Hero(pygame.sprite.Sprite): #головний клас для всіх обектiв гри(спадкоємець класу Спрайт з пайгейма)
    def __init__(self, width, height, image,x,y, speed):# задаэм ширину, висоту, картинку, x, y, швидкість об'єкта.
        super().__init__() #підключаємо всі можливості супер класу
        self.image=pygame.transform.scale(pygame.image.load(image),(width,height))
        self.speed=speed
        self.rect=self.image.get_rect() #створення рамки для картинки
        self.rect.x=x #координати рамки по x
        self.rect.y=y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(Hero):
    def update1(self):
        keys=pygame.key.get_pressed() #створюємо список з натиснутими клавішами
        if keys[pygame.K_UP] and self.rect.y>5: #якщо натиснуто кнопку "стрілка вверх"
            self.rect.y-=self.speed #якщо ми рухаемося вгору Y ЗМЕНШУЄТЬСЯ, рух вверх
        if keys [pygame.K_DOWN] and self.rect.y<1000: #якщо натиснуто кнопку "стрілка вниз"
            self.rect.y+=self.speed #рух вниз
    def update2(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y>5: # якщо HатисHуто кнопку "стPinkа вверх"
            self.rect.y-=self.speed #pyx вверх
        if keys[pygame.K_s] and self.rect.y<990: # натиснуто Kнопку "стрілка вниз"
            self.rect.y+=self. speed #pyx вниз

p1=Player (25, 200, 'raketka.png',10, 300,10)
p2=Player (25, 200, 'raketka2.png',1250,300,10)
ball=Hero (50, 50, 'ball.png',300,300,4)
point=font1.render('Очки:',True,(180,0,0))
points1=0
points2=0
clock = pygame.time.Clock()
pygame.font.init()
font1=pygame.font. SysFont('Arial', 30) 
lose=font1.render('P1 lose', True, (180,0,0))
lose=font1.render('P2 lose!', True, (180,0,0))
game=True
finish=False
sx=7
sy=7
while game:
    if finish !=True:
        window.blit(black, (0,-100))
        p1.update2()
        p1.reset()
        p2.update1()
        p2.reset()
        ball.rect.x+=sx
        ball.rect.y -=sy
        ball.reset()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
    if pygame.sprite.collide_rect(p1, ball) or pygame.sprite.collide_rect(p2, ball): 
        sx*=-1
        sy*=1
    if ball.rect.y<=0:
        sy*=-1
    if ball.rect.y>700:
        sy*= -1
    if ball.rect.x<0:
        points1+=1
        ball.rect.x=600
        ball.rect.y=400
    if ball.rect.x>1280:
        points2+=1
        ball.rect.x=600
        ball.rect.y=400
    text=font1.render('Счёт P1:'+str(points1),1,(250,250,250))
    window.blit(text,(50,40))
    text=font1.render('Счёт P2:'+str(points2),1,(250,250,250))
    window.blit(text,(1100,40))
    ball.reset()
    pygame.display.update()
    clock.tick(50)