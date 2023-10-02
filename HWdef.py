#Exercise 1: Create a function in Python

def demo(name,age):
    print(f"the name is:{name}\nthe age is:{age}")

demo("matan",31)

#Exercise 2: Create a function with variable length of arguments

# call function with 3 arguments
func1  = (20, 40, 60)

# call function with 2 arguments
#func1(80, 100)

def breaking(*func):
    for i in func:
        print(i)

breaking(func1)

#Exercise 3: Return multiple values from a function

