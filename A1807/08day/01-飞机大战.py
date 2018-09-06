import pygame
from mygroup import *
pygame.init()
screen = pygame.display.set_mode((480,700))#创建游戏窗口
bg = pygame.image.load('/home/zwq/A1807/images/background.png')#插入图片
hero = pygame.image.load('/home/zwq/A1807/images/hero1.png')
herorect = pygame.Rect(200,500,120,120)
clock = pygame.time.Clock()
enemy = EnemySprite()
enemy1 = EnemySprite()
enemy1.rect.x = 50
enemy1.rect.y = 700
enemy1.speed = -2
enemy_group = pygame.sprite.Group(enemy,enemy1)
while True:
    clock.tick(60)
    herorect.y-=10#飞机速度
    screen.blit(bg,(0,0))
    screen.blit(hero,herorect)
    if herorect.bottom <= 0:
        herorect.top = 700 

    enemy_group.update()
    enemy_group.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('退出游戏')
            pygame.quit()
            exit()
    pygame.display.update()#更新


