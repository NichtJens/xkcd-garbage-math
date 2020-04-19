#!/usr/bin/env python3


class Garbage:
    """
    https://xkcd.com/2295/
    """

    def __repr__(self):
        return "Garbage"

    def _return_self(self, *args):
        return self

    def __mul__(self, other):
        if other == 0:
            return 0
        return self

    __add__ = __sub__ = __div__ = __truediv__ = __pow__ = _return_self

    __radd__ = __add__
    __rsub__ = __sub__
    __rmul__ = __mul__
    __rdiv__ = __div__
    __rtruediv__ = __truediv__
    __rpow__ = __pow__

    sqrt = _return_self # for numpy.sqrt #TODO math.sqrt



Garbage = Garbage()





if __name__ == "__main__":
    precise_number = 42

    try:
        from numpy import sqrt
    except ImportError:
        def sqrt(x):
            return Garbage**(1/2)

    assert precise_number + Garbage == Garbage
    assert precise_number * Garbage == Garbage
    assert sqrt(Garbage) == Garbage
    assert Garbage**2 == Garbage
    assert precise_number**Garbage == Garbage
    assert Garbage - Garbage == Garbage
    assert precise_number / (Garbage - Garbage) == Garbage
    assert Garbage * 0 == 0



