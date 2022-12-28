import random

random.seed(100)


def sinh_lisst_so_thuc(n, a, b):
    x = [random.uniform(a, b) for i in range(n)]
    print(x)
    return x


def sinh_lisst_so_thuc2(n, a, b):
    y = [random.uniform(a, b) for i in range(n)]
    print(y)
    return y


def sap_xep_tang_dan(x):
    x = sorted(x, reverse=False)
    print(x)


def sap_xep_giam_dan(x):
    x = sorted(x, reverse=True)
    print(x)


def sap_xep(x, flag):
    if flag == True:
        return sap_xep_giam_dan(x)

else:
return sap_xep_giam_dan(x)


def liet_ke(v, n):
    ntn = []
    for i in range(len(v)):
        if v[i] == n:
            ntn.append(i)
    print(ntn)

else:
print('không có')
return ntn


def tap_tin_van_ban(x, file):
    with open(file, 'w') as f:
        for item in x:
            f.write('%s/n' % item)
    print('tap tin van ban')


def tap_tin_nhi_phan(y, file):
    with open(file, 'wb') as f:
        for item in y:
            chuyendoi = int(item)
            f.write(chuyendoi.to_bytes(8, 'big'))
    print('tap tin nhi phan')


def main():
    x = sinh_lisst_so_thuc(3, 5, 7)
    y = sinh_lisst_so_thuc2(2, 4, 6)
    sap_xep(x, True)
    liet_ke(x, 6)


tap_tin_van_ban(x, 'D:/doan/nnn.txt')
tap_tin_nhi_phan(x, 'D:/doan/nnn1.dat')
if __name__ == '__main__':
    main()
