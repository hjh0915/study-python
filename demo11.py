# -*- coding: utf8 -*-

import datetime

class Person(object):
    def __init__(self, n, id):
        self.name = n
        self.id_card = id 

    def __repr__(self):
        return '%s, %s' % (self.name, self.id_card)

    @property
    def birth_date(self):
        return self.id_card[6:14]

    @property
    def sex(self):
        y = int(self.id_card[16])
        # 偶数是女，奇数是男
        if y % 2 == 0:
            return '女'
        else:
            return '男'

    @property
    def age(self):
        #从身份证中取年份
        z = int(self.id_card[6:10]) 
        #获取今年的年份
        d = datetime.datetime.today().year
        return d - z

    def is_student(self):
        if self.age <= 19:
            return True
        else:
            return False

class Student(Person):
    def __init__(self, n, id, school):
        self.school = school
        super(Student, self).__init__(n, id)

class Teacher(Person):
    def __init__(self, n, id, school, level):
        self.school = school
        self.level = level
        super(Teacher, self).__init__(n, id)

if __name__ == '__main__':
    x1 = Student('胡俊华', '360103199909150025', '上高二中')
    x2 = Teacher('胡志刚', '360102197209163874', '上高二中', '中级')
   
    persons = [x1, x2]

    for x in persons:
        print x.name, x.birth_date, x.sex, x.age, x.is_student()