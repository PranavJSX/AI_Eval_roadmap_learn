from decorators import *

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        """Get value of radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set radius, raise error if negative"""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("radius must be non-negative")

    @property
    def area(self):
        """Calculate area inside circle"""
        return self.pi() * self.radius**2

    def cylinder_volume(self, height):
        """Calculate volume of cylinder with circle as base"""
        return self.area * height

    @classmethod
    def unit_circle(cls):
        """Factory method creating a circle with radius 1"""
        return cls(1)

    @staticmethod
    def pi():
        """Value of π, could use math.pi instead though"""
        return 3.1415926535

@timing
class TimeWaster:
    @debugger
    def __init__(self,max_num):
        self.max_num = max_num
        print("called constructor")

    @timing
    def waste_time(self,num_times):
        for _ in range(num_times):
            sum([number**2 for number in range(self.max_num)])
            # print("ran waste_time")


def main():
    tw = TimeWaster(1000)

    tw.waste_time(99)

if __name__ == "__main__":
    main()