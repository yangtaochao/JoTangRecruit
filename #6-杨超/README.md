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

## 构建Python程序

由于做题的时候还没学Python和request库，在网上找了个爬虫模板，了解了一下各个模块，
之后修改了一下，完成程序构建

```python
import urllib.request
import json
import time


end_page = 50
for i in range(0, end_page + 1):
    url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100019125569&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1'
    url = url.format(i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    }

    request = urllib.request.Request(url=url, headers=headers)
    content = urllib.request.urlopen(request).read().decode('gbk')
    content = content.strip('fetchJSON_comment98vv385();')
    obj = json.loads(content)
    comments = obj['comments']
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
    time.sleep(4)
    fp.close()
```

最终输出到了TXT文件



# 任务二.导入库

## 方法一. 通过导出的TXT文件导入数据库(应该不算违规吧awa)

由于做题时还没学sql与python的接口函数怎么用，~~直接偷懒用现成的~~

通过vscode批量编辑，修改输出文本使其全部变成

Insert Into语句

然后就OK了

![image.png](https://tva1.sinaimg.cn/large/008tG9v6ly1h5ya3eqa5ij31rq0q47wj.jpg)

![image.png](https://tva1.sinaimg.cn/large/008tG9v6ly1h5ya3w1x0gj31b50vtwyd.jpg)

## 方法二. 利用Python与MYsql的接口进行数据导入

## 学习sql的笔记

详细见同目录下`SQL learning.md`文件

# 任务三.