#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import math
height_male=178
height_female=158
sigma=5
PI=3.1415926
x=[]
#已知100个男同学的身高和100个女同学的身高，但是性别信息丢失，求男同学和女同学身高的期望
for i in range(200):
    temp=random.gauss(height_male,sigma)
    temp=math.floor(temp)
    x.append(temp)
    temp=random.gauss(height_female,sigma)
    temp=math.floor(temp)
    x.append(temp)
#print x
#初始化
u1=150
u2=170
b1=0.5
b2=0.5

for j in range(200):
    Qi_1=[]#Qi(Zi=1)
    Qi_0=[]#Qi(Zi=0)
    #E步：
    for i in range(200):
        temp=-((x[i]-u1)*(x[i]-u1)/(2*b1*b1))
        temp_1=math.exp(temp)
        temp_2=math.sqrt(2*PI)*b1
        f_1=temp_1/temp_2
        temp=-(x[i]-u2)*(x[i]-u2)/(2*b2*b2)
        temp_1=math.exp(temp)
        temp_2=math.sqrt(2*PI)*b2
        f_0=temp_1/temp_2
        temp_1=f_1/(f_1+f_0+0.00001)
        temp_2=f_0/(f_1+f_0+0.00001)
        Qi_1.append(temp_1)
        Qi_0.append(temp_2)

    #M步:
    sum_1=0
    sum_2=0
    temp_1=0
    temp_2=0
    for i in range(200):
        sum_1=sum_1+Qi_1[i]*x[i]
        sum_2=sum_2+Qi_0[i]*x[i]
        temp_1=temp_1+Qi_1[i]
        temp_2=temp_2+Qi_0[i]
    u1=sum_1/temp_1
    u2=sum_2/temp_2
    sum_1=0
    sum_2=0
    for i in range(200):
        sum_1=sum_1+Qi_1[i]*(x[i]-u1)*(x[i]-u1)
        sum_2=sum_2+Qi_0[i]*(x[i]-u2)*(x[i]-u2)
        b1=math.sqrt(sum_1/temp_1)
        b2=math.sqrt(sum_2/temp_2)
    print u1,u2,b1,b2
    
    