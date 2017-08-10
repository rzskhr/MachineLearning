from math import sqrt, pi, acos
from decimal import Decimal, getcontext

getcontext().prec = 3

class Vector(object):
    
    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'
    
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(self.coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')
    
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    
    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)
    
    def times_scalar(self, c):
        new_coordinates = [Decimal(c)*x for x in self.coordinates]
        return Vector(new_coordinates)
   
    def magnitude(self):
        sumOfSquares = sum([x**2 for x in self.coordinates])
        new_coordinates = math.sqrt(sumOfSquares)
        return new_coordinates
    
    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1./magnitude)
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)
    
    def dot(self, v):
        dotProduct = sum([x*y for x,y in zip(self.coordinates, v.coordinates)])
        return dotProduct
    
    def angle_with(self, v, in_degrees=False):
    
        #cosTheta = dotProduct(self, v)/(magnitude(self)*magnitude(v))

        try:
            u1 = self.normalized()
            u2 = v.normalized()
            dotProduct = u1.dot(u2)
            angle_in_radians = acos(dotProduct)

            if in_degrees:
                degrees_per_radian = 180. /pi
                return angle_in_radians * degrees_per_radian
            else:
                return angle_in_radians

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')      
            else:
                raise e