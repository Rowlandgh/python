import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    def __init__(self,ai_settings,screen,stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        self.prep_image()

    def prep_image(self):
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings,self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
    
    def prep_score(self):
        rounded_score = round(self.stats.score,-1)      #round函数的第二个参数指精确到小数点后几位，负数就是10,100,1000
        score_str = '{:,}'.format(rounded_score)        #字符串格式设置，将数值转为字符串时插入逗号。
        self.score_image = self.font.render('Score:' + score_str,True,self.text_color,self.ai_settings.bg_color)   #字符串转成图像

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20                  #放到屏幕右上角
        self.score_rect.top = 20

    def prep_level(self):
        self.level_image = self.font.render('Level:' + str(self.stats.level),True,self.text_color,self.ai_settings.bg_color)
        self.level_rect = self. level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_high_score(self):
        high_score = int (round(self.stats.high_score,-1))
        high_score_str = '{:,}'.format(high_score)
        self.high_score_image = self.font.render('HighScore:' + high_score_str,True,self.text_color,self.ai_settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)