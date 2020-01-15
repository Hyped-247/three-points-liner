
class Point:
    """
    Stores, and validates X, Y points.
    """
    def __init__(self, x, y):
        """
        :param x: number
        :param y: number
        """
        self._x = x
        self._y = y
        self._validate()

    def get_x(self):
        """
        :return: number
        """
        return self._x

    def get_y(self):
        """
        :return: number
        """
        return self._y

    def get_point(self):
        """
        :return: tuple
        """
        return self._x, self._y

    def _validate(self) -> list or TypeError:
        """
        Validates the input data. If the input data is a list
        containing two numbers, then the will return that list.
        Otherwise, it will throw a TypeError.
        :return: validated point list
        :raise TypeError if points are not numbers.
        """
        if not isinstance(self._x, (int, float)) or not isinstance(self._y, (int, float)):
            raise TypeError("The points list must contain float or int.")
        return self.get_point()

    def __eq__(self, other):
        """
        :param other:
        :return: bool
        """
        return self.get_point() == other.get_point()

    def __hash__(self):
        """
        :return: int
        """
        return hash(self.get_point())
