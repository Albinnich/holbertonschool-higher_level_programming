#!/usr/bin/python3

"""
Module 8. Compare rectangles
"""


class Rectangle:
    """
    Class Rectangle defines area and perimeter of rectangle
    - Private instance attributes: width and height
    - property and setter methods for width and height
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes rectangle area and perimeter
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        self.print_symbol = Rectangle.print_symbol

    @property
    def width(self):
        """
        Getter for the private instance attribute width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the private instance attribute width.
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the private instance attribute height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the private instance attribute height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns the string representation of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(
            [str(self.print_symbol) * self.__width
                for _ in range(self.__height)])

    def __repr__(self):
        """
        Returns a string representation of the rectangle for recreation
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message when the instance is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
