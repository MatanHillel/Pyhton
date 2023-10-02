#string

#1
full_name = "matan hillel"
to_enter= full_name.index(" ")
full_name_fix=full_name.upper()[0]+full_name.lower()[1:to_enter]+" "+full_name.upper()[to_enter+1]+full_name.lower()[to_enter+2:]
print(full_name_fix)

#2
age = 30
print("I am" ,full_name_fix,"and I am" ,age ,"years old")

#3
rev_name = full_name[::-1]
print(rev_name)

#4
s = "I live in mountains. I have a small house in the mountains. The mountains are very beautiful."
s_20 = s[20:]
print(s_20.index("mountains"))

#5
print(s.find("mountains")) #finds the first
print(s.rfind("mountains")) #do reverse and then fint the first (mean find last)

#6
full_sent ="I_am_a_smart_robot"
print(full_sent.split("_"))

#7
remove_str = "Very0small0house"
print(remove_str.replace("0"," "))

#8
replace_sen = "Carissa Mali Tessa Karen"
print(replace_sen.replace(" ",","))

#9
s1 = "TryOne"
firstword = s1[0:len(s1)//2] #to make it in the middle
secondword = s1[len(s1)//2:]
print(firstword+"new"+secondword)

#10
fruts = "Peach Apple Papaya Strawberry Banana"
split_fr = fruts.split(" ")
print(sorted(split_fr))

#fruts = "Peach Apple Papaya Strawberry Banana"
#split_fr = fruts.split(" ")
#split_fr.sort
#print(sorted(split_fr))

#Exercise 1A: Create a string made of the first, middle and last character
str1 = "James"

print(str1[0],str1[len(str1)//2],str1[len(str1)-1])

#Exercise 1B: Create a string made of the middle three characters

str1 = "JhonDipPeta"
str2 = "JaSonAy"

middle_char = len(str1)//2
mid_sec = len(str2)//2

print(str1[middle_char-1:middle_char+2])
print(str2[mid_sec-1:mid_sec+2])

#Exercise 2: Append new string in the middle of a given string
s1 = "Ault"
s2 = "Kelly"
len_s = len(s1)//2
print(s1[0:len_s]+s2+s1[len_s:])

#Exercise 3: Create a new string made of the first, middle, and last characters of each input string
s1 = "America"
s2 = "Japan"

#Exercise 4: Arrange string characters such that lowercase letters should come first
s1 = "America"
s2 = "Japan"
len_s = len(s1)//2
len_s2 = len(s2)//2
print(s1[0]+s2[0]+s1[len_s]+s2[len_s2]+s1[len(s1)-1]+s2[len(s2)-1])

#Exercise 5: Count all letters, digits, and special symbols from a given string
str1 = "PyNaTive"
lower_list = []
upper_list = []
for x in str1:
  if x.islower():
    lower_list.append(x)
  else:
    upper_list.append(x)
sorted_str = ''.join(lower_list+upper_list)
print(sorted_str)


#Exercise 6: Create a mixed String using the following rules
str1 = "P@#yn26at^&i5ve"
Chars = []
Digits = []
Symbol = []
for x in str1:
  if x.isalpha():
    Chars.append(x)
  elif x.isdigit():
    Digits.append(x)
  else:
    Symbol.append(x)
print("chars =",len(Chars),"Digit =",len(Digits),"Symbol =",len(Symbol))

# def find_digits_chars_symbols(sample_str):
#     char_count = 0
#     digit_count = 0
#     symbol_count = 0
#     for char in sample_str:
#         if char.isalpha():
#             char_count += 1
#         elif char.isdigit():
#             digit_count += 1
#         # if it is not letter or digit then it is special symbol
#         else:
#             symbol_count += 1
#
#     print("Chars =", char_count, "Digits =", digit_count, "Symbol =", symbol_count)
#
# sample_str = "P@yn2at&#i5ve"
# print("total counts of chars, Digits, and symbols \n")
# find_digits_chars_symbols(sample_str)

#Exercise 7: String characters balance Test
s1 = "Ynkk"
s2 = "PYnative"

flag= True
for i in s1:
  if i in s2:
    continue
  else:
    flag=False
print(flag)

#Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
str1 = "Welcome to USA. usa awesome, isn't it?"
sub_string = "USA"

temp_str = str1.lower()
count = temp_str.count(sub_string.lower())
print("The USA count is:", count)

#Exercise 9: Calculate the sum and average of the digits present in a string
str1 = "PYnative29@#8496"
digit_list = []
result = 0
for x in str1:
  if x.isdigit():
   digit_list.append(int(x))
sum_digit = sum(digit_list)
avg_digit = round(sum_digit/len(digit_list),2)
print(f"Sum is {sum_digit}, and the Average is {avg_digit}")

#Exercise 10: Write a program to count occurrences of all characters within a string
str1 = "Apple"
dict_word = {}
for x in str1: #keys -a p l e value- count
  counti = str1.count(x)
  dict_word[x] = counti
print(dict_word)

# milon ={"omer":29,"matan":31,"idan":31}
# milon["liraz"] = 34
# print(milon)

#Exercise 11: Reverse a given string

# str1 = "PYnative"
# str1_list = list(str1)
# empty = []
# while str1_list:
#     num = str1_list.pop()
#     empty.append(num)
#
# string_list = ''.join(empty)
# print(string_list)

# str1 = "PYnative"
# str1_list = list(str1)
# str1_list.reverse()
# string_list = ''.join(str1_list)
# print(string_list)

str1 = "PYnative"
rev_str = str1[::-1]
print(rev_str)
#Exercise 12: Find the last position of a given substring

str1 = "Emma is a data scientist who knows Python. Emma works at google data."
str2 = str1.rfind("Emma")
print(str2)

#Exercise 13: Split a string on hyphens

