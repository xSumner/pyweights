from algorithms import entropy, coefficient_of_variation
import numpy as np


li=[[100,90,100,84,90,100,100,100,100],
    [100,100,78.6,100,90,100,100,100,100],
    [75,100,85.7,100,90,100,100,100,100],
    [100,100,78.6,100,90,100,94.4,100,100],
    [100,90,100,100,100,90,100,100,80],
    [100,100,100,100,90,100,100,85.7,100],
    [100,100,78.6,100,90,100,55.6,100,100],
    [87.5, 100,85.7,  100,100,100, 100,100,100],
    [100,100, 92.9, 100,80,100,100,100,100],
    [100,90,100,100,100,100,100,100,100],
    [100,100,92.9,100,90,100,100,100,100]]

# 将列表转化为numpy中的矩阵
li = np.array(li)
# 将矩阵标准化
li = entropy.matrix_standardization(li)

s1, s2 = entropy.get_entropy(li)

rlt = entropy.get_score(li, s2)
print("信息熵为：", s1)
print("权重为：", s2)

print("最后得分为：", rlt)