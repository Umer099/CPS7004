class Location:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, new_x):
        self.__x = new_x

    def set_y(self, new_y):
        self.__y = new_y

    def equals(self, other_location):
        pass

    def __str__(self):
        return f'Location (x = {self.__x}, y = {self.__y})'