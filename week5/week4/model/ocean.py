from week5.week4.model.environment import Environment
from week5.week4.model.location import Location


class Ocean(Environment):

    def __init__(self, width, height):
        self.__grid = [[None for _ in range(width)] for _ in range(height)]

    def clear(self):
        width = len(self.__grid[0])
        height = len(self.__grid)
        self.__grid = [[None for _ in range(width)] for _ in range(height)]

    def get_agent(self, Location):
        x = Location.get_x()
        y = Location.get_y()
        return self.__grid[y][x]

    def set_agent(self, agent, Location):
        x = Location.get_x()
        y = Location.get_y()
        self.__grid[y][x] = agent

    def get_height(self):
        return len(self.__grid)

    def get_width(self):
        return len(self.__grid[0])

    def free_adjacent_locations(self, Location):
        free_locations = []

        # Define offsets for adjacent locations
        offsets = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        # Iterate over each offset to find adjacent locations
        for offset_x, offset_y in offsets:
            adjacent_col = Location.get_x() + offset_x
            adjacent_row = Location.get_y() + offset_y

            # do something e.g., check if adjacent location is empty

            if self.__grid[adjacent_row][adjacent_col] is None:
                free_locations.append(Location(adjacent_col, adjacent_row))

        return free_locations
