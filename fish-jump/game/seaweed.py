from game.actor import Actor
from game.point import Point
from game import constants


class Seaweed(Actor):
    def __init__(self):
        super().__init__()
        self.set_height = constants.SEAWEED_WIDTH
        self.set_width = constants.SEAWEED_WIDTH
        self.set_image(constants.IMAGE_SEAWEED)
        # self._brick_space = constants.BRICK_SPACE
        self._velocity = Point(-3, 0)

    def set_position(self, position):
        self._position = position

    def get_position(self):
        return self._position

    def set_new_image(self, image):
        self.set_image(image)
