my_dist = {'pakistan':'Karachi', 'usa':'new york', 'france':'london'}
# key value = 1pair
print(my_dist)
print(len(my_dist))

#acessing values via keys
print(my_dist['pakistan'])

print(my_dist.keys())
print(my_dist.values())

# print(my_dist('india')) #key error if key not define
print(my_dist.get('india'))
print(my_dist.get('usa'))