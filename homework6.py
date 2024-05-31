#my_disk={'a':1,'b':2,'c':3}
#my_disk.update({'d':4,'e':5})
#del my_disk['4']
#print(my_disk)
#print(my_disk['a'])
#print(my_disk.get('e'))

my_set={1,1,23,'hello',56,4,5,4,23,56,(1,2,3)}
my_set=(set(my_set))
my_set.update({44,55})
my_set.remove(56)
print(my_set)