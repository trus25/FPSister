import pygame
import os
from grid import Grid
w = 600
h = 600
os.environ['SDL_VIDEO_WINDOW_POS'] = '400,100'
surface = pygame.display.set_mode((w,h))
pygame.display.set_caption('Tic-tac-toe')

grid = Grid()
grid.print_grid()
running= True
player = "X"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if (grid.checkWinner() == 0):
            if(grid.is_grid_full() == False):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        pos = pygame.mouse.get_pos()
                        pos1 = pos[0] // 200
                        pos2 = pos[1] // 200
                        if(grid.available(pos1,pos2) == True):
                            cek = grid.get_mouse(pos1, pos2, player)
                            if player == "X":
                                player = "O"
                            else:
                                player = "X"
                            grid.print_grid()
            else:
                grid.clear_grid()
        else:
            print("winner is " + grid.checkWinner() + "!")
            running = False

    surface.fill((0,0,0))
    grid.draw(surface)
    pygame.display.flip()
