def fill_set():
    _set = {}
    str = input()
    while (str!=""):
        _str = str.split()
        _set[_str[0]] = int(_str[2])
        str = input()
    return _set

math = dict()
inf = dict()
phys = dict()

count = int(input())
_list_dict = [0]*count
for i in range(count):
    _list_dict.append(fill_set())
    _list_dict[i] = fill_set()