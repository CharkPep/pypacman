from lib.game import Game
import json
import argparse
import logging

logger = logging.getLogger("lib")
logging.basicConfig(format="%(levelname)s-%(filename)s: %(message)s")

app = argparse.ArgumentParser()
app.add_argument("-w", "--width", default=1000, help="width of the image", type=int)
app.add_argument("-he", "--height", default=1000, help="height of the image", type=int)
app.add_argument('-l', '--map', default="levels/original.json", help="level file", type=str)
app.add_argument("-v", "--verbose", default=False, action="store_true", help="increase output verbosity")
app.add_argument("-c", "--color", default="white", help="background color", type=str)
app.add_argument("-d", "--debug", default=False, action="store_true",
                 help="debug mode, start gameplay stage first")
args = vars(app.parse_args())
if args.get("verbose", False):
    logger.setLevel(logging.DEBUG)
with open("./settings.json") as file:
    settings = json.load(file)
settings["RESOLUTION"] = tuple(map(int, str(settings["RENDER_RESOLUTION"]).split("x")))
game = Game(width=args["width"], height=args["height"], map=args["map"],
            verbose=args["verbose"], color=args["color"], debug=args["debug"], **settings)
game.start()
