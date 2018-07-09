import zlib
s = b'witch which has which witches wrist watch'
len(s)
t = zlib.compress(s)
len(t)
zlib.decompress(t)
zlib.crc32(s)
from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
Timer('a,b = b,a', 'a=1; b=2').timeit()
import repr
repr.repr(set('supercalifragilisticexpialidocious'))
repr.repr(set('super califragi listic expiali docious'))
import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
pprint.pprint(t, width=30)
import textwrap
doc = """The wrap() method is just like fill() except that it returns 
a list of strings instead of one big string with newlines to separate
the wrapped lines."""
print textwrap.fill(doc, width=40)
from string import Template
t = Template('${village}folk send $$10 to $cause.')
t.substitute(d)
from string import Template
t = Template('${village}folk send $$10 to $cause.')
d = dict(item='unladen swallow')
t.substitute(d)
from string import Template
t = Template('${village}folk send $$10 to $cause.')
t.substitute(village='Nottingham', cause='the ditch fund')
import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'
fmt = input('Enter rename style (%d-date %n-seqnum %f-format): ')
fmt = input('Enter rename style (%d-date %n-seqnum %f-format): ')
class BatchRename(Template):
    delimiter = '%'
fmt = input('Enter rename style (%d-date %n-seqnum %f-format): ')
class BatchRename(Template):
    delimiter = '%'
fmt = input('Enter rename style (%d-date %n-seqnum %f-format): ')
from decimal import *
round(decimal('0.70') * decimal('1.05'), 2)
from decimal import *
round(Decimal('0.70') * Decimal('1.05'), 2)
round(.70 * 1.05, 2)
from decimal import *
round(Decimal('0.70') * Decimal('1.05'), 2)
from decimal import *
round(Decimal ('0.70') * Decimal ('1.05'), 2)
round(0.70 * 1.05, 2)
round(Decimal ('0.70') * Decimal ('1.05'), 2)
round(Decimal('0.70') * Decimal('1.05'), 2)
Decimal('1.00') % Decimal('.10')
1.00 % 0.10
sum([Decimal('0.1')]*10) == Decimal('1.0')
sum([0.1]*10) == 1.0
sum([0.1]*10) == 1
getcontext().prec = 36
Decimal(1) / Decimal(7)
1 / 7
from decimal import *
round(Decimal ('0.70') * Decimal ('1.05'), 2)
Decimal ('0.70') * Decimal ('1.05')
round(Decimal('0.735'))
round(Decimal('0.735'), 2)
round(Decimal('0.736'), 2)
round(Decimal('0.255'), 2)
round(Decimal('0.285'), 2)
round(Decimal('0.285'), 3)
round(Decimal('0.285'), 1)
round(Decimal('0.255'), 1)
round(Decimal('0.586'), 1)
Decimal ('0.70') * Decimal ('1.05')
0.7*1.05
2.675
Decimal(2.675)
Decimal('2.675')
getcontext().rounding = ROUND_UP
round(Decimal ('0.70') * Decimal ('1.05'), 2)
getcontext().rounding =  ROUND_05UP
round(Decimal ('0.70') * Decimal ('1.05'), 2)
getcontext().rounding =  ROUND_HALF_UP
round(Decimal ('0.70') * Decimal ('1.05'), 2)
 Decimal("33.505").quantize(Decimal("0.01"), decimal.ROUND_HALF_DOWN)
 Decimal("33.505").quantize(Decimal("0.01"), ROUND_HALF_DOWN)
 Decimal("33.505").quantize(Decimal("0.01"), ROUND_HALF_UP)
 Decimal("0.735").quantize(Decimal("0.01"), ROUND_HALF_UP)
(Decimal("0.70")*Decimal("1.05")).quantize(Decimal("0.01"), ROUND_HALF_UP)
history -f /home/hzg/study/demo19.py
