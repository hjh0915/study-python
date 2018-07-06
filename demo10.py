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

class Student(Person):
    def __init__(self, n, id, school):
        self.school = school
        super(Student, self).__init__(n, id)

    def is_student(self):
        if self.age <= 19:
            return True
        else:
            return False

class Teacher(Person):
    def __init__(self, n, id, school, level):
        self.school = school
        self.level = level
        super(Teacher, self).__init__(n, id)

if __name__ == '__main__':
    x1 = Student('胡俊华', '360103199909150025', '上高二中')
    if x1.is_student():
        print ('''
            姓名: %s 出生日期: %s 性别: %s 年龄: %s 学校: %s
        ''' % (x1.name, x1.birth_date, x1.sex, x1.age, x1.school))
    else:
        if x1.sex == '女':
            print('she is not a student')
        else:
            print('he is not a student')

    x2 = Teacher('胡志刚', '360102197209163874', '上高二中', '中级')
    print '%s, 年龄: %s, 教师级别: %s' % (x2.name, x2.age, x2.level)



