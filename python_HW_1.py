# 1) Создать переменную типа String
_str = 's'
# empty_str = str()

# 2) Создать переменную типа Integer
empty_int = int()

# 3) Создать переменную типа Float
empty_float = float()

# 4) Создать переменную типа Bytes
empty_bytes = b''
# empty_bytes_2 = bytes()

# 5) Создать переменную типа List
empty_list = []
# empty_list_2 = list()

# 6) Создать переменную типа Tuple
empty_tuple = ()
# empty_tuple_2 = tuple()

# 7) Создать переменную типа Set
empty_set = {''}
# empty_set_2 = set()

# 8) Создать переменную типа Frozenset
empty_frozenset = frozenset()

# 9) Создать переменную типа Dict
empty_dict = {}
# empty_dict_2 = dict()

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных
print(_str, type(_str), empty_int, type(empty_int), empty_float, type(empty_float),
      empty_bytes, type(empty_bytes), empty_list, type(empty_list), empty_tuple, type(empty_tuple),
      empty_set, type(empty_set), empty_frozenset, type(empty_frozenset), empty_dict, type(empty_dict))

# 11) Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль
str1 = 'str'
str2 = 'ing'
result = str1 + str2
print(result)

# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
_str = 's'
_int = 1
print(_str, _int)

# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
_str = 's'
_int = 1
print(_str + str(_int))