# empty dictionary
my_dict = {}



# dictionary with integer keys
mu_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}


my_dict = {'name': 'Jack', 'age': 26}


# Output: Jack
print(my_dict['name'])
print(my_dict.get('age'))


#update value
my_dict['age'] = 18
print(my_dict)


#add item
my_dict['address'] = 'Downtown'
print(my_dict)

# remove particular element
mu_dict.clear()
print("my-dict")