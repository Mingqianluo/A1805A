import random
import pygame
SCREEN_RECT = pygame.Rect(0,0,480,700)#设置游戏屏幕大小
CREATE_EVEMY_EVENT = pygame.USEREVENT#敌机定时器常量
CREATE_EVEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1#发射子弹

class GameSprite(pygame.sprite.Sprite):
    def __init__(self,new_image,new_speed=1):
        super().__init__()
        self.image = pygame.image.load(new_image)#图片
        self.rect = self.image.get_rect()#速度
        self.speed = new_speed#位置
    
    def update(self):
        self.rect.y += self.speed
#背景 两张图片交替替换
class Background(GameSprite):
    def __init__(self,is_alt = False):
        super().__init__('home/zwq/A1807/images/background.png')
        if is_alt:
            self.rect.y = -self.rect.height
    def update(self):
        super().update()
        if self.rect.y >=SCREEN_RECT.height:
            self.rect.y = -self.rect.height




class EnemySprite(GameSprite):
    def __init__(self):
        super().__init__('home/zwq/A1807/images/enemy0.png')
        self.speed = random.randint(2,6)#设置初始敌机随机速度
        #设置敌机随机初始位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width -self.rect.width
        self.rect.x = random.randint(0,max_x)
    def update(self):
        super().update()
        #判断是否飞出屏幕，如果是则删除
        if self.rect.y >= SCREEN_RECT.height:
            #将精灵从精灵组中删除
            self.kill()
#英雄            
class Hero(GameSprite):
    def __init__(self):
        super().__init__('home/zwq/A1807/images/ying1.png',0)
        self.bullet = pygame.sprite.Group()
        #设置初始位置
        self.rect.center = SCREEN_RECT.center
        self.rect.bottom =SCREEN_RECT.bottom-120
        self.move = False
def update(self):
        #super().update()
        if not self.move:
            self.rect.x += self.speed
        else:
            self.rect.y += self.speed

        #self.rect.y += self.speed
        #飞机飞出屏幕
        if self.rect.bottom <= 0:
            self.rect.y = self.rect.bottom+SCREEN_RECT.height
        elif self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

        if self.rect.right <= 0:
            self.rect.x = self.rect.right+SCREEN_RECT.width
        elif self.rect.x >= SCREEN_RECT.width:
            self.rect.x = -self.rect.width
def fire(self):
    #print("发射子弹")
    for i in (1,2,3):
        bullet = Bullet()
        bullet.rect.bottom = self.rect.y-i*20
        bullet.rect.center = self.rect.center
        self.bullet.add(bullet)


#子弹精灵
class Bullet(GameSprite):

    def __init__(self):
        super().__init__("/home/zwq/A1805-2/images/bullet.png",-5)
    def update(self):
        super().update()

        #判断是否超出屏幕 如果是 从精灵组删除
        if self.rect.bottom < 0:
            self.kill()



