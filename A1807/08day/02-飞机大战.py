import pygame
from mygroup import *
pygame.mixer.init()
HERO_FIRE_EVENT = pygame.USEREVENT + 1
class PlaneGame(object):
    def __init__(self):#游戏初始化
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)#创建游戏窗口
        self.clock = pygame.time.Clock()#创建游戏时钟
        self.__creat_sprites()
        #创建精灵和精灵组

        pygame.time.set_timer(CREATE_ENEMY_EVENT,500)#设置定时器，每隔多少秒创建一个敌机

    def start_game(self):
        while True:
            self.clock.tick(200)
            #设置刷新频率
            self.__event_handler()
            #事件监听
            self.__check_collide()
            #碰撞检测
            self.__update_sprites()
            #更新精灵组
            pygame.display.update()
            #更新屏幕显示

    def __create_sprites(self):
        bg1 = Background()
        bg2 = Background(True)
        self.bg_group = pygame.sprite.Group(bg1,bg2)
        #敌机组
        self.enemy_group = pygame.sprite.Group()#创建敌机精灵
    
    
    def __event_hanler(self):
        for event in pygame.event.get():
            keys_pressed = pygame.key.get_pressed()
            #控制飞机移动
            if keys_pressed[276]:
                self.hero.move = False
                self.hero.speed = -9

            elif keys_pressed[275]:
                self.hero.move = False
                self.hero.speed = 9

            elif keys_pressed[274]:
                self.hero.move = True
                self.hero.speed = -9

            elif keys_pressed[273]:
                self.hero.move = True
                self.hero.speed = 9

            else:
                self.hero.speed = 0

            if event.type == pygame.QUIT:
                self.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                #print('新敌机产生')
                self.enemy_group.add(enemy())#通过add方法添加
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

#更新精灵和精灵组
def __update_sprites(self):
    for x in [self.back_group,self.enemy_group,self.hero_group,self.hero.bullet]:
        x.update()
        x.draw(self.screen)

    
    def __check_collide(self):#碰撞检测
        pygame.sprite.groupcollide(self.enemy_group,self.hero.bullert,True,True)#子弹
        #敌机撞毁飞机
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        if len(enemies)>0:
            #英雄牺牲
            self.hero.kill()
            PlaneGame.__game_over()
    
    
    #def __update_sprites(self):#更新精灵组
        #self.bg_group.update()
        #self.bg_group.draw(self.screen)
    
    
    @staticmethod
    def __game_over():
        
        print('游戏结束')
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
