import pygame
from pygame.locals import *
from pygame.compat import geterror

import numpy as np
import intersection as inter
from definitions import *  # also imports os, math


if not pygame.font: print ('Warning, fonts disabled')
if not pygame.mixer: print ('Warning, sound disabled')

#globals
#background = None
# alltargets = None
# allrobots = None
# allobstacles = None
#allsounds=None
#clock = None

def init():
    # Initialize Everything

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Nao sim')
    pygame.mouse.set_visible(True)

    # Create The Backgound
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(background_color)

    # Put Text On The Background, Centered
    ##    if pygame.font:
    ##        font = pygame.font.Font(None, 36)
    ##        text = font.render("Pummel The Chimp, And Win $$$", 1, (10, 10, 10))
    ##        textpos = text.get_rect(centerx=background.get_width()/2)
    ##        background.blit(text, textpos)

    # Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Prepare Game Objects
    clock = pygame.time.Clock()

    return screen, background, clock

# functions to create our resources
def load_image(name, colorkey=None):
    fullname = os.path.join(data_dir, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print ('Cannot load image:', fullname)
        raise SystemExit(str(geterror()))
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


def load_sound(name):
    class NoneSound:
        def play(self): pass

    if not pygame.mixer or not pygame.mixer.get_init():
        return NoneSound()
    fullname = os.path.join(data_dir, name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        print ('Cannot load sound: %s' % fullname)
        raise SystemExit(str(geterror()))
    return sound



def clamp(x, xmin, xmax):
    if xmin > xmax:
        temp = xmin
        xmin = xmax
        xmax = temp

    interval = xmax - xmin
    while x > xmax:
        x -= interval
    while x < xmin:
        x += interval
    return x


def screen_coordinates(pos):
    """Transforms world coordinates to screen coordinates"""

    return int((pos[0] % screen_width) / px), screen_height - int((pos[1] % screen_height) / px)


def from_screen_coordinates(pos):
    """Transforms screen coordinates to world coordinates"""

    return float(pos[0]) * px, float(screen_height - pos[1]) * px


def world_coordinates(x, y, robot_x, robot_y, robot_phi):
    rotation = np.array([[math.cos(robot_phi), -math.sin(robot_phi)],
                         [math.sin(robot_phi), math.cos(robot_phi)]])
    return [robot_x, robot_y] + rotation.dot([x, y])


def world_coordinates_polar(rho, theta, robot_x, robot_y, robot_phi):
    return np.arrray([robot_x, robot_y]) + np.array(
        [rho * math.cos(robot_phi + theta), rho * math.sin(robot_phi + theta)])





# classes for our game objects
class nao_robot(pygame.sprite.Sprite):
    """moves a clenched fist on the screen, following the mouse"""

    def __init__(self, background):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = load_image('nao_topview.png', -1)
        # turn image 90 degree clockwise
        rotate = pygame.transform.rotate
        self.image = rotate(self.image, -90)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)
        self.background = background
        self.draw_detections = False

        self.velocity = 0.0
        self.turnrate = 0.0
        self.original = self.image
        self.set_pos(10.0, 10.0, 0.0)
        self.timestep = 0.05  # 50ms

        # sensor locations relative to heading and robot center in polar coordinates
        angle = 10 * degree
        r = float(self.rect.width) * px / 2  # this needs to be computed before the image is rotated again
        self.sensor_positions = [[r, angle], [r, -angle]]  # cm and radians
        self.view_directions = [30, -30]  # degrees
        self.view_angle = 60  # degrees
        self.max_distance = 10

    def update(self):
        "move the robot to the desired position"
        self.x += self.velocity * math.cos(self.phi) * self.timestep
        self.y += self.velocity * math.sin(self.phi) * self.timestep  # larger y-value is down in image
        self.phi += self.turnrate * self.timestep
        self.phi = clamp(self.phi, -math.pi, math.pi)

        #        print self.x, self.y, self.phi*180/math.pi
        self.update_rect()

    def update_rect(self):
        # update the image position and orientation
        [x, y] = screen_coordinates([self.x, self.y])
        self.rect.center = [x, y]
        rotate = pygame.transform.rotate
        self.image = rotate(self.original, self.phi / degree)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)
        pass

    def set_pos(self, x, y, phi, absolute=True):
        self.x = float(x)
        self.y = float(y)
        if absolute:
            self.phi = float(phi)
        else:
            self.phi += float(phi)

        self.phi = clamp(self.phi, -math.pi, math.pi)
        self.update_rect()
        pass

    def set_vel(self, vel, turnrate):
        max_vel = 100.0
        max_turn = 10.0
        self.velocity = clamp(vel, -max_vel / 2, max_vel)
        self.turnrate = clamp(turnrate, -max_turn, max_turn)

    def sonar(self, obstacles):

        scan_resolution = 10
        n=len(self.sensor_positions)
        sonar_values=np.zeros(n)
        for sensor in range(n):
            p = [self.x + self.sensor_positions[sensor][0] * math.cos(self.sensor_positions[sensor][1] + self.phi),
                 self.y + self.sensor_positions[sensor][0] * math.sin(self.sensor_positions[sensor][1] + self.phi)]
            dist_inrange=[]
            for scan_direction in range(-self.view_angle / 2 + self.view_directions[sensor],
                                        self.view_angle / 2 + self.view_directions[sensor] + scan_resolution,
                                        scan_resolution):
                v = [10 * math.cos(self.phi + scan_direction * degree),
                     10 * math.sin(self.phi + scan_direction * degree)]
                for obs in obstacles:
                    if isinstance(obs, obstacle):
                        # for q in obs.point_list:
                        #     if self.draw_detections:
                        #         pygame.draw.circle(self.background, BLACK, screen_coordinates(q), 10, 2)
                        detected_points = inter.intersect_poly(p, v, obs.point_list)
                        dist = inter.compute_distance(p, detected_points)

                        for i in range(len(detected_points)):
                            if dist[i] < self.max_distance:
                                s = detected_points[i]
                                if self.draw_detections:
                                    pygame.draw.circle(self.background, GREEN, screen_coordinates(s), 10, 2)
                                    pygame.draw.line(self.background, RED, screen_coordinates(p), screen_coordinates(s))
                                dist_inrange.append(dist[i])
        #                        print inter.min_distance(p,detected_points)
            if len(dist_inrange)>0:
                sonar_values[sensor] = np.amin(dist_inrange)
            else:
                sonar_values[sensor] = self.max_distance
        return sonar_values

class target(pygame.sprite.Sprite):
    """moves a monkey critter across the screen. it can spin the
       monkey when it is punched."""

    def __init__(self, x=10, y=10):
        pygame.sprite.Sprite.__init__(self)  # call Sprite intializer
        self.image, self.rect = load_image('target.bmp', -1)
        self.screen = pygame.display.get_surface()
        self.mask = pygame.mask.from_surface(self.image)
        self.area = self.screen.get_rect()
        self.set_pos(x, y)

    #        self.move = 9
    #        self.dizzy = 0

    def update(self):
        "walk or spin, depending on the monkeys state"
        #        if self.dizzy:
        #            self._spin()
        #        else:
        #            self._walk()
        pass

    def set_pos(self, x, y):
        self.x=float(x)
        self.y=float(y)
        self.rect.center = screen_coordinates([x, y])
        self.update_rect()
        pass

    def update_rect(self):
        # update the image position and orientation
        self.mask = pygame.mask.from_surface(self.image)
        pass


#    def _walk(self):
#        "move the monkey across the screen, and turn at the ends"
#        newpos = self.rect.move((self.move, 0))
#        if self.rect.left < self.area.left or \
#            self.rect.right > self.area.right:
#            self.move = -self.move
#            newpos = self.rect.move((self.move, 0))
#            self.image = pygame.transform.flip(self.image, 1, 0)
#        self.rect = newpos
#
#    def _spin(self):
#        "spin the monkey image"
#        center = self.rect.center
#        self.dizzy = self.dizzy + 12
#        if self.dizzy >= 360:
#            self.dizzy = 0
#            self.image = self.original
#        else:
#            rotate = pygame.transform.rotate
#            self.image = rotate(self.original, self.dizzy)
#        self.rect = self.image.get_rect(center=center)
#        self.mask = pygame.mask.from_surface(self.image)
#
#    def punched(self):
#        "this will cause the monkey to start spinning"
#        if not self.dizzy:
#            self.dizzy = 1
#            self.original = self.image

class obstacle(pygame.sprite.Sprite):
    """moves a monkey critter across the screen. it can spin the
       monkey when it is punched."""

    def __init__(self, x=5, y=15, width=1, height=10, orientation=0, color=(0, 0, 255)):
        pygame.sprite.Sprite.__init__(self)  # call Sprite intializer

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.width, self.height = float(width), float(height)
        self.image = pygame.Surface([int(width / px), int(height / px)])
        self.image.fill(background_color)
        self.image.set_colorkey(background_color)
        pygame.draw.rect(self.image, BLUE, [0, 0, int(width / px), int(height / px)], 0)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.original = self.image
        self.set_pos(x, y, orientation)

    def update(self):
        "obstacles stay in one place."
        pass

    def set_pos(self, x, y, phi, absolute=True):
        self.x = float(x)
        self.y = float(y)
        if absolute:
            self.phi = float(phi)
        else:
            self.phi = self.phi + float(phi)
        self.phi = clamp(self.phi, -math.pi, math.pi)

        # update the image position and orientation
        self.update_rect()

    def update_rect(self):
        # update the image position and orientation
        self.rect.center = screen_coordinates([self.x, self.y])
        rotate = pygame.transform.rotate
        self.image = rotate(self.original, self.phi / degree)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)
        self.make_pointlist()
        pass

    def make_pointlist(self):
        rotation = np.array([[math.cos(self.phi), -math.sin(self.phi)],
                             [math.sin(self.phi), math.cos(self.phi)]])
        p = np.array([self.x, self.y])
        u = np.array([self.width / 2, -self.height / 2])
        v = np.array([self.width / 2, self.height / 2])
        a1 = p + rotation.dot(-v)
        a2 = p + rotation.dot(-u)
        a3 = p + rotation.dot(v)
        a4 = p + rotation.dot(u)

        self.point_list = [a1, a2, a3, a4]


class polygon(pygame.sprite.Sprite):
    """moves a monkey critter across the screen. it can spin the
       monkey when it is punched."""

    def __init__(self, point_list, color=(0, 0, 255)):
        pygame.sprite.Sprite.__init__(self)  # call Sprite intializer

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk

        self.point_list = point_list
        self.width, self.height = self.bounding_rect()  # self.point_list needs to be initialised first

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(background_color)
        self.image.set_colorkey(background_color)
        self.color = color
        pygame.draw.polygon(self.image, self.color, point_list, 0)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.original = self.image
        self.set_pos(10, 10, 0)

    def bounding_rect(self):
        xmin = xmax = self.point_list[0][0]
        ymin = ymax = self.point_list[0][1]
        for p in self.point_list:
            if p[0] < xmin:
                xmin = p[0]
            elif p[0] > xmax:
                xmax = p[0]
            if p[1] < ymin:
                ymin = p[1]
            elif p[1] > ymax:
                ymax = p[1]
        width = xmax - xmin
        height = ymax - ymin
        if xmin < 0:
            for p in self.point_list:
                p[0] -= xmin
        if ymin < 0:
            for p in self.point_list:
                p[1] -= ymin

        return width, height

    def update(self):
        "obstacles stay in one place."
        pass

    def set_pos(self, x, y, phi, absolute=True):
        self.x = x
        self.y = y
        if absolute:
            self.phi = phi
        else:
            self.phi = self.phi + phi
        self.phi = clamp(self.phi, -math.pi, math.pi)

        # update the image position and orientation
        self.update_rect()

    def update_rect(self):
        # update the image position and orientation
        self.rect.center = screen_coordinates([self.x, self.y])
        rotate = pygame.transform.rotate
        self.image = rotate(self.original, self.phi / degree)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pygame.mask.from_surface(self.image)
        pass

