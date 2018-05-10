import pygame
import random
SCREEN_RECT = pygame.Rect(0,0,480,700)
FRAME_PER_SEC = 60
CREATE_ENEMY_EVENT = pygame.USEREVENT
#精灵类
class GameSprite(pygame.sprite.Sprite):
	def __init__(self, image_name, speed=1):
		# 调用父类的初始化方法
		super().__init__()

		# 加载图像
		self.image = pygame.image.load(image_name)
		# 设置尺寸
		self.rect = self.image.get_rect()
		# 记录速度
		self.speed = speed



	def update(self):
		self.rect.y += self.speed
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
		#self.rect.x=random.randint(0,480-self.rect.x)
	#	k=random.randint(0,50)
		self.speed=random.randint(1,10)
		self.rect.bottom=0
		if self.rect.x == 480:
			self.rect.x-=10
		elif self.rect.x == 0:
			self.rect.x+=10
	
	def update(self):
		super().update()
