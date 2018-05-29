#!/usr/bin/python
#coding=utf-8
from __builtin__ import raw_input
import json


print("hello word !!");
print("你好，刘超");

if True :
    print "this is true"
    print "this is my true"
else :
    print "this is false"
    
myname ="liu" + \
        "chao"+ \
        "he" + \
        "liang"
        
#打印输出
print myname

textArea = '''hello every one , my name is liuchaoheliang ,i am twenty seven years old '''

#不换行输出
print textArea,myname

print myname[3:7] * 3

#列表数据
list = ["liuchao","heliang","chenqian","wangwu"]

print list
print list[2:]

#\元组数据，类似于枚举常量
payType = ("alipay","wechatPay","ubank")
print payType[2]

#列表中包含
if ("alipay" in payType) :
    print "alipay 在列表中"
else :
    print "alipay 不在列表中"

#数据字典（对象）
user = {'name':"liuchao",'age':27,'sex':"man"}

print user.get("name")


json = "{'name':'liuchao','age':24}"

obj = eval(json)

print obj["name"]

a = {'name':"liuchao",'age':27,'sex':"man"}
b = a

if ( user is a ):
    print "user 和  a 是同一个存储空间" 
elif ( a is b )  :
    print "a 和  b是同一个对象"
else :
    print "都说不是"

inputStr = raw_input("please input a number ..\n")

print "输入的文本是：" + inputStr

