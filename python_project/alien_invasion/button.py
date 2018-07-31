import pygame.font

class Button():
    def __init__(self,ai_settings,screen,msg):
            #初始化按钮
        self.screen = screen
        self.screen_rect = screen.get_rect()
            #设置按钮属性
        self.width , self.height = 200 , 50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)
            #设置按钮的rect对象，使其居中
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
            #按钮标签只需创建1次
        self.prep_msg(msg)

    def prep_msg(self,msg):
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)  #render将文本转换为图像，布尔值决定是否开起反锯齿。
                                                                                        #如果不指定背景色，将以透明背景的方式渲染文本。
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)           #绘制表示按钮的矩形
        self.screen.blit(self.msg_image,self.msg_image_rect)       #再绘制表示文本的图像