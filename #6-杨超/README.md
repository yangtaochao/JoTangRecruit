# 任务一

## 找到评论url

因为是动态网页，所以直接开始抓包。

为了方便，~~直接去CSDN搜索评论的JS是哪个，应该可以吧awa~~

![image.png](https://tva1.sinaimg.cn/large/008tG9v6ly1h5y6jx15wvj30qd00uaaa.jpg)

最后发现这个文件是评论url

然后看到page=每增加一页就加1

然后评论是content 

时间是 creationtime

名字是 nickname

## 分析json格式

![image.png](https://tva1.sinaimg.cn/large/008tG9v6ly1h69wttm5r2j31yy04bqkt.jpg)

![image.png](https://tva1.sinaimg.cn/large/008tG9v6ly1h69wv350b2j30ec01adgt.jpg)

直接获取json中的comment中的content,nickname,creationTime即可

## 构建Python程序

```python
import urllib.request
import json
import time

#网址和页码处理
#添加headers请求头
end_page = 50
for i in range(0, end_page + 1):
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100019125569&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1'
    url = url.format(i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    }
#发送请求
    request = urllib.request.Request(url=url, headers=headers)
#接收响应,并编码
    content = urllib.request.urlopen(request).read().decode('gbk')
#移除指定字符
    content = content.strip('fetchJSON_comment98vv385();')
#获取响应内容搞的json内容
    obj = json.loads(content)
#获取json中comments项内容
    comments = obj['comments']
#写入txt文件
    fp = open('JoTangTask.txt', 'a', encoding='utf8')
    for comment in comments:
        # 评论时间
        creationTime = comment['creationTime']
        # 评论人
        nickname = comment['nickname']
        # 评论内容
        contents = comment['content']
        item = {
            '评论时间': creationTime,
            '用户名称': nickname,
            '评论内容': contents,
        }
        string = str(item)
        fp.write(string + '\n')
        
#休眠时间
    time.sleep(4)
    fp.close()
```

最终输出到了TXT文件



# 任务二.导入库

## 方法一. 通过导出的TXT文件导入数据库(应该不算违规吧awa)

~~由于做题时还没学sql与python的接口函数怎么用，直接偷懒用现成的~~

通过vscode批量编辑，修改输出文本使其全部变成

Insert Into语句

然后就OK了

![image.png](https://tva1.sinaimg.cn/large/008tG9v6ly1h5ya3eqa5ij31rq0q47wj.jpg)

![image.png](https://tva1.sinaimg.cn/large/008tG9v6ly1h5ya3w1x0gj31b50vtwyd.jpg)

## 方法二. 利用Python与MYsql的接口进行数据导入

将文件处理部分换成数据库接口

- 安装cryptography
  - $ pip install cryptography

```python 
import urllib.request
import json
import time
import pymysql
import datetime
#接入数据库
db = pymysql.connect(host='localhost',
                         user='root',
                         password='密码',
                         database='jotangtask2')
cursor = db.cursor()
#网址和页码处理
#添加headers请求头
end_page = 50
for i in range(0, end_page + 1):
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100019125569&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1'
    url = url.format(i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    }
#发送请求
    request = urllib.request.Request(url=url, headers=headers)
#接收响应,并编码
    content = urllib.request.urlopen(request).read().decode('gbk')
#移除指定字符
    content = content.strip('fetchJSON_comment98vv385();')
#获取响应内容的json内容
    obj = json.loads(content)
#获取json中comments项内容
    comments = obj['comments']
    #插入数据
    for comment in comments:
        # 评论时间
        creationTime = comment['creationTime']
        creationTime = datetime.datetime.strptime(creationTime, '%Y-%m-%d %H:%M:%S') #转化字符串为时间格式
        # 评论人
        nickname = comment['nickname']
        # 评论内容
        contents = comment['content']
        sql = """INSERT INTO `jotangtask2`.`jd` (`jd`.`Time`,`jd`.`User`,`jd`.`ConTent`)
         VALUES ('{creationTime}', '{nickname}', '{contents}')""".format(creationTime=creationTime, nickname=nickname, contents=contents)
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        # 休眠时间
        time.sleep(4)
db.close()
```

## 学习sql的笔记

详细见同目录下`SQL learning.md`文件

# 任务三.

详细见同目录下`WEB.md`