"""
python基本语法

"""


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    @staticmethod
    def full():
        print(100)

    pass


Student.full()
student1 = Student('Tom', 95)
student1.print_score()
