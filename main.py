import time

from lib.map import parser
from lib.game import Game
from lib.stages.gameplay import GameplayStage
import pygame
import argparse

FPS = 60
TARGET_FPS = 60
app = argparse.ArgumentParser()

app.add_argument("-w", "--width", default=400, help="width of the image")
app.add_argument("-he", "--height", default=400, help="height of the image")
app.add_argument('-l', '--level', default="./levels/original.json", help="level file")
app.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")

args = vars(app.parse_args())
screen_size = (int(args['width']), int(args['height']))
# Create a window
pygame.init()
screen = pygame.display.set_mode(screen_size)
render = parser.DefaultMapParser("./levels/original.json", screen)
render.parse(screen_size)
gameplay = GameplayStage(screen)
game = Game(gameplay)
images = {
    'up': pygame.image.load('assets/pacman/pacman0.png'),
    'down': pygame.image.load('assets/pacman/pacman1.png'),
    'left': pygame.image.load('assets/pacman/pacman2.png'),
    'right': pygame.image.load('assets/pacman/pacman3.png')
}
pygame.display.set_caption("NPacman")
running = True
current_time = time.time()
prev_time = current_time
frame = 0
while running:
    current_time = time.time()
    game.handle_events(pygame.event.get())
    dt = current_time - prev_time
    game.update(dt)
    prev_time = current_time
    game.render()
    pygame.display.flip()
