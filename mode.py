import pandas as pd
import os

# 加载知网情感词典
def load_dict(dict_path, encoding='UTF-8'):
    dict_list = []
    with open(dict_path, 'r', encoding=encoding) as f:
        for line in f:
            line = line.strip()
            if line != '':
                dict_list.append(line)
    return dict_list

# 加载情感词典
pos_words = load_dict(os.path.join(os.getcwd(), 'NLPCC-Emotion-NT-1.0', '正面情感词语（中文）.txt'), encoding='GBK')
pos_eval_words = load_dict(os.path.join(os.getcwd(), 'NLPCC-Emotion-NT-1.0', '正面评价词语（中文）.txt'), encoding='GBK')
neg_words = load_dict(os.path.join(os.getcwd(), 'NLPCC-Emotion-NT-1.0', '负面情感词语（中文）.txt'), encoding='GBK')
neg_eval_words = load_dict(os.path.join(os.getcwd(), 'NLPCC-Emotion-NT-1.0', '负面评价词语（中文）.txt'), encoding='GBK')
degree_words = load_dict(os.path.join(os.getcwd(), 'NLPCC-Emotion-NT-1.0', '程度级别词语（中文）.txt'), encoding='GBK')
adv_words = load_dict(os.path.join(os.getcwd(), 'NLPCC-Emotion-NT-1.0', '主张词语（中文）.txt'), encoding='GBK')

# 计算情感得分
def calculate_sentiment(text, pos_dict, neg_dict, degree_dict):
    pos_score = 0
    neg_score = 0
    degree_score = 1
    words = text.split(' ')
    for word in words:
        if word in pos_dict:
            pos_score += 1
        elif word in pos_eval_words:
            pos_score += 1
        elif word in neg_dict:
            neg_score += 1
        elif word in neg_eval_words:
            neg_score += 1
        elif word in degree_dict:
            degree_score *= 1.5
    sentiment_score = (pos_score - neg_score) * degree_score
    return abs(sentiment_score)

# 导入数据
data = pd.read_csv('collect4.csv')

# 计算情感得分
data['情感得分'] = data['分词后标题'].apply(calculate_sentiment, pos_dict=pos_words, neg_dict=neg_words, degree_dict=degree_words)

# 输出结果
data.to_csv('collect5.csv', index=False, encoding='utf-8-sig')
