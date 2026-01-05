"""
Docstring for Introduction.data_types

numeric types
int-whole numbers 100 200 -1000

float-decimal numbers
complex- real & imaginary part
a+bi
3+4j

"""
a=10
b=10.20
c=3+4j
print(a,b,c)

print(type(a),type(b),type(c))

"""
Boolean-logical operation
True/False

"""
is_raining=True
is_sunny=False
print(is_raining,is_sunny)

#none type
result=None
print(result)


#sequence- string,list,tuple

text_str="this is a string , i am a sequence of chars"

print(type(text_str))


#list

my_list=['data1','data2','data3']
print(my_list)
print(type(my_list))

#tuple

my_tuple=('data1','data2','data3','data4')

#set

unique_numbers={1,2,3,4,5,5,6,6,7}
print(unique_numbers)

immutable_set=frozenset([1,1,2,3,4,5,8,8])
print(immutable_set)


#mapping data types -dictionary -> key -value pair

person={
  'name':'gopal','age':100, 'mobile':9889973750083
}

print(person)





