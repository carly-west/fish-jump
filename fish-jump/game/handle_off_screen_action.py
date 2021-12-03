import random
from game import constants
from game.action import Action
from game.point import Point
from game.actor import Actor


class HandleOffScreenAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.

    Stereotype:
        Controller
    """

    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """

        submarines = cast["submarine"]
        for submarine in submarines:

            # seaweed = cast["seaweed"]

            sub_position = submarine.get_position()
            x_sub = sub_position.get_x()
            y_sub = sub_position.get_y()
            y_vel_sub = submarine._velocity.get_y()
            x_vel_sub = submarine._velocity.get_x()

            if x_sub < -200:
                x_sub = 800

            submarine.set_position(Point(x_sub, y_sub))
