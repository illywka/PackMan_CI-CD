import pygame
from src.utils.constants import WIDTH, HEIGHT, TILE_SIZE, BLACK
from src.map.testMap import Map
from src.entities.pacman import Pacman

game_map = Map()

if __name__ == "__main__":
    pygame.init() 

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    player = Pacman(TILE_SIZE, TILE_SIZE, game_map.walls)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update()
        screen.fill(BLACK)
        game_map.draw_map(screen)
        screen.blit(player.image, player.rect)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()