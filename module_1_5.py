Mutable_list = [1,2,'a','b', 'Modified']
print(Mutable_list)
print(Mutable_list[2:4])
Mutable_list[2] = 3
Mutable_list[3] = 4
print(Mutable_list)

Immutable_var = tuple([1,2,'a','b'])
print(Immutable_var)
Immutable_var[2] = 3
#'Tuple' object does not support item assignment (Объект «Кортеж» не поддерживает присвоение значений элементам)