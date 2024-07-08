from sklearn.datasets import load_boston
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
import numpy as np
from openpyxl import load_workbook #加载表格数据
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader #对数据进行批量加载
housing_boston = load_boston
x = housing_boston.data
y = housing_boston.target.reshape(-1,1)
def sigmoid(x): #激活函数
    return np.tanh(x)

def dsigmoid(x): #求激活函数的导数
    return 1.0-np.multiply(x,x)

def standrd(data): #数据进行标准化，归一化处理
    mean = data.mean(axis = 1)
    mean = mean.reshape(-1,1)
    std = data.std(axis=1)
    std = std.reshape(-1,1)
    data = (data-mean)/std
    return data
data = np.hstack((x,y)) #将特征与标签拼在一起，形成一个矩阵，x:特征  y:标签
data = standrd(data) #进行标准化处理
train_data = data[:400] #train_data由特征和标签组成，400为训练样本数
test_data = data[400:]#test_data由特征和标签组成，剩下的为测试样本数
keep_prob = 0.8 #

class NN():
    def __init__(self,layers,data):
        """
        :param layers: 从输入层到输出层各层神经元个数的列表
        :param data:
        """
        L = len(layers) #L:表示有多少层，包含输入层，隐藏层，输出层
        #先定义了两个字典，一个放权重值，一个放偏置值
        self.w = {}
        self.b = {}
        for l in range(1,L):
            self.w["w"+str(l)] = np.mat(np.random.randn(layers[1],layers[l-1]*0.1))#赋值给权值的初值
            self.b["b"+str(l)] = np.mat(np.random.randn(layers[1],1)*0.1)
        self.A = {} #这个字典里存储了输入，和后面各个层的激活值；输出层的激活值在这个字典的最后一个
        self.Z = {}# 这个字典里存储了从第二层到输出层没被激活的值
        self.cache = {} #这个字典里存储了[]()
        #将数据写入类中
        self.data = data

    def forward_activation_02(self,L,flag):#这个L和上面的L是一样的，包含了总层数
        """
        前向传播函数
        :param L: 神经网络的层数
        :param flag: flag为标记，是否启用dropout正则化，flag = 1启用dropout正则化，
        如果熟悉dropout正则化，可以令flag = 0,关闭它。
        :return: 返回大致误差
        """
        #初始化输入
        self.A["A0"] = self.inputs
        for l in range(1,L):
            if flag == 0 or l == 1 or l == L-1:
                self.Z["Z"+str(l)] = self.w["w"+str(l)]*self.A["A"+str(l-1)]+self.b["b"+str(l)]
                self.A["A"+str(l)] = sigmoid(self.Z["Z"+str(l)])