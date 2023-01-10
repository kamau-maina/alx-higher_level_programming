#!/usr/bin/python3
"""
Defines a rectangle
"""


class Rectangle:
    '''
    Represents a rectangle
    '''

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    # using the getter function
    @property
    def width(self):
        return self.__width

    # using setter funtion
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        peri = (self.__height + self.__width) * 2
        if self.__height == 0 or self.__width == 0:
            peri = 0
            return peri
        else:
            return peri

    def __str__(self):
        emptyString = ''
        if self.height == 0 or self.width == 0:
            return emptyString
        for number in range(self.height):
            if number != self.height - 1:
                emptyString = emptyString + str(self.print_symbol)\
                    * self.width + '\n'
            else:
                emptyString = emptyString + str(self.print_symbol) * self.width
        return emptyString

    def __repr__(self):
        newString = "Rectangle(" + str(self.__width) + ", "\
            + str(self.__height) + ")"
        return newString

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
