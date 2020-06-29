
class Road:

    def __init__(self):
        self._length = 20
        self._width = 5000

    def weight(self, heft=25, thick=5):
        print(str(self._width * self._length * heft * thick) + ' kg')


rw = Road()
rw.weight()