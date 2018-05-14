import pygame
import random
SCREEN_RECT = pygame.Rect(0,0,480,700)
FRAME_PER_SEC = 300 
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1
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
	def update(self):  #,*args):
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
#class Count(GameSprite):
#	def __init__+
class EnemyCollide(GameSprite):
	def __init__(self,image_name):
		super().__init__()
		#	self.image.name=image_name
			
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
		self.bullets = pygame.sprite.Group()
	def update(self):  #,*args):

		self.rect.x += self.speed
		self.rect.y += self.speed1
		# 获取用户按键
		if self.rect.left < 0:
			self.rect.left = 0
		elif self.rect.right > SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right
		elif self.rect.bottom < 0:
			self.rect.y = SCREEN_RECT.height
		elif self.rect.y > SCREEN_RECT.height:
			self.rect.bottom = 0
	def fire(self):
		print("发射子弹...")
		bullet = Bullet()
		# 2. 设置精灵的位置
		bullet.rect.bottom = self.rect.y - 20
		bullet.rect.centerx = self.rect.centerx
		# 3. 将精灵添加到精灵组
		self.bullets.add(bullet)
class Bullet(GameSprite):
#"""子弹精灵"""
	def __init__(self):
		super().__init__("./images/bullet1.png", -5)
	def update(self):
		super().update()
	# 判断是否超出屏幕，如果是，从精灵组删除
		if self.rect.bottom < 0:
			self.kill()

class EnemyCollide():
	def __init__(self):
		image_name1 = EnemyCollide("./images/enemy0_down1.png")
		self.screen.blit(image_name0,image_name1.rect.size)
		image_name2 = EnemyCollide("./images/enemy0_down2.png")
		self.screen.blit(image_name0,image_name2.rect.size)
		image_name3 = EnemyCollide("./images/enemy0_down3.png")
		self.screen.blit(image_name0,image_name3.rect.size)
		image_name4 = EnemyCollide("./images/enemy0_down4.png")
		self.screen.blit(image_name4,image_name4.rect.size)
		self.enemy_collide_group.add(image_name1,image_name2,image_name3,image_name4)
