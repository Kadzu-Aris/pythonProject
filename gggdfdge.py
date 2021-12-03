def fill_set():
    _set = {}
    str = input()
    while (str!=""):
        _str = str.split()
        _set[_str[0]+ ' ' + _str[1]] = int(_str[2])
        str = input()
    return _set

math = dict()
inf = dict()
phys = dict()

count = int(input())
_list_dict = [0]*count
for i in range(0,count):
    _list_dict[i] = fill_set()
for k in _list_dict:
    print(k)