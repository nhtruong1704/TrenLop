from math import ceil


def main(z):
    n = len(z)
    result = 0
    for i in range(1, n + 1):
        result += (z[n - ceil(i / 3)] + 79 * z[n - ceil(i / 3)] ** 2 + 79 * z[n - ceil(i / 3)] ** 3) ** 2

    return result


print('%.2e' % main([-0.87, 0.77]))
