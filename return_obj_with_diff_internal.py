# coding:utf-8

"""
usage： 
obj = func(lst)
obj.next()  # 依次返回列表的每个元素，然后不停返回列表最后一个～
某些情景下还是有用的：比如时间间隔依次上涨，到某个值之后就保持不变了
"""

last_time = 9999
lst = [10, 20, 30, 40]

def func(lst):
    a = 0
    while True:
        if a < len(lst):
            yield lst[a]
            a += 1
        else:
            yield lst[-1]

if __name__ == '__main__':
    obj = func(lst)
    for i in range(10):
        print obj.next()