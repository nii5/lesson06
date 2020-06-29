import time


class TrafficLight:

    def __init__(self):
        self.__color = {'red': 7, 'yellow': 2, 'green': 5}

    def running(self):
        for key in self.__color:
            print(key)
            time.sleep(self.__color[key])


tl = TrafficLight()
tl.running()
