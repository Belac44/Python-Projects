def add(*args):
    sum = 0
    for items in args:
        sum += items
    return sum

# print (add(2,3,4,5,6,7,8,9))

def calculate(n, **kwargs):
    for (key, value) in kwargs.items():
        print(key, value)
    n += kwargs['add']
    n *= kwargs['multiply']
    return n


# print(calculate(2, add=3, multiply=5))

class Car:

    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get("model")
        self.color = kw.get('color')
        self.seats = kw.get('seat')


my_car = Car(make="Nissan")
print(my_car.model)