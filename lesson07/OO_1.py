class Human:
    name = ''
    sex = ''
    age = 0

    def __str__(self):
        return self.name + ", " + self.sex + ", " + str(self.age)

#print(__name__)
if __name__ == '__main__':
    h = Human()
    h.name = 'Vincent'
    h.sex = '男'
    h.age = 18
    print(h.name, h.sex, h.age)
    print(h)
