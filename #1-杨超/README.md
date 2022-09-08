# 任务1

直接根据招新提示

用GitHub桌面程序创建仓库awa

<img src="https://tva1.sinaimg.cn/large/008tG9v6gy1h5wsvb8c2vj30zu0h4tbk.jpg" alt="image.png" style="zoom:50%;" />

# 任务2

见后面文件~

# 任务3

*之前在暑假的时候弄好了一个博客，~~这能算是押中题吗qwq~~，*

*所以可能没有太多过程截图捏┭┮﹏┭┮*
~~善良的学长不会要我再搭建一遍的对叭awa~~

> https://zhuanlan.zhihu.com/p/102592286 参考教程
>
> https://yangtaochao.github.io/ 博客链接
> https://github.com/yangtaochao/yangtaochao.github.io 网站源码

### 配置过程

1. 安装git和node.js,创建GitHub仓库

2. 通过SSH将本地仓库链接到远程仓库，
   大致了解了GitHub的强大功能

   1. 复制公钥 id_rsa.pub 文件里的内容
   2. 将复制的公钥 id_rsa.pub 的内容粘贴到 key 内，再点击 Add SSH key
   3. ssh -T [git@github.com](mailto:git@github.com)  进行校验
   4. git init 
   5.  git remote add origin https://github.com/yangtaochao/yangtaochao.github.io.git
   6. git push origin main 同步仓库

3. 安装hexo和next主题

   ```
   npm install hexo-deployer-git --save
   git clone https://github.com/theme-next/hexo-theme-next themes/next
   ```

   

4. 利用hexo下的next主题进行傻瓜式配置
   虽然还没学JS，CSS,style等等网站文件的语言，但通过漫长的调试过程(一直在调_config.yml，一直hexo g && hexo s)
   了解了网站的组成结构，以及调试bug的技巧（控制单一变量awa）
   为了让自己网站看起来~~高端~~一点，学着装载了**来必力评论系统和一些精美的动态效果**
   ![image.png](https://tva1.sinaimg.cn/large/008tG9v6ly1h5z1l3d4i8j31ps0xraz6.jpg)

5. 上传到GitHub
   最近到学校后用hexo deploy上传一直超时┭┮﹏┭┮
   结果发现是上传用的端口没走代理,而校园网裸连又上不去GitHub（感谢学长的帮助(#>д<)）
   最后把git的端口换到clash的就解决了！
   代码如下

   ```
   git config --global https.proxy http://127.0.0.1:7890
   ```

   
