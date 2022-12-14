from student import SinhVien
import os
import pickle

def ghi_sinhvien(thumuc: str, ten_taptin: str, objs: list[SinhVien]):
    try:
        with open(os.path.join(thumuc, ten_taptin), 'wb') as f:
            pickle.dump(objs, f)
        print('Hoan thanh qua trinh ghi du lieu vao tap tin')
    except Exception as e:
        print(e)
        print('Xay ra loi trong qua trinh ghi file')

def doc_sinhvien(thumuc: str, ten_taptin: str) -> list[SinhVien]:
    try:
        with open(os.path.join(thumuc, ten_taptin), 'rb') as f:
            sv = pickle.load(f)
        return sv
    except Exception as e:
        return None

def in_list_sinhvien(content: list[SinhVien]):
    for item in content:
        print(item)

def main():
    path = 'C:\\ntn\\data'
    filename = 'sinhvien3.dat'
    sv1 = [SinhVien('Van Nhi', 2004, 10.0),
           SinhVien('Duy', 2005, 12.0),
           SinhVien('Tri', 2005, 3.0)]
    ghi_sinhvien(path, filename, sv1)
    noidung = doc_sinhvien(path, filename)
    in_list_sinhvien(noidung)
    print('ket thuc chuong trinh')

if __name__ == '__main__':
    main()