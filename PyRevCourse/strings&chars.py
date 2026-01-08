#Strings and Characters-1.immutable

#singleline , multiline, single quote , double quote
name_1='Raju'
name_2="Raju Bhai"
name_3="""
Apple
Banana
Grapes
"""
name_4='''
lily
Rose
tulip
'''
print(name_1,name_2,name_3,name_4)

#2.string are indexed
a="python"
print(a[0]) #+ve indexing L to R
print(a[-1]) #-ve indexing R to L

#3.strings are iterable means travesed using loop
for i in a:
  print(i)

#4.len function

str="Python is HLL"
print(len(str))

#5.Slicing

print(a[0:5:2])
print(str[10:0:-1])

#6. String Replication
print(a*5)
 
#7.Concatenation
print(str+ ".")

#8.Membership(in not in)

print("HLL" in str) 
print("Sweet" in str)
print("cute" not in str)

email="apple@ggmail.com"
if '@' in email:
  print('valid email')
else:
  print('in-valid')  

#9. case conversion

print(str.lower())
print(str.upper())
print(str.capitalize())
print(str.title())
print(str.swapcase())

#10.searching and replacing method

print(str.find("HLL"))

print(str.replace("HLL","High Level Language"))

#11.Splitting and joining

splt_var="a,b,c"

splt_mthd=splt_var.split(",")#returns a list

print('after splitting',splt_mthd)

join_mthd=",".join(splt_mthd)
print(join_mthd)

#12.Checking Method

print(a.startswith('p'))
print(a.endswith('N'))
print(a.isalpha())
print(a.isdigit())
print(a.isalnum())