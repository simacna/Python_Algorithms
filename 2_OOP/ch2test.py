class Vector:
    """ Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros"""
        self._coords =[0]*d

    def __len__(self):
        """Return the dimension of the vector"""
        return len(self._coords)

    def __getitem__(self, j):
        """ Return jth coordinate of vector"""
        return self._coords[j]

    def __setitem__(self, j, val):
        """set jth coordinate of vector a given value"""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors"""
        if len(self) != len(other): #relies on __len__ method
            raise ValueError('Dimensions must agree')
        result = Vector(len(self))  #start with vector of zeros

        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result #
    def __whole__(self):
        return self._coords
    def __eq__(self, other):
        """Return True if vector has same coordinates as other"""
        return self._coords == other._coords #Personal question - other._coords? That isn't clicking for some reason
    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other
    def __str__(self):
        """Produce string representation of vector"""
        return '<' + str(self._coords)[1:-1]+ '>' #adapt list representation -- QUESTION. why not str.(self._coords)[0:-1]?
    def __sub__(self, other):
        """Return the subtraction of two vectors"""
        # sub = []
        # if len(self) != len(other):
        #     raise ValueError("Dimensions must agree")
        # for v in self._coords:
        #     a = self._coords[v] - other[v]
        #     sub.append(a)
        # return sub
        if len(self) != len(other): #relies on __len__ method
            raise ValueError('Dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result


vex = Vector(4)
who = vex.__setitem__(0,2)
a = vex.__sub__([3,3,3,3])

print(a)