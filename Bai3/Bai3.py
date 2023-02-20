from math import sin, log


def main(a, n, b):
    answer = float(0)
    for j in range(1, b + 1):
        for c in range(1, n + 1):
            for i in range(1, a + 1):
                answer += float(log(78 * c ** 3) ** 6 + sin(j - i ** 3))
    return answer


x = float(input())
y = float(input())
z = float(input())
print(main(x, y, z))
