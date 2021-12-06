from game.actor import Actor
from game.point import Point
from game import constants


class Submarine(Actor):
    def __init__(self):
        super().__init__()
        self.set_height = constants.SUBMARINE_WIDTH
        self.set_width = constants.SUBMARINE_WIDTH
        self.set_image(constants.IMAGE_SUBMARINE)
        self._velocity = Point(-5, 0)
        self._position = Point(0, 200)

    def set_position(self, position):
        self._position = position

    def get_position(self):
        return self._position

    def set_new_image(self, image):
        self.set_image(image)
