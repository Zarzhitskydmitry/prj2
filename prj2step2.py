import pygame


loc_x = 800                                                         # задаем разрешение экрана x и y
loc_y = 600
loc_i_x = 1                                                         # Ставим расположение картинки
loc_i_y = 1
image_size_y = 160                                                  # Задаем размеры картинки по x и y
image_size_x = 380
move_right = False
move_left = False
move_up = False
move_down = False 
game_over = False
bg_color = (1, 56, 61)

pygame.init()                                                       # инициилизируем pygame
pygame.display.set_caption("My first videogame on python(pygame)")  # задаем название игры
screen = pygame.display.set_mode((loc_x, loc_y))                    # дает переменной screen наше разрешение

myimage = pygame.image.load("art.jpg").convert()                    # загружаем картинку в игру и конвертируем ее
myimage = pygame.transform.scale(myimage, (image_size_x, image_size_y))

while game_over == False:                                           # выводим картинку до тех пор пока пользователь не нажмет кнопку Escape
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_UP:                            
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
                
        if event.type == pygame.KEYUP:                              # Если мы отпускаем кнопку, то переменная вкходит состояние False или "не делать"     
            if event.key == pygame.K_UP: 
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
                
        if event.type == pygame.MOUSEBUTTONDOWN:                    # тут картинка перемещается по нажатию кнопки мыши
            loc_i_x, loc_i_y = event.pos        

    if move_up == True:                                         # Теперь наша картинка двигается по ЗАжатию стрелок на 1
        loc_i_y -= 1
        if loc_i_y <= 0:                                        # Здесь мы делаем упор экрана, чтобы картинка не заходила за экран и останавливалась
            loc_i_y = 0        
    if move_down == True:
        loc_i_y += 1
        if loc_i_y >= loc_y - image_size_y:                     # Здесь тоже задаем границу по формуле Если каринка уходит вниз, то ее положение не будет превышать размера по y картинки
            loc_i_y = loc_y - image_size_y
    if move_left == True:
        loc_i_x -= 1
        if loc_i_x <= 0:
            loc_i_x = 0
    if move_right == True:
        loc_i_x += 1
        if loc_i_x >= loc_x - image_size_x:
            loc_i_x = loc_x - image_size_x
                

    screen.fill(bg_color)                                           # добавим задний план выбранного цвета
    screen.blit(myimage, (loc_i_x, loc_i_y))                        # расположение картинки
    pygame.display.flip()                                           # вывести все на экран      