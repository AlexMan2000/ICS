#Defining class
class Car(object):
    def __init__(self,year_model,brand,speed=0):
        self._year_model = year_model
        self._brand = brand
        self._speed = speed

    def accelerate(self):
        self._speed += 5

    def brake(self):
        self._speed -= 5

    def get_speed(self):
        return self._speed

def main():
    car = Car('2012','tesla',5)
    for i in range(5):
        car.accelerate()
    for i in range(5):
        car.brake()
    print(car.get_speed())
    distance = 0
    for i in range(5):
        distance += car.get_speed()
        car.accelerate()
    for i in range(5):
        distance += car.get_speed()
        car.brake()
    print(distance)

main()
