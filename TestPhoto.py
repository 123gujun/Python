# coding=utf-8
import sys
import pygame
import game_function as gf
from ship import Ship

class settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)



def  display_spacecraft():
    pygame.init()
    ai_settings = settings()
    pygame.display.set_caption("Alien Invasion")
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship = Ship(screen)
   #监视鼠标和键盘事件

    while True:
        gf.check_events(ship)
         #显示
        gf.update_screen(ai_settings,screen,ship)
display_spacecraft()



