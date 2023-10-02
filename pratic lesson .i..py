# #
# # n=10
# # empty = []
# #
# #
# # for x in range(0,n+1):
# #     empty.append(x)
# # print(empty)
# #
# # for x in range(11):
# #     print(x)
# #
# # x = 0
# # while x < 10:
# #     x += 1
# #     print(x)
# #
# n = 5
# for x in range(1,n+1):
#     for i in range(1,x+1):
#         print(i, end= ' ')
#     print('')
#
# # for i in range (1,6):
# #     print(*range(1, i+1))
# #
# for i in range (1,7):
#     print(*range(1,7 -i))
# #
# #
# #
# #
# # # Decide the row count. (above pattern contains 5 rows)
# # row = 5
# # # start: 1
# # # stop: row+1 (range never include stop number in result)
# # # step: 1
# # # run loop 5 times
# #
# # row = 5
# # for i in range(1, row + 1, 1):
# #     # Run inner loop i+1 times
# #     for j in range(1, i + 1):
# #         print(j, end=' ')
# #     # empty line after each row
# #     print("")
#
# Enter number 10
# Sum is:  55
#
#
# number = 10
# i = 0
# for x in range (1, number+1):
#     i = i+x
# print(i)
#
# number = 2
# for x in range(1,11):
#     number = 3
#     number = number*x
#     print(number)
#
# number = int(input('inter a number: '))
# empty_list = []
# for x in range(1,11):
#     x = x * number
#     empty_list.append(x)
# print(empty_list)
#
# numbers = [12, 75, 150, 180, 145, 525, 50]
# for x in numbers:
#     if x<=150 and x%5==0:
#         print(x)
#     elif x>500:
#         break
#
# numbers = 21234
# x = str(numbers)
# i = 0
# while i<len(x):
#     i += 1
#     print(i)
#
# n = 5
# for x in range(n,0,-1):
#     for i in range(x,0,-1):
#         print(i, end=' ')
#     print("")
#     # print(*range(n,1), x)
#
# given_number = 75869
# list_str = str(given_number)
# listi = list(list_str)
# the_len = len(listi)
# print(the_len)
#
#
# list1 = [10, 20, 30, 40, 50]
# list1.reverse()
# for x in list1:
#     print(x)
#
#
#
#
# list1 = [10, 20, 30, 40, 50]
# while list1:
#     x = list1.pop()
#     print(x)
#
#
# for x in range(-10,0):
#     print(x)
#
# for i in range(5,0,-1):
#     if True:
#         print(i)
# else:
#     print("Done")
#
# # range
# start = 25
# end = 50
# print("Prime numbers between", start, "and", end, "are:")
# for x in range(start,end):
#     for i in range(2,x):
#         if x%i==0:
#             break
#     else:
#         print(x)
#
# num0 = 0
# num1 = 1
# counter = 0
# while counter<10:
#     counter = counter+1
#     new_num = num1+num0
#     print(new_num)
#
#
# fib_list = [0,1]
# counter = 0
# while counter<10:
#     new_num = fib_list[-1]+fib_list[-2]
#     fib_list.append(new_num)
#     counter = counter+1
# print(fib_list)
#
# # first two numbers
# num1, num2 = 0, 1
# print("Fibonacci sequence:")
# for i in range(10):
#     print(num1, end="  ")
#     num1 = num2
#     num2 = num1 + num2
#
# n=5
# i=1
# for x in range(1,n+1):
#     i=i*x
#     print(i,end=' ')
#
# number = 79542
# listi = list(str(number))
# listi.reverse()
# for x in listi:
#     print(x, end='')
# # for x in numb_list:
# #     print(x)
#
#
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#
# for x in my_list[1::2]:
#     print(x,end=' ')
#
#
#
# input_number = 6
# for x in range(1,input_number+1):
#     i=x**3
#     print(f'Current Number is : {x}  and the cube is {i}')
#
#
# # number of terms
# n = 5
# i = 0
# sumi=0
# for x in range(1,n+1):
#     i=(i*10)+2
#     sumi +=i
# print(sumi)
#
#
# n=5
# for x in range(0,n+1):
#     for i in range(0,x+1):
#         print('*',end=' ')
#     print('')
# for l in range(n-1,0,-1):
#     for m in range(l,0,-1):
#         print('*', end=' ')
#     print('')
#
#
#
