name = 'python '
#displaying lengthe of a string
print(len(name))

#Indexing in strings
print(name[0]) 
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

#string slice
print(name[0:2])
print(name[0:3])
print(name[0:4])
print(name[0:5])
print(name[0:6])
print(name[1:5])

print(name[:len(name)])

#step size 
print(name[0:6:2]) #output : python
print(name[0:6:3]) #output : python
print(name[0:2:4]) #output : python
print(name[::-1]) #output : python
print(name[6:0:2]) #output : python
print(name[0:1:4]) #output : python
print(name[0:2:-1]) #output : python
print(name[6:1:-1]) #output : python