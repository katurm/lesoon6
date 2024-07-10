my_dict = {'Nikita': 2007, 'Ivan': 2001, 'Anton': 1999, }
print(my_dict)
print(my_dict['Nikita'])
my_dict.update({'Egor': 2000, 'Ira': 2009})
a = my_dict.pop('Anton')
print(a)
print(my_dict.get('Ivan'))
print(my_dict)
my_set = {1, 1, 2, 3, 3, 'Nikita', True}
print(my_set)
my_set.update({5, 6,})
my_set.discard(2)
print(my_set)