class MetaConst(type):
    def __getattr__(cls, key):
        return cls[key]

    def __setattr__(cls, key, value):
        raise TypeError#

class Const(object, metaclass=MetaConst):
    def __getattr__(self, name):
        return self[name]

    def __setattr__(self, name, value):
        raise TypeError

class MyConst(Const):
    A = 42
    B = int(43)

x = MyConst.A
y = MyConst.B


print(x, y)
print(type(x), type(y))
