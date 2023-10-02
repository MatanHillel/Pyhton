#tuple

#1
even_num1= [2, 3, 5, 7, 11, 3, 2, 12]
tuple1= tuple(even_num1)
print(tuple1)

#2
new_even=tuple1[::-1]
print(new_even)

#3
print(new_even.index(11))

#4
print(sorted(new_even))

#5
sort_even=sorted(tuple1)
print(sort_even[-1],sort_even[-2])

#6
tuple2 = (1, 2, 3)
tup_count = len(tuple2)
print(tup_count)

#7
#x,y,z=(1,2,3)
t= (1,2,3)
x,y,z = t
print(x,y,z)


#8
x,y,z = y,z,x
print(x,y,z)

#9
list_1= [1,2]
list_2= [3,4]
list_tuple= (list_1,list_2)
print(list_tuple)

#10
list_1.insert(0,0)
print(list_tuple)