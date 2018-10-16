# coding=utf-8
import sys
import pygame

class settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

class Ship():
    def __init__(self,screen):

        #加载屏幕图像，获取其外接矩形
        self.screen = screen
        self.image = pygame.image.load(r"C:\WorkSpace\Project\Alien_Invasion\images\ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘飞船放到屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    def blit(self):
        self.screen.blit(self.image,self.rect)

def  display_spacecraft():
    pygame.init()
    ai_settings = settings()
    pygame.display.set_caption("Alien Invasion")
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship = Ship(screen)
   #监视鼠标和键盘事件

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
         #显示
        screen.fill(ai_settings.bg_color)
        ship.blit()
        pygame.display.flip()


display_spacecraft()



