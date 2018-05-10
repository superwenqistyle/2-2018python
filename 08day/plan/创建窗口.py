#import time
import pygame
pygame.init()
clock=pygame.time.Clock()
hero_rect=pygame.Rect(100,500,120,126)
screan = pygame.display.set_mode((480,700))
bg=pygame.image.load("./images/background.png")
screan.blit(bg,(0,0))
#pygame.display.update()
hero=pygame.image.load("./images/hero.gif")
screan.blit(hero,(200,500))
pygame.display.update()
while True:
	hero_rect.y-=10
	if hero_rect.y+hero_rect.height <= 0:
		hero_rect.y=700
	#if hero_rect.bottom <= 0:
	#	hero_rect.y == 500
	clock.tick(100)
	screan.blit(bg,(0,0))
	screan.blit(hero,hero_rect)
	pygame.display.update()
	#if hero_rect == 0:
	#	hero_rect.y=500
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print("退出游戏....")
			pygame.quit()
			exit()

	
'''
for event in pygame.event.get():

# 判断用户是否点击了关闭按钮
	if event.type == pygame.QUIT:
		print("退出游戏...")

		pygame.quit()

# 直接退出系统
		exit()
#while True:
#	pass 
'''
#time.sleep(5)
#pygame.quit()
