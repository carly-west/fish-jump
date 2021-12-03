import random
from game.actor import Actor
from game.point import Point


class Lives(Actor):
    """Points earned. The responsibility of the ScoreBoard is to keep track of the player's points.

    Stereotype:
        Information Holder

    Attributes: 
        _points (integer): The number of points the food is worth.
    """

    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the text.

        Args:
            self (Score): an instance of Score.
        """
        super().__init__()
        self._lives = 3
        position = Point(1, 0)
        self.set_position(position)
        self.set_text(f"Lives: {self._lives}")

    def add_lives(self, lives):
        """Adds the given lives to the running total and updates the text.

        Args:
            self (Score): An instance of Score.
            lives (integer): The lives to add.
        """
        self._lives += lives
        self.set_text(f"Lives: {self._lives}")

    def lose_lives(self, lives):
        """removes the given lives to the running total and updates the text.

        Args:
            self (Score): An instance of Score.
            lives (integer): The lives to remove.
        """
        self._lives -= lives
        self.set_text(f"Lives: {self._lives}")

    def is_no_lives(self):
        if self._lives == 0:
            return True
        else:
            return False
