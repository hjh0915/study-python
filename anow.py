import time 
import angle

from typing import Tuple
from datetime import datetime


def call():
    """
    Return the angle between hour hands and min hands 
    and the time now.
    """
    try:
        while True:
            t = datetime.now()
            minute = t.minute
            hour = t.hour 
            print(t, angle.angle(hour, minute))
            time.sleep(60)
    except KeyboardInterrupt:
        print('安全退出')

if __name__ == '__main__':
    x = datetime.now()
    call()