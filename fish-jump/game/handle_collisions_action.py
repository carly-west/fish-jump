import random
import os

from game import constants
from game.action import Action
from game.point import Point
from game.lives import Lives
from game.director import Director
from game.background import Background
from game.actor import Actor


class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.

    Stereotype:
        Controller
    """

    def __init__(self, physics_service, audio_service):
        super().__init__()
        self._physics_service = physics_service
        self._audio_service = audio_service
        self._lives = Lives()
        self.background = Background()
        self.actor = Actor()

    def execute(self, cast):
        """Executes the action using the given actors.

            Args:
                cast (dict): The game actors {key: tag, value: list}.
            """
        submarines = cast["submarine"]
        # seaweed = cast["seaweed"]
        fishes = cast["fish"]
        life = cast["life"]
        seaweed = cast["seaweeds"]
        lose_life = False

        # if self._physics_service.is_collision(fish, submarine):
        #     print("CRASH")

        if len(fishes) >= 1 and len(seaweed) >= 1:

            for fish in fishes:
                fish_position = fish.get_position()
                x_fish = fish_position.get_x()
                y_fish = fish_position.get_y()

            for submarine in submarines:

                sub_position = submarine.get_position()
                x_sub = sub_position.get_x()
                y_sub = sub_position.get_y()

            lose_life = False

            if x_fish + 70 in range(x_sub, x_sub + 129) and y_fish + 57 in range(y_sub, y_sub + 200):
                submarine.set_position(Point(0, 850))
                lose_life = True

            for weed in seaweed:
                weed_position = weed.get_position()
                x_weed = weed_position.get_x()
                y_weed = weed_position.get_y()

                if x_fish + 50 in range(x_weed, x_weed + 92) and y_fish + 57 in range(y_weed, y_weed + 300):
                    fish.set_position(Point(100, 250))
                    lose_life = True

            if lose_life:
                for lives in life:
                    lives.lose_lives(1)
                    lose_life = False

            for lives in life:
                is_game_over = lives.is_no_lives()

            if is_game_over:
                for weed in seaweed:
                    seaweed.clear()
                for fish in fishes:
                    fishes.clear()
                for sub in submarines:
                    submarines.clear()
                for lives in life:
                    lives.set_words("YOU LOST!")
                    lives.set_position(Point(375, 250))
