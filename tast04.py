import random
import time

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('You started moving')

    def stop(self):
        print('You stopped')

    def turn(self, direction):
        print(f'You turned on {direction}')

    def show_speed(self):
        print(f'You go fast {self.speed}')

class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'You go fast {self.speed}. Excess, please slow down')
        else:
            print(f'You go fast {self.speed}')
    def your_car(self):
        print(f'Your car is {self.name}')

class WorkCar(Car):

    def show_speed(self):
        if self.speed >40:
            print(f'You go fast {self.speed}. Excess, please slow down')
        else:
            print(f'You go fast {self.speed}')
    def your_car(self):
        print(f'Your car is {self.name}')

class SportCar(Car):

    def your_car(self):
        print(f'Your car is {self.name}')


class PoliceCar(Car):
    def your_car(self):
        print(f'Your have policecar is {self.name}')

my_colors = {1: 'red', 2: 'blue', 3: 'yellow', 4: 'white', 5: 'black'}
my_models = {1: 'BMW', 2: 'Mercedes', 3: 'Toyota', 4: 'Volvo', 5: 'Jaguar', 6: 'Jeep'}
my_dirs = {1: 'left', 2: 'right', 3: 'U-turn'}
i=0
while i < 14:
    i +=1
    num = random.randint(1, 4)
    if num == 1:
        tc = TownCar(random.randint(30, 150),
                     my_colors[random.randint(1, 5)],
                     my_models[random.randint(1, 6)])
    elif num == 2:
        tc = WorkCar(random.randint(30,150),
                     my_colors[random.randint(1, 5)],
                     my_models[random.randint(1, 6)])
    elif num == 3:
        tc = SportCar(random.randint(30,150),
                     my_colors[random.randint(1, 5)],
                     my_models[random.randint(1, 6)])
    elif num == 4:
        tc = PoliceCar(random.randint(30, 150),
                     my_colors[random.randint(1, 5)],
                     my_models[random.randint(1, 6)],
                     True)
    tc.your_car()
    tc.go()
    tc.turn(my_dirs[random.randint(1, 3)])
    tc.show_speed()
    tc.stop()

    time.sleep(2)