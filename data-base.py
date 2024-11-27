#python datatypes
a = 10 #this is an integer"
b = 'python' #this is an string"
c = True #this is an boolean"
d = 5.43 #this is an float"
e = complex(2,3) #this is an complex"

print(a)
print(type(a))

print(b)
print(type(b))

print(c)
print(type(c))


print(d)
print(type(d))

print(e)
print(type(e))

type_casted = int(d) #change form 5.43 to 5
type_casted2 = float(a) #change from 10 to 10.00
type_casted3 = str(a) #change interger 10 to string 10
type_casted4 = int(d) #change 'python' to integer
print(type_casted)
print(type_casted2)
print(type_casted3)
print(type_casted4)
print(type(type_casted3))
print(type_casted3)
#string concatenation    
print(b + b)