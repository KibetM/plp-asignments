my_list=[]
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1,15)

my_list.extend([50,60,70])
del my_list[-1]

print(my_list)

my_list.sort(reverse=True)
print(my_list)

print(my_list.index(30))