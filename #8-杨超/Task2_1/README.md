# 一.

## Train.py

1. 缺少cuda驱动

> https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=11&target_type=exe_local

2. ```python
   keras.emotion_models 模型不存在
   改成from tensorflow import keras
   然后Sequential()改成keras.Sequential()
   ```

3. ```python
   ValueError: ('Invalid color mode:', 'gray_framescale', '; expected "rgb", "rgba", or "grayscale".')
   吧gray_framescale 改成grayscale
   ```

   改完OK,看样子要做50轮训练,要等挺久的.说是炼丹不为过

![image.png](https://tva1.sinaimg.cn/large/008tG9v6ly1h6lea8dvpbj31b105lwip.jpg)

4. ```Python
   Could not load dynamic library 'cudnn64_8.dll'; dlerror: cudnn64_8.dll not found
   ```

   到dll网站下了个cudnn64_8.dll装到cuda里面,之后出现了这种情况:

5. ![image.png](https://tva1.sinaimg.cn/large/008tG9v6ly1h6lf2q8qubj31is051tf6.jpg)

突然又不跑了

查了一下4方法错误,直接下dll有问题

那么我们直接去到TensorFlow官网看GPU支持事项,提示我们安装cuDNN

![image.png](https://tva1.sinaimg.cn/large/008tG9v6gy1h6lfrk2mp2j30wz0e27bn.jpg)

将下载好的压缩包解压到C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.7下面

然后看到cudnn的安装手册中还要安装一个Zlib

![image.png](https://tva1.sinaimg.cn/large/008tG9v6gy1h6lft2m3toj31fv08v0vq.jpg)

解压之后按照说明文件把zlibwapi.dll装到\CUDA\v11.7\bin下面

GPU加速配置成功!,速度翻倍

![image.png](https://tva1.sinaimg.cn/large/008tG9v6ly1h6lga54e9bj31ek03mtcr.jpg)

6. 提示没找到函数.

   网上找到办法:向解释器中添加cv2的目录

7. AttributeError: module 'cv2' has no attribute 'COLOR_BGR2gray_frame'
   把COLOR_BGR2gray_frame 换成COLOR_BGR2GRAY
8. Impl::open Can't open file: '/home/shivam/.local/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml' in read mode
   Traceback (most recent call last):
   路径更换为适合的路径
   haarcascade_frontalface_default.xml

## gui.py

1. 

```python
emoji_dist={0:"./emojis/angry.png",2:"./emojis/disgusted.png",2:"./emojis/fearful.png",3:"./emojis/happy.png",4:"./emojis/neutral.png",5:"./emojis/sad.png",6:"./emojis/surpriced.png"}
有两个2,修改第一个2为1
```

2. pic2没用到![image.png](https://tva1.sinaimg.cn/large/008tG9v6ly1h6mjlccdm0j30jv06bjtz.jpg)
3. 去掉lmain2.after(10, show_vid2)    lmain.after(10, show_vid)修改代码,让摄像头识别到人脸再弹窗
   ![image.png](https://tva1.sinaimg.cn/large/008tG9v6gy1h6ndfedr0yj30d002h3yp.jpg)

## 二.

见./emoji-creator-project-code/train.py

# 三.

![image.png](https://tva1.sinaimg.cn/large/008tG9v6gy1h6nay280sxj31mf12uk9l.jpg)

![image.png](https://tva1.sinaimg.cn/large/008tG9v6gy1h6nazprskvj31lr0zy1ae.jpg)

![image.png](https://tva1.sinaimg.cn/large/008tG9v6gy1h6nb4yj6dqj316p0qgwos.jpg)

![image.png](https://tva1.sinaimg.cn/large/008tG9v6gy1h6nb74vbnmj31mf12unhg.jpg)

![image.png](https://tva1.sinaimg.cn/large/008tG9v6gy1h6nbavfmqoj31mf12uh5q.jpg)

# 四. 

1. 将训练集逐步加载,分批训练
2. 设计卷积神经网络,设置训练模型参数
3. 训练完测试,然后保存数据
