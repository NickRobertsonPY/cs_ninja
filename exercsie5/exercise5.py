
class pizza:
    def __init__(self, number):
        self.number = number

    def __int__(self):
        return self.number


x = pizza(5)
y = x
print(type(y))
print(y.number)
print(type(x))
print(x.number)
