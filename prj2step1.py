import pygame


loc_x = 800                                                         # задаем разрешение экрана x и y
loc_y = 600
loc_i_x = 10
loc_i_y = 10
game_over = False
bg_color = (1, 56, 61)

pygame.init()                                                       # инициилизируем pygame
pygame.display.set_caption("My first videogame on python(pygame)")  # задаем название игры
screen = pygame.display.set_mode((loc_x, loc_y)) # дает переменной screen наше разрешение

myimage = pygame.image.load("art.jpg").convert()                    # загружаем картинку в игру и конвертируем ее
myimage = pygame.transform.scale(myimage, (480, 220))

while game_over == False:                                           # выводим картинку до тех пор пока пользователь не нажмет кнопку Escape
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_UP:                            # Теперь наша картинка двигается по нажатию стрелок на 5
                loc_i_y -= 5
            if event.key == pygame.K_DOWN:
                loc_i_y += 5
            if event.key == pygame.K_LEFT:
                loc_i_x -= 5
            if event.key == pygame.K_RIGHT:
                loc_i_x += 5
        if event.type == pygame.MOUSEBUTTONDOWN:                    # тут картинка перемещается по нажатию кнопки мыши
            loc_i_x, loc_i_y = event.pos
        
    screen.fill(bg_color)                                           # добавим задний план выбранного цвета
    screen.blit(myimage, (loc_i_x, loc_i_y))                        # расположение картинки
    pygame.display.flip()                                           # вывести все на экран