import pygame
#SCREEN.RECT=pygame.rect(0,0,480,700)
class Gamesprite(pygame.sprite.Sprite):
	def __init__(self,image_name,speed=1):
		super().__init__()
		self.image=pygame.image.load(image_name)
		self.rect=self.image.get_rect()
		self.speed=speed
	def update(self):
		self.rect.y+=self.speed
