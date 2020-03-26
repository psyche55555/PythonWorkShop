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

################ tuple ########################

# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = 1, 2, 3, 4, 5
# print(tuple1[3])
# print(tuple1.index(4))
# print(tuple1.count(3))
# print(tuple1 + tuple2)
# sorted(tuple1)
# sorted(tuple1, reverse=True)
#
# 20 in tuple2
# 1 in tuple2
#
# tuple3 = 88, 12, 34
# x, y, z = tuple3 #用變數去接tuple
# print(x)
# print(y)
# print(z)
#
#
# gradesTuple = ((5, 14, 7),(23, 36, 28),(88, 80, 92))
# print(gradesTuple[2])
# print(sum(gradesTuple[0])/len(gradesTuple[0]))
# print(sum(gradesTuple[1])/len(gradesTuple[1]))
# print(sum(gradesTuple[2])/len(gradesTuple[2]))




############ Dictionary ##############################
###沒有順序,不會有index, 但有 key(身份證字號) & value(身份證字號裡面的東西)

# family = {
#
#     'dad': 'Homer',
#     'mom': 'Marge',
#     'son': 'Bart',
#     'daughter': 'Lisa'
#
# }
#
# print(family.get('dad'))
# 'dad' in family
# 'cousin' in family
# family.keys()
# family.values()
# family.items()
#
# family1 = {}
#
# family1['cousin'] ='Max' #新增
# family1['cousin'] ='Maxy' #修改
# family1.update({'uncle': 'Martin', 'aunt': 'May'}) #新增多個
# del family1['cousin']
# # family.pop('cousin')
#
#
# gradesDict = {'Chinese': [5, 14, 7], 'English': [23, 36, 28], 'math': [88, 80, 92]}
# print(gradesDict.get('math'))
# print(sum(gradesDict.get('Chinese'))/len(gradesDict['Chinese']))
# print(sum(gradesDict.get('English'))/len(gradesDict['Chinese']))
# print(sum(gradesDict.get('math'))/len(gradesDict['Chinese']))
# gradesDict.update({'science': [94, 90, 96]})
# print(gradesDict.items())


################# Set ############
# 沒有value的dictionary,且值不能重複

# fruits = {
#     'apple',
#     'banana',
#     'guava',
#
# }
#
# fruits1 = {
#     'strawberry',
#     'papaya',
#     'banana'
# }
#
# fruits | fruits1 #聯集
# fruits & fruits1 #交集
# fruits - fruits1 #差集
#
# fruits.add('watermelon') #新增
# fruits.remove('apple') #如果'apple'不存在會出錯
# fruits.discard('apple') #如果'apple'不存在則不動作
# fruits.clear() #刪除全部元素
# sorted(fruits1) #排序(回傳List)


allStudents = {
    'John', 'Eva', 'Jill', 'Eric', 'Andy',
    'Albert', 'Polina', 'Kristin', 'Angela'
}

danceClub = {
    'John', 'Eva', 'Jill', 'Eric', 'Andy'
}

guitarClub = {
    'Eric', 'Andy','Albert', 'Polina', 'Kristin',
}

print(danceClub & guitarClub)
print(guitarClub - danceClub)
bothClub = danceClub | guitarClub
print(allStudents - bothClub)

