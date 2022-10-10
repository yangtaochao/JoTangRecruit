#请先根据以下代码先安装好对应的package哦
#ps:大致了解各个package的作用而不需要仔细学习每个package的用法
import numpy as np
import torch
from sklearn import datasets
import torch.nn as nn
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#获得神奇的iris数据集
dataset = datasets.load_iris()
#善用print功能,观察数据集的特点哦,分为它data和target两个部分,属性和种类分别是用哪些数据表示的呢?想清楚之后就可以继续往下啦!
#完善代码:寻找一个合适的函数按照二八比例划分测试集和数据集数据
input, x_test, label, y_test = train_test_split(dataset.data,dataset.target,test_size=0.2)
#完善代码:利用pytorch把数据张量化,
input = torch.FloatTensor(input)
label = torch.LongTensor(label)
x_test = torch.FloatTensor(x_test)
y_test = torch.LongTensor(y_test)

label_size = int(np.array(label.size()))

# 搭建专属于你的神经网络 它有着两个隐藏层,一个输出层
#请利用之前所学的知识,填写各层输入输出参数以及激活函数.
#两个隐藏层均使用线性模型和relu激活函数 输出层使用softmax函数(dim参数设为1)(在下一行注释中写出softmax函数的作用哦)
#####将各个输出结果映射到[0,1]之间，并且约束各个输出值之和为1，这样就表示了某种数据是各种类型的概率
class NET(nn.Module):
    def __init__(self, n_feature, n_hidden1, n_hidden2, n_output):
        super(NET, self).__init__()
        self.hidden1 = nn.Linear(n_feature,n_hidden1)
        self.relu1 = nn.functional.relu

        self.hidden2 =nn.Linear(n_hidden1,n_hidden2)
        self.relu2 = nn.functional.relu

        self.out = nn.Linear(n_hidden2,n_output)
        self.softmax = nn.functional.softmax
#前向传播函数
    def forward(self, x):
        hidden1 = self.hidden1(x)
        relu1 = self.relu1(hidden1)
#完善代码:
        hidden2 = self.hidden2(relu1)
        relu2 = self.relu2(hidden2)

        outpre = self.out(relu2)
        out = self.softmax(outpre,dim=1)

        return out
#测试函数
    def test(self, x):
        y_pred = self.forward(x)
        y_predict = self.softmax(y_pred,dim=1)

        return y_predict


# 定义网络结构以及损失函数
#完善代码:根据这个数据集的特点合理补充参数,可设置第二个隐藏层输入输出的特征数均为20
net = NET(n_feature=4, n_hidden1=20, n_hidden2=20, n_output=3)
#选一个你喜欢的优化器
#举个例子 SGD优化器 optimizer = torch.optim.SGD(net.parameters(),lr = 0.02)
#完善代码:我们替你选择了adam优化器,请补充一行代码
optimizer = torch.optim.Adam(net.parameters(),lr = 0.02)
#这是一个交叉熵损失函数,不懂它没关系(^_^)
loss_func = torch.nn.CrossEntropyLoss()
costs = []
#完善代码:请设置一个训练次数的变量(这个神经网络需要训练200次)
count = 200
# 训练网络
#完善代码:把参数补充完整
for epoch in range(count):
    cost = 0
#完善代码:利用forward和损失函数获得out(输出)和loss(损失)
    out = net(input)
    loss = loss_func(out,label)
#请在下一行注释中回答zero_grad这一行的作用
#使上一步梯度参数归零，避免影响下一步的反向传播和参数更新
    optimizer.zero_grad()
#完善代码:反向传播 并更新所有参数
    loss.backward()
    optimizer.step()
    cost = cost + loss.cpu().detach().numpy()
    costs.append(cost / label_size)
#可视化

plt.plot(costs)
plt.show()

# 测试训练集准确率
out = net.test(input)
prediction = torch.max(out, 1)[1]
pred_y = prediction.numpy()
target_y = label.numpy()
accuracy = float((pred_y == target_y).astype(int).sum()) / float(target_y.size)
print("训练集准确率为", accuracy * 100, "%")

# 测试测试集准确率
out1 = net.test(x_test)
prediction1 = torch.max(out1, 1)[1]
pred_y1 = prediction1.numpy()
target_y1 = y_test.numpy()

accuracy1 = float((pred_y1 == target_y1).astype(int).sum()) / float(target_y1.size)
print("测试集准确率为", accuracy1 * 100, "%")


#至此,你已经拥有了一个简易的神经网络,运行一下试试看吧
#最后,回答几个简单的问题,本次的问题属于监督学习还是无监督学习呢?batch size又是多大呢?像本题这样的batch size是否适用于大数据集呢,原因是?
###监督学习，Batch_Size=m 训练样本数量，不适用，因为一次抓取所有数据用于训练会导致GPU或CPU算力不够