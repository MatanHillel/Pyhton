#dictionaries

#1
cars ={
'Ford Model T' : 1908,
'Volkawagon Beetle' :1938,
'Toyota Corolla': 1966,
'Pointac Firebird': 1978,
'Chevrolet Panther': 1969
}

#2
print(cars['Ford Model T'])
#cars.get('Ford Model T')

#3
cars['Pointac Firebird']= 1977
print(cars)

#4
cars.update({'Dodge Charger' :1968 })
print(cars)

#5
cars.pop('Toyota Corolla')
print(cars)

#6
print(cars.keys())

#7
print(len(cars))

#8
print('MG Hector' in cars)

#9

earliest_car = min(cars,key=cars.get)
print(earliest_car)

#d = {'Name': 'Ram', 'Age': '19', 'Country': 'India'}
#print(list(d.items())[1][0])
#print(list(d.items())[1][1])


#10
cars['Chevrolet Camaro'] = cars.pop('Chevrolet Panther')
print(cars)



