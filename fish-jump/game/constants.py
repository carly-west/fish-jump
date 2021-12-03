import os

MAX_X = 1000
MAX_Y = 600
FRAME_RATE = 30

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

# IMAGE_BRICK = os.path.join(os.getcwd(), "./batter/assets/brick-3.png")
# IMAGE_BRICK_RED = os.path.join(os.getcwd(), "./batter/assets/brick-2.png")

IMAGE_BACKGROUND = os.path.join(
    os.getcwd(), "/Users/carlywest/Desktop/fish-jump/fish-jump/assets/ocean.png")
IMAGE_SEAWEED = os.path.join(
    os.getcwd(), "/Users/carlywest/Desktop/fish-jump/fish-jump/assets/seaweed-big.png")
IMAGE_FISH = os.path.join(
    os.getcwd(), "/Users/carlywest/Desktop/fish-jump/fish-jump/assets/fish3.png")

IMAGE_SUBMARINE = os.path.join(
    os.getcwd(), "/Users/carlywest/Desktop/fish-jump/fish-jump/assets/submarine2.png")


# SOUND_START = os.path.join(os.getcwd(), "./batter/assets/start.wav")
# SOUND_BOUNCE = os.path.join(os.getcwd(), "./batter/assets/boing.wav")
# SOUND_OVER = os.path.join(os.getcwd(), "./batter/assets/over.wav")

SEAWEED_X = MAX_X / 2
SEAWEED_Y = MAX_Y - 125

SEAWEED_DX = 8
SEAWEED_DY = SEAWEED_DX * -1

SUBMARINE_X = MAX_X / 2
SUBMARINE_Y = MAX_Y - 25

BRICK_WIDTH = 48
BRICK_HEIGHT = 24

BRICK_SPACE = 5

FISH_SPEED = 15

FISH_WIDTH = 70
FISH_HEIGHT = 57

SEAWEED_WIDTH = 46
SEAWEED_HEIGHT = 150

SUBMARINE_WIDTH = 200
SUBMARINE_HEIGHT = 129
