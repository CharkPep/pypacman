import time

from lib.map import parser
from lib.game import Game
from lib.states.gameplay import GameplayState
from lib.entity.player import Player
from lib.entity.ghost import Ghost
from lib.entity.state.manager import StateManager
from lib.entity.state.scatter import ScatterState
from lib.entity.state.eaten import EatenState
from lib.entity.state.chase import ChaseState
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
chase = ChaseState(player.get_movement())
scatter = ScatterState((0, 0))
eaten = EatenState(None, map)
ghost = Ghost(None, (1, 1), map, StateManager(map, chase, {chase: chase}))
gameplay.add_entity(ghost)
pygame.display.set_caption("NPacman")
running = True
clock = pygame.time.Clock()
current_time = time.time()
prev_time = current_time
FPS = 60
TARGET_FPS = 60
while running:
    current_time = time.time()
    game.handle_events(pygame.event.get())
    game.update(current_time - prev_time)
    prev_time = current_time
    game.render()
    clock.tick(FPS)
    pygame.display.flip()
