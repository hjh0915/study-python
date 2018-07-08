# -*- coding: utf8 -*-

import datetime

class Person:
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
            return 'F'
        else:
            return 'M'

    @property
    def age(self):
        #从身份证中取年份
        z = int(self.id_card[6:10]) 
        #获取今年的年份
        d = datetime.datetime.today().year
        return d - z


if __name__ == '__main__':
    x1 = Person('hjh', '360103199909150025')
    print ('姓名: %s 出生日期: %s 性别: %s 年龄: %s' % (x1.name, x1.birth_date, x1.sex, x1.age))

    x2 = Person('hzg', '360102197209163874')
    print ('姓名: %s 出生日期: %s 性别: %s 年龄: %s' % (x2.name, x2.birth_date, x2.sex, x2.age))
    
    f = open('work_demo9.txt', 'w')
    f.write('{0:10} {1:10} {2:10} {3:<10}'.format('name','date','sex','age'))
    f.write('\n')
    f.write('{0:10} {1:10} {2:10} {3:<10d}'.format(x1.name, x1.birth_date, x1.sex, x1.age))
    f.write('\n')
    f.write('{0:10} {1:10} {2:10} {3:<10d}'.format(x2.name, x2.birth_date, x2.sex, x2.age))
    f.close()


