# -*- coding: utf8 -*-

import unittest
import demo41 

class TestDemo41(unittest.TestCase):
    """测试十进制转化为二进制"""
    
    def test_even_number(self):
        """测试偶数"""

        expected = '1100'
        result = demo41.change(12)
        self.assertEqual(expected, result)

    def test_odd_number(self):
        """测试奇数"""

        expected = '1011'
        result = demo41.change(11)
        self.assertEqual(expected, result)
        

#python test_demo41.py -v
unittest.main()
    

