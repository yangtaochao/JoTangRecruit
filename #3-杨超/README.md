# 任务1：安装wsl2

1. 启用虚拟机和Linux功能

2. 安装WSL2 Linux内核更新包

   <img src="https://tva1.sinaimg.cn/large/008tG9v6ly1h5rbt530wgj30li0gpwi6.jpg" style="zoom: 67%;" />

   3. 设置WSL默认版本为2
      ![image.png](https://tva1.sinaimg.cn/large/008tG9v6ly1h5rbvqmr4ej30m307jdk4.jpg)
   4. 安装 Ubuntu LTS
      <img src="https://tva1.sinaimg.cn/large/008tG9v6ly1h5rbx1dr1nj316s0zik3h.jpg" alt="image.png" style="zoom: 33%;" />
   5. 初始化，设置
   6. ![image.png](https://tva1.sinaimg.cn/large/008tG9v6ly1h5rc5q4ygjj30to04zdgr.jpg)
      - \\wsl$ 查看Ubuntu文件

# 加分项

## 通过VScode的WSL remote插件连接至你的WSL2

1. ssh安装插件
   ![image.png](https://tva1.sinaimg.cn/large/008tG9v6ly1h5wu2klpl4j315j0r1aqk.jpg)

2. Ubuntu安装ssh服务端并启动ssh服务

   ```
   sudo apt install openssh-server
   sudo service ssh start
   ```

3. 直接在WSL2中输入code自动与VS code进行连接

![image.png](https://tva1.sinaimg.cn/large/008tG9v6ly1h5wu4ggbrnj31z10sakf7.jpg)
