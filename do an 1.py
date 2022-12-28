import numpy as np

np.random.seed(123)


def tao_ma_tran(a, b, m, n):
    y = np.random.randint(low=a, high=b, size=m * n).reshape(m, n)
    print('ket qua la :', y)
    return (y)


def nhan_ma_tran(n, y):
    C = n * y
    print('ket  qua la :', C)


def nhan_ma_tran1(x, y):
    C = np.multiply(x, y)
    print('ket qua la :', C)


def nhan_ma_tran2(n, x):
    y = tao_ma_tran(4, 6, 3, 5)
    y_chuyenvi = y.T
    C = np.dot(x, y_chuyenvi)
    print('ket qua la :', C)


def main():
    x = tao_ma_tran(2, 4, 3, 5)
    y = tao_ma_tran(2, 4, 3, 5)
    nhan_ma_tran(x, y)
    nhan_ma_tran1(x, y)
    nhan_ma_tran2(2, x)


if __name__ == "__main__":
    main()

