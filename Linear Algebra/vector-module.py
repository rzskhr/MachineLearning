import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')
    
    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return new_coordinates
    
    def times_scalar(self, c):
        new_coordinates = [c*x for x in self.coordinates]
        return new_coordinates
   
    def magnitude(self):
        sumOfSquares = sum([x**2 for x in self.coordinates])
        new_coordinates = math.sqrt(sumOfSquares)
        return new_coordinates
    
    def normalized(self):
        try:
            inverse = 1/abs((magnitude(self)))
            norm = times_scalar(self, inverse)
            return norm
        except ZeroDivisionError:
            raise Exception('Cannot Normalize the zero vector')
    

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
