import math

class Position (object):

    def __init__(self,x,y):
        self._x= x
        self._y= y

    def x(self):
        return self._x

    def y(self):
        return self._y

    def distance_to(self, aux):
        delta_x= self._x()-aux.x()
        delta_y= self._y()-aux.y()
        return math.sqrt(delta_x** +delta_y**2)

class Velocity(object):

    def __init__(self,start,end):
        self.start = start
        self.end = end

    def magnitude(self):
        return self.end.distance_to(self.start)