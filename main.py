from lib.map import map, parser, tile
from lib.game import Game
from lib.entity.ghost import Ghost
from lib.entity.state.manager import StateManager, States
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
render = parser.DefaultMapParser("./levels/original.txt", screen)
map = render.parse(screen_size)
gameplay = GameplayState(map, screen)
game = Game(gameplay)
player = Player(None, (4, 4), map)
gameplay.add_entity(player)
pygame.display.set_caption("NPacman")
running = True
while running:
    game.handle_events(pygame.event.get())
    game.update()
    game.render()
    pygame.display.flip()
