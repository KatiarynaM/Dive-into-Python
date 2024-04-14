"""Дан список повторяющихся элементов. Вернуть список с дублирующимися
элементами. В результирующем списке не должно быть дубликатов."""


my_list = [1, 1, 3, 1, 2, 3, 7, 8, 1, 5, 4, 7, 7, 8, 9, 9, 10]

dic = {}
for item in my_list:
      dic[item] = my_list.count(item)

print(dic)

new_list = []
for k, v in dic.items():
      if v > 1:
            if k not in new_list:
                  new_list.append(k)

print(new_list)
            