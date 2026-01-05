"""
Docstring for Introduction.operators

PEMDAS
parenthesis()->exponent**->mlt* div/->add+ sub-

arith-math calc
comparison-compare value
logical-combine
assignment-assign value
identity-object memory location
membership-value exist in sequences

"""
#Arithmetic Operator

a=20
b=10

add=a+b
print("addition",add)

sub=a-b
print("subtraction",sub)

mlt=a*b
print("multiplication",mlt)

div=a/b
print("division",div)

fdiv=a//b
print("floordivison",fdiv)

mod=a%b
print("Modulus",mod)

expo=a**b
print("exponent",expo)

#Comparison Operators

print("equal to",a==b)
print("not equal to",a!=b)
print("greater than",a>b)
print("less than",a<b)
print("greater than equal to",a>=b)
print("less than equal to",a<=b)

#logical operators
#multiple condition combine -Boolean True/False
#and- all condition must be True 

age=20
is_student=True

print(age>18 and is_student)
print(age>25 or is_student)
print(not is_student)

#Assignment Operator

print(a)

a+=5
print(a)

a-=5
print(a)

#Identity Operator-compare memory location
#is-True if same
#is not - True if not same

l1=[1,2,3]
l2=l1
l3=[1,2,3]
print(l1 is l2)
print(l1 is l3)

#Membership Operator

veggie=["Beetroot","Broccli","Zuchinni"]
print('Broccli' in veggie)
