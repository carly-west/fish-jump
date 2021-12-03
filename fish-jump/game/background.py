from game.actor import Actor
from game.point import Point
from game import constants


class Background(Actor):
    def __init__(self):
        super().__init__()
        self.image = constants.IMAGE_BACKGROUND
        self.set_image(self.image)
        self.set_height = 600
        self.set_width = 1000

    def set_position(self, position):
        self._position = position

    def get_position(self):
        return self._position

    def set_background(self, background):
        self.image = background
