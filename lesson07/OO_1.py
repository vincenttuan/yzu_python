class Human:
    name = ''
    sex = ''
    age = 0
    def __str__(self):  # self 相當於 java 中的 this
        return self.name + ", " + self.sex + ", " + str(self.age)

class Student(Human):
    number = 0
    grade = ''
    def __str__(self):
        return ", " + str(self.number) + ", " + self.grade


#print(__name__)
if __name__ == '__main__':
    h = Human()
    h.name = 'Vincent'
    h.sex = '男'
    h.age = 18
    print(h.name, h.sex, h.age)
    print(h)

    s = Student()
    s.name = 'Tom'
    s.sex = '男'
    s.age = 20
    s.number = 1
    s.grade = '一年級'
    print(s)