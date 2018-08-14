# -*- coding: utf8 -*-

import unittest
import work
from datetime import datetime
import settings

class TestWork(unittest.TestCase):
    def test_01(self):
        s = '债券2018年第235期三个月定开成长净值型'
        x = '三个月'
        self.assertEqual(work.get_period(s), x)
    
    def test_02(self):
        s = '债券2018年第235期三个月定开成长净值型'
        x = 90
        y = work.get_period(s)
        self.assertEqual(work.get_days(y, settings.PERIOD), x)
    
    def test_03(self):
        loop_days = 30
        start = datetime(2018, 5, 18)
        now = datetime.today()
        #x = (datetime(2018,8,18), datetime(2018,9,23))
        print(work.get_date(loop_days, start, now))
    
    def test_04(self):
        loop_days = 30
        start = datetime(2018, 5, 18)
        now = datetime.today()
        #x = (datetime(2018,8,18), datetime(2018,9,23))
        print(work.get_days_02(loop_days, start, now))

unittest.main()
