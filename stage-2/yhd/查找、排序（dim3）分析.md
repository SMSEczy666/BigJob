# 查找、排序（dim3）分析

## 1. 提交次数

结果阶段一的处理后，dim3有5796份样本，提交次数为1次的有4633份，提交次数为2次的有545份。

![](https://yhd123.oss-cn-hangzhou.aliyuncs.com/img/提交次数分布.png)


## 2. debug时间

注：最后一次提交时间-第一次提交时间，如果最后一次提交之前获得满分，则将首次获得满分的时间作为被减数。

dim3有5796份样本，debug时间少于60s的有4891份，debug时间少于30分钟的有5633份

样本中所有人debug时间在24小时内

![](https://yhd123.oss-cn-hangzhou.aliyuncs.com/img/debug时间分布.png)



## 3. 代码有效行数

样本中，有效行数最多为340行

![](https://yhd123.oss-cn-hangzhou.aliyuncs.com/img/有效行数分析.png)

## 4. mi指数

![](https://yhd123.oss-cn-hangzhou.aliyuncs.com/img/mi指数分析.png)



## 总结

分析了提交次数和debug时间的情况，结合我们自身经验发现，大部分同学首先在本地对代码做debug，首次上传的代码往往是几乎没有bug的。

所以，一个用户的得分又各个维度得分相加而得



### debug得分

体现在提交次数和debug时间上，这里我们只考虑debug时间

我们过滤发现，debug时间小于30分钟的有5633份样本，超过总样本的95%.

用户i 做的n题中每一题的debug时间为
$$
DT_i（单位：秒）
$$


用户i 做的n题中每一题的debug得分为
$$
DTS_i=\begin{cases} 1, DT_i<30*60\\ 1-\frac{DT_i}{30*60}*0.01， DT_i\geq30*60\end{cases}
$$


得分为
$$
DT^{score}_{dim3}=\frac{\sum_{i=1}^{n}{DTS_i}}{n}
$$


### 有效行数得分

所有用户的dim3代码的有效行数均值为
$$
VL_{avg}
$$
用户i 做的n题中每一题的有效行数为 
$$
VL_i
$$
得分为
$$
VL^{score}_{dim3}=\frac{\sum_{i=1}^{n}{\frac{VL_{avg}}{VL_i}}}{n}
$$



### mi指数得分

所有用户的dim3代码的MI均值为
$$
MI_{avg}
$$
用户i 做的n题中每一题的MI指数为 
$$
MI_i
$$
得分为
$$
MI^{score}_{dim4}=\frac{\sum_{i=1}^{n}{(\frac{MI_i}{MI_{avg}})}^2}{n}
$$



### 用户的查找、排序得分

$$
S^{score}_{dim3}=DT^{score}_{dim3}+VL^{score}_{dim3}+MI^{score}_{dim3}
$$



计算得到：

![](https://yhd123.oss-cn-hangzhou.aliyuncs.com/img/分数分布.png)





