"""
deal_data2.py - 
Author: Alwin
Date:   2024/7/17
"""
import os
import pandas as pd

def load_data(file_path):
    """
    加载csv，返回副本
    :param file_path: The path to the CSV file.
    :return: A pandas DataFrame containing the data.
    """
    df = pd.read_csv(file_path)
    return df.copy()

def evaluation_data_structure(df):
    '''
    评估数据结构：
    是否需要优化索引--T方法
    每列/每行/每个单元格
    :param df:
    :return:
    '''
    df.head()
    # 本数据不需要处理，直接返回
    return df.reset_index(drop=True)


def evaluate_data_info(df):
    """
    评估数据内容是否缺失、重复、不一致、错误等问题。
    :param df: The DataFrame to evaluate.
    :return: None
    """
    # 删除关键值缺失了的数据
    print(df.info())
    if df['Weight'].isnull().sum() > 0:
        print('Weight列存在缺失数据')
        df.dropna(subset='Weight',inplace=True)
        return df
    # 评估关键数据是否存在重复数据
    if df['ProductID'].duplicate().sum() > 0:
        print('ProductID列存在重复数据')
        df.drop_duplicates(subset='ProductID',inplace=True)
        return df
    # 不一致
    df['FatContent'] = df['FatContent'].replace(
        {'low fat': 'Low Fat', 'LF': 'Low Fat', 'reg': 'Regular'})
    # 查看所有数值列的描述性统计信息--查看是否有错误信息
    print(clean_data.describe())


def clean_data(df):
    """
    Clean data in a DataFrame.

    :param df: The DataFrame to clean.
    :return: The cleaned DataFrame.
    """
    # Fill missing values with the mean of the column
    df = df.fillna(df.mean())

    # Convert data types if necessary
    # df['column_name'] = df['column_name'].astype('new_type')
    return df

def clean_data(file_path,saved_path):
    '''
    清洗并返回处理好的数据
    :param file_path:
    :param saved_path:
    :return:
    '''
    clean_data = load_data(file_path)
    clean_data = evaluation_data_structure(clean_data)
    clean_data = evaluate_data_info(clean_data)
    clean_data.to_csv(saved_path, index=False)


if __name__ == '__main__':
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = base_path + '/data/sale_data.csv'
    clean_data(file_path,base_path + '/data/cleaned_sale_data.csv')
    print('数据处理完成')