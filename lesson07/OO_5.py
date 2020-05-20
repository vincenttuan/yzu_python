class Engine:
    power = 0

class Wheel:
    count = 0

class Car(Engine, Wheel):
    def __init__(self, price, power, count):
        self.price = price
        self.power = power
        self.count = count

    def __str__(self):
        return str(self.price) + ", " + str(self.power) + ", " + str(self.count)

if __name__ == '__main__':
    car = Car(100000, 150, 2)
    print(car)
