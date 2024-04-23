class Vector:
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

    def __add__(self, other):
        return Vector(self.x + other.x, self.y+other.y)


v1 = Vector(3, 4)
v2 = Vector(5, 9)

result = v1+v2

print(result.x, result.y)