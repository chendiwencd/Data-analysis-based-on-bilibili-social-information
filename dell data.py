import pandas as pd
import jieba
from snownlp import SnowNLP

url = "http://api.bosonnlp.com/sentiment/analysis"
headers = {
    "Content-Type": "application/json",
    "X-Token": "你的API Token"
}


# 读取CSV文件
df = pd.read_csv('collect2.csv', encoding='utf-8')

# 将第二列中的0替换为0.0001
df.iloc[:, 1].replace(0, 0.0001, inplace=True)
df.iloc[:, 2] = df.iloc[:, 2].replace(0, 0.0001).astype(float)

# 将第二列的数据类型转换为float类型
df.iloc[:, 1] = df.iloc[:, 1].astype('float')

# 将第三列的数据类型转换为float类型
df.iloc[:, 2] = df.iloc[:, 2].astype('float')

# 计算第四列的数据
df['回馈率'] = df.iloc[:, 2] / df.iloc[:, 1]
df = df[df['回馈率'] >= 0.00001]

# 修改列名
df = df.rename(columns={"回馈率": "回馈率（‰）"})

# 把回馈率列整列乘以 1000
df["回馈率（‰）"] = df["回馈率（‰）"] * 1000

# 保存修改后的数据到CSV文件中
df.to_csv('collect3.csv', index=False, encoding='utf-8-sig')
