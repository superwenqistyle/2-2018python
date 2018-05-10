import pygame
from PlanSprite import *
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
		
		
	def __event_handler(self):
		for event in pygame.event.get():
			# 判断是否退出游戏
			if event.type == pygame.QUIT:
				PlaneGame.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:
				print("敌机出场...")
				enemy = Enemy()
				self.enemy_group.add(enemy)
	def __check_collide(self):
		pass
	def __update_sprites(self):
		self.back_ground.update()
		self.back_ground.draw(self.screen)
		self.enemy_group.update()
		self.enemy_group.draw(self.screen)
	def __game_over(self):
		print("游戏结束")
		pygame.quit()
		exit()
if __name__ == "__main__":
	plangame = PlanGame()
	plangame.startGame()
