import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    pygame.init()                                                          
    ai_settings = Settings()                         #创建Setting的实例
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    play_button = Button(ai_settings,screen,'Play')

    stats = GameStats(ai_settings)                          #创建一个用于统计游戏信息的实例
    sb = Scoreboard(ai_settings,screen,stats)

    ship = Ship(ai_settings,screen)                             #创建Ship的实例
    bullets = Group()                                       #从Group()创建实例，这个实例是全局的？不太懂
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)  
   
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)        #检测点击事件
        if stats.game_active:
            ship.update()                                                            #更新飞船的坐标
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)                              #更新子弹组的坐标
            gf.update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets)                                #更新外星人组的坐标
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)       #刷新屏幕的所有显示                  

run_game()