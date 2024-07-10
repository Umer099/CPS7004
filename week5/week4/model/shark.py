from random import random

from agent import Agent


class Shark(Agent):


    def __init__(self, location):
        super().__init__(location)


    def __eat(self, ocean):
        pass

    def __swim(self, ocean):
        free_locations = ocean.free_adjacent_locations()
        if len(free_locations) > 0:
            index = random.randint(0, len(free_locations))
            free_locations = free_locations[index]

            ocean.set_agent(self.get_location(), None)
            ocean.set_agent(free_locations, self)
            self.set_location(free_locations)


    def act(self, ocean):
        self.__swim(ocean)
