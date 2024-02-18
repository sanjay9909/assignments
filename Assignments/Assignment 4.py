name = "some name"

print(name.upper())


print(name.lower())

print(name.capitalize())

print(name.replace('e', 'E'))

# -------------------------------------------------------------------

l = [1, 2, 3]

l.extend([5, 6, 7])

print(l)

l.remove(6)

print(l)

# ---------------------------------------------------------------
d = {'mango': 10, 'banana': 0, 'apple': 15, 'orange': 0, 'pineapple': 20}

out_of_stock = [fruit for fruit, stock in d.items() if stock == 0]

for fruit in out_of_stock:
    del d[fruit]

d['mango'] = 15
d['pineapple'] -= 5

print(d)

#-------------------------------------------------------------

# For list
my_list = [1, 2, 3, 4, 5]
my_list.pop()  
print("List after pop:", my_list)

# For dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.pop('b')  
print("Dictionary after pop:", my_dict)

# For set
my_set = {1, 2, 3, 4, 5}
my_set.remove(3) 
print("Set after remove:", my_set)