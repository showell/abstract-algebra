from lib.type_enforcers import enforce_type

class AbstractMath:
    def __init__(self, *, value_type, zero, one):
        self.value_type = value_type
        self.zero = zero
        self.one = one

    def add(self, a, b):
        enforce_type(a, self.value_type)        
        enforce_type(b, self.value_type)        
        return a + b

    def additive_inverse(self, a):
        enforce_type(a, self.value_type)        
        return -a

    def multiply(self, a, b):
        enforce_type(a, self.value_type)        
        enforce_type(b, self.value_type)        
        return a * b

    def power(self, n, p):
        enforce_type(n, self.value_type)        
        enforce_type(p, int)
        return n ** p
