import json
from lib.game import Game
import pygame
import argparse

with open("settings.json") as file:
    settings = json.load(file)

settings["RESOLUTION"] = tuple(map(int, str(settings["RENDER_RESOLUTION"]).split("x")))
TARGET_FPS = settings["TARGET_FPS"]

app = argparse.ArgumentParser()

app.add_argument("-w", "--width", default=1000, help="width of the image")
app.add_argument("-he", "--height", default=1200, help="height of the image")
app.add_argument(
    '-l', '--level', default="./levels/original.json", help="level file")
app.add_argument("-v", "--verbose", default=False,
                 action="store_true", help="increase output verbosity")

args = vars(app.parse_args())
args["width"] = int(args["width"])
args["height"] = int(args["height"])

game = Game(width=args["width"], height=args["height"],
            level=args["level"], verbose=args["verbose"], **settings)
game.start()
running = True
while running:
    try:
        game.handle_events(pygame.event.get())
        game.update()
        game.render()
        pygame.display.flip()
    except KeyboardInterrupt:
        game.handle_events([pygame.event.Event(pygame.QUIT)])
    except Exception as e:
        print("Error: ", e)
        break
