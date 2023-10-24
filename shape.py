"""
This module defines classes for different shapes.
"""

class Shape:
    """
    The base class for all shapes.
    """

    def __init__(self, color, name):
        """
        Initializes a Shape object with the given name and color.
        """
        self.name = name
        self.color = color

    def say_name(self):
        """
        Returns the name of the shape.
        """
        return f"My name is {self.name}"

    def set_name(self, name):
        """
        Set the name of the shape.
        Args: name (str): The name to set.
        Returns: None
        """
        self.name = name

    def get_name(self):
        """_summary_
        Get the name of the shape.
        Returns: str: The name of the shape.
        """
        return self.name

class Rectangle(Shape):
    """
    Represents a rectangle shape.
    """

    def __init__(self, color, name, width, height):
        """
        Initializes a Rectangle object with the given name, color, width, and height.
        """
        super().__init__(color, name)
        self.width = width
        self.height = height

    def say_name(self):
        """
        Returns the name of the rectangle along with its shape type.
        """
        return f"My name is {self.name} and I am a rectangle."

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


class Circle(Shape):
    """
    Represents a circle shape.
    """

    def __init__(self, color, name, radius):
        """
        Initializes a Circle object with the given name, color, and radius.
        """
        super().__init__(color, name)
        self.radius = radius

    def say_name(self):
        """
        Returns the name of the circle along with its shape type.
        """
        return f"My name is {self.name} and I am a circle."

    def area(self):
        """
        Calculates and returns the area of the circle.
        """
        return 3.14159265359 * self.radius ** 2

    def perimeter(self):
        """
        Calculates and returns the perimeter of the circle.
        """
        return 2 * 3.14159265359 * self.radius
