from lib.map import map, parser, object
from lib.entity import entity
from lib.entity.player import PlayerStrategy, Player
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
render = parser.DefaultMapParser("./lib/map/big_map.txt", screen)
gameMap = render.parse(screen_size)
pygame.display.set_caption("NPacman")
clock = pygame.time.Clock()
running = True
# playerMovementStrategy = PlayerStrategy()
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    # playerMovementStrategy.move()
    screen.fill((255, 255, 255))
    gameMap.render(screen)
    pygame.display.flip()
    clock.tick(60)