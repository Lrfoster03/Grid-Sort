from types import SimpleNamespace


class WithXY:
    """A container with uppercase X, Y attributes."""
    def __init__(self, x, y):
        self.X = x
        self.Y = y


class WithxyLower:
    """A container with lowercase x, y attributes."""
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Nested:
    """A container with nested X, Y attributes in an inner object."""
    def __init__(self, x, y):
        self.inner = SimpleNamespace(X=x, Y=y)


class WithPropsUpper:
    """A container with X, Y properties instead of direct attributes."""
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def X(self):
        return self._x

    @X.setter
    def X(self, v):
        self._x = v

    @property
    def Y(self):
        return self._y

    @Y.setter
    def Y(self, v):
        self._y = v