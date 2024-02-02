import pygame
import argparse


app = argparse.ArgumentParser()

app.add_argument("-w", "--width", default=400, help="width of the image")
app.add_argument("-he", "--height", default=400, help="height of the image")

args = vars(app.parse_args())

# Create a window
pygame.init()
screen = pygame.display.set_mode((int(args['width']), int(args['height'])))
pygame.display.set_caption("My first Pygame program")
clock = pygame.time.Clock()
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# Fill the background with white screen.fill((255, 255, 255))
    pygame.display.flip()
    clock.tick(60)