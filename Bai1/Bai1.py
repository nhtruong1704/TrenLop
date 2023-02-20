'''
import math


def main(c):
    answer = 19 * c ** 6 / 89 * math.asin(c) ** 2 \
             + 76 * (c ** 2 + 69 * c ** 3 + c) ** 4 + 18 * c ** 6
    b = float('{:.2e}'.format(answer))
    return b
'''
import math
from cmath import sqrt, cos, tan
from math import log2


def main(z, x):
    answer = float(sqrt((cos(((z ** 3) / 13) + x ** 2) ** 4) / (7 * math.floor(97 - x ** 3) - z ** 4)) \
                   + sqrt((36 * (tan(39 + x) ** 6) + 86 * (z ** 4))
                          / (80 * (log2(22 + z ** 3) ** 4) - x ** 3)))

    return float(answer)


a = float(input())
b = float(input())
print(main(a, b))
