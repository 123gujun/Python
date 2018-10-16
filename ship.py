# coding=utf-8
import pygame
class Ship():
    def __init__(self,screen):

        #加载屏幕图像，获取其外接矩形
        self.screen = screen
        self.image = pygame.image.load(r"C:\WorkSpace\Project\Alien_Invasion\Python\images\ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘飞船放到屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    def blitme(self):
        self.screen.blit(self.image,self.rect)