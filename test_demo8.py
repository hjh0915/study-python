# -*- coding: utf8 -*-
from demo8 import birth_date
from demo8 import sex
from demo8 import age 

def test_date():
    assert birth_date('360103199909150025') == '19990915'

def test_sex():
    assert sex('360103199909150025') == '女'
    assert sex('360102197209163874') == '男'

def test_age():
    assert age('360103199909150025') == 19
    assert age('360102197209163874') == 46