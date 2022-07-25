nes (71 sloc)  2.17 KB

#!/usr/bin/python3

"""

    module to create a class Rectangle that defines a rectangle

"""


class Rectangle():

    """
    Rectangle - defines a rectangle
    Attributes:
        width (int): width class attribute
        height (int): height class attribute
        area(): returns the rectangle area
        perimeter(): returns the rectangle parameter
    Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
    Raises:
        TypeError: width must be an integer
        ValueError: width must be >= 0
        TypeError: height must be an integer
        ValueError: height must be >= 0
    """

    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = width
            self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) != int:
          return 2 * (self.__height  def __str__(self):
        h = self.__height
   uuu
