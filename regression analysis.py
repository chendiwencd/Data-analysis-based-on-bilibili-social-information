import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#字体乱码
plt.rcParams['font.family'] = 'SimHei'

# 读取数据
data = pd.read_csv("collect5.csv")

# 绘制柱状图
plt.bar(data["情感得分"], data["回馈率（‰）"])
plt.xlabel("情感强度得分")
plt.ylabel("回馈率")
plt.savefig('柱状图.png', dpi=300, bbox_inches='tight')
plt.show()

# 将情感强度得分和回馈率转换为NumPy数组
X = np.array(data["情感得分"]).reshape(-1, 1)
y = np.array(data["回馈率（‰）"])

# 拟合线性回归模型
model = LinearRegression()
model.fit(X, y)

# 预测回归值
y_pred = model.predict(X)

# 绘制回归曲线
plt.scatter(X, y, color='blue')
plt.plot(X, y_pred, color='red', linewidth=2)

# 添加斜率标注
slope = model.coef_[0]
plt.text(0.1, 0.9, "斜率 = {:.2f}".format(slope), transform=plt.gca().transAxes)

plt.xlabel("情感强度得分")
plt.ylabel("回馈率")
plt.savefig('回归曲线.png', dpi=300, bbox_inches='tight')
plt.show()