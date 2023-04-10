import glob
import pandas as pd

path =r"D:\code\code\data" # csv文件所在的目录，注意通配符*表示匹配所有文件名
all_files = glob.glob(path)

li = []  # 用于存放所有csv文件的数据
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

# 合并所有数据
df_all = pd.concat(li, axis=0, ignore_index=True)

# 删除标题相同的行
df_all.drop_duplicates(subset=['标题'], inplace=True)

# 保存结果
df_all.to_csv('collect1.csv', index=False)
