import os, math

# globals
main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'data')

degree = math.pi / 180.0 # to convert degrees to radians
px = 0.034  # cm if 75 px/inch
background_color = (150, 150, 150)
obstacle_color = (0,0,250)

BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)

screen_width = 1920
screen_height = 1080
