# 神经网络基本概念

## 两种人工神经元

### 感知机

在神经系统中，神经元的基本功能有以下三个：
接受刺激、产生兴奋，传导兴奋。
感知机模型模拟出了这三个基本功能。

a) 输出为输入的加权求和（接受刺激）
![o = \sum_{i=1}^n x_iw_i](https://math.jianshu.com/math?formula=o%20%3D%20%5Csum_%7Bi%3D1%7D%5En%20x_iw_i)

b) 输入和输出均为0或1， 当输入的加权求和大于阈值时，输出为1，否则为0（神经元需要接受到达一定阈值的信号后才能产生兴奋）

<img src="https://upload-images.jianshu.io/upload_images/6341685-9a847144588c436e.png?imageMogr2/auto-orient/strip|imageView2/2/w/622/format/webp" alt="img" style="zoom:33%;" />

- 使用多个感知机合成一个神经网络时，可以将网络分为三层
  - 输入层
  - 隐层
  - 输出层

|   层   |          组成          |
| :----: | :--------------------: |
| 输入层 |    若干个输入神经元    |
|  隐层  | 一层或多层的中间神经元 |
| 输出层 |     一个输出神经元     |

### Sigmoid神经元

Sigmoid神经元可以输出0~1之间的任何实数结果，是一个平滑的感知机

Sigmoid函数：

![、\sigma = \frac{1}{1+e^{ -z}}](https://math.jianshu.com/math?formula=%E3%80%81%5Csigma%20%3D%20%5Cfrac%7B1%7D%7B1%2Be%5E%7B%20-z%7D%7D)


  SIgmoid神经元：

![Output = \frac{1}{1+e^{ -(\sum_{i=1}^n w_ix_i +b)}}](https://math.jianshu.com/math?formula=Output%20%3D%20%5Cfrac%7B1%7D%7B1%2Be%5E%7B%20-(%5Csum_%7Bi%3D1%7D%5En%20w_ix_i%20%2Bb)%7D%7D)

*神经元可统一表达为*

![Output =f(\sum_{i=1}^n w_ix_i +b)](https://math.jianshu.com/math?formula=Output%20%3Df(%5Csum_%7Bi%3D1%7D%5En%20w_ix_i%20%2Bb))

### 两种模型

|     模型     |                             特点                             |                             比较                             |
| :----------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
| 前馈神经网络 |        前一层的输出为后一层的输入，网络中不存在回环。        |                     目前为止，效果更强大                     |
| 递归神经网络 | 让神经元在变为止之前在一段有限的时间内激发，而非持续兴奋。 网络中存在回环（循环不会在这样的模型中引起问题，因为神经元的输出仅在稍后的某个时间影响其输入，而不是瞬间影响它的输入。） | 原理更贴近生物神经元的工作模式，可能在前馈无法解决的复杂问题上有良好的效果 |

#  人工智能

## 什么叫智能，何谓学习

### 为什么生命需要智能

为了生存

### 什么是智能

> Intelligence is The ability to adapt to change   -霍金

智能是根据变化而变化的能力

![image.png](https://tva1.sinaimg.cn/large/008tG9v6gy1h66e0egl7oj307b026mx9.jpg)

人工智能本质就是人类设计出来的智能，以适应变换的环境，人类就是人工智能的造物主

自然生命智能的进化过程：

<img src="https://tva1.sinaimg.cn/large/008tG9v6gy1h66dwwps7pj30a309w40f.jpg" alt="image.png" style="zoom:33%;" />

 

![image.png](https://tva1.sinaimg.cn/large/008tG9v6gy1h66e111or4j30bz053wf5.jpg)

**高等智能都是由低等智能迭代生成的**

### 神经网络：寻找过去事件到未来事件的关联

![image.png](https://tva1.sinaimg.cn/large/008tG9v6gy1h66edavc0zj309z029weg.jpg)

**智能的内容在于关联，核心在于学习，还包含意识**

## 人工智能

![image.png](https://tva1.sinaimg.cn/large/008tG9v6ly1h66eik0y1bj30w90hrwkw.jpg)

学习需要从有限的例子中找到合理的关联，适应变化的环境

# 人工智能概述

## 什么是机器学习

### 定义

机器学习是从**数据**中**自动分析获得模型**，并利用**模型**对未知数据进行预测。

### 数据集构成

- 结构：特征值+目标值

## 机器学习与人工智能、深度学习

![人工智能范围](https://www.freeaihub.com/ml/images/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E8%8C%83%E5%9B%B4.png)

## 机器学习算法分类

- **监督学习(supervised learning)（输入数据有标签）**
- 定义：输入数据是由输入特征值和目标值所组成。函数的输出可以是一个连续的值(称为回归），或是输出是有限个离散值（称作分类）。
- **无监督学习(unsupervised learning)**（输入数据没标签，需要机器自己探索）
- 定义：输入数据是由输入特征值所组成。
- 例子：谷歌news

聚类 k-means





- 预测器
  - 输出的结果连续不间断
- 分类器
  - 输出结果可以将其分成有限个类型

## 机器学习开发流程

- 流程图：

![开发流程](https://www.freeaihub.com/ml/images/%E5%BC%80%E5%8F%91%E6%B5%81%E7%A8%8B.png)