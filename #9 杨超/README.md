# 一.初识数据库

1. 下载安装包

<img src="https://tva1.sinaimg.cn/large/008tG9v6ly1h5xvhg1wldj315h0o6dr8.jpg" alt="image.png" style="zoom:50%;" />

2. 一路点下去后再配置环境变量以方便操作
   ![image.png](https://tva1.sinaimg.cn/large/008tG9v6ly1h5xvoykynzj30oa03vju9.jpg)

3. 测试语句
   <img src="https://tva1.sinaimg.cn/large/008tG9v6ly1h5xw2ysm1oj31z41211he.jpg" alt="image.png" style="zoom:50%;" />

# 二. 使用数据库

```sql
-- 1. 
create database EstateDB;
use EstateDB;
```

```sql
-- 2.
create table Owner 
(
	PersonID char(18) NOT NULL,
    Name varchar(20) NOT NULL,
    Gender char(2) NOT NULL,
    Occupation varchar(20) NOT NULL,
    Addr varchar(50) NOT NULL,
    Tel varchar(11) NOT NULL,
    PRIMARY KEY (PersonID)
);

create table Estate
(
	EstateID char(15) NOT NULL,
    EstatcName varchar(50) NOT NULL,
    EstateBuildName varchar(50) NOT NULL,
    EstateAddr varchar(60) NOT NULL,
    EstateCity varchar(60) NOT NULL,
    EstateType char(4) NOT NULL CHECK (EstateType IN ("住宅","商铺","别墅","车位") ) , 
    PropertyArea numeric(5,2) NOT NULL,
    UsableArea numeric(5,2) NOT NULL,
    CompletedDate date NOT NULL,
    YearLength int NOT NULL DEFAULT (70),
    Remark varchar(100),
    PRIMARY KEY (EstateID)
);

create table Registration
(
	RegisterID int NOT NULL,
    PersonID char(18) NOT NULL,
    EstateID char(15) NOT NULL,
    Price DOUBLE NOT NULL,
    PurchasedDate date NOT NULL,
    DeliverDate date NOT NULL,
    PRIMARY KEY (EstateID),
	FOREIGN KEY (PersonID) REFERENCES Owner(PersonID),
	FOREIGN KEY	(EstateID) REFERENCES Estate(EstateID)
);
```

第三个创建的时候说没有money这种类型，改为double

-- 3.
为了方便后面debug，根据后面的题目用Mysql workbench可视化设置了几个数据，~~主要是没找到怎么随机生成样本┭┮﹏┭┮~~

![image.png](https://tva1.sinaimg.cn/large/008tG9v6ly1h5ybx3p5nej30ze04k77o.jpg)

![image.png](https://tva1.sinaimg.cn/large/008tG9v6ly1h5ybwv9e9bj30ej056q48.jpg)

![image-20220907204805882](../../../../AppData/Roaming/Typora/typora-user-images/image-20220907204805882.png)




```sql
-- 4.
select EstateType from estate 
WHERE EstateType = "商铺"
-- 5.
select * from estate
WHERE PropertyArea > 90
AND CompletedDate > '2018-12-1'
-- 6.
select distinct Name,Tel, gender,occupation,addr from `owner`
left join registration
	on `owner`.`PersonID` = `registration`.`PersonID`
group by name
having count(name) >= 2;
-- 7. 
SELECT `owner`.`PersonID`,
    `owner`.`Name`,
    `owner`.`Gender`,
    `owner`.`Occupation`,
    `owner`.`Addr`,
    `owner`.`Tel`
FROM registration
join estate 
	on `registration`.`EstateID` = `estate`.`EstateID`
join `owner`
	on `registration`.`PersonID` = `owner`.`PersonID`
group by Name,estatecity
having count(name) >=2;
-- 8.
select estatecity,sum(PropertyArea),EstateType from estate
join registration 
	on `estate`.`estateid` = `registration`.`estateid`
WHERE `PurchasedDate` LIKE '2018%'
group by estatecity,EstateType
-- 9.
select estatecity,sum(Price),estatetype from estate
join registration 
	on `estate`.`estateid` = `registration`.`estateid`
WHERE `registration`.`PurchasedDate` LIKE '2018%'
group by estatecity,EstateType
```
/* 奇怪的现象：WHERE换成HAVING并放到最后一行会报错,最后去掉了`registration`.
就成功了，查了一下执行顺序可知WHERE与HAVING执行中间插了group的执行，所以registration的表可能在group后被“丢弃”了，再在这时用`registration`.就会找不到*/

```sql
-- 10.
create view Search AS
select `estate`.`estateid`, `estate`search.`EstatcName`, `estate`.`estatetype`, `estate`.`propertyarea`,
 `registration`.`price`, `registration`.`purchaseddate`, `estate`.`estatebuildname`, `estate`.`estatecity`
from registration 
join estate 
	on `registration`.`estateid` = `estate`.`estateid`
group by `registration`.`PersonID`
order by purchaseddate desc
-- 11.
select distinct EstateCity,count(EstateCity) as Total ,sum(price)  from registration
 join estate
	on `registration`.`estateid` = `estate`.`estateid`
WHERE `registration`.`PurchasedDate` LIKE '2018%'
group by `estate`.`EstateCity`
```

## 个人感想

sql语句老是因为蜜汁原因报错，大部分是执行顺序搞错了导致报错，但每次对着执行顺序表查真的很烦欸┭┮﹏┭┮
个人认为未来应该加强对于sql底层执行顺序的理解~

## 学习sql过程

详细见同目录下`SQL learning.md`
