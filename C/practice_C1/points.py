class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        print('test1')
        # return self is other
        return self.x == other.x and self.y == other.y

    def __str__(self):

        return f'Dokkkkt: {self.x, self.y}'


p1 = Dot(1, 2)
p2 = Dot(1, 2)
# print(p1 == p2)

print(str(p1))
print(p2)
