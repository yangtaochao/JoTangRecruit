# 机器学习方法

1. 监督式学习（有标签）
2. 非监督式学习（无标签）
3. 半监督学习
4. 强化学习
5. 遗传算法（适者生存）

# 神经网络（Neural Network）

## 神经网络

- 卷积 和 神经网络
  - 我们先把卷积神经网络这个词拆开来看. “卷积” 和 “神经网络”. 卷积也就是说神经网络不再是对每个像素的输入信息做处理了,而是图片上每一小块像素区域进行处理, 这种做法加强了图片信息的连续性. 使得神经网络能看到图形, 而非一个点. 
  - 图片具有高度，即为RGB颜色信息，卷积的过程就是把图片的高度加高，长宽变小，这样，特征相似的一类图片区域就被集中在一个地方，从而使得计算机分类并“理解”图片
- 池化(pooling)
  - 池化是筛选过滤的过程，负责压缩的工作，提高了准确性
- 流行的 CNN 结构

# Pytorch 简介

## 神经网络 梯度下降

### Optimization(优化问题)

优化能力是人类历史上的重大突破, 他解决了很多实际生活中的问题.

### 梯度下降

误差方程 (Cost Function). 用来计算预测出来的和我们实际中的值有多大差别. 在预测数值的问题中, 我们常用平方差 (Mean Squared Error) 来代替. 

二维的情况：
![image.png](https://tva1.sinaimg.cn/large/008tG9v6ly1h66m4z3c8hj30ro0e8dvg.jpg)

根据点的导数指引点走向导数为0的地方。

### 全局 and 局部最优

全局最优固然最好，但是有时局部最优就足够用来完成任务.

## **神经网络的黑盒不黑**

### 神经网络分区

输入层，隐层，输出层

神经网络将输入端处理后形成代表特征，再次加工又形成新的代表特征，

### 迁移学习

吧现有神经网络的输出层拆掉，套上另外一个神经网络，用这种移植的方式进行训练

## WHY PyTorch

### 神经网络在做什么

1. 学习拟合线条（回归）
2. 学习区分数据（分类）

### PyTorch 安装

```

conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/menpo/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/peterjc123/
conda config --set show_channel_urls yes

conda install pytorch torchvision torchaudio cudatoolkit=11.6
```

利用清华镜像源安装pytorch

然后添加conda配置的解释器

![image.png](https://tva1.sinaimg.cn/large/008tG9v6ly1h67dw7bdm3j31500tpk0w.jpg)

# PyTorch 神经网络基础

## Torch 或 Numpy

## **变量 (Variable)**

### 什么是Variable

在 Torch 中的 Variable 就是一个存放会变化的值的地理位置. 里面的值会不停的变化. 就像一个裝鸡蛋的篮子, 鸡蛋数会不停变动. 那谁是里面的鸡蛋呢, 自然就是 Torch 的 Tensor 咯. 如果用一个 Variable 进行计算, 那返回的也是一个同类型的 Variable.

### Variable计算，梯度

**Variable 计算时, 它在背景幕布后面一步步默默地搭建着一个庞大的系统, 叫做计算图, computational graph. 其将所有的计算步骤 (节点) 都连接起来, 最后进行误差反向传递的时候, 一次性将所有 variable 里面的修改幅度 (梯度) 都计算出来, 而 tensor 就没有这个能力**

```python
import torch
from torch.autograd import Variable

函数名.data  将Variable形式转化为tensor形式
```

## 什么是激励函数(Activation Function)

### 非线性方程

y=wx

### 激励函数

将原来的线性方程函数套进一个非线性函数里面,比如y=tanh(WX)

 ![image.png](https://tva1.sinaimg.cn/large/008tG9v6ly1h69vmso2rcj30pc0e6k0t.jpg)

## 激励函数

### Torch 激励函数

`relu`, `sigmoid`, `tanh`, `softplus`

# 建造第一个神经网络

## 关系拟合

### 建立数据集

```python
import torch
import matplotlib.pyplot as plt

x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)  # x data     (tensor), shape=(100, 1)
y = x.pow(2) + 0.2*torch.rand(x.size())                 # noisy y data (tensor), shape=(100, 1)

.unsqueeze将一维数据转化为二维,相当于[]变成了[[]]
```

### 搭建神经网络

搭建输入层,隐藏层,输出层

```python
import torch
import torch.nn.functional as F     # 激励函数都在这

class Net(torch.nn.Module):  # 继承 torch 的 Module
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()     # 继承 __init__ 功能
        # 定义每层用什么样的形式
        self.hidden = torch.nn.Linear(n_feature, n_hidden)   # 隐藏层线性输出
        self.predict = torch.nn.Linear(n_hidden, n_output)   # 输出层线性输出

    def forward(self, x):   # 这同时也是 Module 中的 forward 功能
        # 正向传播输入值, 神经网络分析出输出值
        x = F.relu(self.hidden(x))      # 激励函数(隐藏层的线性值)
        x = self.predict(x)             # 输出值
        return x

net = Net(n_feature=1, n_hidden=10, n_output=1)

print(net)  # net 的结构
```

### 训练网络

```python
# optimizer 是训练的工具
optimizer = torch.optim.SGD(net.parameters(), lr=0.2)  # 传入 net 的所有参数, 学习率
loss_func = torch.nn.MSELoss()      # 预测值和真实值的误差计算公式 (均方差)
#这是预测器用均方差模块
for t in range(100):
    prediction = net(x)     # 喂给 net 训练数据 x, 输出预测值

    loss = loss_func(prediction, y)     # 计算两者的误差 Predicition在前,y在后

    optimizer.zero_grad()   # 清空上一步的残余更新参数值
    loss.backward()         # 误差反向传播, 计算参数更新值
    optimizer.step()        # 将参数更新值施加到 net 的 parameters 上
```

## 分类

```Python
    
```



