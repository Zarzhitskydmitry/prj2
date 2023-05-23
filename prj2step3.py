import pygame
import random
import sys
import time

max_x = 1920                                                         # задаем разрешение экрана x и y
max_y = 1080
max_snow = 400
snow_size = 64
snowfall = []

pygame.init()                                                       # инициилизируем pygame
pygame.display.set_caption("My second videogame on python(pygame)")
screen = pygame.display.set_mode((max_x, max_y), pygame.FULLSCREEN) 
bg_color = (0, 0, 0)

class snow():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(1, 3)
        self.img_num = random.randint(1, 4)
        self.img_file = "snow" + str(self.img_num) + ".png"
        self.image = pygame.image.load(self.img_file).convert_alpha()
        self.image = pygame.transform.scale(self.image, (snow_size, snow_size))
    
    def move_snow(self):
        self.y = self.y + self.speed        
        if self.y > max_y:
            self.y = (0 - snow_size)
        i = random.randint(1, 20)      
        if i == 1:                      # move right
            self.x += 2 
            if self.x > max_x:
                self.x = (0 - snow_size)
        elif i == 3: 
            self.x -= 2   
            if self.x < (0 - snow_size):
                self.x = max_x     
    def draw_snow(self):
        screen.blit(self.image, (self.x, self.y))

def init_snow(max_snow, snowfall):
    for i in range(0, max_snow):
        xx = random.randint(0, max_x)
        yy = random.randint(0, max_y)
        snowfall.append(snow(xx, yy))

def check_for_exit():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            sys.exit()
 
init_snow(max_snow, snowfall)

while True:
    check_for_exit()
    screen.fill(bg_color)
    for i in snowfall:
        i.move_snow()
        i.draw_snow()
    time.sleep(0.02)
    pygame.display.flip()