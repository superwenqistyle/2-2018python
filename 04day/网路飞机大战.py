import pygame  
  
class MyPlane(pygame.sprite.Sprite):  
    def __init__(self,bg_size):  
        pygame.sprite.Sprite.__init__(self)  
          
        self.image1 = pygame.image.load(r'E:\learn pygame\image\me1.png').convert_alpha()  
        self.image2 = pygame.image.load(r'E:\learn pygame\image\me2.png').convert_alpha()  
        self.image3 = pygame.image.load(r'E:\learn pygame\image\me_protect.png').convert_alpha()  
        self.destroy_images = []  
        self.destroy_images.extend([\  
            pygame.image.load(r'E:\learn pygame\image\me_destroy_1.png').convert_alpha(), \  
            pygame.image.load(r'E:\learn pygame\image\me_destroy_2.png').convert_alpha(), \  
            pygame.image.load(r'E:\learn pygame\image\me_destroy_3.png').convert_alpha(), \  
            pygame.image.load(r'E:\learn pygame\image\me_destroy_4.png').convert_alpha() \  
            ])  
        self.rect = self.image1.get_rect()  
        self.width,self.height = bg_size[0],bg_size[1]  
        self.rect.left,self.rect.top = (self.width - self.rect.width) // 2,self.height - self.rect.height - 60  
        self.speed = 10  
        self.active = True  
        self.invincible = False  
        self.mask = pygame.mask.from_surface(self.image1)  
  
    def moveUp(self):  
        if self.rect.top > 0:  
            self.rect.top -= self.speed  
        else:  
            self.rect.top = 0  
              
    def moveDown(self):  
        if self.rect.bottom < self.height - 30:  
            self.rect.top += self.speed  
        else:  
            self.rect.bottom = self.height - 30  
              
    def moveLeft(self):  
        if self.rect.left > 0:  
            self.rect.left -= self.speed  
        else:  
            self.rect.left = 0  
              
    def moveRight(self):  
        if self.rect.right < self.width:  
            self.rect.left += self.speed  
        else:  
            self.rect.right = self.width  
              
    def reset(self):  
        self.rect.left,self.rect.top = (self.width - self.rect.width) // 2,self.height - self.rect.height - 30  
        self.active = True    
        self.invincible = True  
      
          
2、敌机与背景动图模块
[python] view plain copy
import pygame  
from random import *  
  
class SmallEnemy(pygame.sprite.Sprite):  
    energy = 1  
    def __init__(self,bg_size):  
        pygame.sprite.Sprite.__init__(self)  
        self.image = pygame.image.load(r'E:\learn pygame\image\enemy1.png').convert_alpha()  
        self.destroy_images = []  
        self.destroy_images.extend([\  
            pygame.image.load(r'E:\learn pygame\image\enemy1_down1.png').convert_alpha(), \  
            pygame.image.load(r'E:\learn pygame\image\enemy1_down2.png').convert_alpha(), \  
            pygame.image.load(r'E:\learn pygame\image\enemy1_down3.png').convert_alpha(), \  
            pygame.image.load(r'E:\learn pygame\image\enemy1_down4.png').convert_alpha() \  
            ])  
        self.rect = self.image.get_rect()  
        self.width,self.height = bg_size[0],bg_size[1]  
        self.speed = 2  
        self.active = True  
        self.rect.left,self.rect.top = \  
                        randint(0,self.width - self.rect.width), \  
                        randint(-5 * self.height, 0)  
        self.mask = pygame.mask.from_surface(self.image)  
        self.energy = SmallEnemy.energy  
        self.hit = False  
          
    def move(self):  
        if self.rect.top < self.height:  
            self.rect.top += self.speed  
        else:  
            self.reset()  
      
    def reset(self):  
        self.active = True  
        self.energy = SmallEnemy.energy  
        self.rect.left,self.rect.top = \  
                    randint(0,self.width - self.rect.width), \  
                    randint(-5 * self.height, 0)  
                      
class MidEnemy(pygame.sprite.Sprite):  
    energy = 4   
      
    def __init__(self,bg_size):  
        pygame.sprite.Sprite.__init__(self)  
          
        self.image = pygame.image.load(r'E:\learn pygame\image\enemy2.png').convert_alpha()  
        self.image_hit = pygame.image.load(r'E:\learn pygame\image\enemy2_hit.png').convert_alpha()  
        self.destroy_images = []  
        self.destroy_images.extend([\  
            pygame.image.load(r'E:\learn pygame\image\enemy2_down1.png').convert_alpha(), \  
            pygame.image.load(r'E:\learn pygame\image\enemy2_down2.png').convert_alpha(), \  
            pygame.image.load(r'E:\learn pygame\image\enemy2_down3.png').convert_alpha(), \  
            pygame.image.load(r'E:\learn pygame\image\enemy2_down4.png').convert_alpha() \  
            ])  
        self.rect = self.image.get_rect()  
        self.width,self.height = bg_size[0],bg_size[1]  
        self.speed = 2  
        self.active = True  
        self.rect.left,self.rect.top = \  
                        randint(0,self.width - self.rect.width), \  
                        randint(-10 * self.height, -self.height)  
        self.mask = pygame.mask.from_surface(self.image)  
        self.energy = MidEnemy.energy  
        self.hit = False  
          
    def move(self):  
        if self.rect.top < self.height:  
            self.rect.top += self.speed  
        else:  
            self.reset()  
      
    def reset(self):  
        self.active = True  
        self.energy = MidEnemy.energy  
        self.rect.left,self.rect.top = \  
                    randint(0,self.width - self.rect.width), \  
                    randint(-10 * self.height, -self.height)  
                      
                      
class BigEnemy(pygame.sprite.Sprite):  
    energy = 8  
    def __init__(self,bg_size):  
        pygame.sprite.Sprite.__init__(self)  
          
        self.image1 = pygame.image.load(r'E:\learn pygame\image\enemy3_n1.png').convert_alpha()  
        self.image2 = pygame.image.load(r'E:\learn pygame\image\enemy3_n2.png').convert_alpha()  
        self.image_hit = pygame.image.load(r'E:\learn pygame\image\enemy3_hit.png').convert_alpha()  
        self.destroy_images = []  
        self.destroy_images.extend([\  
            pygame.image.load(r'E:\learn pygame\image\enemy3_down1.png').convert_alpha(), \  
            pygame.image.load(r'E:\learn pygame\image\enemy3_down2.png').convert_alpha(), \  
            pygame.image.load(r'E:\learn pygame\image\enemy3_down3.png').convert_alpha(), \  
            pygame.image.load(r'E:\learn pygame\image\enemy3_down4.png').convert_alpha(), \  
            pygame.image.load(r'E:\learn pygame\image\enemy3_down5.png').convert_alpha(), \  
            pygame.image.load(r'E:\learn pygame\image\enemy3_down6.png').convert_alpha() \  
            ])  
        self.rect = self.image1.get_rect()  
        self.width,self.height = bg_size[0],bg_size[1]  
        self.speed = 2  
        self.active = True  
        self.rect.left,self.rect.top = \  
                        randint(0,self.width - self.rect.width), \  
                        randint(-15 * self.height, -5 * self.height)  
        self.mask = pygame.mask.from_surface(self.image1)  
        self.energy = BigEnemy.energy  
        self.hit = False  
          
    def move(self):  
        if self.rect.top < self.height:  
            self.rect.top += self.speed  
        else:  
            self.reset()  
      
    def reset(self):  
        self.active = True  
        self.energy = BigEnemy.energy  
        self.rect.left,self.rect.top = \  
                    randint(0,self.width - self.rect.width), \  
                    randint(-15 * self.height, -5 * self.height)  
                      
class Cloud1(pygame.sprite.Sprite):  
    energy = 2  
    def __init__(self,bg_size):  
        pygame.sprite.Sprite.__init__(self)  
          
        self.image = pygame.image.load(r'E:\learn pygame\image\cloud1.png').convert_alpha()  
        self.rect = self.image.get_rect()  
        self.width,self.height = bg_size[0],bg_size[1]  
        self.speed = 1  
        self.active = True  
        self.rect.left,self.rect.top = \  
                        randint(0,self.width - self.rect.width), \  
                        randint(-5 * self.height, 0)  
        self.energy = Cloud1.energy  
          
    def move(self):  
        if self.rect.top < self.height:  
            self.rect.top += self.speed  
        else:  
            self.reset()  
      
    def reset(self):  
        self.active = True  
        self.energy = Cloud1.energy  
        self.rect.left,self.rect.top = \  
                    randint(0,self.width - self.rect.width), \  
                    randint(-5 * self.height, 0)  
                      
class Cloud2(pygame.sprite.Sprite):  
    energy = 2  
    def __init__(self,bg_size):  
        pygame.sprite.Sprite.__init__(self)  
          
        self.image = pygame.image.load(r'E:\learn pygame\image\cloud1.png').convert_alpha()  
        self.rect = self.image.get_rect()  
        self.width,self.height = bg_size[0],bg_size[1]  
        self.speed = 1  
        self.active = True  
        self.rect.left,self.rect.top = \  
                        randint(0,self.width - self.rect.width), \  
                        randint(-5 * self.height, 0)  
        self.energy = Cloud2.energy  
      
    def move(self):  
        if self.rect.top < self.height:  
            self.rect.top += self.speed  
        else:  
            self.reset()  
      
    def reset(self):  
        self.active = True  
        self.energy = Cloud2.energy  
        self.rect.left,self.rect.top = \  
                    randint(0,self.width - self.rect.width), \  
                    randint(-5 * self.height, 0)  
                      
class BombEnemy(pygame.sprite.Sprite):  
    energy = 10  
      
    def __init__(self,bg_size):  
        pygame.sprite.Sprite.__init__(self)  
          
        self.image1 = pygame.image.load(r'E:\learn pygame\image\bomb_enemy1.png').convert_alpha()  
        self.image2 = pygame.image.load(r'E:\learn pygame\image\bomb_enemy2.png').convert_alpha()  
        self.rect = self.image1.get_rect()  
        self.destroy_images = []  
        self.destroy_images.extend([ \  
            pygame.image.load(r'E:\learn pygame\image\bomb_enemy_down1.png').convert_alpha(), \  
            pygame.image.load(r'E:\learn pygame\image\bomb_enemy_down2.png').convert_alpha(), \  
            pygame.image.load(r'E:\learn pygame\image\bomb_enemy_down3.png').convert_alpha(), \  
            pygame.image.load(r'E:\learn pygame\image\bomb_enemy_down4.png').convert_alpha(), \  
            ])  
        self.width,self.height = bg_size[0],bg_size[1]  
        self.speed = 2  
        self.active = True  
        self.rect.left,self.rect.top = \  
                        randint(0,self.width - self.rect.width), \  
                        randint(-15 * self.height, -5 * self.height)  
        self.mask = pygame.mask.from_surface(self.image1)  
        self.energy = BombEnemy.energy  
        self.hit = False  
          
    def move(self):  
        if self.rect.top < self.height:  
            self.rect.top += self.speed  
        else:  
            self.reset()  
      
    def reset(self):  
        self.active = True  
        self.energy = BombEnemy.energy  
        self.rect.left,self.rect.top = \  
                    randint(0,self.width - self.rect.width), \  
                    randint(-15 * self.height, -5 * self.height)  
                      
class BackGround1(pygame.sprite.Sprite):  
    def __init__(self,bg_size):  
        pygame.sprite.Sprite.__init__(self)  
          
        self.image = pygame.image.load(r'E:\learn pygame\image\background1.png').convert_alpha()  
        self.rect = self.image.get_rect()  
        self.width,self.height = bg_size[0],bg_size[1]  
        self.speed = 1  
        self.active = True  
        self.rect.center = ((self.width // 2), (self.height // 2))  
      
    def move(self):  
        if self.rect.top < self.height:  
            self.rect.top += self.speed  
        else:  
            self.reset()  
              
    def reset(self):  
        self.active = True  
        self.rect.center = ((self.width // 2), -(self.height // 2))  
          
class BackGround2(pygame.sprite.Sprite):  
    def __init__(self,bg_size):  
        pygame.sprite.Sprite.__init__(self)  
          
        self.image = pygame.image.load(r'E:\learn pygame\image\background1.png').convert_alpha()  
        self.rect = self.image.get_rect()  
        self.width,self.height = bg_size[0],bg_size[1]  
        self.speed = 1  
        self.active = True  
        self.rect.center = ((self.width // 2), -(self.height // 2))  
      
    def move(self):  
        if self.rect.top < self.height:  
            self.rect.top += self.speed  
        else:  
            self.reset()  
              
    def reset(self):  
        self.active = True  
        self.rect.center = ((self.width // 2), -(self.height // 2))  
3、子弹模块
[python] view plain copy
import pygame  
  
class Bullet1(pygame.sprite.Sprite):  
    def __init__(self,position):  
        pygame.sprite.Sprite.__init__(self)  
          
        self.image = pygame.image.load(r'E:\learn pygame\image\bullet1.png').convert_alpha()  
        self.rect = self.image.get_rect()  
        self.rect.left,self.rect.top = position  
        self.speed = 18  
        self.active = False  
        self.mask = pygame.mask.from_surface(self.image)  
      
    def move(self):  
        self.rect.top -= self.speed  
          
        if self.rect.top < 0:  
            self.active = False  
              
    def reset(self,position):  
        self.rect.left,self.rect.top = position  
        self.active = True  
          
class Bullet2(pygame.sprite.Sprite):  
    def __init__(self,position):  
        pygame.sprite.Sprite.__init__(self)  
          
        self.image = pygame.image.load(r'E:\learn pygame\image\bullet2.png').convert_alpha()  
        self.rect = self.image.get_rect()  
        self.rect.left,self.rect.top = position  
        self.speed = 18  
        self.active = False  
        self.mask = pygame.mask.from_surface(self.image)  
      
    def move(self):  
        self.rect.top -= self.speed  
          
        if self.rect.top < 0:  
            self.active = False  
              
    def reset(self,position):  
        self.rect.left,self.rect.top = position  
        self.active = True  
          
class Bullet3(pygame.sprite.Sprite):  
    def __init__(self,position):  
        pygame.sprite.Sprite.__init__(self)  
          
        self.image = pygame.image.load(r'E:\learn pygame\image\bullet3.png').convert_alpha()  
        self.rect = self.image.get_rect()  
        self.rect.left,self.rect.top = position  
        self.speed = 120  
        self.active = False  
        self.mask = pygame.mask.from_surface(self.image)  
      
    def move(self):  
        self.rect.top -= self.speed  
          
        if self.rect.top < 0:  
            self.active = False  
              
    def reset(self,position):  
        self.rect.left,self.rect.top = position  
        self.active = True  
          
class Bullet4(pygame.sprite.Sprite):  
    def __init__(self,position,bg_size):  
        pygame.sprite.Sprite.__init__(self)  
          
        self.image = pygame.image.load(r'E:\learn pygame\image\bullet4.png').convert_alpha()  
        self.rect = self.image.get_rect()  
        self.rect.left,self.rect.top = position  
        self.width,self.height = bg_size[0],bg_size[1]  
        self.speed = 9  
        self.active = False  
        self.mask = pygame.mask.from_surface(self.image)  
      
    def move(self):  
        self.rect.top -= self.speed  
          
        if self.rect.top < 0:  
            self.active = False  
              
    def reset(self,position):  
        self.rect.left,self.rect.top = position  
        self.active = True  
          
4、补给模块
[python] view plain copy
import pygame  
from random import *  
  
class Bullet_Supply(pygame.sprite.Sprite):  
    def __init__(self,bg_size):  
        pygame.sprite.Sprite.__init__(self)  
          
        self.image = pygame.image.load(r'E:\learn pygame\image\bullet_supply.png').convert_alpha()  
        self.rect = self.image.get_rect()  
        self.width,self.height = bg_size[0],bg_size[1]  
        self.rect.left,self.rect.bottom = \  
                        randint(0,self.width - self.rect.width), -100  
        self.speed = 5  
        self.active = False  
        self.mask = pygame.mask.from_surface(self.image)  
          
    def move(self):  
        if self.rect.top < self.height:  
            self.rect.top += self.speed  
        else:  
            self.active = False  
      
    def reset(self):  
        self.active = True  
        self.rect.left,self.rect.bottom = \  
                        randint(0,self.width - self.rect.width), -100  
          
class Bomb_Supply(pygame.sprite.Sprite):  
    def __init__(self,bg_size):  
        pygame.sprite.Sprite.__init__(self)  
          
        self.image = pygame.image.load(r'E:\learn pygame\image\bomb_supply.png').convert_alpha()  
        self.rect = self.image.get_rect()  
        self.width,self.height = bg_size[0],bg_size[1]  
        self.rect.left,self.rect.bottom = \  
                        randint(0,self.width - self.rect.width), -100  
        self.speed = 5  
        self.active = False  
        self.mask = pygame.mask.from_surface(self.image)  
          
    def move(self):  
        if self.rect.top < self.height:  
            self.rect.top += self.speed  
        else:  
            self.active = False  
      
    def reset(self):  
        self.active = True  
        self.rect.left,self.rect.bottom = \  
                        randint(0,self.width - self.rect.width), -100  
  
class Laser_Supply(pygame.sprite.Sprite):  
    def __init__(self,bg_size):  
        pygame.sprite.Sprite.__init__(self)  
          
        self.image = pygame.image.load(r'E:\learn pygame\image\laser_supply.png').convert_alpha()  
        self.rect = self.image.get_rect()  
        self.width,self.height = bg_size[0],bg_size[1]  
        self.rect.left,self.rect.bottom = \  
                        randint(0,self.width - self.rect.width), -100  
        self.speed = 5  
        self.active = False  
        self.mask = pygame.mask.from_surface(self.image)  
          
    def move(self):  
        if self.rect.top < self.height:  
            self.rect.top += self.speed  
        else:  
            self.active = False  
      
    def reset(self):  
        self.active = True  
        self.rect.left,self.rect.bottom = \  
                        randint(0,self.width - self.rect.width), -100     
  
class Fire_Supply(pygame.sprite.Sprite):  
    def __init__(self,bg_size):  
        pygame.sprite.Sprite.__init__(self)  
          
        self.image = pygame.image.load(r'E:\learn pygame\image\fire_supply.png').convert_alpha()  
        self.rect = self.image.get_rect()  
        self.width,self.height = bg_size[0],bg_size[1]  
        self.rect.left,self.rect.bottom = \  
                        randint(0,self.width - self.rect.width), -100  
        self.speed = 5  
        self.active = False  
        self.mask = pygame.mask.from_surface(self.image)  
          
    def move(self):  
        if self.rect.top < self.height:  
            self.rect.top += self.speed  
        else:  
            self.active = False  
      
    def reset(self):  
        self.active = True  
        self.rect.left,self.rect.bottom = \  
                        randint(0,self.width - self.rect.width), -100         
  
class Me_Protect_Supply(pygame.sprite.Sprite):  
    def __init__(self,bg_size):  
        pygame.sprite.Sprite.__init__(self)  
          
        self.image = pygame.image.load(r'E:\learn pygame\image\me_protect_supply.png').convert_alpha()  
        self.rect = self.image.get_rect()  
        self.width,self.height = bg_size[0],bg_size[1]  
        self.rect.left,self.rect.bottom = \  
                        randint(0,self.width - self.rect.width), -100  
        self.speed = 5  
        self.active = False  
        self.mask = pygame.mask.from_surface(self.image)  
          
    def move(self):  
        if self.rect.top < self.height:  
            self.rect.top += self.speed  
        else:  
            self.active = False  
      
    def reset(self):  
        self.active = True  
        self.rect.left,self.rect.bottom = \  
                        randint(0,self.width - self.rect.width), -100                                 
                          
class Life_Supply(pygame.sprite.Sprite):  
    def __init__(self,bg_size):  
        pygame.sprite.Sprite.__init__(self)  
          
        self.image = pygame.image.load(r'E:\learn pygame\image\life_supply.png').convert_alpha()  
        self.rect = self.image.get_rect()  
        self.width,self.height = bg_size[0],bg_size[1]  
        self.rect.left,self.rect.bottom = \  
                        randint(0,self.width - self.rect.width), -100  
        self.speed = 5  
        self.active = False  
        self.mask = pygame.mask.from_surface(self.image)  
          
    def move(self):  
        if self.rect.top < self.height:  
            self.rect.top += self.speed  
        else:  
            self.active = False  
      
    def reset(self):  
        self.active = True  
        self.rect.left,self.rect.bottom = \  
                        randint(0,self.width - self.rect.width), -100                                 
5、掉落星星模块（还没完善好）
[python] view plain copy
import pygame  
  
class Star(pygame.sprite.Sprite):  
    energy = 1  
    def __init__(self,bg_size,star_left,star_top):  
        pygame.sprite.Sprite.__init__(self)  
          
        self.image = pygame.image.load(r'E:\learn pygame\image\star_bling1.png').convert_alpha()  
        self.rect = self.image.get_rect()  
        self.star_images = []  
        self.star_images.extend([pygame.image.load(r'E:\learn pygame\image\star_bling1.png').convert_alpha(),pygame.image.load(r'E:\learn pygame\image\star_bling2.png').convert_alpha(),pygame.image.load(r'E:\learn pygame\image\star_bling3.png').convert_alpha(),pygame.image.load(r'E:\learn pygame\image\star_bling4.png').convert_alpha(),pygame.image.load(r'E:\learn pygame\image\star_bling5.png').convert_alpha(),pygame.image.load(r'E:\learn pygame\image\star_bling6.png').convert_alpha(),pygame.image.load(r'E:\learn pygame\image\star_bling7.png').convert_alpha(),pygame.image.load(r'E:\learn pygame\image\star_bling8.png').convert_alpha(),pygame.image.load(r'E:\learn pygame\image\star_bling9.png').convert_alpha(),pygame.image.load(r'E:\learn pygame\image\star_bling10.png').convert_alpha()])   
        self.width,self.height = bg_size[0],bg_size[1]  
        self.rect.left,self.rect.top = star_left,star_top  
        self.speed = 1  
        self.active = True  
        self.is_star = False  
        self.star_is_touch = False  
          
    def move(self):  
        if self.rect.top < self.height:  
            self.rect.top += self.speed  
        else:  
            self.reset()  
      
    def reset(self):  
        self.active = True  
6、主模块
[python] view plain copy
import pygame  
import sys  
import traceback  
import time  
import myplane  
import enemy  
import bullet  
import supply  
import star  
from random import *  
from pygame.locals import *  
  
pygame.init()  
pygame.mixer.init()  
  
bg_size = width, height = 450,675  
screen = pygame.display.set_mode(bg_size)  
pygame.display.set_caption('飞机大战')  
  
background = pygame.image.load(r'E:\learn pygame\image\background1.png').convert()  
background_rect = background.get_rect()  
  
BLACK = (0,0,0)  
WHITE = (255,255,255)  
GREEN = (0,255,0)  
RED = (255,0,0)  
  
#载入游戏音乐  
pygame.mixer.music.load(r'E:\learn pygame\music\bg_music.ogg')  
pygame.mixer.music.set_volume(0.2)  
bomb_enemy_fly_sound = pygame.mixer.Sound(r'E:\learn pygame\music\bomb_enemy_flying.wav')  
bomb_enemy_fly_sound.set_volume(0.1)  
enemy3_fly_sound = pygame.mixer.Sound(r'E:\learn pygame\music\enemy3_flying.wav')  
enemy3_fly_sound.set_volume(0.1)  
enemy1_down_sound = pygame.mixer.Sound(r'E:\learn pygame\music\enemy1_down.wav')  
enemy1_down_sound.set_volume(0.5)  
enemy2_down_sound = pygame.mixer.Sound(r'E:\learn pygame\music\enemy2_down.wav')  
enemy2_down_sound.set_volume(0.5)  
enemy3_down_sound = pygame.mixer.Sound(r'E:\learn pygame\music\bomb_enemy_down.wav')  
enemy3_down_sound.set_volume(0.5)  
bomb_enemy_down_sound = pygame.mixer.Sound(r'E:\learn pygame\music\bomb_enemy_down.wav')  
bomb_enemy_down_sound.set_volume(0.5)  
me_down_sound = pygame.mixer.Sound(r'E:\learn pygame\music\me_down.wav')  
me_down_sound.set_volume(0.5)  
upgrade_sound = pygame.mixer.Sound(r'E:\learn pygame\music\upgrade.wav')  
upgrade_sound.set_volume(0.5)  
bomb_sound = pygame.mixer.Sound(r'E:\learn pygame\music\use_bomb.wav')  
bomb_sound.set_volume(0.5)  
supply_sound = pygame.mixer.Sound(r'E:\learn pygame\music\supply.wav')  
supply_sound.set_volume(0.5)  
get_bomb_sound = pygame.mixer.Sound(r'E:\learn pygame\music\get_bomb.wav')  
get_bomb_sound.set_volume(0.5)  
get_bullet_sound = pygame.mixer.Sound(r'E:\learn pygame\music\get_bullet.wav')  
get_bullet_sound.set_volume(0.5)  
get_laser_sound = pygame.mixer.Sound(r'E:\learn pygame\music\get_laser.wav')  
get_laser_sound.set_volume(0.5)  
get_fire_sound = pygame.mixer.Sound(r'E:\learn pygame\music\get_fire.wav')  
get_fire_sound.set_volume(0.5)  
get_me_protect_sound = pygame.mixer.Sound(r'E:\learn pygame\music\get_me_protect.wav')  
get_me_protect_sound.set_volume(0.5)  
get_life_sound = pygame.mixer.Sound(r'E:\learn pygame\music\get_life.wav')  
get_life_sound.set_volume(0.5)  
bullet_sound = pygame.mixer.Sound(r'E:\learn pygame\music\bullet.wav')  
bullet_sound.set_volume(0.2)  
fire_bullet_sound = pygame.mixer.Sound(r'E:\learn pygame\music\fire_bullet.wav')  
fire_bullet_sound.set_volume(0.2)  
  
def add_small_enemies(group1,group2,num):  
    for i in range(num):  
        e1 = enemy.SmallEnemy(bg_size)  
        group1.add(e1)  
        group2.add(e1)  
          
def add_mid_enemies(group1,group2,num):  
    for i in range(num):  
        e2 = enemy.MidEnemy(bg_size)  
        group1.add(e2)  
        group2.add(e2)  
          
def add_big_enemies(group1,group2,num):  
    for i in range(num):  
        e3 = enemy.BigEnemy(bg_size)  
        group1.add(e3)  
        group2.add(e3)  
          
def add_bomb_enemies(group1,group2,num):  
    for i in range(num):  
        e3 = enemy.BombEnemy(bg_size)  
        group1.add(e3)  
        group2.add(e3)  
          
def add_cloud1_enemies(group1,group2,num):  
    for i in range(num):  
        e4 = enemy.Cloud1(bg_size)  
        group1.add(e4)  
        group2.add(e4)  
          
def add_cloud2_enemies(group1,group2,num):  
    for i in range(num):  
        e5 = enemy.Cloud2(bg_size)  
        group1.add(e5)  
        group2.add(e5)  
          
def add_background1(group1,group2,num):  
    for i in range(num):  
        e6 = enemy.BackGround1(bg_size)  
        group1.add(e6)  
        group2.add(e6)  
          
def add_background2(group1,group2,num):  
    for i in range(num):  
        e7 = enemy.BackGround2(bg_size)  
        group1.add(e7)  
        group2.add(e7)  
          
def add_star(group1,group2,star_left,star_top,num):  
    for i in range(num):  
        e8 = star.Star(bg_size,star_left,star_top)  
        group1.add(e8)  
        group2.add(e8)  
  
def inc_speed(inc,*targets):  
    for each in targets:  
        for every in each:  
            every.speed += inc  
  
def inc_speed_background(inc,target):  
    for each in target:  
        each.speed += inc     
  
def inc_speed_me(inc,target):  
    target.speed += inc   
      
def inc_speeds(inc,*targets):  
    for each in targets:  
        for every in each:  
            every.speed += inc  
      
def main():  
      
    pygame.mixer.music.play(-1)  
      
    #生成我方飞机、背景、敌机、云朵、星星的类，以便做碰撞检测  
    me = myplane.MyPlane(bg_size)  
    backgrounds = pygame.sprite.Group()  
    enemies = pygame.sprite.Group()  
    clouds = pygame.sprite.Group()  
    stars = pygame.sprite.Group()  
    bullets = pygame.sprite.Group()  
    #生成背景1  
    background1 = pygame.sprite.Group()  
    add_background1(background1,backgrounds,1)  
  
    #生成背景2  
    background2 = pygame.sprite.Group()  
    add_background2(background2,backgrounds,1)  
      
    #生成敌方小型飞机  
    small_enemies = pygame.sprite.Group()  
    add_small_enemies(small_enemies,enemies,15)  
      
    #生成敌方中型飞机  
    mid_enemies = pygame.sprite.Group()  
    add_mid_enemies(mid_enemies,enemies,4)  
      
    #生成敌方大型飞机  
    big_enemies = pygame.sprite.Group()  
    add_big_enemies(big_enemies,enemies,2)  
      
    #生成敌方超级炸弹  
    bomb_enemies = pygame.sprite.Group()  
    add_bomb_enemies(bomb_enemies,enemies,1)  
      
    #生成云朵1  
    cloud1_enemies = pygame.sprite.Group()  
    add_cloud1_enemies(cloud1_enemies,clouds,1)  
      
    #生成云朵2  
    cloud2_enemies = pygame.sprite.Group()  
    add_cloud2_enemies(cloud2_enemies,clouds,1)  
      
    #生成星星  
    star = pygame.sprite.Group()  
      
    #生成普通子弹  
    bullet1 = []  
    bullet1_index = 0  
    BULLET1_NUM = 6  
    for i in range(BULLET1_NUM):  
        bullet1.append(bullet.Bullet1(me.rect.midtop))  
    clock = pygame.time.Clock()  
      
    #生成超级子弹  
    bullet2 = []  
    bullet2_index = 0  
    BULLET2_NUM = 12  
    for i in range(BULLET2_NUM // 2):  
        bullet2.append(bullet.Bullet2((me.rect.centerx - 33,me.rect.centery)))  
        bullet2.append(bullet.Bullet2((me.rect.centerx + 30,me.rect.centery)))  
    clock = pygame.time.Clock()  
          
    #生成激光  
    bullet3 = []  
    bullet3_index = 0  
    BULLET3_NUM = 1  
    for i in range(BULLET3_NUM):  
        bullet3.append(bullet.Bullet3((me.rect.midtop)))  
    clock = pygame.time.Clock()  
          
    #生成火焰弹  
    bullet4 = []  
    bullet4_index = 0  
    BULLET4_NUM = 4  
    for i in range(BULLET4_NUM):  
        bullet4.append(bullet.Bullet4((me.rect.midtop),bg_size))  
    clock = pygame.time.Clock()  
      
    #中弹图片索引  
    e1_destroy_index = 0  
    e2_destroy_index = 0  
    e3_destroy_index = 0  
    e4_destroy_index = 0  
    me_destroy_index = 0  
      
    #统计得分和星星  
    score = 0  
    score_font = pygame.font.Font(r'E:\learn pygame\font\font.ttf',20)  
      
    #统计星星和加载星星图片  
    star_score = 0  
    star_score_font = pygame.font.Font(r'E:\learn pygame\font\font.ttf',20)  
    star_score_image = pygame.image.load(r'E:\learn pygame\image\star_score.png').convert_alpha()  
    star_score_rect = star_score_image.get_rect()  
      
    #标志是否暂停游戏  
    paused = False  
    paused_nor_image = pygame.image.load(r'E:\learn pygame\image\pause_nor.png').convert_alpha()  
    paused_pressed_image = pygame.image.load(r'E:\learn pygame\image\pause_pressed.png').convert_alpha()  
    resume_nor_image = pygame.image.load(r'E:\learn pygame\image\resume_nor.png').convert_alpha()  
    resume_pressed_image = pygame.image.load(r'E:\learn pygame\image\resume_pressed.png').convert_alpha()  
    paused_rect = paused_nor_image.get_rect()  
    paused_rect.left,paused_rect.top = width - paused_rect.width - 10,10  
    paused_image = paused_nor_image  
      
    #游戏暂停画面  
    continues_image = pygame.image.load(r'E:\learn pygame\image\continues.png').convert_alpha()  
    continues_rect = continues_image.get_rect()   
    continues_rect.left,continues_rect.top = \  
                    (width - continues_rect.width) // 2, \  
                    (height - continues_rect.height) // 2  
      
    #设置难度级别  
    level = 1  
      
    #全屏炸弹  
    bomb_image = pygame.image.load(r'E:\learn pygame\image\bomb.png').convert_alpha()  
    bomb_rect = bomb_image.get_rect()  
    bomb_font = pygame.font.Font(r'E:\learn pygame\font\font.ttf',30)  
    bomb_num = 3  
      
    #每30秒发放一个补给包  
    bullet_supply = supply.Bullet_Supply(bg_size)  
    bomb_supply = supply.Bomb_Supply(bg_size)  
    laser_supply = supply.Laser_Supply(bg_size)  
    fire_supply = supply.Fire_Supply(bg_size)  
    me_protect_supply = supply.Me_Protect_Supply(bg_size)  
    life_supply = supply.Life_Supply(bg_size)  
    SUPPLY_TIME = USEREVENT  
    pygame.time.set_timer(SUPPLY_TIME, 18 * 1000)  
      
    #标志是否使用正常子弹  
    is_normal_bullet = True  
      
    #超级子弹定时器  
    DOUBLE_BULLET_TIME = USEREVENT + 1  
      
    #标志是否使用超级子弹  
    is_double_bullet = False  
      
    #解除我方无敌状态定时器  
    INVINCIBLE_TIME = USEREVENT + 2  
      
    #激光定时器  
    LASER_BULLET_TIME = USEREVENT + 3  
      
    #标志是否使用激光  
    is_laser_bullet = False  
      
    #火焰弹定时器  
    FIRE_BULLET_TIME = USEREVENT + 4  
      
    #标志是否使用火焰弹  
    is_fire_bullet = False  
      
    #保护罩定时器  
    ME_PROTECT_BULLET_TIME = USEREVENT + 5  
      
    #标志是否使用保护罩  
    is_me_protect_bullet = False  
  
    #死亡生成星星图片索引  
    s1_star_index = 0  
      
    #生命数量  
    life_image = pygame.image.load(r'E:\learn pygame\image\life.png').convert_alpha()  
    life_rect = life_image.get_rect()  
    life_num = 3  
      
    #游戏开始画面  
    logo_image = pygame.image.load(r'E:\learn pygame\image\logo.png').convert_alpha()  
    logo_rect = logo_image.get_rect()  
    logo_rect.left,logo_rect.top = \  
                (width - logo_rect.width) // 2, \  
                (height - logo_rect.height) // 2  
    begingame_image = pygame.image.load(r'E:\learn pygame\image\begingame.png').convert_alpha()  
    begingame_rect = begingame_image.get_rect()  
    begingame_rect.left,begingame_rect.top = \  
                (width - begingame_rect.width) // 2, \  
                (logo_rect.bottom + 10)  
      
    #游戏结束画面  
    gameover_font = pygame.font.Font(r'E:\learn pygame\font\font.ttf',48)  
    again_image = pygame.image.load(r'E:\learn pygame\image\again.png').convert_alpha()  
    again_rect = again_image.get_rect()  
    gameover_image = pygame.image.load(r'E:\learn pygame\image\gameover.png').convert_alpha()  
    gameover_rect = gameover_image.get_rect()  
      
    #用于阻止重复打开记录文件  
    recorded = False  
      
    #用于切换图片  
    switch_image = True  
      
    #用于延迟  
    delay = 100  
      
    #游戏开始  
    running = True  
      
    #正式开始游戏  
    start = False  
  
    while running:  
      
        for event in pygame.event.get():  
            if event.type == QUIT:  
                pygame.quit()  
                sys.exit()  
              
            elif event.type == MOUSEBUTTONDOWN:  
                if event.button == 1 and paused_rect.collidepoint(event.pos):  
                    paused = not paused  
                    if paused:  
                        pygame.time.set_timer(SUPPLY_TIME,0)  
                        pygame.mixer.music.pause()  
                        pygame.mixer.pause()  
                    else:  
                        pygame.time.set_timer(SUPPLY_TIME,30 * 1000)  
                        pygame.mixer.music.unpause()  
                        pygame.mixer.unpause()                    
            elif event.type == MOUSEMOTION:  
                if paused_rect.collidepoint(event.pos):  
                    if paused:  
                        paused_image = resume_pressed_image  
                    else:  
                        paused_image = paused_pressed_image  
                else:  
                    if paused:  
                        paused_image = resume_nor_image  
                    else:  
                        paused_image = paused_nor_image  
            elif event.type == KEYDOWN:  
                if event.key == K_SPACE:  
                    if bomb_num:  
                        bomb_num -= 1  
                        bomb_sound.play()  
                        for each in enemies:  
                            if each.rect.bottom > 0:  
                                each.active = False  
            elif event.type == SUPPLY_TIME:  
                supply_sound.play()  
                if choice([1,2,3,4,5,6]) == 1:  
                    bomb_supply.reset()  
                elif choice([1,2,3,4,5,6]) == 2:  
                    bullet_supply.reset()  
                elif choice([1,2,3,4,5,6]) == 3:  
                    laser_supply.reset()  
                elif choice([1,2,3,4,5,6]) == 4:  
                    fire_supply.reset()  
                elif choice([1,2,3,4,5,6]) == 5:  
                    me_protect_supply.reset()  
                else:  
                    life_supply.reset()  
            elif event.type == DOUBLE_BULLET_TIME:  
                is_double_bullet = False  
                pygame.time.set_timer(DOUBLE_BULLET_TIME,0)  
            elif event.type == INVINCIBLE_TIME:  
                me.invincible = False  
                pygame.time.set_timer(INVINCIBLE_TIME,0)  
            elif event.type == LASER_BULLET_TIME:  
                is_laser_bullet = False  
                pygame.time.set_timer(LASER_BULLET_TIME,0)  
            elif event.type == FIRE_BULLET_TIME:  
                is_fire_bullet = False  
                is_normal_bullet = True  
                pygame.time.set_timer(FIRE_BULLET_TIME,0)     
            elif event.type == ME_PROTECT_BULLET_TIME:  
                is_me_protect_bullet = False  
                pygame.time.set_timer(ME_PROTECT_BULLET_TIME,0)   
          
        #绘制移动背景   
        for each1 in background1:  
            screen.blit(each1.image,each1.rect)  
            each1.move()  
            if each1.rect.height > 0:  
                for each2 in background2:   
                    screen.blit(each2.image,each2.rect)  
                    each2.move()  
        #根据用户的得分增加难度  
        if level == 1 and score > 100000:  
            level = 2  
            upgrade_sound.play()  
            #增加3架小型敌机、2架中型敌机和1驾大型敌机  
            add_small_enemies(small_enemies,enemies,3)    
            add_mid_enemies(mid_enemies,enemies,2)  
            add_big_enemies(big_enemies,enemies,1)  
            #提高敌机速度  
            inc_speed(1,small_enemies)  
  
            #提高背景速度  
  
        elif level == 2 and score > 300000:  
            level = 3  
            upgrade_sound.play()  
            #增加5架小型敌机、3架中型敌机和2驾大型敌机  
            add_small_enemies(small_enemies,enemies,5)  
            add_mid_enemies(mid_enemies,enemies,3)  
            add_big_enemies(big_enemies,enemies,2)  
            #提高敌机、云朵、背景、星星速度  
            inc_speeds(1,enemies,clouds,star)  
            #inc_speed_background(1,background1)  
            #inc_speed_background(1,background2)  
            inc_speed_me(3,me)  
  
              
        elif level == 3 and score > 8000000:  
            level = 4  
            upgrade_sound.play()  
            #增加5架小型敌机、3架中型敌机、2驾大型敌机和1枚超级炸弹  
            add_small_enemies(small_enemies,enemies,5)  
            add_mid_enemies(mid_enemies,enemies,3)  
            add_big_enemies(big_enemies,enemies,2)  
            add_bomb_enemies(big_enemies,enemies,1)  
            #提高敌机速度  
            inc_speeds(1,enemies,clouds,star)  
            inc_speed_background(1,background1)  
            inc_speed_background(1,background2)  
            inc_speed_me(3,me)  
              
        elif level == 4 and score > 1200000:  
            level = 5  
            upgrade_sound.play()  
            #增加5架小型敌机、3架中型敌机和2驾大型敌机和1枚超级炸弹  
            add_small_enemies(small_enemies,enemies,5)  
            add_mid_enemies(mid_enemies,enemies,3)  
            add_big_enemies(big_enemies,enemies,2)  
            add_bomb_enemies(big_enemies,enemies,1)  
            #提高敌机速度  
            inc_speeds(1,enemies,clouds,star)  
            inc_speed_background(1,background1)  
            inc_speed_background(1,background2)  
            inc_speed_me(3,me)  
              
        #绘制开始界面  
        if not start:  
            screen.blit(logo_image,logo_rect)                                 
            screen.blit(begingame_image,begingame_rect)  
            #检测用户的鼠标操作  
            #如果用户按下鼠标左键  
            if pygame.mouse.get_pressed()[0]:  
                #获取鼠标坐标  
                pos = pygame.mouse.get_pos()  
                #如果用户点击重新开始  
                if begingame_rect.left < pos[0] < begingame_rect.right and \  
                   begingame_rect.top < pos[1] < begingame_rect.bottom:  
                    start = True  
                              
        elif life_num and not paused and start:       
            #检测用户的键盘操作  
            key_pressed = pygame.key.get_pressed()  
              
            if key_pressed[K_w] or key_pressed[K_UP]:  
                me.moveUp()  
            if key_pressed[K_s] or key_pressed[K_DOWN]:  
                me.moveDown()     
            if key_pressed[K_a] or key_pressed[K_LEFT]:  
                me.moveLeft()  
            if key_pressed[K_d] or key_pressed[K_RIGHT]:  
                me.moveRight()  
              
            #绘制云朵  
            for each in cloud1_enemies:  
                each.move()  
                screen.blit(each.image,each.rect)  
                              
            for each in cloud2_enemies:  
                each.move()  
                screen.blit(each.image,each.rect)  
                          
  
              
            #绘制全屏炸弹补给并检测是否获得  
            if bomb_supply.active:  
                bomb_supply.move()  
                screen.blit(bomb_supply.image,bomb_supply.rect)  
                if pygame.sprite.collide_mask(bomb_supply,me):  
                    get_bomb_sound.play()  
                    if bomb_num < 3:  
                        bomb_num += 1  
                    bomb_supply.active = False  
                      
            #绘制超级子弹补给并检测是否获得  
            if bullet_supply.active:  
                bullet_supply.move()  
                screen.blit(bullet_supply.image,bullet_supply.rect)  
                if pygame.sprite.collide_mask(bullet_supply,me):  
                    get_bullet_sound.play()  
                    is_double_bullet = True  
                    pygame.time.set_timer(DOUBLE_BULLET_TIME,18 * 1000)  
                    bullet_supply.active = False  
              
            #绘制激光补给并检测是否获得  
            if laser_supply.active:  
                laser_supply.move()  
                screen.blit(laser_supply.image,laser_supply.rect)  
                if pygame.sprite.collide_mask(laser_supply,me):  
                    get_laser_sound.play()  
                    is_laser_bullet = True  
                    pygame.time.set_timer(LASER_BULLET_TIME,18 * 1000)  
                    laser_supply.active = False  
              
            #绘制火焰弹补给并检测是否获得  
            if fire_supply.active:  
                fire_supply.move()  
                screen.blit(fire_supply.image,fire_supply.rect)  
                if pygame.sprite.collide_mask(fire_supply,me):  
                    get_fire_sound.play()  
                    is_fire_bullet = True  
                    is_normal_bullet = False  
                    pygame.time.set_timer(FIRE_BULLET_TIME,18 * 1000)  
                    fire_supply.active = False  
              
            #绘制保护罩补给并检测是否获得  
            if me_protect_supply.active:  
                me_protect_supply.move()  
                screen.blit(me_protect_supply.image,me_protect_supply.rect)  
                if pygame.sprite.collide_mask(me_protect_supply,me):  
                    get_me_protect_sound.play()  
                    is_me_protect_bullet = True  
                    pygame.time.set_timer(ME_PROTECT_BULLET_TIME,15 * 1000)  
                    me_protect_supply.active = False  
                      
            #绘制生命补给并检测是否获得  
            if life_supply.active:  
                life_supply.move()  
                screen.blit(life_supply.image,life_supply.rect)  
                if pygame.sprite.collide_mask(life_supply,me):  
                    get_life_sound.play()  
                    if life_num < 3:  
                        life_num += 1  
                    life_supply.active = False  
              
            #发射普通子弹、激光、双弹  
            if not(delay % 10):  
                bullet_sound.play()  
                if is_double_bullet:  
                    bullets = bullet2  
                    bullets[bullet2_index].reset((me.rect.centerx - 33,me.rect.centery))  
                    bullets[bullet2_index + 1].reset((me.rect.centerx + 33,me.rect.centery))                  
                    bullet2_index = (bullet2_index + 2) % BULLET2_NUM  
                elif is_laser_bullet:  
                    bullets = bullet3  
                    bullets[bullet3_index].reset((me.rect.centerx - 20,me.rect.top - 70))  
                    bullet3_index = (bullet3_index + 1) % BULLET3_NUM  
                else:  
                    bullets = bullet1  
                    bullets[bullet1_index].reset(me.rect.midtop)  
                    bullet1_index = (bullet1_index + 1) % BULLET1_NUM  
              
            #发生普通子弹、火焰弹  
            if not(delay % 10):       
                if is_normal_bullet:  
                    bullet_sound.play()  
                else:  
                    fire_bullet_sound.play()  
                    if is_fire_bullet:  
                        bullets = bullet4  
                        bullets[bullet4_index].reset((me.rect.centerx - 20,me.rect.top - 70))  
                        bullet4_index = (bullet4_index + 1) % BULLET4_NUM  
                  
            #检测子弹是否击中敌机  
            for b in bullets:  
                if b.active:  
                    b.move()  
                    screen.blit(b.image,b.rect)  
                    enemy_hit = pygame.sprite.spritecollide(b,enemies,False,pygame.sprite.collide_mask)  
                    if enemy_hit:  
                        b.active = False  
                        for e in enemy_hit:                       
                            #火焰弹击中掉2血  
                            if b == bullet4:  
                                if e in mid_enemies or e in big_enemies or e in bomb_enemies:  
                                    e.hit = True  
                                    e.energy -= 2  
                                    #敌机死亡  
                                    if e.energy == 0:  
                                        e.active = False  
                                        #记录敌机死亡位置和生成星星  
                                        enemies_death_down_left,enemies_death_down_top = e.rect.left,e.rect.top  
                                        print(enemies_death_down_left,enemies_death_down_top)  
                                        add_star(star,stars,starenemies_death_down_left,enemies_death_down_top,1)  
                                else:  
                                    e.active = False  
                            #普通子弹击中掉1血  
                            else:  
                                if e in mid_enemies or e in big_enemies or e in bomb_enemies:  
                                    e.hit = True  
                                    e.energy -= 1  
                                    #敌机死亡  
                                    if e.energy == 0:  
                                        e.active = False  
                                    #记录敌机死亡位置和生成星星  
                                        enemies_death_down_left,enemies_death_down_top = e.rect.left,e.rect.top  
                                        print(enemies_death_down_left,enemies_death_down_top)  
                                        add_star(star,stars,enemies_death_down_left,enemies_death_down_top,1)  
                                else:  
                                    e.active = False  
              
            #绘制生成的星星  
            for each in star:  
                if each.active:  
                    each.move()  
                    if not(delay % 3):  
                        screen.blit(each.image,each.rect)  
                        screen.blit(each.star_images[s1_star_index],each.rect)  
                        s1_star_index = (s1_star_index + 1) % 10  
                    star_touch = pygame.sprite.spritecollide(me,star,False,pygame.sprite.collide_mask)  
                    if star_touch:  
                        for s in star_touch:  
                            s.active = False  
                elif each.rect.top > height:  
                    each.active = False  
              
            #绘制敌方超级炸弹  
            for each in bomb_enemies:  
                if each.active:  
                    each.move()  
                    if switch_image:  
                        screen.blit(each.image1,each.rect)  
                    else:  
                        screen.blit(each.image2,each.rect)  
                      
                    #绘制血槽  
                    pygame.draw.line(screen,BLACK, \  
                                        (each.rect.left,each.rect.top - 5), \  
                                        (each.rect.right,each.rect.top - 5), \  
                                        2)  
                    #当生命大于20%显示绿色，否则显示红色  
                    energy_remain = each.energy / enemy.BombEnemy.energy  
                    if energy_remain > 0.2:  
                        energy_color = GREEN  
                    else:  
                        energy_color = RED  
                    pygame.draw.line(screen,energy_color, \  
                                        (each.rect.left,each.rect.top - 5),\  
                                        (each.rect.left + each.rect.width * energy_remain, \  
                                        each.rect.top - 5),2)  
                      
                    #即将出现在画面中，播放音效  
                    if (height + 50) > each.rect.bottom > -50:  
                        bomb_enemy_fly_sound.play(-1)  
                    if each.rect.bottom > (height + 50):  
                        bomb_enemy_fly_sound.stop()  
                        each.reset()  
                else:  
                    #毁灭  
                    if not(delay % 3):  
                        if e4_destroy_index == 0:  
                            bomb_enemy_down_sound.play()                  
                        screen.blit(each.destroy_images[e4_destroy_index],each.rect)  
                        e4_destroy_index = (e4_destroy_index + 1) % 4  
                        if e4_destroy_index == 0:  
                            bomb_enemy_fly_sound.stop()  
                            score += 12000  
                            each.reset()  
              
            #绘制大型敌机  
            for each in big_enemies:  
                if each.active:  
                    each.move()  
                    if each.hit:  
                        #绘制被打到的特效  
                        screen.blit(each.image_hit,each.rect)  
                        each.hit = False  
                    else:     
                        if switch_image:  
                            screen.blit(each.image1,each.rect)  
                        else:  
                            screen.blit(each.image2,each.rect)  
                      
                    #绘制血槽  
                    pygame.draw.line(screen,BLACK, \  
                                        (each.rect.left,each.rect.top - 5), \  
                                        (each.rect.right,each.rect.top - 5), \  
                                        2)  
                    #当生命大于20%显示绿色，否则显示红色  
                    energy_remain = each.energy / enemy.BigEnemy.energy  
                    if energy_remain > 0.2:  
                        energy_color = GREEN  
                    else:  
                        energy_color = RED  
                    pygame.draw.line(screen,energy_color, \  
                                        (each.rect.left,each.rect.top - 5),\  
                                        (each.rect.left + each.rect.width * energy_remain, \  
                                        each.rect.top - 5),2)  
                                          
                                          
                      
                    #即将出现在画面中，播放音效  
                    if height > each.rect.bottom > -50:  
                        enemy3_fly_sound.play(-1)  
                    if each.rect.bottom > height:  
                        enemy3_fly_sound.stop()  
                        each.active = False  
                        each.reset()  
                else:  
                    #毁灭  
                    if not(delay % 3):  
                        if e3_destroy_index == 0:  
                            enemy3_down_sound.play(-1)  
                        screen.blit(each.destroy_images[e3_destroy_index],each.rect)  
                        e3_destroy_index = (e3_destroy_index + 1) % 6  
                        if e3_destroy_index == 0:  
                            enemy3_fly_sound.stop()  
                            score += 10000  
                            each.reset()  
                      
            #绘制中型敌机  
            for each in mid_enemies:  
                if each.active:  
                    each.move()  
                    if each.hit:  
                        #绘制被打到的特效  
                        screen.blit(each.image_hit,each.rect)  
                        each.hit = False  
                    else:  
                        screen.blit(each.image,each.rect)  
                  
                    #绘制血槽  
                    pygame.draw.line(screen,BLACK, \  
                                        (each.rect.left,each.rect.top - 5), \  
                                        (each.rect.right,each.rect.top - 5), \  
                                        2)  
                    #当生命大于20%显示绿色，否则显示红色  
                    energy_remain = each.energy / enemy.MidEnemy.energy  
                    if energy_remain > 0.2:  
                        energy_color = GREEN  
                    else:  
                        energy_color = RED  
                    pygame.draw.line(screen,energy_color, \  
                                        (each.rect.left,each.rect.top - 5),\  
                                        (each.rect.left + each.rect.width * energy_remain, \  
                                        each.rect.top - 5),2)  
                  
                else:  
                    #毁灭  
                    if not(delay % 3):  
                        if e2_destroy_index == 0:  
                            enemy2_down_sound.play()  
                        screen.blit(each.destroy_images[e2_destroy_index],each.rect)  
                        e2_destroy_index = (e2_destroy_index + 1) % 4  
                        if e2_destroy_index == 0:  
                            score += 6000  
                            each.reset()  
                                                                                                  
            #绘制小型敌机  
            for each in small_enemies:  
                if each.active:  
                    each.move()  
                    screen.blit(each.image,each.rect)  
                else:  
                    #毁灭  
                    if not(delay % 3):  
                        if e1_destroy_index == 0:  
                            enemy1_down_sound.play()                  
                        screen.blit(each.destroy_images[e1_destroy_index],each.rect)  
                        e1_destroy_index = (e1_destroy_index + 1) % 4  
                        if e1_destroy_index == 0:  
                            score += 1000  
                            each.reset()  
                                          
            #检测我方飞机是否被撞  
            enemies_down = pygame.sprite.spritecollide(me,enemies,False,pygame.sprite.collide_mask)  
            if enemies_down and not me.invincible:  
                  
                #开启保护罩保护功能  
                if is_me_protect_bullet:  
                    me.active = True  
                else:  
                    me.active = False  
                for e in enemies_down:  
                    e.active = False  
              
  
            #绘制保护罩  
            if is_me_protect_bullet:  
                if switch_image:  
                    screen.blit(me.image1,me.rect)  
                    screen.blit(me.image3,me.rect)  
                else:  
                    screen.blit(me.image2,me.rect)  
            #绘制我方飞机  
            elif me.active:  
                if switch_image:  
                    screen.blit(me.image1,me.rect)  
                else:  
                    screen.blit(me.image2,me.rect)  
            #毁灭  
            else:                 
                if not(delay % 3):  
                    if me_destroy_index == 0:  
                        me_down_sound.play()  
                    screen.blit(me.destroy_images[me_destroy_index],me.rect)  
                    me_destroy_index = (me_destroy_index + 1) % 4  
                    if me_destroy_index == 0:  
                        life_num -= 1  
                        me.reset()  
                        pygame.time.set_timer(INVINCIBLE_TIME, 3 * 1000)  
                      
            #绘制全屏炸弹数量  
            bomb_text = bomb_font.render('x %d' % bomb_num,True,WHITE)  
            text_rect = bomb_text.get_rect()  
            screen.blit(bomb_image,(0,height - bomb_rect.height))  
            screen.blit(bomb_text,(bomb_rect.width - 10,height - 10 - text_rect.height))  
          
            #绘制剩余生命数量  
            if life_num:  
                for i in range(life_num):  
                    screen.blit(life_image, \  
                                (width - 10 - (i + 1) * life_rect.width, \  
                                height - 10 - life_rect.height))  
            #绘制得分  
            score_text = score_font.render('Score:%s' % str(score),True,WHITE)  
            screen.blit(score_text,(10,5))  
            star_score_text = star_score_font.render('Stars:%s' % str(star_score),True,WHITE)  
            screen.blit(star_score_text,(10,25))  
          
            #绘制暂停按钮  
            screen.blit(paused_image,paused_rect)  
              
        #绘制暂停游戏界面  
        elif paused:  
            screen.blit(continues_image,continues_rect)  
            #检测用户的鼠标操作  
            #如-果用户按下鼠标左键  
            if pygame.mouse.get_pressed()[0]:  
                #获取鼠标坐标  
                pos = pygame.mouse.get_pos()  
                #如果用户点击继续游戏  
                if continues_rect.left < pos[0] < continues_rect.right and \  
                   continues_rect.top < pos[1] < continues_rect.bottom:  
                    paused = not paused  
                    pygame.time.set_timer(SUPPLY_TIME,30 * 1000)  
                    pygame.mixer.music.unpause()  
                    pygame.mixer.unpause()  
              
        #绘制游戏结束界面  
        elif life_num == 0:  
            #背景音乐停止  
            pygame.mixer.music.stop()  
              
            #停止全部音效  
            pygame.mixer.stop()  
              
            #停止发放补给  
            pygame.time.set_timer(SUPPLY_TIME,0)  
              
            if not recorded:  
                recorded = True  
              
                #读取历史最高得分  
                with open(r'E:\learn pygame\record.txt','r') as f:  
                    record_score = int(f.readline())  
                    record_star_score = int(f.readline())  
                  
                #如果玩家得分高于历史最高得分，则存档  
                if score > record_score or star_score > record_star_score:  
                    with open(r'E:\learn pygame\record.txt','w') as f:  
                        if score > record_score and star_score <= record_star_score:  
                            f.write('{0}{1}{2}'.format(str(score),'\n',str(record_star_score)))  
                        elif score <= record_score and star_score > record_star_score :  
                            f.write('{0}{1}{2}'.format(str(score),'\n',str(star_score)))  
                        elif score > record_score and star_score > record_star_score:  
                            f.write('{0}{1}{2}'.format(str(score),'\n',str(star_score)))  
            #绘制结束画面  
            record_score_text = score_font.render('Best : %d' % record_score,True,WHITE)  
            screen.blit(record_score_text,(20,20))  
            star_score_text = star_score_font.render('Total : %d' % record_star_score,True,WHITE)  
            screen.blit(star_score_text,(20,60))  
              
            gameover_text1 = gameover_font.render('Your Score',True,WHITE)  
            gameover_text1_rect = gameover_text1.get_rect()  
            gameover_text1_rect.left,gameover_text1_rect.top = \  
                                (width - gameover_text1_rect.width) // 2, \  
                                (height - gameover_text1_rect.bottom) // 2  
            screen.blit(gameover_text1,gameover_text1_rect)  
              
            gameover_text2 = gameover_font.render(str(score),True,WHITE)  
            gameover_text2_rect = gameover_text2.get_rect()  
            gameover_text2_rect.left,gameover_text2_rect.top = \  
                                (width - gameover_text2_rect.width) // 2, \  
                                gameover_text1_rect.bottom + 10  
            screen.blit(gameover_text2,gameover_text2_rect)  
              
            again_rect.left,again_rect.top = \  
                        (width - again_rect.width) // 2, \  
                        gameover_text2_rect.bottom + 50  
            screen.blit(again_image,again_rect)  
              
            gameover_rect.left,gameover_rect.top = \  
                        (width - again_rect.width) // 2, \  
                        again_rect.bottom + 10  
            screen.blit(gameover_image,gameover_rect)  
              
            #检测用户的鼠标操作  
            #如果用户按下鼠标左键  
            if pygame.mouse.get_pressed()[0]:  
                #获取鼠标坐标  
                pos = pygame.mouse.get_pos()  
                #如果用户点击重新开始  
                if again_rect.left < pos[0] < again_rect.right and \  
                   again_rect.top < pos[1] <again_rect.bottom:  
                    #调用main函数，重新开始游戏  
                    main()  
                #如果用户点击结束游戏  
                elif gameover_rect.left < pos[0] < gameover_rect.right and \  
                     gameover_rect.top < pos[1] <gameover_rect.bottom:  
                    #退出游戏  
                    pygame.quit()  
                    sys.exit(0)  
          
        #切换图片  
        if not(delay % 5):  
            switch_image = not switch_image  
              
        delay -= 1  
        if not delay:  
            delay = 100  
      
        pygame.display.flip()  
        clock.tick(60)  
          
if __name__ == '__main__':  
    try:  
        main()  
    except SystemError:  
        pass  
    except:  
        traceback.print_exc()  
        pygame.quit()  
        input()  
