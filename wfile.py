#encoding=gbk
# pyexcel_xls �� OrderedDict �ṹ��������
from collections import OrderedDict
from pyexcel_xls import get_data
from pyexcel_xls import save_data
def read_xls_file():
    xls_data = get_data(r"D:\PythonCode\muban.xls")
    print("Get data type:", type(xls_data))
    for sheet_n in xls_data.keys():
        print(sheet_n, ":", xls_data[sheet_n])
    return xls_data
# дExcel����, xls��ʽ
def save_xls_file():
    data = OrderedDict()
    # sheet�������
    sheet_1 = []
    row_1_data = [u"ID", u"�ǳ�", u"�ȼ�"]  # ÿһ�е�����
    row_2_data = [1, 2, 6]
    # �����������
    sheet_1.append(row_1_data)
    sheet_1.append(row_2_data)
    # ���sheet��
    data.update({u"����XX��": sheet_1})

    # �����xls�ļ�
    save_data("D:\PythonCode\muban.xls", data)


if __name__ == '__main__':
    save_xls_file()