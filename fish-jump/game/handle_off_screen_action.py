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
        foods = cast["food"]
                

        for food in foods:

            food_position = food.get_position()
            x_food = food_position.get_x()
            y_food = food_position.get_y()

            if x_food <= 5:
                y_food = random.randint(0, 450)

                food.set_position(Point(1000, y_food))

        for submarine in submarines:

            sub_position = submarine.get_position()
            x_sub = sub_position.get_x()
            y_sub = sub_position.get_y()

            if x_sub <= 0:
                y_sub = random.randint(0, 450)

                submarine.set_position(Point(1000, y_sub))
