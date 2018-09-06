import pygame
from plan_sprites import *

#初始化

pygame.mixer.init()
pygame.init()

HERO_FIRE_EVENT = pygame.USEREVENT +1
class PlaneGame(object):
    def __init__(self):
        #print("游戏初始化")

        #1.创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #2.创建游戏时钟
        self.clock = pygame.time.Clock()
        #3.创建精灵和精灵组
        #调用创建精灵的方法
        self.__creat_sprites()
        #self.a = True
        #4.设置定时器 每隔多少秒创建一个敌机
        #pygame.time.set_timer相当于写了一个定时器 每隔一秒调用一次
        pygame.time.set_timer(CREATE_ENEMY_EVENT,500)
        #再写一个定时器 发射子弹
        pygame.time.set_timer(HERO_FIRE_EVENT,500)
        #敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        #得分
        self.count = 0
        self.score = 0
        #下面去事件监听方法里监听事件


    def star_game(self):
        while True:
            # 1 设置帧率
            self.clock.tick(200)
            # 2 事件监听 
            self.__event_handler()

            # 3 碰撞检测 
            self.__check_collide()
            # 4 更新精灵和精灵组
            self.__update_sprites()
            # 5 更新显示
            pygame.display.update()
            #每1\60秒就会调用一次
    #创建精灵和精灵组
    def __creat_sprites(self):
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1,bg2)
    

        #英雄
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

        
        


    #事件监听
    def __event_handler(self):

        for event in pygame.event.get():
            keys_pressed = pygame.key.get_pressed()
            #控制飞机移动
            if keys_pressed[276]:
                self.hero.move = False
                self.hero.speed = -9
            elif keys_pressed[275]:
                self.hero.move = False
                self.hero.speed = 9
            elif keys_pressed[273]:
                self.hero.move = True
                self.hero.speed = -9
            elif keys_pressed[274]:
                self.hero.move = True
                self.hero.speed = 9
            else:
                self.hero.speed = 0
            #if a:
                #self.a = True


            if event.type == pygame.QUIT:
                self.__game_over()

            elif event.type == CREATE_ENEMY_EVENT:
                #print("新的敌机产生")

                self.enemy_group.add(Enemy())

             #发射子弹
            elif event.type == HERO_FIRE_EVENT:
                    self.hero.fire()

    #更新精灵和精灵组
    def __update_sprites(self):

        for x in[self.back_group,self.enemy_group,self.hero_group,self.hero.bullet]:
            x.update()
            x.draw(self.screen)
        #绘制分数
        self.drawText(str(self.score),SCREEN_RECT.width - 30,50)

    def __check_collide(self):
        #碰撞检测
        pygame.sprite.groupcollide( self.enemy_group,self.hero.bullet, True, True)#子弹
        #2.敌机撞毁飞机
        enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        if len(enemies)>0:
            #英雄牺牲
            self.hero.kill()

            #结束游戏
            PlaneGame.__game_over()
    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()
    def __update_sprites(self):
                self.back_group.update()
                self.back_group.draw(self.screen)
                self.enemy_group.update()
                self.enemy_group.draw(self.screen)
                self.hero_group.update()
                self.hero_group.draw(self.screen)
                self.hero.bullet_group.update()
                self.hero.bullet_group.draw(self.screen)
		#绘制分数
                self.drawText(str(self.score),SCREEN_RECT.width - 30,50)
                #敌机销毁
                for enemy1_down in enemy1_down_group:
                    self.screen.blit(enemy1_down_surface[enemy1_down.down_index],enemy1_down.rect)
                    if self.count % 15 == 0:
                        enemy1_down.down_index += 1
                        if enemy1_down.down_index == 3:
                            self.score +=5
                            enemy1_down_group.remove(enemy1_down)
                            print(self.score)	
        
if __name__ == "__main__":
    game = PlaneGame()
    game.star_game()
