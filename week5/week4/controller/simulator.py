from week5.week4.model.ocean import Ocean
from week5.week4.view.tui import Tui
class Simulator():
    def __init__(self):
        self.__ocean = Ocean(10, 10)
        self.__tui = Tui()

    def run(self):
        pass


if __name__ == "__main__":
    sim = Simulator()
    sim.run()