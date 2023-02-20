from cmath import atan


def main(n: float):
    if n == 0:
        return float(0.16)
    if n == 1:
        return float(-0.52)
    if n >= 2:
        return (atan(main(n - 2)) ** 2 + 29 * atan(93 * main(
            n - 1) - main(n - 2) ** 3 - 96 * main(n - 1) ** 2) ** 3).real


a = float(input())
print(main(a))
