#sets

#1
flowers = ['Rose', 'Orchids', 'Lily', 'Sunflower']
set_flower = set(flowers)
print(f"set flowers {set_flower}")

#2
more_flowers = {'Poppy', 'Vilot', 'Rose'}
print(f"more flowers {more_flowers}")

#3
combine = set_flower.union(more_flowers)
print(combine)

#4
common = set_flower.intersection(more_flowers)
print(f"common {common}")


#5
uniq = more_flowers.difference(set_flower)
print(uniq)

#6 ??
uniq2 = set_flower.difference(more_flowers)
print(uniq,uniq2)

#7
print(set_flower.issuperset(more_flowers))
print(set_flower.issubset(more_flowers))

#8 cnrl "/" makes all in #
# print(set_flower)
# print(more_flowers)
# print(set_flower.intersection(more_flowers))
# list_com = str(common)
# set_flower.difference_update(list_com)
# print(set_flower)
# print(more_flowers)
#
ijud = set_flower.difference(more_flowers)
print(ijud)
#
#
# print(set_flower)
#
# set_flower.discard({ijud})
# print(set_flower)
#ed.remove(common)
#print(set_flower)


#9 ???????
all_flowers =set_flower.union(more_flowers)
print(all_flowers)

#10
list1 = [2, 3, 5,1, 3, 4, 1, 2]

set_lis= set(list1)
print(len(set_lis))


#extra quition
# 1. Write a Python program to create a set
set1 = {'T', True, 45, 23, 56, 'Joes', 45.6}
print(type(set1))
#
#3. Write a Python program to add member(s) in a set

animal = {"Lion","Cat"}
print(animal)
animal.add('Dog')
print(animal)
animal.update({'Wolf','Tiger'})
print(animal)
#the diffrance between add(adding 1 element) and update(posible addin more than 1)
#
# 4. Write a Python program to remove item(s) from a given set
Before_removing = {50, 20, 70, 60, 30}
Before_removing.pop()
print(Before_removing)
#
# 5. Write a Python program to remove an item from a set if it is present in the set
list2 = {50, 20, 70, 60, 30}
list2.remove(50)
print(list2)
#
# 6. Write a Python program to create an intersection of sets
seta ={40, 20, 70, 30}
setb = {40, 50, 20, 60}
interset = seta.intersection(setb)
print(interset)
#
# 7. Write a Python program to create a union of sets
uniset = seta.union(setb)
print(uniset)
#
# 8. Write a Python program to create set difference
A = {80, 50, 20, 70, 40, 30}
B = {50, 20, 90, 40, 10, 60}
diff_a_b = A.difference(B)
diff_b_a = B.difference(A)
print(diff_a_b)
print(diff_b_a)
#
# 9. Write a Python program to create a symmetric difference
A = {80, 50, 20, 70, 40, 30}
B = {50, 20, 90, 40, 10, 60}
a_b = A.symmetric_difference(B)
b_a = B.symmetric_difference(A)

print(a_b)
print(b_a)
# full outer join
# 10. Write a Python program to create a shallow copy of sets
origin = {"Tutor" , "Joes"}
copy_or = origin.copy()
print(copy_or)
#
# 11. Write a Python program to find the elements in a given set that are not in another set
X = {50, 20, 70, 40, 10, 60, 30}
Y = {80, 50, 100, 70, 90, 60}
X_Y = X.difference(Y)
Y_X = Y.difference(X)
print(X_Y)
print(Y_X)
#
# 12. Write a Python program to check if two given sets have no elements in common
a = {23, 8, 56, 45, 78}
b = {42, 26, 55, 87}
Z = {46, 87}
Compare_A_B = a.isdisjoint(b)
Compare_B_Z = b.isdisjoint(Z)
Compare_A_Z = a.isdisjoint(Z)
print(Compare_A_B,Compare_B_Z,Compare_A_Z)
#the isdisjoint() method is used to compare the sets and check if they have any elements in common
#The method returns True for all three comparisons, indicating that the sets have no elements in common.
# 13. Write a Python program to find maximum and the minimum value in a set
listi = {17, 56, 23, 8, 10, 45}
Maximum = max(listi)
Minimum = min(listi)
print(Maximum)
print(Minimum)
#
# 14. Write a Python program to remove all elements from a given set
set_remove ={ "Red", "Green", "Pink", "White", "Black", "Yellow", "Blue" }
set_remove.clear()
print(set_remove)

#
# 15. Write a Python program to Intersection of two lists
l1 =[1,2,3,4,5,6,7,8]
l2= [11,2,43,48,55,6,76,8]
s1= set(l1)
s2= set(l2)
print(s1.intersection(l2))
#
# 16. Write a Python program to Convert String to Set
str1 = "TutorJoes"
conv = set(str1)
print(type(conv))
print(conv)
#
# 17. Write a Python program to Convert Set to String
Set = {'T', 'u', 't', 'o', 'r', 'J', 'o', 'e' , 's'}
convi = str(Set)
print(convi)
print(type(convi))
#
# 18. Write a Python program to Convert Set to List
Set = {'T', 'u', 't', 'o', 'r', 'J', 'o', 'e' , 's'}
to_list = list(Set)
print(to_list)
#
# 19. Write a Python program to Convert Set to Tuple
Set = {'T', 'u', 't', 'o', 'r', 'J', 'o', 'e' , 's'}
to_tumple = tuple(Set)
print(to_tumple)
#
#
# 20. Write a Python program to Convert Tuple to Set
Tuple = ('T', 'u', 't', 'o', 'r', 'J', 'o', 'e' , 's')
to_set1 = set(Tuple)
print(to_set1)

# 21. Write a program to add all its elements into a given set
s1 ={10,20,30,40,50}
l2 =[60,70,80,90,100]
s2 =set(l2)
s1.update(s2)
print(s1)
#with update i join the items from list 2 and added to set 1
# 22. Write a Python program to return a new set with unique items from both sets by removing duplicates.
s1={10, 20, 30, 40, 50}
s2={40, 50, 60, 70,80}
new = s1.union(s2)
print(new)
#
# 23.Write a Python program to Check if two sets have any elements in common.If  yes, display the common elements
s1 = {1, 2, 3, 4, 5}
s2 = {5, 3, 7, 8, 9}
s3 = {6, 7, 8, 9, 10}

print(s1.intersection(s2))
print(s1.isdisjoint(s3))
# if isdisjoin is true that mean they got nothing in common
# 24. Write a Python program to Check if a set a subset of another set
A = {4,5}
B = {1,2,3,4,5}
print(A.issubset(B)) # This method returns True if all the elements of set "a" are present in set "b"
print(B.issubset(A))
#This method returns True if all the elements of set "b" are present in set "a". In this case,
#the result will be False since set "b" contains additional elements (1, 2, and 3) not present in set "a".
# 25. Write a Python program to Check if a set is a subset, using comparison operators
A = {'a','b'}
B = {'a','b','c'}
print("A Subset of B :",A<=B)
print("B Subset of A :",B<=A)
#
# 26. Write a Python program to Check is a set a subset of itself?
A = {1,2,3,4,5}
print(A.issubset(A))
#
# 27. Write a Python program to Check if a specific value exists in a set
Set = {10,20,30,40,50}
print(30 in Set)
print(60 in Set)
#
# 28. Find the union, symmetric difference, and intersection of the two sets. Print the results of each operation
Set_1 = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
Set_2 = {20, ('Python', 'C') , 10, 11, ('J', 'O', 'E') }
uni_sets = Set_1.union(Set_2)
sem_dif = Set_1.symmetric_difference(Set_2)
inter = Set_1.intersection(Set_2)
print(uni_sets)
print(sem_dif)
print(inter)

#
# 29. Create a sequence of numbers using range, then ask the user to enter a number.
# Inform the user whether or not their number was within the range you specified
a = list(range(1,50))
#print(a)
num = int(input("Enter the Number :"))
if num in a:
	print("The Number is a Within a Range...")
else:
	print("The Number is a Not Within a Range...")
#
# 30. program to count number of vowels using sets in given string
#
str = "Tutor Joes"
count = 0
vowel = set("aeiouAEIOU")
print("String :", str)
print("Vowels :", vowel)
for alphabet in str:
    if alphabet in vowel:
        count = count + 1
print("Number of Vowels :", count)
