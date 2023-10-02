#class 3

# lecturer exemaple
#Create a Python script that give the average value of the numbers in a given tuple of tuples
nums_1 = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
a,b,c,d = nums_1
avg1 = sum(a)/len(a)
avg2 = sum(b)/len(b)
avg3 = sum(c)/len(c)
avg4 = sum(d)/len(d)

print(avg1,avg2,avg3,avg4)

ID_list = {'30111':'matan','15555':'sharon','44556':'idan'}
print(ID_list)

print(ID_list['30111'])
print(ID_list.get('30111'))

#update
ID_list['15556'] = 'omer'
print(ID_list)
ID_list.update({'15555':'liraz','13332':'ron'}) #update is update exsist and also insert depend if it exsist(also we can do a couple of changes)
print(ID_list)


