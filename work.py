from datetime import datetime
from datetime import timedelta

def get_period(s: str) -> str:
    """
       提取产品周期
    
    >>> s = '债券2018年第235期三个月定开成长净值型'
    >>> get_period(s)
    '三个月'
    """
    start = s.index('期') + 1
    end = s.index('定开')
    return s[start:end]
    
def get_days(s: str, period: dict) -> int:
    """
       计算日期
    
    >>> s = '三个月'
    >>> period = {'三个月': 30}
    >>> get_days(s, period)
    90
    """
    return period[s]

def get_date(loop_days: int, start: datetime, now: datetime) -> str:
    """
       日期区间

    >>> loop_days = 30
    >>> start = start = datetime(2018, 5, 18)
    >>> now = datetime.today()
    >>> get_date(loop_days, start, now)
    (datetime.datetime(2018, 7, 19, 0, 0), datetime.datetime(2018, 8, 16, 0, 0))
    """
    x1 = start
    x2 = x1 + timedelta(days=loop_days)
    #开始日期是start, 循环加loop_days
    while True:
        if (x1 < now) and (now < x2):
            return (x1, x2)
        x1 = x1 + timedelta(days=loop_days+1)
        x2 = x2 + timedelta(days=loop_days)
        
def get_days_02(loop_days: int, start: datetime, now: datetime) -> str:
    """
       日期区间

    >>> loop_days = 30
    >>> start = start = datetime(2018, 5, 18)
    >>> now = datetime.today()
    >>> get_date(loop_days, start, now)
    (datetime.datetime(2018, 7, 19, 0, 0), datetime.datetime(2018, 8, 16, 0, 0))
    """
    x1 = start 
    x2 = x1 + timedelta(days=loop_days)
    diff = now - x1
    x = diff % loop_days
    while True:
        if (x1 < now) and (now < x2):
            return (x1, x2)
        x1 = x1 + x * timedelta(days=loop_days+1)
        x2 = x2 + x * timedelta(days=loop_days)


