import pygame
from src.utils.constants import WIDTH, HEIGHT, TILE_SIZE, BLACK, FPS
from src.map.testMap import Map
from src.entities.pacman import Pacman
from src.entities.ghost import Pinky, Inky, Clyde, Sue
from src.map.randomized_map import RandomMap

game_map = Map()

if __name__ == "__main__":
    pygame.init() 

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    player = Pacman(TILE_SIZE, TILE_SIZE, game_map.walls)

    ghosts = [ 
        Pinky(game_map, player),
        Inky(game_map, player),
        Clyde(game_map, player),
        Sue(game_map, player)
    ]
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update()
        
        screen.fill(BLACK)
        game_map.draw_map(screen)
        screen.blit(player.image, player.rect)
        for ghost in ghosts:
            screen.blit(ghost.image, ghost.pos)
            ghost.update()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()