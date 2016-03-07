'''
Using the template below, create ball objects that start at random
x,y locations with a random radius.  The location and radius should be
no larger or smaller than the max/min values given as the constants.

Using a while loop, have your balls move around the cartesian plane using
the .move() method.  If your circle hits the edge, change its angle by creating
and calling a .changeAngle() method.  Take some time to research how the ball's
angle would change if it hits an edge.

To figure out if two balls are colliding, you will need to compute the distance 
between their centers, then see if this distance is less than or equal to the 
sum of their radii. If so, they are colliding.  Create a class method that you
will call to check for collision between 2 balls.

If any two balls collide, exit the while loop and print Collision.

I recommend you create a class method to print the location and current angle of
your ball instances to help with debug.

Go above and beyond and figure out a way to have your program create objects
on its own (i.e. ask the user for the number of balls they want to run the
program with, then create that number of balls and test for collision between
all of them)
'''

import math
import time
MAX_X = 25
MAX_Y = 25
MIN_X = -25
MIN_Y = -25
MIN_R = 1
MAX_R = 8
MIN_ANGLE = 0
MAX_ANGLE = 359
from random import randint

class Ball(object):
    def __init__():
        pass
 
        
    def move(self):
        self.x = self.x + math.cos(math.radians(self.angle))
        self.y = self.y + math.sin(math.radians(self.angle))
        

while True:
    time.sleep(.5)
