import cmath
from math import sqrt


def main():
    a = 10 + 5j
    print(a)              # (10+5j)
    print(a.real)         # 10.0
    print(a.imag)         # 5.0
    print(abs(a))         # 11.180339887498949
    print(a.conjugate())  # (10-5j)

    b = complex(6, -3.5)
    print(b)              # (6-3.5j)
    print(b.real)         # 6.0
    print(b.imag)         # -3.5
    print(abs(b))         # 6.946221994724902
    print(b.conjugate())  # (6+3.5j)

    c = b.conjugate()
    d = c * b
    print(d)              # (48.25+0j)

    print(d + 2)          # (50.25+0j)
    print(a - b)          # (4+8.5j)
    print(a * 2)          # (20+10j)
    print(a ** 2)         # (75+100j)
    print(b / a)          # (0.34-0.52j)

    print(cmath.sqrt(a))   # (3.254254130173222+0.7682251907803299j)
    print(cmath.phase(a))  # 0.4636476090008061
    c = cmath.polar(a)
    print(c)               # (11.180339887498949, 0.4636476090008061)
    print(cmath.rect(*c))  # (10+5j)


def solve_quadratic(a, b, c):
    D = b ** 2 - 4 * a * c
    if D >= 0:
        root_1 = (-b + sqrt(D)) / (2 * a)
        root_2 = (-b - sqrt(D)) / (2 * a)
    else:
        root_1 = complex(-b / (2 * a), sqrt(abs(D)) / (2 * a))
        root_2 = complex(-b / (2 * a), -sqrt(abs(D)) / (2 * a))
    return root_1, root_2


if __name__ == '__main__':
    main()
    print("###################")
    roots = solve_quadratic(4, 7, 8)
    # Roots: ((-0.875+1.1110243021644486j), (-0.875-1.1110243021644486j))
    print("Roots:", roots)
