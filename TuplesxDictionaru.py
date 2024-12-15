my_dict = {'name': 'Josh', 'age': '1000'}

print(my_dict['name'])
print(my_dict['age'])

my_dict['age'] = 100
print(my_dict)

my_dict['address'] = 'Neverland'
print(my_dict)

my_dict.pop('age')
print(my_dict)

print("Address :", my_dict.get('address'))

my_dict.clear()
print(my_dict)

