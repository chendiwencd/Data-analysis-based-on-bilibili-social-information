# import pandas as pd
# from ltp import LTP
#
# # 加载LTP情感分析模型
# ltp = LTP()
#
# # 读取数据文件
# df = pd.read_csv('collect4.csv')
#
# # 对“分词后标题”列进行情感分析
# sentiment_scores = []
# for text in df['分词后标题']:
#     # 调用LTP的情感分析接口，获取每个词语在积极情感、消极情感、悲伤情感、愉快情感和愤怒情感五个维度上的得分
#     seg, hidden = ltp.seg([text])
#     sents = ltp.sentiment(hidden, [len(seg)])
#     # 将得分转换为绝对值，并计算每个样本五个维度绝对值得分的总和
#     sentiment_score = [sum([abs(score[i]) for score in sents]) for i in range(5)]
#     sentiment_scores.append(sentiment_score)
#
# # 将得分总和添加为新的一列，并将结果保存为collect6.csv文件
# df['情感得分'] = sentiment_scores
# df.to_csv('collect5.csv', index=False)


import pandas as pd
from snownlp import SnowNLP

# 读取CSV文件
df = pd.read_csv('collect4.csv', encoding='utf-8')

# 对文本列进行情感强度分析
sentiments = []
for text in df['标题']:
    s = SnowNLP(text)
    sentiments.append(s.sentiments)

# 将情感强度得分作为新的一列添加到DataFrame中
df['情感强度得分'] = sentiments

df = df.drop('分词后标题', axis=1)

# 将结果保存为新的CSV文件
df.to_csv('testdata_with_sentiment.csv', index=False, encoding='utf-8-sig')
