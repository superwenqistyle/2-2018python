import pygame
import time
import random
SCREEN_RECT = pygame.Rect(0,0,480,700)
FRAME_PER_SEC = 300 
CREATE_ENEMY_EVENT = pygame.USEREVENT
#精灵类
class GameSprite(pygame.sprite.Sprite):
	def __init__(self, image_name,speed=1,speed1=0):  #,x_speed=0,y_speed=0):
		# 调用父类的初始化方法
		super().__init__()

		# 加载图像
		self.image = pygame.image.load(image_name)
		# 设置尺寸
		self.rect = self.image.get_rect()
		# 记录速度
		self.speed = speed
		self.speed1 = speed1
		#self.x_speed=x_speed
		#self.y_speed=y_speed


	def update(self):  #,*args):
		self.rect.y += self.speed
		#self.rect+=x_speed
		#self.rect+=y_speed
class Background(GameSprite):
	def __init__(self,is_alt=False):
		image_name="./images/background.png"
		super().__init__(image_name)
		if is_alt:
			self.rect.y=-SCREEN_RECT.height
		
		pass
	def update(self):
		super().update()
		if self.rect.y >= SCREEN_RECT.height:
			self.rect.y = -SCREEN_RECT.height
class Enemy(GameSprite):
	def __init__(self):
		image_name = "./images/enemy-1.gif"
		super().__init__(image_name)
		self.rect.x=random.randint(0,480-self.rect.x)
		self.speed=random.randint(1,10)
		self.rect.bottom=0
	def update(self):
		super().update()
		if self.rect.y == SCREEN_RECT.height:
			self.kill()
	def __del__(self):
		print("删除")
class Hero(GameSprite):
	def __init__(self):
		super().__init__("./images/hero.gif",0,0)
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120
		#pygame.time.set_timer(HERO_FIRE_EVENT, 500)
		
		self.bullets = pygame.sprite.Group()
	def update(self):  #,*args):
		#super().update()

		# 飞机水平移动
		self.rect.x += self.speed
		self.rect.y += self.speed1
		#self.rect.y += self.y_speed
		# 获取用户按键

		if self.rect.left < 0:
			self.rect.left = 0
		elif self.rect.right > SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right
		elif self.rect.bottom < 0:
			self.rect.y = SCREEN_RECT.height
		elif self.rect.y > SCREEN_RECT.height:
			self.rect.bottom = 0
		#elif self.rect.right > SCREEN_RECT.right:
		#	self.rect.right = SCREEN_RECT.right
	def fire(self):
		print("发射子弹...")
	#	k = int(input("输入模式:1.三连射 2.单射"))
	#	if k == 1:
	#	for i in (1, 2, 3):
		#1. 创建子弹精灵
		bullet = Bullet()
		# 2. 设置精灵的位置
		bullet.rect.bottom = self.rect.y - 20
		bullet.rect.centerx = self.rect.centerx
		# 3. 将精灵添加到精灵组
		self.bullets.add(bullet)
		#	time.sleep(1)
		#elif k ==2:
		#	for i in (1,2,3):
		#		bullet=Bullet()
		#		bullet.rect.rect.bottom=self.rect.y - 60*i
		#		bullet.rect.centerx = self.rect.centerx
		#		self.bullets.add(bullet)
class Bullet(GameSprite):
#"""子弹精灵"""
	def __init__(self):
		super().__init__("./images/bullet1.png", -2)
	def update(self):
		super().update()
	# 判断是否超出屏幕，如果是，从精灵组删除
		if self.rect.bottom < 0:
			self.kill()

