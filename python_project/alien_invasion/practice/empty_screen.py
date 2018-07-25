import sys
import pygame
                  

def run_game():
    pygame.init()                                   
    screen = pygame.display.set_mode((1200,800))    
    pygame.display.set_caption('Print Press')    
    bg_color = (190,190,190)                        

    while True:
        for event in pygame.event.get():           
            if event.type == pygame.QUIT:           
                sys.exit()   
            elif event.type == pygame.KEYDOWN:
                print(event.key)                  
        screen.fill(bg_color)                      
        pygame.display.flip()                    

run_game()


