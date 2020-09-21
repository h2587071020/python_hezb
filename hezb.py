
# l =[1,2,3,4,5,2,3,1]
#
# l[2]=8
# print (l)
#
# t=(1,2,3,4,5,6,5,4,3,2,1)
#
# print (t)
#
#
# s={1,2,3,4,5,5,5}
# print(s)
#
# a=10
# b="11"
# print(a+int(b))
#
# a=10
# b="1.1"
# print(a+float(b))
#
# a=9
# b=True
# print(a+b)
#
# d={"name":"否含","age":22}
# print(d)
#
# l=[1,2,2,3,4,4,5,5,]
# print(tuple(l))
# print(set(l))
#
# t=(1,2,3,3,4,4,5)
# print(list(t))
# print(set(t))
#
# s={1,2,3,4,5}
# print(list(s))
# print(tuple(s))
#
# a="1234567"
# print(tuple(a))
# print(set(a))
# print(list(a))
#
# a="ahelog"
# l=["a","4","g"]
# t=("a","4","g")
# s={"a","4","g"}
# d={"name":"老骚","sex":"男"}
# print("a"in a)
# print("a"in l)
# print("a"in s)
# print("a"in t)
# print("name"in d)

# money=100
# if(money<1000):
#     print("找老邵")
# elif(money <10000):
#     print("啊哈哈")
# elif(money <100000):
#     print("买两包辣条")
# else:
#     print("洗洗睡吧")
#
# for i in [1,2,3,4,5,6]:
#       print(i)
#       print("重要的事情说三遍!");
#
# for i in range(100):
#     print("重要的事情说三遍!")
#
# print(list(range(1,11,1)))
# print(list(range(12,1,-3)))
# print(list(range(1,11,1)))
# print(tuple(range(1,11,1)))
# print(set(range(1,11,1)))

# i=1
# while(i<13):
#     print(i)
#     i +=1

# while True:
#     print("hello")

# for i in range(1,11):
#     if(i==7):
#         continue
#     print(i)

# for i in range(1,11):
#     if(i==7):
#         pass
#     else:
#         print(i)

# for i in range(1,11):
#     if(i==7 or i==9):
#         continue
#     print(i)
# 九九乘法表
# 冒泡排序


# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%s*%s=%s"%(i,j,i*j),end ="")
#     print()



# def s(a,b):
#     if b==0:
#         print("被除数不能为0")
#     else:
#         print(a/b)
# s(10,20)
# div(20,10)
# div(10,0)
# div(50,100)

# def jiu_jiu():
#     print("456789")
# jiu_jiu()

# def select_data():
#     res=("查询结果")
#     return res
#
# result=select_data()
# print(result

# def a(a,b):
#     return(a+b)
# b=a(10,10)
# print(b)
#
# def d(a=3,b=2):
#     return a+b
# print(d(1,9))
# print(d(b=20))
# print(d(1,5))


# def f(a,*args,b=4,**kwargs):
#     # print(a)
#     print(args)
#     print(kwargs)
# f(1,2,3,4,5,c=9,l=6)


# #操作文件
# f=open("work.py","w")
# f.write("hello python")
# f.close()

#
# f=open("work.py","r")
# result=f.read()
# print(result)
# f.close


# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,"x",j,"=",i*j,end="\t")
#     print()


# c=10
# def aaa():
#     global c
#     c=20
#
# aaa()
# print(c)
import random

a='1234567890'
# b='456'
# print(a[:9])#1-9
# print(a[:-1])#1-9
# print(a[3:-3])#4-7
# print(a[3:7])#4-7
# print(a[4])#5
# print(a[-5:-1])#6-9
# print(a[-5:])#6-0
# print(a[::2])#
#

# 切片  去空格 （字符串）
# a=" fhsjsghk "
# a.strip()
# print(a.strip())
# print(a.rstrip())
# print(a.lstrip())

# line="用户名,账户,金额,时间"
# line=line.replace(",","，")
# print(line)
# print(line.split("，"))

# 字符串格式化
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{}x{}={}".format(j,i,i*j),end='\t')
#     print()


# l=[1,2,3,4,5,6,7,8]
# for i in l:
#     print(i)

# l[0]=99   #根据下标修改列表元素的值
# l.append(9)
# l.insert(2,40)
# l.extend((6,7,5,4))
# l.pop()
#
# print(l)




# # 字典
# d = {"name":"小明","age":"20"}
#
# print(d["name"]) # 访问字典值
# d["name"] = "小红" # 修改value
# d["sex"] = "女" # 因为sex在原字典中不存在，所以是新增
# d.pop("sex") # 删除字典中的数据
# #
# d2 = {"sex":"女"}
# d.update(d2) # 合并两个字典
# print(dict(d,addr="上海闵行",phone="1856954125")) # 创建一个新字典，并把数据放进去
#
#
# print(d)


#类的封装

# class Demo():
#     __a=None
#     def set__a(self,value):
#         self.__a=value
#     def get__a(self):
#         return self.__a
#
# p=Demo()
# p.set__a('hello')
# print(p.get__a())


# class demo():
#     b='类变量'
#     __a='类变量2'
#     def __say(self):
#      print('hello')
#     def hello(self):
#      print(self.__a)
#      self.__say()
# d=demo
# print(d.b)

# import random
# import random # 随机模块
# print(random.randint(1,20)) # 获取随机整数
# print(random.random()) # 获取随机数 小数
# print(random.choice("0123456789")) # 在指定集合中，随机获取一个数据
# l = random.choices("0123456789",k=10)# 在指定集合中，随机获取一组数据
# print(l)
# print("".join(l)) # 把可迭代对象转成字符串

#编写一个返回随机手机号的方法
# import random

# def demo():
#     l = random.choices("1", k=1)
#     k= random.choices("123456789",k=10)
#     s='l'+"".join(k)
#     print(s)

# demo()



#编写一个返回指定长度和内容的随机字符串方法
# import random
# def kkk():
#
#     l = random.choices('dfhjfdjfhdjfhjdfh',k=random.randint(1,10))
#
#     print("".join(l))
#
# kkk()

#编写一个返回随机姓名的方法
# import random
# def cc():
#     l=random.choice("张王赵钱孙李")
#     f= random.choices("刚亮柳露金军伟强",k=random.randint(1,2))
#     d=l+"".join(f)
#     print(d)
# cc()


print('asdf')
try:
    # r=open('module_4.py','r')#报错 FileNotFoundError
    print(1/3)
except FileNotFoundError as e:
    print(e)
    print('程序执行遇到问题')
    print('重新打开文件')
except ZeroDivisionError as e :
    print('除数不能为0')
else:
    print('程序没有错运行')
finally:
    print('不管错没错都运行')

print('文件已经打开')


print('我是天选之子田贺元')

print('我是天选之子田贺元')
print('我是天选之子田贺元')






