import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()                                                          
    ai_settings = Settings()                         #创建Setting的实例
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(ai_settings,screen)                             #创建Ship的实例
    bullets = Group()

    while True:
        gf.check_events(ship,bullets)                       #检测点击事件
        ship.update()                                       #刷新飞船的位置
        bullets.update()                                    #刷新子弹位置     
        gf.update_screen(ai_settings,screen,ship,bullets)   #刷新屏幕                   

run_game()

