my_dict={
   1:'one',
  'Name':'Jayant',
  'Age':100,
  'Marks':50.55,
  
}

print(my_dict)

my_dict1={
  'fruits':['Banana','Apple','Oranges'],
  'category':'indian fruits',

}

print(my_dict1)
my_dict1['price']=[100,200,300]
print(my_dict1)

my_dict2={
  'name':'python',
  'version':3.9,
  'use_case':['ai','ml','ds','wd']

}
print(my_dict2)

my_dict2['version']=4.0
print(my_dict2)

del my_dict2['version']
print(my_dict2)

profile={
  'name':'raju',
  'age':100,
  'salary':25000
}

age=profile.get('age','Not found')
print(age)

keys=profile.keys()
print(list(keys))

value=profile.values()
print(list(value))

all_items=profile.items()
print(list(all_items))

popped=profile.pop('age')
print(popped)
print(profile)

pop_item=profile.popitem()
print(pop_item)
print(profile)

cleared=profile.clear()
print(profile)

# dictionary comprehension
squares={x:x*x for x in range(1,6)}
print(squares)

# nested dictionary

prog_lang={
  "python":{"name":"python","usecase":["ai","ml","webdev","ds"]},
  "java":{"name":"java","use_case":['app_dev','oops']}
}

print(prog_lang)

# loops in dict

for k in prog_lang:
  print(k)

for k in prog_lang.values():
  print(k)