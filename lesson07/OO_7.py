class Point(object):
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return self.x == other.x

    def __lt__(self, other):
        return self.x > other.x

if __name__ == '__main__':
    p1 = Point(10)
    p2 = Point(20)
    print(p1 == p2)
    print(p1 > p2)