from game.seaweed import Seaweed
from game.submarine import Submarine

from game.handle_off_screen_action import HandleOffScreenAction
from game.audio_service import AudioService
from game.physics_service import PhysicsService
from game.output_service import OutputService
from game.input_service import InputService
from game.handle_collisions_action import HandleCollisionsAction
from game.control_actors_action import ControlActorsAction
from game.move_actors_action import MoveActorsAction
from game.draw_actors_action import DrawActorsAction
from game.fish import Fish
from game.point import Point
from game.actor import Actor
from game.director import Director
from game import constants
from game.lives import Lives
from game.background import Background

import raylibpy
import random


def main():

    # create the cast {key: tag, value: list}
    cast = {}

    cast["background"] = []
    backgrounds = []

    position_background = Point(1, 1)
    background = Background()
    background.set_position(position_background)
    backgrounds.append(background)

    cast["background"] = backgrounds

    # Sets up lives
    cast["life"] = []
    lives = []

    position_life = Point(10, 10)
    life = Lives()
    life.set_position(position_life)
    lives.append(life)

    cast["life"] = lives

    # FISH
    cast["fish"] = []
    fishes = []

    position_fish = Point(100, 250)
    fish = Fish()
    fish.set_position(position_fish)
    fishes.append(fish)

    cast["fish"] = fishes

    # OBSTACLES
    seaweeds = []

    for spot in range(2):
        random_num = random.randint(300, 500)
        position_seaweed = Point(random_num * spot, 330)
        seaweed = Seaweed()
        seaweed.set_position(position_seaweed)
        seaweeds.append(seaweed)

        cast["seaweeds"] = seaweeds

    # Submarine

    submarines = []

    for spot in range(1):
        # Submarine isn't going to random spot
        random_num2 = random.randint(0, 300)
        position_submarine = Point(0, random_num2)
        submarine = Submarine()
        submarine.set_position(position_submarine)
        submarines.append(submarine)

    cast["submarine"] = submarines

    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()
    move_actors_action = MoveActorsAction()
    handle_off_screen_action = HandleOffScreenAction(physics_service)
    draw_actors_action = DrawActorsAction(output_service)
    control_actors_action = ControlActorsAction(input_service)
    handle_collisions_action = HandleCollisionsAction(
        physics_service, audio_service)

    # TODO: Create additional actions here and add them to the script

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action,
                        handle_off_screen_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

# , handle_collisions_action

    # Start the game
    output_service.open_window("fish-jump")
    audio_service.start_audio()
    # audio_service.play_sound(constants.SOUND_START)

    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()


if __name__ == "__main__":
    main()
