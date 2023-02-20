import math
from cmath import atan
from math import floor


def main(y: float):
    if y < 81:
        s = y / 4
        return float(s)
    elif 81 <= y < 138:
        s = 88 * y ** 2 + 43 * (y - 50 * y ** 3) ** 7
        return float(s)
    elif 138 <= y < 229:
        s = y ** 5
        return float(s)
    elif 229 <= y < 242:
        s = 20 * y ** 4 + 77 * atan(1 + y) ** 7
        return float(s)
    elif y >= 242:
        s = math.log(y) ** 5 - (floor(y)) ** 2
        return float(s)


a = float(input())
print(type(main(a)))
