# Словари
my_dict = {'Masha': 2000, 'Egor': 1995, 'Vasya': 1967}
print(my_dict)
print(my_dict.get('Vasya')) #существующий ключ
print(my_dict.get('Oleg')) #отсутствующий ключ
my_dict.update({'Kamila': 1981, 'Artem': 1915})
print(my_dict)
print(my_dict.get('Egor'))
del my_dict['Egor']
print(my_dict)

# Множества
my_set = {3,3,3, 'Груша', 5.75, 'Груша'}
print(my_set)
# вариант №1
my_set.update([99, (13,26,3.14)])
print(my_set)
# вариант №2
list_ = [99, (13,26,3.14)]
print(set(list_))
print(my_set.union(list_))
# или так
my_set_2 = my_set.union(list_)
print(my_set_2)

my_set.discard('Груша')
print(my_set)
my_set.remove(5.75)
print(my_set)
print(list_.pop()) # удаляет случайный компонент множества
# или так
my_set_2.pop()
print(my_set_2)

