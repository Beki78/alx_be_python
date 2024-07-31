# def factorial(num):
#     assert num > 0 and int(num) == num, f"The {num} is less than 0"
#     if num in [0,1]:
#         return 1
#     else:
#         return num * factorial(num-1)   
# print(factorial(4))

# def p(num):
#     if num == 0:
#         return 1
#     else:
#         powr = p(num-1)
#         return powr * 2
# print(p(1))

# def p(num):
#     i = 0
#     powe = 1
#     while i < num:
#         powe = powe * 2
#         i = i + 1
#     return powe
# print(p(3))

# def factorial(n):
#     k = 1
#     form = 1
    
#     while k in [1, n]:
#         n *= k
#         k += 1
       
#     return n

# print(factorial(5))

# def sumOfDigigts(num):
#     assert num > 0,  f"{num} should be positive"
#     assert  int(num) == num,  f"{num} should be integer"
#     if num == 0:
#         return 0
#     else:
#         return int(num % 10) + sumOfDigigts(int(num / 10))
# print(sumOfDigigts(-9.9))

# def count_ways_to_steal(n, cookies):
#     total_sum = sum(cookies)
#     even_count = sum(1 for x in cookies if x % 2 == 0)
#     odd_count = n - even_count 

#     if total_sum % 2 == 0:
#         return even_count
#     else:
#         return odd_count
# n = int(input())
# cookies = list(map(int, input().split()))
# print(count_ways_to_steal(n, cookies))

# def can_form_names(guest, host, pile):
#     combined_names = guest + host
#     sorted_combined_names = sorted(combined_names)
#     sorted_pile = sorted(pile)
    
#     if sorted_combined_names == sorted_pile:
#         return "YES"
#     else:
#         return "NO"

# # Example usage:
# guest = input().strip()
# host = input().strip()
# pile = input().strip()

# print(can_form_names(guest, host, pile))

# def min_rotations_to_even_sums(n, dominoes):
#     sum_upper = 0
#     sum_lower = 0
#     has_odd_even_pair = False

#     for xi, yi in dominoes:
#         sum_upper += xi
#         sum_lower += yi
#         if (xi % 2 != yi % 2):
#             has_odd_even_pair = True

#     if sum_upper % 2 == 0 and sum_lower % 2 == 0:
#         return 0
#     if sum_upper % 2 == 1 and sum_lower % 2 == 1 and has_odd_even_pair:
#         return 1
#     return -1

# # Example usage:
# n = int(input())
# dominoes = [tuple(map(int, input().split())) for _ in range(n)]
# print(min_rotations_to_even_sums(n, dominoes))


# class Animal:
#   def __init__(self, name):
#     self.name = name

#   def make_sound(self):
#     print("Generic animal sound")

# class Dog():
#   def make_sound(self):
#     print("Woof!")

# lassie = Dog("Lassie")
# lassie.make_sound()  # Output: Woof!

# from array import *

#first commit
# def traverse():
#     arr = array("i", [])
#     arr.append(5)
#     for i in arr:
#         return print(i)
# traverse()


#second commit
# arr = array("i", [1,2,3,4])
# def traverse(Beki, index):
#     Beki.append(5)
#     if index >= len(Beki):
#         print("The is no element")
#     else:
#         print(Beki[index])
# traverse(arr, 4)


#third commit 
# arr = array("i", [1,2,3,4])
# def traverse(Beki, index):
#     Beki.insert(0, 10)
#     if index >= len(Beki):
#         print("The is no element")
#     else:
#         print(Beki[index])
# traverse(arr, 0)


#fourth commit 
# arr = array("i", [1,2,3,4])
# def traverse(Beki, index):
#     Selam = [10,11,12]
#     Beki.extend(Selam)
#     if index >= len(Beki):
#         print("The is no element")
#     else:
#         print(Beki[index])
# traverse(arr, 5)


#fifth commit 
# arr = array("i", [1,2,3,4])
# def traverse(Beki, index):
#     Beki.insert(0, 10)
#     if index >= len(Beki):
#         print("The is no element")
#     else:
#         print(Beki[index])
# traverse(arr, 0)


# my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
# def findMissing(mylist):
#     sum1 = 100*101/2
#     sum2 = sum(mylist)
#     print(sum1 - sum2)
# findMissing(my_list)


# arr = [1,2,3,4, 5]
# def twosum(mylist:int, target:int):
#     for i in arr:
#         for j in arr:
#             if i + j == target and j == i +1:
#                 print([arr.index(i),arr.index(j)])
#             elif i or j <= 0:
#                 print('invalid')
            
# twosum(arr, -3)



# import numpy as np
# myArr = np.array([62,34,39,13,58,64,17,18,38,37,35,53,43,59,36])
# def bigprodut(array):
#     array.sort()
#     product = array[-1] * array[-2]
#     print(array[-1] , array[-2])
#     print(product)
# bigprodut(myArr)


# l1 = ["c", "a", "t", "e"]
# l2 = ["t", "c", "a", "z"]

# def permutation(list1, list2):
#     if len(list1) != len(list2):
#         return False
#     list1.sort()
#     list2.sort()
#     if list1 == list2:
#         return True
#     else:
#         return False
# print(permutation(l1, l2))


# 1,2,3     7,4,1
# 4,5,6     8,5,2
# 7,8,9     9,6,3


# import numpy as np
# myArr = np.array([[1,2,3], [4,5,6], [7,8,9]])

# myArr[2][2] = myArr[0][2]
# myArr[0][2] = myArr[0][0]
# myArr[0][0] = myArr[2][0]
# myArr[2][0] = myArr[2][2]

# print(myArr)

# myArr = [[1,2,3], [4,5,6], [7,8,9]]
# for i in range(0,len(myArr)):
#     for j in range(0,len(myArr[i])):
#         print(myArr[i][j], end="\t")
#     print("\n")


# def temp():
#     myList = []
#     myNewList = []
#     user = int(input("How many day's temperature: "))
#     for i in range(1, user + 1):
#         if i > user:
#             break
#         else:
#             temperature = (int(input(f"Day {i} highest temp: ")))
#             i = i +1
#             myList.append(temperature)
#     AVG = sum(myList) / len(myList)
#     print(f"Average = {AVG}")
    
#     for temp in myList:
#         if temp > AVG:
#             myNewList.append(temp)
#     print(f"{len(myNewList)} day(s)  is above average")        
# temp()


# def sumOf(n):
#     z = str(2)
#     lists = []
#     for i in range(1, n + 1):
#         lists.append(int(z * i))
#     print(sum(lists))    
# (sumOf(5))


# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]


# def merge(list):
    
#     print(sorted(list))
#     for i in list:
#         list.cou
# merge(sample_list)

# list1 = [5, 20, 15, 20, 25, 50, 20]
# def findOccurrence(list, num):
#     for i in list:
#         if i == num:
#             list.remove(num)
#     print(list)
# findOccurrence(list1, 20)



# list1 = [5, 20, 15, 20, 25, 50, 20]
# print(sorted(list1))
# def findOccurrence(list):
#     sortedList = sorted(list)
#     for i in range(0, len(sortedList)):
#         if sortedList[i] == sortedList[i + 1]:
#             sortedList.remove(sortedList[i + 1])  
#     print(sortedList)
# findOccurrence(list1)



#   Created by Elshad Karimov on 26/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved

# Dictionary Interview Questions


# Q-1. What will be the output of the following code snippet?
# c=[1,2,3]
# print(c[0,1])
# b={1:"p",2:"j"}
# print(b[1,2])
# a = {(1,2):1,(2,3):2}
# print(a[(1,2)])
# # A. Key Error
# # B.  1
# # C. {(2,3):2}
# # D. {(1,2):1}
 

# # Q-2. What will be the output of the following code snippet?

# a = {'a':1,'b':2,'c':3}
# print (a['a','b'])
# # # A. Key Error
# # B. [1,2]
# # C. {‘a’:1,’b’:2}
# # D. (1,2)

 

# # Q-3. What will be the output of the following code block?

# fruit = {}

# def addone(key):
#     if key in fruit:
#         fruit[key] =fruit[key]+1
#     else:
#         fruit[key] = 1
        
# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('apple')
# addone('apple')
# print (fruit)
# A. 1 
# B. 2
# C. 3 
# D. 4

 

# Q-4. What will be the output of the following code block?

# arr = {}
# arr[1] = 1
# arr['1'] = 2
# arr[1] += 1

# sum = 0
# for k in arr:
#     sum += arr[k]

# print(sum)
 # A. 1 
 # B. 2
 # C. 3 
 # D. 4

 

# Q-5. What will be the output of the following code snippet?



# my_dict = {}
# my_dict[1] = 1
# my_dict['1'] = 2
# my_dict[1.0] = 4

# sum = 0
# for k in my_dict:
#     sum += my_dict[k]
    
# print (sum)
# A. 7
# B. Syntax error
# C. 3
# D. 6

 

# # Q-6. What will be the output of the following code snippet?

# my_dict = {(1,2,4): 8, }
# my_dict[(1,2,4)] = 8
# my_dict[(4,2,1)] = 10
# my_dict[(1,2)] = 12

# sum = 0
# for k in my_dict:
#     sum += my_dict[k]

# print (sum)
# print(my_dict)
# # A. Syntax error
# # B. 30   
# #     {(1, 2): 12, (4, 2, 1): 10, (1, 2, 4): 8}
# # C. 47
# #     {(1, 2): 12, (4, 2, 1): 10, (1, 2, 4): 8}
# # D. 30
# #     {[1, 2]: 12, [4, 2, 1]: 10, [1, 2, 4]: 8}

 

# # Q-7. What will be the output of the following code snippet?

# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates[box]))

# # A. 1
# # B. 3
# # C. 4
# # D. Type Error

 

# # Q-8. What will be the output of the following code block?

# dict = {'c': 97, 'a': 96, 'b': 98}

# for key in sorted(dict):
#     print (dict[key])
# A. 96 98 97
# B. 96 97 98
# C. 98 97 96
# D. NameError

 

# # Q-9. What will be the output of the following code snippet?

# rec = {"Name" : "Python", "Age":"20"}
# id1 = rec
# del rec
# # rec = {"Name" : "Python", "Age":"20"}

# print(id(id1))
# # print(id(rec))

# print(id(r) == id(rec))
# # A. True
# # B. False
# # C. 0
# # D. 1

 

# # Q-10. What will be the output of the following code snippet?

# rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
# id1 = id(rec)
# del rec
# rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
# id2 = id(rec)
# print(id1)
# print(id2)
# print(id1 == id2)
# # A. True
# # B. False
# # C. 1
# # D. Exception
# rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
# id1 = id(rec)
# id2 = id(rec)
# print(id1 == id2)
# rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
# id1 = id(rec)
# id2 = id(rec)
# print(id(id1))
# print(id(id2))
# print(id(id1) == id(id2))



    




        

        






