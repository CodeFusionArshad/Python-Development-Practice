str1 = 'introduction tO python programing'
print(len(str1))

# capitilizing whole string 
print(str1.upper())

#lowers the case of the whole string
print(str1.lower())

# returns the title case
print(str1.title())


#string multipilication/ repeat
str2 = ' hello'
print(str2 * 10)

# string concatenation
print(str1 + str2)

# using 'sep' in print
print(str1, str2, sep =":")

#using 'end' in print
print(str1, end = str2)

#
print(str1.capitalize())

print(str1.split())

splitted = str1.split()
print(splitted) #splitted string 

joined = " ".join(splitted) #joining the splitted string 
print(joined)

print(str1.count('p'))
