import json
import argparse
import pygame
from lib.game import Game


class Menu:
    def __init__(self):
        self.game = None
        self.app = None
        self.settings = self.load_settings()
        self.setup_arg_parser()
        self.running = False

    def load_settings(self):
        with open("settings.json") as file:
            settings = json.load(file)
        settings["RESOLUTION"] = tuple(map(int, str(settings["RENDER_RESOLUTION"]).split("x")))
        return settings

    def setup_arg_parser(self):
        self.app = argparse.ArgumentParser()
        self.app.add_argument("-w", "--width", default=800, help="width of the image")
        self.app.add_argument("-he", "--height", default=800, help="height of the image")
        self.app.add_argument('-l', '--level', default="./levels/original.json", help="level file")
        self.app.add_argument("-v", "--verbose", default=False, action="store_true", help="increase output verbosity")
        self.app.add_argument("-c", "--color", default="blue", help="background color")

    def start_game(self, args):
        args["width"] = int(args["width"])
        args["height"] = int(args["height"])

        self.game = Game(width=args["width"], height=args["height"],
                         level=args["level"], verbose=args["verbose"], color=args["color"], **self.settings)
        self.game.start()
        self.running = True

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((800, 800))
        font = pygame.font.Font(None, 36)
        start_button = font.render("Start", True, (255, 255, 255))

        button_width, button_height = start_button.get_size()

        while not self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.is_button_clicked(screen, mouse_pos, button_width, button_height):
                        self.start_game(vars(self.app.parse_args()))

            if self.game:
                self.game.render()

            self.draw_centered_button(screen, start_button, button_width, button_height)

            pygame.display.flip()
            clock.tick(60)

    def is_button_clicked(self, screen, mouse_pos, button_width, button_height):
        button_x = screen.get_width() / 2 - button_width / 2
        button_y = screen.get_height() / 2 - button_height / 2
        return (button_x <= mouse_pos[0] <= button_x + button_width and
                button_y <= mouse_pos[1] <= button_y + button_height)

    def draw_centered_button(self, screen, button_surface, button_width, button_height):
        button_x = screen.get_width() / 2 - button_width / 2
        button_y = screen.get_height() / 2 - button_height / 2
        screen.blit(button_surface, (button_x, button_y))

        while self.running:
            try:
                self.game.handle_events(pygame.event.get())
                self.game.update()
                self.game.render()
                pygame.display.flip()
            except KeyboardInterrupt:
                self.game.handle_events([pygame.event.Event(pygame.QUIT)])
                break
            except Exception as e:
                print("Error: ", e)
                break

