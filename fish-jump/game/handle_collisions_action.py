import random
from game import constants
from game.action import Action
from game.point import Point
from game.lives import Lives


class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.

    Stereotype:
        Controller
    """

    def __init__(self, physics_service, audio_service):
        super().__init__()
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, cast):
        """Executes the action using the given actors.

            Args:
                cast (dict): The game actors {key: tag, value: list}.
            """
        submarine = cast["submarine"][0]
        # seaweed = cast["seaweed"]
        fish = cast["fish"][0]
        life = cast["life"][0]

        # if self._physics_service.is_collision(fish, submarine):
        #     print("CRASH")

        sub_position = submarine.get_position()
        x_sub = sub_position.get_x()
        y_sub = sub_position.get_y()

        fish_position = fish.get_position()
        x_fish = fish_position.get_x()
        y_fish = fish_position.get_y()

        if x_fish + 70 in range(x_sub, x_sub + 129) and y_fish in range(y_sub, y_sub + 200):
            submarine.set_position(Point(0, 850))
            life.lose_lives(1)
            print(life.get_text)

        is_game_over = life.is_no_lives()

        if is_game_over:
            print("YOU LOSE")
