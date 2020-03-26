import numpy as np
import matplotlib.pyplot as plt

############# List #############################

# list1 = [1, 2, 3, 4, 5]
# mathScores = [60, 70, 10, 20, 10]
# mathScores.append(200)
# mathScores.insert(0, -99)
# mathScores.insert(1, 4)
# mathScores.insert(4, 70)
# mathScores.insert(3, 60)
# mathScores.remove(200)
# del mathScores[0:1]
# mathScores.pop(2)
# mathScores[0]=50
# 3 in mathScores
# 50 in mathScores
# mathScores.count(60)
# mathScores.index(70)
# print(mathScores)
# print(mathScores.index(70))
# print(mathScores + list1)
# print(list1 + mathScores)
# print(sorted(mathScores))
# print(sorted(mathScores, reverse=True))

# ls=[[1,2,3],[4,5,6]]
# ls[0]
# ls[0][2]
# print(ls)
#
#
# grades=[[5, 14, 7],[23, 36, 28],[88, 80, 92]]
# print(grades[2])
# print(sum(grades[0])/len(grades[0]))
# print(sum(grades[1])/len(grades[1]))
# print(sum(grades[2])/len(grades[2]))
# grades.append([94, 90, 96])
# print(grades)
# grades[0][2]=20
# print(grades)


# pi = 3.14
# pi_Area = 2 ** 3.14
#
#
# score = 60
#
# if score >= 60:
#     print("及格了")
#
# elif 55 <= score <60:
#     print("教授拜託調個分")
#
# elif 55 <= score <60:
#     print("可誤差一點點")
#
# else:
#     print("被當了")
#
#
# x = 42
# print(f"Value of x is {x}")

mathScores =[60, 70, 10, 20, 81, 63, 4]
# firstItem = f"first item in mathScores is [mathScores [0]]"
# print(firstItem)
#
# for i in range(10):
#     print(i)
# 也可寫成: [print(i) for i in range(10)]

#
# for i in range(0, 10):
#     print(i)
#
# for i in range(0, 10, 3):
#     print(i)
#
# for i in range(len(mathScores)):
#     print(i, mathScores[i])
#
# for i in mathScores: #印出list裡面每個索引值
#     print(i)
#
# family = {
#
#     'dad': 'Homer',
#     'mom': 'Marge',
#     'son': 'Bart',
#     'daughter': 'Lisa'
#
# }
#
# for member in family.items():
#     print(member)
#
# for key, value in family.items():
#     print(f"my {key} is {value}")
#
#

import math
#
# for i in mathScores:
#
#     print(math.sqrt(i) *10)
#
# #也可寫成: [ print(math.sqrt(i) *10) for i in mathScores]
#
#
# ######### while 迴圈 ###############
#
# # while 搭配 else
# count = 0
#
# while count < 10:
#     print(count)
#     count += 1
# else:
#     print("loop end")
#
#
import random
# i = random.randit(1,50)
# print(i)
#
# x = eval(input("How many rows:")) #型別轉換
# print(type(x))

#####練習1###九九乘法表#####

# i = 1
# j = 1
# for i in range(9):
#     for j in range(9):
#         print(f"{i} * {j} = {i * j}\n")
#

#
# count = 1
#
#
# while count <= 50:
#     print("你好")
#     count += 1
#
# else:
#     print("我說完了啦")
#
#
#
# x = eval(input("Please input a Integer:")) #型別轉換
# y = 1
#
# for i in range(1, x):
#
#     if y <= x:
#         print(y)
#     else:
#         break
#
#     y += 2
#

###################



#
# x = eval(input("Please input row:"))
# y = eval(input("Please input column:"))
# totalSum = 0
# rowSum = 0
# colSum = 0
#
# for i in range(y):
#     for j in range(x):
#         r = random.randint(1, 100)
#         print(f"{r}\t",end="")
#
#         totalSum += r
#         rowSum += r
#
#
#     print('\n')
#     print(rowSum)
#     rowSum = 0
#     colSum += r
#
# print(totalSum)


ls = []

for i in range(2):
    ls.append([])

    for j in range(2):
        num = random.randint(1, 100)
        ls[i].append(num)
        print(f"{ls}", end=" ")
