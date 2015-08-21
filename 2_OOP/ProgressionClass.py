class Progression:
    """ Iterator producing a generic progression

    Default iterator produces the whole numbers 0, 1, 2...
    """

    def __init__(self, start=0):
        """ Initialize current to the first value of progression."""
        self._current = start

    def _advance(self):
        """Update self._current to a new value.
        This should be overriden by a subclass to customize progression.
        By convention, if current is set to None, this designated the end of a finite progression.
        """

        self._current += 1

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""

        if self._current is None:
            raise StopIteration
        else:
            answer = self._current  # record current value to return
            self._advance()         # advance to prepare for next time
            return answer           # return the answer

    def __iter__(self):
       """By convention, an iterator must return itself as an iterator"""
       return self #QUESTION - what does this return? The init constructor?

    def print_progression(self, n):
        """  Print next n values of the progression."""

        print (''.join(str(next(self)) for j in range(n)))

class ArithmeticProgression(Progression):
    """Iterator producing an arithmetic progression"""

    def __init__(self, increment=1, start=0):
        """ Create a new arithmetic progression
        increment the fixed constant to add to each term (default 1)
        start     the first term of the progression
        """

        super().__init__(start) #call super constructor/initialize base class
        self._increment = increment

    def _advance(self): #override inherited version
        """ Update current value by adding the fixed increment"""
        self._current += self._increment

class GeometricProgression(Progression):
    """ Iterator producing a geometric progression"""

    def __init__(self, base=2, start=1):
        """Create a new geometric progression

    base the fixed constant multiplied to each term (default 2)
    start first term of the progression
        """

        super().__init__(start)
        self._base = base

    def _advance(self):
        """Update current value by multiplying base"""

        self._current *= self._base


class FibonacciProgression(Progression):
    """Iterator producing a generalized Fibonacci progression."""


    def __init__(self, first=0, second=1):
        """Create a new fibonacci progression

        first   the first term of the progression (default 0)
        second  the second term of the progression (default 1)
        """

        super().__init__(first)  #start progression at first
        self._prev = second - first  #fictious value preceding the first

    def _advance(self):
        """Update current value by taking sum of previous two."""

        self._prev, self._current = self._current, self._prev + self._current #does self._current, which is
        #on the parent class's __init__ self._current = start get passed

if __name__ == '__main__':
    print('Default progression:')
    Progression().print_progression(10)

    print('Arithmetic progression with increment 5:')
    ArithmeticProgression(5).print_progression(10)

    print('Arithmetic progression with incrememnt 5 and start 2:')
    ArithmeticProgression(5,2).print_progression(10)

    print('Geometric progression with default base:')
    GeometricProgression().print_progression(10)

    print('Geometric progression with base 3:')
    print (GeometricProgression(3).print_progression(10))

    print('Fibonacci progression with default start values:')
    FibonacciProgression().print_progression(10)

    print('Fibonacci progression with start values 4 and 6:')
    FibonacciProgression(4,6).print_progression(10)

