#lesson 2

#1
name= "matan hillel"

print(name[0].upper()+name[1:name.index(" ")+1].lower()+name[name.index(" ")+1].upper()
      +name[name.index(" ")+2:].lower())

print(name.title())

#2
age=30

print('my name is {} and i am {} years old.'.format(name,age))

#3
#done

#4
#done


#Lists Home Work

#1
southpark = ["cartmen","kyle","Kenny","sten"]

#2
places = ["tel aviv","shoham","london","rishon le zion"]
southpark.extend(places)
print(southpark)

#3
a_list=[2,4,6,8,10]
a_list.insert(2,5)
print(a_list)

#4
a_list.pop()
print(a_list)

#5
l2=[3,6,7,9]
a_list.extend(l2)
print(a_list)

#6
a_list.remove(6)
print(a_list)

#7
list1 = [1,2,3,4,5,6,7,8,9]
list2 = list1[1::2]
print(list2)

#8
years = [2000, 1987, 2010, 1786, 2100]
#sort_years = years.sort()
sort_years = sorted(years)
print(sort_years)

#years = [2000, 1987, 2010, 1786, 2100]
#years.sort()
#print(years)
#years_sort=years[::-1]
#print(years_sort)

#9
up_years = sort_years[::-1]
secound_top_year = up_years[1]
print(secound_top_year)

#10
sort_years.pop(0)
print(sort_years)

