import jieba
import pandas as pd

# 读取CSV文件
df = pd.read_csv('collect3.csv')

# 对标题列进行分词
df['分词后标题'] = df['标题'].apply(lambda x: ' '.join(jieba.cut(x)))

# 输出结果
print(df.head())
df.to_csv('collect4.csv', index=False, encoding='utf-8-sig')