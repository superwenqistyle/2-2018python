import pygame
from planesprite import *
import time
pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((480,700))
background=pygame.image.load("./images/background.png")
screen.blit(background,(0,0))
hero=pygame.image.load("./images/hero.gif")
screen.blit(hero,(240,500))
hero_rect=pygame.Rect(240,500,200,200)
enemy1=Gamesprite("./images/enemy1.png")
enemy2=Gamesprite("./images/enemy1.png",2)
enemy2.rect.x=200
enemy_group=pygame.sprite.Group(enemy1,enemy2)
#enemy_group.update()
#enemy_group.draw(screen)
while True:
	clock.tick(60)
	hero_rect.y-=10
	if hero_rect.bottom <= 0:
		hero_rect.y=700
	screen.blit(background,(0,0))
	screen.blit(hero,hero_rect)
	enemy_group.update()
	enemy_group.draw(screen)
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
			print("退出系统........")
			time.sleep(3)
	

