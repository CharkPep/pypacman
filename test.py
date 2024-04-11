import pygame
import logging
import sys
from lib.map import parser, map
import xml.etree.ElementTree as ET
from lib.utils import tileset, singleton
from lib.map.tile import Tile

# resolution = (800, 800)
# 
# pygame.init()
# screen = pygame.display.set_mode(resolution)
# pygame.display.set_caption("Test")
# clock = pygame.time.Clock()
# running = True
# render = parser.TiledMapParser("./levels/original.json", verbose=True)
# render.parse()
# map.GameMap().layers[0][0].kill()
# while running:
#     screen.fill((255, 255, 255))
#     map.GameMap().render(screen)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# 
#     pygame.display.flip()
#     clock.tick(60)

# with open("./levels/pacman-map.tsx", "r") as file:
#     props = ET.parse(file)
#     root = props.getroot()
#     for tile in root.findall("./tile"):
#         print(tile.attrib, tile.tag)
#         for child in tile.findall("./properties/property"):
#             print(child.attrib, child.tag)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.info("INFO: Starting game")
