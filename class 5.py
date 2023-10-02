#! the way to do funcorial
n =3
f =1

for i in range(1,n+1):
    f=f*i
print(f)

# prime number

n=13

for i in range(2,n):
    if n%i==0:#if the number / in a smoller num
        print("Not Prime")
        break
else:
    print("Prime")


#def functorial(n):
#    if n == 0:
#        return 1
#    return functorial(n-1)*n



#1.Create a Python script to calculate the deposit in 10 years
#deposit*(1+rate)**10
year = 2023
deposit = 2000
rate = 0.02
period = 3
counter=1

#while counter<period:
#    deposit =deposit*(1+rate)
#    counter +=1
#    print(deposit)

#year = 2023
#deposit = 2000
#rate = 0.02
#period = 10
#counter=year

#while counter<=year+period:
#  deposit=round(deposit*(1+rate),1)
#  counter+=1
#  print(counter,":",deposit)

#2.Create a Python script to play 7 Boom

#n=1
#
#while n<101:
#    if n%7==0 or '7' in str(n):
#        print("boom")
#    else:
#        print(n)
#    n+=1

#3 1.Create a Python script to ask if the user wants to continue to add numbers to a list. If not, print the numbers and the sum of them
listi = []
flag = True

while flag:
    ask = input("wanna add number to the list? yes/no: " ).lower().strip()
    if ask== "yes":
        add = int(input("enter the num:"))
        listi.append(add)
    else:
        flag= False

sumi = sum(listi)
print(f"the list include: {listi},\n the sum: {sumi}")

#1.Create a Python script that prints each item and its corresponding type from the following list
#datalist = [1452, 11.23, 1+2j, True, (0, -1), [5, 12],
list1 = [{"class":'V', "section":'A'},34,'jhvh']

for i in list1:
    print(i,type(i))


#2.Create a Python script that take a string from a given string where all occurrences of its first char
#have been changed to'$', except the first char itself

str1 = "alphabat"
new_str = ""
revers = str1[::-1]

for i,char in enumerate(revers):
    if i == revers.index("a"):
        new_str += char
    elif char == "a":
        new_str = new_str + "$"
    else:
        new_str = new_str + char
print(new_str[::-1])

# 0,a
# 1,l
# 2,p
# 3,h
# 4,a
# 5,b
# 6,a
# 7,t
#
# new word = "a"

str1 = "alphabat"
print(str1[0]+str1[1:].replace('a','$'))


statement = 'alphabat'
counter = 1

while counter<2:
    for i in statement:
        if i == "a":
            counter = counter + 1
        first_half = statement[:counter]
        second_half = statement[counter:]

print(first_half + second_half.replace('a','$'))