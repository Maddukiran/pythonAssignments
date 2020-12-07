'''
__call__ --> decoration class

'''

class Num:
    def __init__(self, value):
        self.var = 10
        if type(value) == type(10):
            self.var = value

    def __str__(self):
        return str(self.var)

    def __add__(self, other): #overloading + operator
        return Num(self.var + other.var)

    def __sub__(self, other): #overloading - operator
        return Num(self.var + other.var)

    def __lt__(self, other): #overloading > operator
        return self.var > other.var

    def __gt__(self, other): #overloading < operator
        return self.var < other.var

var1 = Num(100)

var2 = Num('hello')

var3 = var1 + var2

print(var1 > var2)
print(var1 < var2)

print(f'var1--> {var1}')
print(f'var2--> {var2}')
print(f'var3--> {var3}')