# select查询语句

```sql
Select查询语法
SELECT column, another_column, …
FROM mytable
WHERE condition(s)
ORDER BY column ASC/DESC
LIMIT num_limit OFFSET num_offset;
```

**一定要注意各个关键字之间的顺序，不能颠倒**

## SQL操作符汇总

| Operator（操作符） | Condition（解释）                                            | Example（例子）                                              |
| ------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| =                  | Case sensitive exact string comparison (*notice the single equals*)完全等于 | col_name = "abc"                                             |
| != or <>           | Case sensitive exact string inequality comparison 不等于     | col_name != "abcd"                                           |
| LIKE               | Case insensitive exact string comparison 没有用通配符等价于 = | col_name LIKE "ABC"                                          |
| NOT LIKE           | Case insensitive exact string inequality comparison 没有用通配符等价于 != | col_name NOT LIKE "ABCD"                                     |
| %                  | Used anywhere in a string to match a sequence of zero or more characters (only with LIKE or NOT LIKE) 通配符，代表匹配0个以上的字符 | col_name LIKE "%AT%" (matches "AT", "ATTIC", "CAT" or even "BATS") "%AT%" 代表AT 前后可以有任意字符 |
| _                  | Used anywhere in a string to match a single character (only with LIKE or NOT LIKE) 和% 相似，代表1个字符 | col_name LIKE "AN_" (matches "AND", but not "AN")            |
| IN (…)             | String exists in a list 在列表                               | col_name IN ("A", "B", "C")                                  |
| NOT IN (…)         | String does not exist in a list 不在列表                     | col_name NOT IN ("D", "E", "F")                              |

## 多表联合查询

1. 连接：join ;left join;right join;full join.
1. union 联合

```sql
用INNER JOIN 连接表的语法
SELECT column, another_table_column, …
FROM mytable （主表）
INNER JOIN another_table （要连接的表）
    ON mytable.id = another_table.id (想象一下刚才讲的主键连接，两个相同的连成1条)
WHERE condition(s)
ORDER BY column, … ASC/DESC
LIMIT num_limit OFFSET num_offset;

SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;
//UNION 操作符用于合并两个或多个 SELECT 语句的结果集
UNION 内部的每个 SELECT 语句必须拥有相同数量的列。列也必须拥有相似的数据类型。
union & union all 
不重复    重复
```

## 特殊关键字NULL

```sql
在查询条件中处理 NULL
SELECT column, another_column, …
FROM mytable
WHERE column IS/IS NOT NULL
AND/OR another_condition
AND/OR …;
```

## 查询中使用表达式并记作另外的量

```sql
表达式 AS 名称
```

## 统计函数

```sql
对全部结果数据做统计
SELECT AGG_FUNC(column_or_expression) AS aggregate_description, …
FROM mytable
WHERE constraint_expression;
```

## 对分组完的数据再筛选出几条

```sql
用HAVING进行筛选
SELECT group_by_column, AGG_FUNC(column_expression) AS aggregate_result_alias, …
FROM mytable
WHERE condition
GROUP BY column
HAVING group_condition;
```

`HAVING` 和 `WHERE` 语法一样，只不过作用的结果集不一样. 在我们例子数据表数据量小的情况下可能感觉 `HAVING`没有什么用，但当你的数据量成千上万属性又很多时也许能帮上大忙

## 总结查询语句

```sql
这才是完整的SELECT查询
SELECT DISTINCT column, AGG_FUNC(column_or_expression), …
FROM mytable
    JOIN another_table
      ON mytable.column = another_table.column
    WHERE constraint_expression
    GROUP BY column
    HAVING constraint_expression
    ORDER BY column ASC/DESC
    LIMIT count OFFSET COUNT;
```

一个查询SQL的执行总是先从数据里按条件选出数据，然后对这些数据再次做一些整理处理，按要求返回成结果，让结果尽可能是简单直接的。因为一个 查询SQL由很多部分组成，所以搞清楚这些部分的执行顺序还挺重要的，这有助于我们更深刻的理解SQL执行过程.

## 查询执行顺序

## 1. `FROM` 和 `JOIN`s

`FROM` 或 `JOIN`会第一个执行，确定一个整体的数据范围. 如果要JOIN不同表，可能会生成一个临时Table来用于 下面的过程。总之第一步可以简单理解为确定一个数据源表（含临时表)

2. ## `WHERE`

我们确定了数据来源 `WHERE` 语句就将在这个数据源中按要求进行数据筛选，并丢弃不符合要求的数据行，所有的筛选col属性 只能来自`FROM`圈定的表. AS别名还不能在这个阶段使用，因为可能别名是一个还没执行的表达式

## 3. `GROUP BY`

如果你用了 `GROUP BY` 分组，那`GROUP BY` 将对之前的数据进行分组，统计等，并将是结果集缩小为分组数.这意味着 其他的数据在分组后丢弃.

## 4. `HAVING`

如果你用了 `GROUP BY` 分组, `HAVING` 会在分组完成后对结果集再次筛选。AS别名也不能在这个阶段使用.

## 5. `SELECT`

确定结果之后，`SELECT`用来对结果col简单筛选或计算，决定输出什么数据.

## 6. `DISTINCT`

如果数据行有重复`DISTINCT` 将负责排重.

## 7. `ORDER BY`

在结果集确定的情况下，`ORDER BY` 对结果做排序。因为`SELECT`中的表达式已经执行完了。此时可以用AS别名.

## 8. `LIMIT` / `OFFSET`

最后 `LIMIT` 和 `OFFSET` 从排序的结果中截取部分数据.

## 查询语句总结

不是每一个SQL语句都要用到所有的句法，但灵活运用以上的句法组合和深刻理解SQL执行原理将能在SQL层面更好的解决数据问题，而不用把问题 都抛给程序逻辑.

## 个人探索&思考

想到select是输出一个表格
而from和join 则是输入一个表格,倘若我select输出的表格又输入给from,join
那是不是可以实现select语句的嵌套捏awa

个人认为select语句嵌套应当用于需要对数据多次复杂处理的情况下，需要用select来输出一个中间过程的处理结果，从而使过程清晰，明了。

实验环节：这部分由于时间关系没法实验了啦┭┮﹏┭┮

# 对表进行修改操作的语句

## insert update delete 


```sql
INSERT INTO table_name (column1,column2,column3,...)
VALUES (value1,value2,value3,...);

UPDATE table_name
SET column1=value1,column2=value2,...
WHERE some_column=some_value;

DELETE FROM table_name
WHERE some_column=some_value;
#添加列
ALTER TABLE table_name
ADD column_name datatype
#改变表中数据类型
ALTER TABLE table_name
MODIFY COLUMN column_name datatype
```

## insert into  ... select

从一个表复制数据，然后把数据插入到另一个新表中。

```sql
INSERT INTO table2
(column_name(s))
SELECT column_name(s)
FROM table1;
```

# 对数据库进行操作的语句

```sql
CREATE DATABASE dbname;

CREATE TABLE table_name
(
column_name1 data_type(size),
column_name2 data_type(size),
column_name3 data_type(size),
....
);
DROP TABLE table_name
DROP DATABASE database_name
TRUNCATE TABLE table_name 只删除表内数据
```

# Mysql数据类型

## text类型

| 数据类型         | 描述                                                         |
| :--------------- | :----------------------------------------------------------- |
| CHAR(size)       | 保存固定长度的字符串（可包含字母、数字以及特殊字符）。在括号中指定字符串的长度。最多 255 个字符。 |
| VARCHAR(size)    | 保存可变长度的字符串（可包含字母、数字以及特殊字符）。在括号中指定字符串的最大长度。最多 255 个字符。**注释：**如果值的长度大于 255，则被转换为 TEXT 类型。 |
| TINYTEXT         | 存放最大长度为 255 个字符的字符串。                          |
| TEXT             | 存放最大长度为 65,535 个字符的字符串。                       |
| BLOB             | 用于 BLOBs（Binary Large OBjects）。存放最多 65,535 字节的数据。 |
| MEDIUMTEXT       | 存放最大长度为 16,777,215 个字符的字符串。                   |
| MEDIUMBLOB       | 用于 BLOBs（Binary Large OBjects）。存放最多 16,777,215 字节的数据。 |
| LONGTEXT         | 存放最大长度为 4,294,967,295 个字符的字符串。                |
| LONGBLOB         | 用于 BLOBs (Binary Large OBjects)。存放最多 4,294,967,295 字节的数据。 |
| ENUM(x,y,z,etc.) | 允许您输入可能值的列表。可以在 ENUM 列表中列出最大 65535 个值。如果列表中不存在插入的值，则插入空值。**注释：**这些值是按照您输入的顺序排序的。可以按照此格式输入可能的值： ENUM('X','Y','Z') |
| SET              | 与 ENUM 类似，不同的是，SET 最多只能包含 64 个列表项且 SET 可存储一个以上的选择。 |

## **Number 类型：**

| 数据类型        | 描述                                                         |
| :-------------- | :----------------------------------------------------------- |
| TINYINT(size)   | 带符号-128到127 ，无符号0到255。                             |
| SMALLINT(size)  | 带符号范围-32768到32767，无符号0到65535, size 默认为 6。     |
| MEDIUMINT(size) | 带符号范围-8388608到8388607，无符号的范围是0到16777215。 size 默认为9 |
| INT(size)       | 带符号范围-2147483648到2147483647，无符号的范围是0到4294967295。 size 默认为 11 |
| BIGINT(size)    | 带符号的范围是-9223372036854775808到9223372036854775807，无符号的范围是0到18446744073709551615。size 默认为 20 |
| FLOAT(size,d)   | 带有浮动小数点的小数字。在 size 参数中规定显示最大位数。在 d 参数中规定小数点右侧的最大位数。 |
| DOUBLE(size,d)  | 带有浮动小数点的大数字。在 size 参数中规显示定最大位数。在 d 参数中规定小数点右侧的最大位数。 |
| DECIMAL(size,d) | 作为字符串存储的 DOUBLE 类型，允许固定的小数点。在 size 参数中规定显示最大位数。在 d 参数中规定小数点右侧的最大位数。 |

*以上的 size 代表的并不是存储在数据库中的具体的长度，如 int(4) 并不是只能存储4个长度的数字。*

*实际上int(size)所占多少存储空间并无任何关系。int(3)、int(4)、int(8) 在磁盘上都是占用 4 btyes 的存储空间。就是在显示给用户的方式有点不同外，int(M) 跟 int 数据类型是相同的。*

## **Date 类型：**

| 数据类型    | 描述                                                         |
| :---------- | :----------------------------------------------------------- |
| DATE()      | 日期。格式：YYYY-MM-DD**注释：**支持的范围是从 '1000-01-01' 到 '9999-12-31' |
| DATETIME()  | *日期和时间的组合。格式：YYYY-MM-DD HH:MM:SS**注释：**支持的范围是从 '1000-01-01 00:00:00' 到 '9999-12-31 23:59:59' |
| TIMESTAMP() | *时间戳。TIMESTAMP 值使用 Unix 纪元('1970-01-01 00:00:00' UTC) 至今的秒数来存储。格式：YYYY-MM-DD HH:MM:SS**注释：**支持的范围是从 '1970-01-01 00:00:01' UTC 到 '2038-01-09 03:14:07' UTC |
| TIME()      | 时间。格式：HH:MM:SS**注释：**支持的范围是从 '-838:59:59' 到 '838:59:59' |
| YEAR()      | 2 位或 4 位格式的年。**注释：**4 位格式所允许的值：1901 到 2155。2 位格式所允许的值：70 到 69，表示从 1970 到 2069。 |

*即便 DATETIME 和 TIMESTAMP 返回相同的格式，它们的工作方式很不同。在 INSERT 或 UPDATE 查询中，TIMESTAMP 自动把自身设置为当前的日期和时间。TIMESTAMP 也接受不同的格式，比如 YYYYMMDDHHMMSS、YYMMDDHHMMSS、YYYYMMDD 或 YYMMDD。*

# 约束

SQL 约束用于规定表中的数据规则。

如果存在违反约束的数据行为，行为会被约束终止。

约束可以在创建表时规定（通过 CREATE TABLE 语句），或者在表创建之后规定（通过 ALTER TABLE 语句）。

```sql
CREATE TABLE table_name
(
column_name1 data_type(size) constraint_name auto-increment,
column_name2 data_type(size) constraint_name,
column_name3 data_type(size) constraint_name,
PRIMARY KEY (column_name)
FOREIGN KEY (P_Id) REFERENCES Persons(P_Id)
CHECK (条件)
    CONSTRAINT 别名 CHECK (条件&条件) 可以对多个列约束
);
constraint_name： 
NOT NULL  & UNIQUE & DEFAULT（插入默认值）
```

FOREIGN KEY 约束用于预防破坏表之间连接的行为。

FOREIGN KEY 约束也能防止非法数据插入外键列，因为它必须是它指向的那个表中的值之一。

# 添加索引

```sql
CREATE (unique) INDEX index_name
ON table_name (column_name)
```

# AUTO_INCREMENT

![image.png](https://tva1.sinaimg.cn/large/008tG9v6ly1h5xqcwee3nj31030i6alp.jpg)

# 创建视图

![image.png](https://tva1.sinaimg.cn/large/008tG9v6ly1h5xqf74tmgj30sn0ag101.jpg)

更新视图只需再创建一遍同名的视图即可

# date 函数

| 函数                                                         | 描述                                |
| :----------------------------------------------------------- | :---------------------------------- |
| [NOW()](https://www.runoob.com/sql/func-now.html)            | 返回当前的日期和时间                |
| [CURDATE()](https://www.runoob.com/sql/func-curdate.html)    | 返回当前的日期                      |
| [CURTIME()](https://www.runoob.com/sql/func-curtime.html)    | 返回当前的时间                      |
| [DATE()](https://www.runoob.com/sql/func-date.html)          | 提取日期或日期/时间表达式的日期部分 |
| [EXTRACT()](https://www.runoob.com/sql/func-extract.html)    | 返回日期/时间的单独部分             |
| [DATE_ADD()](https://www.runoob.com/sql/func-date-add.html)  | 向日期添加指定的时间间隔            |
| [DATE_SUB()](https://www.runoob.com/sql/func-date-sub.html)  | 从日期减去指定的时间间隔            |
| [DATEDIFF()](https://www.runoob.com/sql/func-datediff-mysql.html) | 返回两个日期之间的天数              |
| [DATE_FORMAT()](https://www.runoob.com/sql/func-date-format.html) | 用不同的格式显示日期/时间           |

如果希望使查询简单且更易维护，那么请不要在日期中使用时间部分！

# SQL Aggregate 函数

SQL Aggregate 函数计算从列中取得的值，返回一个单一的值。

有用的 Aggregate 函数：

- AVG() - 返回平均值
- COUNT() - 返回行数
- FIRST() - 返回第一个记录的值
- LAST() - 返回最后一个记录的值
- MAX() - 返回最大值
- MIN() - 返回最小值
- SUM() - 返回总和

------

# SQL Scalar 函数

SQL Scalar 函数基于输入值，返回一个单一的值。

有用的 Scalar 函数：

- UCASE() - 将某个字段转换为大写
- LCASE() - 将某个字段转换为小写
- MID() - 从某个文本字段提取字符，MySql 中使用
- SubString(字段，1，end) - 从某个文本字段提取字符
- LEN() - 返回某个文本字段的长度
- ROUND() - 对某个数值字段进行指定小数位数的四舍五入
- NOW() - 返回当前的系统日期和时间
- FORMAT() - 格式化某个字段的显示方式

# 正则表达式匹配

 REGEXP 操作符来进行正则表达式匹配

```sql
WHERE name REGEXP '^[aeiou]|ok$';
```

