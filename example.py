class Person:
    def __init__(self, car):
        self.car = car
    
class Car:
    def __init__(self, color, price):
        self.color = color
        self.price = price
        
car = Car('red', 20000)
hamza = Person(car)