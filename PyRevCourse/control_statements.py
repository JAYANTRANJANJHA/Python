"""
Docstring for PyRevCourse.control_statements

normally-top to bottom approach

conditional-if,elif,else
for while else suite
nested
infinite loop
pass
continue
break
assert return

"""


"""
pi=3.147
radius=float(input('enter radius='))
area_of_circle=pi*radius*radius
print(f'Area  of Circle:{area_of_circle}')
"""
age=int(input("Enter Your age to check voting eligibilty: "))

if(age>=18):
  print("You can vote")
  if(age>80):
    print("Now you can vote from home or get free cab to pooling booth")
elif(age<18 and age >=1):
  print("You are Minor Not Eligble to vote")  
else:
  print("Invalid Input")


