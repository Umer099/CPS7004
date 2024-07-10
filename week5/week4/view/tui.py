from week5.week4.model.location import Location
from week5.week4.model.shark import Shark
from week5.week4.model.environment import Environment

class Tui:
    def display_environmnet(self, environment):
        for row in range(environment.get_height()):
            for col in range(environment.get_width()):
                location = Location(col, row)
                agent = Environment.get_agent(location):
                    if agent is None:
                        print("!", end = "")
                    elif isinstance(agent, Shark):
                        print("S", end = "")





