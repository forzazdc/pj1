'''utf-8'''


import pandas as pd


def data_read_excel(file_path):
    df = pd.read_excel(file_path)
    print(df)


if __name__ == '__main__':
    path = r'E:\decheng\new_bi\new_project_20200921\data_source\Actuals Compound.xlsx'
    data_read_excel(path)