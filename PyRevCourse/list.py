#List
#ordered
#mutable
#dynamic
#hetrogeneous

#1-square brackets
my_list=[1,2,3,4,10.56,"hello",True]

print(my_list)

#2- using list constructor
my_list0=list((1,2,3,4,6,"hello"))
print(my_list0)

lst=[1,2,3,4,5]
print(f'Before list:{lst}')
lst[0]="Hello"
print(f'After list:{lst}')

lst[1:4]="How","are","you"
print(lst)

lst_1=[1,2,3,4,5]
lst_2=[6,7,8,9,10]
concatrslt=lst_1+lst_2
print(concatrslt)


reptlst=lst_1*2
print(reptlst)


"""check=int(input('Enter a number to check = '))
if check in lst_1:
  print('Found')
else:
  print('Not Found')  """

a=[1,2,3]
a.append(4)
print(a) 

b=[4,5,6]
a.extend(b)
print(a)

a.insert(0,"Hi")
print(a)

print(a.index("Hi"))

print(a.count(4))

print(min(lst_1))
print(max(lst_2))

print(a.reverse())

a_copy=a.copy()
print(a_copy)

a.remove(6) #direct data input
print(a)

a.pop(1) #index
print(a)

a.clear()
print(a)

a1=[1,2,3,4,56,70,89,7,7,6,8,3,6,3,4]
b1=[2,4,5,6,87,8,7,21,20,3,1]

s1=set(a1)
s2=set(b1)

s3=s1.intersection(s2)
print(list(s3))

lst_rng=list(range(1,110,10))
print(lst_rng)

nstd_lst=[4,5,6,[7,8,9],[10,11,12]]
print(nstd_lst)

#list comprehension




