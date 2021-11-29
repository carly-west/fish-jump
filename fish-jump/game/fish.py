from game.actor import Actor
from game.point import Point
from game import constants


class Fish(Actor):
    def __init__(self):
        super().__init__()
        # self.set_height = constants.PADDLE_HEIGHT
        # self.set_width = constants.PADDLE_WIDTH
        self.set_image(constants.IMAGE_FISH)
        # self._paddle_speed = constants.PADDLE_SPEED
        self.set_height = 3333
        self.set_width = 3333
        # self._velocity = Point(0, 0)

    def set_position(self, position):
        self._position = position

    def get_position(self):
        return self._position
