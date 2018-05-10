import pygame
from PlanSprite import *
HERO_FIRE_EVENT = pygame.USEREVENT + 1
#CREATE_ENEMY_EVENT = pygame.USEREVENT
class PlanGame(object):
	def __init__(self):
		print("游戏初始化...")
		SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
		self.screen=pygame.display.set_mode(SCREEN_RECT.size)
		self.clock=pygame.time.Clock()
		pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
		self.__create_sprite()
		self.enemy_group = pygame.sprite.Group()
		pygame.time.set_timer(HERO_FIRE_EVENT, 500)
		pass
	def startGame(self):
		print("开始游戏")
		while True:
			self.clock.tick(FRAME_PER_SEC)
			self.__event_handler()
			self.__check_collide()
			self.__update_sprites()
			pygame.display.update()
			pass
	def __create_sprite(self):
		background=Background()
		background1=Background(True)
		self.back_ground=pygame.sprite.Group(background,background1)
		self.hero = Hero()
		self.hero_group = pygame.sprite.Group(self.hero)
		
		
	def __event_handler(self):
		for event in pygame.event.get():
			# 判断是否退出游戏
			if event.type == pygame.QUIT:
				PlaneGame.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:
				print("敌机出场...")
				enemy = Enemy()
				self.enemy_group.add(enemy)
			elif event.type == HERO_FIRE_EVENT:
				self.hero.fire()
		# 获取用户按键
		keys_pressed = pygame.key.get_pressed()

		if keys_pressed[pygame.K_RIGHT]:
			self.hero.speed = 2
		elif keys_pressed[pygame.K_LEFT]:
			self.hero.speed = -2
		elif keys_pressed[pygame.K_UP]:
			self.hero.speed1 = -2
		elif keys_pressed[pygame.K_DOWN]:
			self.hero.speed1 = 2
		else:
			self.hero.speed = 0
			self.hero.speed1 = 0
	def __check_collide(self):
		# 1. 子弹摧毁敌机
		pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

# 2. 敌机撞毁英雄
		enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

# 判断列表时候有内容
		if len(enemies) > 0:

# 让英雄牺牲
			self.hero.kill()

# 结束游戏
			PlaneGame.__game_over()
	def __update_sprites(self):
		self.back_ground.update()
		self.back_ground.draw(self.screen)
		self.enemy_group.update()
		self.enemy_group.draw(self.screen)
		self.hero_group.update()
		self.hero_group.draw(self.screen)
		self.hero.bullets.update()
		self.hero.bullets.draw(self.screen)
		
	#@staticmethod
	def __game_over(self):
		print("游戏结束")
		pygame.quit()
		exit()
if __name__ == "__main__":
	plangame = PlanGame()
	plangame.startGame()
