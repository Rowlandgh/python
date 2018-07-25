import sys
import pygame

class Ship():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('practice\ship.bmp')    
        self.rect = self.image.get_rect()                       #get_rect()获取相应surface的属性rect
        self.screen_rect = screen.get_rect()                    

        self.rect.centerx = self.screen_rect.centerx            #把飞船的中心点x坐标设为屏幕矩形的属性centerx
        self.rect.bottom = self.screen_rect.bottom/2              #把飞船下边缘的y坐标设为屏幕矩形的属性bottom的中点

    def blitme(self):
        self.screen.blit (self.image,self.rect)                 #blit把图像按照坐标绘制在屏幕上

def run_game():
    pygame.init()                                   #初始化背景
    screen = pygame.display.set_mode((1200,800))    
    pygame.display.set_caption('Blue Window')    
    bg_color = (0,0,255)                        #设置背景色，RGB值，蓝色。
    ship = Ship(screen)

    while True:
        for event in pygame.event.get():           
            if event.type == pygame.QUIT:           
                sys.exit()                          
        screen.fill(bg_color)                       #用背景色填充屏幕。
        ship.blitme()                               #显示飞船
        pygame.display.flip()                       #更新屏幕

run_game()


