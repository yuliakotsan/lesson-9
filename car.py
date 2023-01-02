class Car(object):
    def __init__(self, brand, color, engine):
        self._brand = brand
        self._color = color
        self._engine = engine
        self.status = 'At Parking'

    @property
    def brand(self):
        return self._brand
    @property
    def color(self):
        return self._color
    @property
    def engine(self):
        return self._engine
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = self.color + ' ' + self.brand + ' ' + value

    def drive(self):
        self.status = 'Driving'

    def reverse(self):
        self.status = 'Reversing'
    
    def stop(self):
        self.status = 'At Parking'

car = Car('Toyota', 'Red', '1.3tsi')
print(car.status)
car.drive()
print(car.status)
car.reverse()
print(car.status)
car.stop()
print(car.status)
print('-------------')

class Turning(Car):
    def turn_left(self):
        self.status = 'Turning Left'
    def turn_right(self):
        self.status = 'Turning Right'

car2 = Turning('Skoda', 'Black', '1.1tsi')

print(car2.status)
car2.turn_left()
print(car2.status)
car2.turn_right()
print(car2.status)
car2.stop()
print(car2.status)