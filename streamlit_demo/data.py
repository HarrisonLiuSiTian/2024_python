"""
@文件名: data.py
@作者: HarrisonLiu
@日期: 2024-03-29：22-42-37
@描述: 
@Version : 0.0.0
"""
import pickle
from pathlib import Path

import pandas as pd


def load_file(path: str) -> pd.DataFrame:
    with open(path, 'rb') as f:
        data_set = pickle.load(f)
        return data_set


def load_data(folder: str) -> pd.DataFrame:
    all_datasets = [load_file(file) for file in Path(folder).iterdir()]
    df = pd.concat(all_datasets)
    return df


if __name__ == '__main__':
    # glob("*.pkl")
    df = load_file(".\\data\\2018-04-01.pkl")
    print(df)
