import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        super().__init__()                   #继承Sprite的__init__()
        self.screen = screen

        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)         #pygame.Rect在0，0处创建一个矩形，并定义了宽高。
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y               #更新表示子弹的rect的位置

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)          #绘制子弹