import pygame
from PlanSpritetest import *
HERO_FIRE_EVENT = pygame.USEREVENT + 1
list_bullet=[]
#resolution=0
class PlanGame(object):
	def __init__(self):
		print("游戏初始化...")
		SCREEN_RECT = pygame.Rect(0,0,480,700)
		self.screen=pygame.display.set_mode(SCREEN_RECT.size)
		self.clock=pygame.time.Clock()
		pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
		self.__create_sprite()
		self.enemy_group = pygame.sprite.Group()
		#self.enemy_collide_group = pygame.sprite.Group()
		pygame.time.set_timer(HERO_FIRE_EVENT,500)
		#resolution=0
		pass
	def startGame(self):
		print("开始游戏")
		resolution=0
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
			#elif event.key == K_space:  #获取键盘空格键
			#	pass
			elif event.type == HERO_FIRE_EVENT:
				self.hero.fire()
			#elif event.type == pygame.KEYDOWN and event.key == pygame.K_space:
			#	pass
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
		for i in self.hero.bullets:
			for j in self.enemy_group:
				if i.rect in j.rect:
					 
		i=1
		#@Global resolution
		#resolution=0
		k=pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
		if k != "{<Bullet sprite(in 0 groups)>: [<Enemy sprite(in 0 groups)>]}":
		#if k == None:
			list_bullet.append(i)
			print("起作用了..")
			resolution=0
			for temp in list_bullet:
				resolution+=temp
				print("什么鬼啊...")
		print("击落敌机数:%d"%resolution)
		#	image_name1 = EnemyCollide("./images/enemy0_down1.png")
		#	self.screen.blit(image_name0,image_name1.rect.size)
		#	image_name2 = EnemyCollide("./images/enemy0_down2.png")
		#	self.screen.blit(image_name0,image_name2.rect.size)
		#	image_name3 = EnemyCollide("./images/enemy0_down3.png")
		#	self.screen.blit(image_name0,image_name3.rect.size)
		#	image_name4 = EnemyCollide("./images/enemy0_down4.png")
		#	self.screen.blit(image_name4,image_name4.rect.size)
		#	self.enemy_collide_group.add(image_name1,image_name2,image_name3,image_name4)

		# 2. 敌机撞毁英雄
		enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
		print(enemies)
		# 判断列表时候有内容
		if len(enemies) > 0:
			# 让英雄牺牲
			self.hero.kill()
			# 结束游戏
			PlaneGame.__game_over()
#	def __EnmeyCollide(self):
#		for 
	def __update_sprites(self):
		self.back_ground.update()
		self.back_ground.draw(self.screen)
		self.enemy_group.update()
		self.enemy_group.draw(self.screen)
		self.hero_group.update()
		self.hero_group.draw(self.screen)
		self.hero.bullets.update()
		self.hero.bullets.draw(self.screen)
		#self.enemy_collide_group.draw(self.screen)
	def __game_over(self):
		print("游戏结束")
		pygame.quit()
		exit()
if __name__ == "__main__":
	plangame = PlanGame()
	plangame.startGame()
