a = str(input("Nhập n= "))
def luu_tep_tin(x):
    with open(x,'w') as f:
        f.write(a)
        f.close()
luu_tep_tin(r'D:\projiect\tệp tin.txt')


def doc_tep_tin(x):
    with open(x,'r') as f:
        z = f.read()
        print(z)
        f.close()
doc_tep_tin(r'D:\projiect\tệp tin.txt')


a = str(input("nhập n =  "))
def ghi_tep_tin(x):
    with open(x,'a') as f:
        f.write('\n')
        f.write(a)
        f.close()
ghi_tep_tin(r'D:\projiect\tệp tin.txt')


def doc_tep_tin_bai_3(x):
    with open(x,'r') as f:
        z = f.read()
        print(z)
        f.close()
doc_tep_tin_bai_3(r'D:\projiect\tệp tin.txt')


import numpy as np
def sinh_ngau_nhien_so_nguyen():
    np.random.seed(10001)
    a = np.random.randint(low = -1000, high = 1000, size = 1000)
    return a
def ghi_tep_tin(x,a):
    with open(x,'w') as f:
        for i in range (0,1000,1):
            if i % 10 != 0:
                f.write(str(a[i]))
                f.write(',')
            else:
                f.write('\n')
                f.write(str(a[i]))
                f.write(',')
        f.close()
def main():
    z = sinh_so_nguyen()
    print(z)
    ghi_tep_tin(r'D:\projiect\1000 số.txt',sinh_so_nguyen())
if __name__ == "__main__":
    main()