from sympy import symbols, Eq, solve


def giai_he_phuong_trinh(a, b, c, g, d, e, f, h, r, t, w, q):
    x, y, z = symbols('x y z')
    eq1 = Eq(a * x + b * y + c * z, g)
    eq2 = Eq(d * x + e * y + f * z, h)
    eq3 = Eq(r * x + t * y + w * z, q)
    answer = solve((eq1, eq2, eq3), (x, y, z))


print(answer)

from sympy import *


def giai_ham(x, f, a):
    answer = limit(f, x, a)
    print('Kết quả giới hạn: ', answer)


def dao_ham(x, f):
    answer = diff(f, x)
    print(answer)


def nguyen_ham(x, f):
    answer = integrate(f, x)
    print(answer)


def tich_phan(x, f, a, b):
    answer = integrate(f, (x, a, b))
    print(answer)


def main():
    x = symbols('x')
    giai_he_phuong_trinh(2, -5, 1, -5, 4, 2, -2, 2, 1, 1, -1, 0)
    giai_ham(x, (x ** 3 - 3 * x ** 2) ** 1 / 3 + (x ** 2 - 2 * x) ** 1 / 2, +00)
    dao_ham(x, (2 * x - 1) / (x + 2))
    nguyen_ham(x, (x / (x ** 2 + 1)))
    tich_phan(x, (1 - (x ** 2 * tan(x)) / (x ** 2 + cos(x) + x)), pi, (2 * pi / 3))


if __name__ == "__main__":
    main()
