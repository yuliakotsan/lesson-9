class Parallelogram(object):
    def __init__(self, width, length):
        self._width = width
        self._length = length
    
    def get_area(self):
        print('Paraallelogram', self._width * self._length)


class Square(Parallelogram):
    def get_area(self):
        print('Square', self._width**2)
    













par = Parallelogram(10,20)
par.get_area()

print('----------------')

squ = Square(10,10)
squ.get_area()