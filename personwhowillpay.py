import random
# from re import split
# random_number=random.randint(0,1)
# if random_number==0:
#     print('Head')
# else:
#     print('Tail')
#now if you want something you made


# import my_module
# print(pi)


total_names=input('Enter names of everyone:')
names=total_names.split(',')
# x=len(names)
# random_names=random.randint(1,x-1)
# person_who_will_pay=names[random_names]
# print(person_who_will_pay)
person_who_will_pay=random.choice(names) #by using choice it will randomly pick one item from your list
print(person_who_will_pay)

