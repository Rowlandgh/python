import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        super().__init__()                                   #super(ship,self).__init__()
            #初始化飞船
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('D:\\python_git\\python_project\\alien_invasion\\images\\ship.bmp')       #pygame.image.load()加载图片
            #设定飞船的起始位置
        self.rect = self.image.get_rect()                       #get_rect()获取相应surface的属性rect
        self.screen_rect = screen.get_rect()                    #获取屏幕的矩形
        self.rect.centerx = self.screen_rect.centerx            #把飞船的中心点x坐标设为屏幕矩形的属性centerx
        self.rect.bottom = self.screen_rect.bottom              #把飞船下边缘的y坐标设为屏幕矩形的属性bottom.
            #在飞船的center属性中储存小数
        self.center = float(self.rect.centerx)
            #移动标志
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:        #self.rect.right返回矩形右边缘的x坐标。
            self.center += self.ai_settings.ship_speed_factor           
        if self.moving_left and self.rect.left > self.screen_rect.left:           #禁止飞出边缘
            self.center -= self.ai_settings.ship_speed_factor
            #根据self.center更新rect的对象center
        self.rect.centerx = self.center                                #更新飞船的位置坐标

    def blitme(self):
        self.screen.blit (self.image,self.rect)                 #blit把图像按照坐标绘制在屏幕上

    def center_ship(self):
        self.center = self.screen_rect.centerx