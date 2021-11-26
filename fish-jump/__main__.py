from game.obstacle import Obstacle
# from game.handle_off_screen_action import HandleOffScreenAction
from game.audio_service import AudioService
from game.physics_service import PhysicsService
from game.output_service import OutputService
from game.input_service import InputService
# from game.handle_collisions_action import HandleCollisionsAction
from game.control_actors_action import ControlActorsAction
from game.move_actors_action import MoveActorsAction
from game.draw_actors_action import DrawActorsAction
from game.fish import Fish
from game.point import Point
from game.actor import Actor
from game.director import Director
from game import constants
import raylibpy
import random
# from game.ball import Ball

# from game.control_actors_action import ControlActorsAction
# from game.handle_collisions_action import HandleCollisionsAction
# from game.handle_off_screen_action import HandleOffScreenAction
# from game.move_actors_action import MoveActorsAction


def main():

    # create the cast {key: tag, value: list}
    cast = {}

    # FISH
    cast["fish"] = []
    fishes = []

    position_fish = Point(400, 450)
    fish = Fish()
    fish.set_position(position_fish)
    fishes.append(fish)

    cast["fish"] = fishes

    # OBSTACLES
    obstacles = []

    position_obstacle = Point(400, 450)
    obstacle = Obstacle()
    obstacle.set_position(position_obstacle)
    obstacles.append(obstacle)

    cast["obstacles"] = obstacles

    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()
    move_actors_action = MoveActorsAction()
    # handle_off_screen_action = HandleOffScreenAction(physics_service)
    draw_actors_action = DrawActorsAction(output_service)
    control_actors_action = ControlActorsAction(input_service)
    # handle_collisions_action = HandleCollisionsAction(
    #     physics_service, audio_service)

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action]
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
