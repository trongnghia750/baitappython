from student import SinhVien
import os
import pickle

def ghi_sinhvien(thumuc: str, ten_taptin: str, obj: SinhVien):
    try:
        with open(os.path.join(thumuc, ten_taptin), 'wb') as f:
            pickle.dump(obj, f)
        print('Hoan thanh qua trinh ghi du lieu vao tap tin')
    except Exception as e:
        print('Xay ra loi trong qua trinh ghi file')

def doc_sinhvien(thumuc: str, ten_taptin: str) -> SinhVien:
    try:
        with open(os.path.join(thumuc, ten_taptin), 'rb') as f:
            sv = pickle.load(f)
        return sv
    except Exception as e:
        return None

def main():
    path = 'C:\\ntn\\data'
    filename = 'sinhvien2.dat'
    sv1 = SinhVien('Van Nhi', 2004, 10.0)
    ghi_sinhvien(path, filename, sv1)
    noidung = doc_sinhvien(path, filename)
    print(noidung)
    print('ket thuc chuong trinh')

if __name__ == '__main__':
    main()