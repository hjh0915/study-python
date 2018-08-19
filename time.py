from typing import Tuple

MIN_ANGLE = 6 #每分钟转过的角度，360 / 60所得
HOUR_ANGLE = 30 #每小时转过的角度，360 / 12所得
PI = 360
HALF_DAY = 12


def get_hands(s: str) -> Tuple[int]:
    x = s.split(':')
    return (int(x[0]), int(x[1]))


def angle(hour_hand: int, min_hand: int) -> float:
    """
    Return the angle between hour_hand and second_hand.

    >>> angle(1, 20)
    80.0
    >>> angle(1, 40) 
    190.0
    """

    hour_in_12 = hour_hand % HALF_DAY
    x = min_hand * MIN_ANGLE
    y = (hour_in_12 + min_hand / 60) * HOUR_ANGLE 
    return abs(x - y) % PI

def call(s):
    h, m = get_hands(s)
    return angle(h, m)

if __name__ == '__main__':
    print(call('12:00'))
    print(call('20:35'))
    print(call('8:35'))