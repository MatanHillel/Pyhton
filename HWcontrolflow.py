#control flow

#1
number = 2

if number%2==0:
    print(number,"is even")
else:
    print(number,"is Odd")

#2
list1 = []
num = 10

for i in range(1,num+1):
    list1.append(i)
print(list1)

#3
for i in list1:
    if i%2==0:
        print(i)

#4

for i in range(1,num+1,2):#range(where to start,where to finish, how MANY jumps)
    print(list1[i])

#5
# for i in range(num,0,-1):
#     print(i)
list_rev = []

for i in list1[::-1]:
    list_rev.append(i)
print(list_rev)

#6
mark_list = [67, 83, 45, 78, 32]
grades = []

for i in mark_list:
    if i<=45:
        grades.append("d")
    elif i<=60:
        grades.append("c")
    elif i<=75:
        grades.append("c")
    else:
        grades.append("a")
print(grades)

#7
n= 5
x = 1   #   5! = 1*2*3*4*5=120   8!=1*2*3*4*5*6*7*8
for i in range(1,n+1): #    1,2,3,4,5
    x = x*i  #   1*1=1  1*2=2  2*3=6 6*4=24 24*5=120
print(x)

#1 facto=1 = facto=1*i=1 -> facto =1
#2 facto=1 = 1*2 -> facto=2
#3 facto=2 = 2*3-> facto=6
#4 facto=6 = facto*i 6*4= facto=24
#5 facto=24 = 24*5 =  facto = 120

#8
num= 9

for i in range(2,num):
    if num%i == 0:
        print(num,"Is Not Prime")
        break
else:
    print(num,"Is Prime")

#9

number = str(12345640)
seprate = []

for i in number:
    seprate.append(i)
print(seprate)

#10
peramid = []
for i in range(1,6):
    peramid.append(i)
    print(peramid)

#1
#1 +2
#1,2 +3
#1,2,3 +4
#1,2,3,4 +5

# Exercise 1: Print First 10 natural numbers using while loop
n= 10

for i in range(1,n+1):
    print(i)

i = 1

while i <=10:
    print(i)
    i+=1

# Exercise 2: Print the following pattern
emp_list = []
num=5

for i in range(1,num+1):
    emp_list.append(i)
    print(emp_list)

# Exercise 3: Calculate the sum of all numbers from 1 to a given number
sum_num = 10
result=0

for i in range(1,sum_num+1):
    result = result+i
print(result)

# Exercise 4: Write a program to print multiplication table of a given number
num = 3

for i in range(1,11):
    ans = num*i
    print(ans)

# Exercise 5: Display numbers from a list using loop
numbers = [12, 75, 150, 180, 145, 525, 50]
slected = []
for i in numbers:
    if i>500:
        break
    elif i>150:
        continue
    elif i%5==0:
        print(i)
#continue means jump over the number and ignore it

# numbers = [12, 75, 150, 180, 145, 525, 50]
# slected = []
# for i in numbers:
#     if i>500:
#      break
#     if i<=150:
#         if i%5==0:
#            print(i)

#In Python, the continue statement is used to skip the rest of the current iteration
# of a loop and move on to the next iteration. In the code you provided,

# Exercise 6: Count the total number of digits in a number


# Exercise 7: Print the following pattern
n= 5
k= 5

for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()

# 0 5-1 5--1 -1
# 1 5-1 4--1 -1
# 2 5-2 3--1 -1

# Exercise 8: Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]

for i in list1[::-1]:
    print(i)

# rev_list = reversed(list1)
#
# for i in rev_list:
#     print(i)

# Exercise 9: Display numbers from -10 to -1 using for loop
for i in range(-10,0,1):
    print(i)

# Exercise 10: Use else block to display a message “Done” after successful execution of for loop
for i in range(0,3):
    if i>=1:
        break
print("done")

#Exercise 11: Write a program to display all prime numbers within a rangen= 10

start = 1
end = 50

for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)


# Exercise 12: Display Fibonacci series up to 10 terms
# Fibonacci sequence:
# 0  1  1  2  3  5  8  13  21  34
n= 10
fibo = [0,1]

while len(fibo)<=n:
    next_num = fibo[-1]+fibo[-2]
    fibo.append(next_num)
print(fibo)

# Exercise 13: Find the factorial of a given number
num = 5
functorial = 1

for i in range(1,num+1):
    functorial= functorial*i
print(functorial)

#
# num = 5
# factorial = 1
# if num < 0:
#     print("Factorial does not exist for negative numbers")
# elif num == 0:
#     print("The factorial of 0 is 1")
# else:
#     # run loop 5 times
#     for i in range(1, num + 1):
#         # multiply factorial by current number
#         factorial = factorial * i
#     print("The factorial of", num, "is", factorial)

# Exercise 14: Reverse a given integer number
inti = 76542
rev_inti = int(str(inti)[::-1])
print(rev_inti)

# inti = 76542
# rev_int = 0
#
# while inti > 0:
#     remainder = inti % 10
#     rev_int = rev_int * 10 + remainder
#     inti = inti // 10
#
# print(rev_int)

# Exercise 15: Use a loop to display elements from a given list present at odd index positions
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
odd_place =[]
for i,num in enumerate(my_list):
    if i%2 != 0:
        odd_place.append(num)
print(odd_place)

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#
# for i in my_list[1::2]:
#     print(i,end=' ')

# Exercise 16: Calculate the cube of all numbers from 1 to a given number
input_number = 4

cube = (input_number**2)*input_number
print(f"number is:{input_number}, and the cube:{cube}")

# input_number = 6
# for i in range(1, input_number + 1):
#     print("Current Number is :", i, " and the cube is", (i * i * i))

# Exercise 17: Find the sum of the series upto n terms
n = 5
num = 2
sumi = 0

for i in range(0,n):
    sumi += num
    num = num*10+2
print(sumi)

# Exercise 18: Print the following pattern
rows = 5

for i in range(0,rows):
    for j in range(0,i+1):
        print("*",end=' ')
    print("\r")

for i in range(rows,0,-1):
    for j in range(0,i-1):
        print("*",end=' ')
    print("\r")
