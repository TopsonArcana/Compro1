class Item:
    def __init__(self, id, type, color):
        self.__id = id
        self.__type = type
        self.__color = color

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def __eq__(self, other):
        return (self.__id == other.__id) and (self.__type == other.__type) and (self.__color == other.__color)

    def __str__(self):
        return f"{self.__id},{self.__type},{self.__color}"

