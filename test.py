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