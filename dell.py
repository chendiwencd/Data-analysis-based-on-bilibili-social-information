import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('collect1.csv')

# 遍历 DataFrame 中的每一行
for index, row in df.iterrows():
    # 判断第二列的值是否包含 '万' 字符串
    if '万' in str(row[1]):
        # 将第二列的值乘以 10000
        df.at[index, df.columns[1]] = float(str(row[1]).replace('万', '')) * 10000
    if '万' in str(row[2]):
        # 将第二列的值乘以 10000
        df.at[index, df.columns[2]] = float(str(row[2]).replace('万', '')) * 10000

# 将修改后的 DataFrame 写入新的 CSV 文件
df.to_csv('collect2.csv', index=False, encoding='utf-8-sig')
