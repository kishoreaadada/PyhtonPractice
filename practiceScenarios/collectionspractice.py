from functools import reduce

#Python lists are mutable and resizable
num_2_11 = list(range(2, 12))
print(num_2_11)
num_2_11[2] = 100
num_2_11.insert(4, 100)
print(num_2_11)

#Python tuples immutable and non resizable
inst_name = ("Inceptez", "Technologies", "Pvt", "Ltd.")
inst = (inst_name[1], inst_name[3])
print(inst)
#inst_name[2] = "public"
#inst_name.insert(4, "test")
print(len(inst_name))

tup_list = [("Inceptez", "Technologies"), ("Apple", "Incorporation")]
print(tup_list)
dict_list = []
for tup in tup_list:
    dict_list.append({tup[0]: tup[1]})
print(dict_list[0]['Inceptez'])
print(dict_list[0].get('Inceptez'))

lst=[("Inceptez","Technologies"),("Apple","Incorporation"),
     ("Inceptez","Technologies"),("Inceptez","Technologies")]
lst = list(set(lst))
print(lst)
lst.append(('Intel', 'Corp'))
print(lst)
lst1=[]
for dl in dict_list:
    lst1.append(list(dl.keys())[0])
print(lst1)

lst = [10, 20, 40, 30, 20]
print(lst[0], lst[-1])
lst.sort()
print('min value: {}, max value: {}'.format(lst[0], lst[-1]))
lst.sort(reverse=True)
print('max value: {}, min value: {}'.format(lst[0], lst[-1]))
print('sum of values in list: {}'.format(reduce(lambda x, y: x+y, lst)))
lst.remove(30)
lst.remove(20)
print(lst)

tup = (10, 20, 40, 30, 20)
print(tup)
print(tup[0], tup[-1])
lst_tup = list(tup)
lst_tup.sort()
tup = tuple(lst_tup)
print(tup)
print('min in tuple: {}, max in tuple: {}'.format(tup[0], tup[-1]))
lst_tup.sort(reverse=True)
tup = tuple(lst_tup)
print('max in tuple: {}, min in tuple: {}'.format(tup[0], tup[-1]))

str1 = "Inceptez Technologies Pvt Ltd"
lst_str1 = str1.split(' ')
print(lst_str1)

emplstlst = [["1", ("Arun", "Kumar"), "10000"], ["2", ("Bala", "Mohan"), "12000"]]
print(tuple(emplstlst[0]))
print(emplstlst[1][1][::-1])
emptuptup = []
for i in emplstlst:
    emptuptup.append(tuple(i))
print(tuple(emptuptup))
print(reduce(lambda x, y: x+y, map(lambda x: int(x[2]), emplstlst)))
