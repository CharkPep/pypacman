from lib.map import map, parser, tile
from lib.states.gameplay import GameplayState
from lib.game import Game
import pygame
import argparse
app = argparse.ArgumentParser()

app.add_argument("-w", "--width", default=400, help="width of the image")
app.add_argument("-he", "--height", default=400, help="height of the image")
app.add_argument('-l', '--level', default="./levels/small.txt", help="level file")

args = vars(app.parse_args())
screen_size = (int(args['width']), int(args['height']))
# Create a window
pygame.init()
screen = pygame.display.set_mode(screen_size)
render = parser.DefaultMapParser("./levels/small.txt", screen)
gameplay = GameplayState(render.parse(screen_size), screen)
game = Game(gameplay)
pygame.display.set_caption("NPacman")
running = True
while running:
    game.handle_events(pygame.event.get())
    game.update()
    game.render()
    pygame.display.flip()
