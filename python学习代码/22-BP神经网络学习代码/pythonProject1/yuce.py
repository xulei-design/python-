import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

mpl.rcParams['font.sans-serif'] = [u'simHei']
mpl.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("Result_8.xlsx")
print(df.head())

x = df[['总氮','总烟碱','总糖','总还原糖','水份','PH值','氯']]
y = df[['浓度','劲头']]

# print(x.shape)
# #数据归一化操作
x_scaler = MinMaxScaler(feature_range=(-1,1))
y_scaler = MinMaxScaler(feature_range=(-1,1))
x = x_scaler.fit_transform(x)
y = y_scaler.fit_transform(y)
# 对样本数据进行转置,为了方便后续矩阵乘法操作
sample_in = x.T
sample_out = y.T
print(sample_in.shape)

#网络参数设置 bp
max_epochs = 60000 #最大迭代次数
learn_rate = 0.035
mse_final = 6.5e-4 #误差最小值
sample_number = x.shape[0]
input_number = 7
output_number = 2
hidden_unit_number = 8 #隐藏神经元的个数，一层8个

# 学习 训练 超参数
#8*8
w1 = 0.5 * np.random.rand(hidden_unit_number,input_number) - 0.1
#8*1
b1 = 0.5 * np.random.rand(hidden_unit_number,1) - 0.1

#2*8
w2 = 0.5 * np.random.rand(output_number,hidden_unit_number) - 0.1
#2*1
b2 = 0.5 * np.random.rand(output_number,1) - 0.1

def sigmoid(z):
    return 1.0/(1+np.exp(-z))
#print(sigmoid(0))

mse_history = []#每一迭代，会产生一个误差，将误差保存到列表中
for i in range(max_epochs):
    #FP:正向传播
    hidden_out = sigmoid(np.dot(w1,sample_in)+b1) #w1*sample_in:(8,3)*(3,20)=(8,20)+(8,1)
    network_out = np.dot(w2 ,hidden_out)+b2 #输出层输出
    #误差
    err = sample_out - network_out
    mse = np.average(np.square(err))
    mse_history.append(mse)
    if mse < mse_final:
        break
    #bp:反向传播
    delta2 = -err
    delta1 = np.dot(w2.transpose(),delta2) * hidden_out * (1 - hidden_out)
    #偏导
    delta_w2 = np.dot(delta2,hidden_out.transpose()) #transpose转置
    delta_b2 = np.dot(delta2,np.ones((sample_number,1)))

    delta_w1 = np.dot(delta1,sample_in.transpose())
    delta_b1 = np.dot(delta1,np.ones((sample_number,1)))
    #梯度下降进行跟新
    w2 -= learn_rate * delta_w2
    b2 -= learn_rate * delta_b2
    w1 -= learn_rate * delta_w1
    w1 -= learn_rate * delta_w1

# print('所有的误差',mse_history)
# 误差曲线图
mse_history10 = np.log10(mse_history)
min_mse = min(mse_history10)
plt.plot(mse_history10)
plt.plot([0, len(mse_history10)], [min_mse, min_mse])
ax = plt.gca()
ax.set_yticks([-2, -1, 0, 1, 2, min_mse])
ax.set_xlabel('iteration')
ax.set_ylabel('MSE')
ax.set_title('Log10 MSE History', fontdict={'fontsize': 18, 'color': 'red'})
plt.show()

# 仿真输出和实际输出对比图
# 隐藏层输出
hidden_out = sigmoid((np.dot(w1, sample_in) + b1))
# 输出层输出
network_out = np.dot(w2, hidden_out) + b2
# 反转获取实际值
network_out = y_scaler.inverse_transform(network_out.T)
sample_out = y_scaler.inverse_transform(y)

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 10))
line1, = axes[0].plot(network_out[:, 0], 'k', marker='o')
line2, = axes[0].plot(sample_out[:, 0], 'r', markeredgecolor='b', marker='*', markersize=9)
axes[0].legend((line1, line2), ('预测值', '实际值'), loc='upper left')
axes[0].set_title('浓度模拟', fontdict={'fontsize': 18, 'color': 'red'})
line3, = axes[1].plot(network_out[:, 1], 'k', marker='o')
line4, = axes[1].plot(sample_out[:, 1], 'r', markeredgecolor='b', marker='*', markersize=9)
axes[1].legend((line3, line4), ('预测值', '实际值'), loc='upper left')
axes[1].set_title('劲头模拟', fontdict={'fontsize': 18, 'color': 'red'})
plt.show()