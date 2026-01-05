"""
Docstring for Introduction.operators

PEMDAS
parenthesis()->exponent**->mlt* div/->add+ sub-


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


