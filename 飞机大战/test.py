# coding=utf8
import random
import pygame
from pygame.locals import *
from cStringIO import StringIO
from PIL import Image
from random import randint as rint


class MySprite(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # extend the base Sprite class
        self.master_image = None
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0
        self.direction = 0
        self.velocity = Point(0.0, 0.0)

    # X property
    def _getx(self): return self.rect.x

    def _setx(self, value): self.rect.x = value
    X = property(_getx, _setx)

    # Y property
    def _gety(self): return self.rect.y

    def _sety(self, value): self.rect.y = value
    Y = property(_gety, _sety)

    # position property
    def _getpos(self): return self.rect.topleft

    def _setpos(self, pos): self.rect.topleft = pos
    position = property(_getpos, _setpos)

    def load(self, filename, width, height, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.rect = Rect(0, 0, width, height)
        self.columns = columns
        # try to auto-calculate total frames
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

    def update(self, current_time, rate=30):
        # update animation frame number
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time

        # build current frame only if it changed
        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = Rect(frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame

    def __str__(self):
        return str(self.frame) + "," + str(self.first_frame) + \
            "," + str(self.last_frame) + "," + str(self.frame_width) + \
            "," + str(self.frame_height) + "," + str(self.columns) + \
            "," + str(self.rect)

# Point class


class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    # X property
    def getx(self): return self.__x

    def setx(self, x): self.__x = x
    x = property(getx, setx)

    # Y property
    def gety(self): return self.__y

    def sety(self, y): self.__y = y
    y = property(gety, sety)

    def __str__(self):
        return "{X:" + "{:.0f}".format(self.__x) + \
            ",Y:" + "{:.0f}".format(self.__y) + "}"


pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("SimpleSample")
timer = pygame.time.Clock()
flame_group = pygame.sprite.Group()


def cropimg(image, region):
    img = Image.open(image)
    # region = (64, 0, 192, 95)
    cropImg = img.crop(region)
    imgBuf = StringIO(cropImg.tobytes())
    imgx = pygame.image.frombuffer(
        imgBuf.getvalue(), (region[2] - region[0], region[3] - region[1]), "RGBA")
    return imgx


img = r'resources/images/map.png'
region = (0, 97, 160, 223)
imgx = cropimg(img, region)

boomnum = 0
while True:
    boomnum += 1
    if boomnum % 13 == 1:
        flame = MySprite()
        flame.load("resources/images/flame.png", 64, 64, 4)
        flame.position = rint(150, 300), rint(150, 300)
        flame_group.add(flame)
    elif boomnum > 130:
        flame_group.remove(flame)
    print(boomnum)
    timer.tick(60)
    ticks = pygame.time.get_ticks()
    screen.fill((50, 205, 50))
    screen.blit(imgx, (200, 200))
    # draw sprite
    flame_group.update(ticks)
    flame_group.draw(screen)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        exit()

