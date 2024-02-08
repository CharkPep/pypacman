from lib.map import map, parser, tile
from lib.game import Game
import pygame
import argparse
app = argparse.ArgumentParser()

app.add_argument("-w", "--width", default=400, help="width of the image")
app.add_argument("-he", "--height", default=400, help="height of the image")

args = vars(app.parse_args())

screen_size = (int(args['width']), int(args['height']))
# Create a window
pygame.init()
screen = pygame.display.set_mode(screen_size)
render = parser.DefaultMapParser("./levels/big_map.txt", screen)
game = Game()
game.set_map(render.parse(screen_size))
game.spawn_player()

# game.spawn_player()
pygame.display.set_caption("NPacman")
clock = pygame.time.Clock()
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    game.render(screen)
    pygame.display.flip()
    clock.tick(60)