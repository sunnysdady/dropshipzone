import pandas as pd

def read_excel_or_csv(file):
    """自动识别上传的 Excel 或 CSV 并返回 DataFrame"""
    if file.name.endswith('.xlsx') or file.name.endswith('.xls'):
        return pd.read_excel(file)
    else:
        return pd.read_csv(file)
