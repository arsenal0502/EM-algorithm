#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import sys
import time
import jieba
import datetime
from collections import Counter
reload(sys)
sys.setdefaultencoding('utf-8')
#使用二维字典
def add_two_dim_dict(thedict,key1,key2,val):
    if(key1 in thedict):
        thedict[key1].update({key2:val})
    else:
        thedict.update({key1:{key2:val}})
def random_list(ran_list):
    result=[]
    if(len(ran_list)==1):
        return ran_list
    elif(len(ran_list)>1):
        for r in ran_list:
            list_temp=[]
            for t in ran_list:
                if(r!=t):
                    list_temp.append(t)
            list_result=random_list(list_temp)
            temp=[]
            if(len(list_result)==1):
                temp.append(r)
                for i in list_result:
                    temp.append(i)
                result.append(temp)
            elif(len(list_result)>1):
                for i in list_result:
                    temp.append(r)
                    for j in i:
                        temp.append(j)
                    result.append(temp)
                    temp=[]
        return result
        
def search_list(ran_list,dic_1,dic_2):#dic_1是先验概率，dic_2是条件概率
    global num
    #p=1
    for i in range(len(ran_list)):
        if(i==0):
            if(ran_list[i] in dic_1):
                p=dic_1[ran_list[i]]
            else:
                p=1.0/num
        else:
            if(ran_list[i-1] in dic_2):
                if(ran_list[i] in dic_2[ran_list[i-1]]):
                    p=p*dic_2[ran_list[i-1]][ran_list[i]]
                else:
                    p=p*(1.0/num)
            else:
                p=p*(1.0/num)
    return p
        
    
        
#主程序


#print u'\u6c5f\u6e56',u'\u7b11\u50b2'
str1=raw_input(u"请输入汉语词语，以空格分开：")
#str1="你 我 喜欢"
time1=datetime.datetime.now()
#print str1
file1=open("novel.txt",'rb')
file2=open("Chinese-stop-words.txt")
stop_list=[]
for line in file2:
    content2=line.decode()
    stop_list.append(content2[0])
    #print content2[0]
file2.close()

content1=file1.read().decode()
list2=[]
dic={}
i=0
num=0
for j in range(len(content1)):
    if(content1[j]=='。'):
        #text.append(content[i:j])
        list1=jieba.cut(content1[i:j])
        list2=[]
        for l in list1:
            #print type(l),type(stop_list[1])
            #print l
            if((l in stop_list)or(l==u'\n')):
                #print 1,l
                continue
            else:
                
                if(len(list2)==0):
                    list2.append(l)
                else:
                    k=list2[len(list2)-1]
                    if(k in dic):
                        if(l in dic[k]):
                            val=dic[k][l]
                            #print k,l
                            num+=1
                            add_two_dim_dict(dic,k,l,val+1)
                        else:
                            #print k,l
                            num+=1
                            add_two_dim_dict(dic,k,l,1)
                    else:
                        #print k,l
                        num+=1
                        add_two_dim_dict(dic,k,l,1)
                    list2.append(l)                    
        i=j+1
dic_total={}
for m in dic:
    sum=0
    for n in dic[m]:
        sum+=dic[m][n]
    dic_total[m]=sum
    for n in dic[m]:
        dic[m][n]=(dic[m][n]+0.0000)/sum
        #print dic[m][n]
sum=0
for m in dic_total:
    sum+=dic_total[m]
for m in dic_total:
    dic_total[m]=1000*(dic_total[m]+0.000)/sum
    #print dic_total[m]
str2=unicode(str1,'utf8')
result=[]
i=0
for j in range(len(str2)):
    if(str2[j]==' '):
        result.append(str2[i:j])
        i=j+1
result.append(str2[i:])
result_random=random_list(result)
temp_max=0
for x in result_random:
    temp=search_list(x,dic_total,dic)
    if(temp>temp_max):
        temp_max=temp
        temp_result=x
for x in temp_result:
    print x
time2=datetime.datetime.now()
print "运行时间%d秒"%(time2-time1).seconds
time.sleep(10)       