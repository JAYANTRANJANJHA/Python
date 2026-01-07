num_1=float(input('Enter Number 1 = '))
num_2=float(input('Enter Number 2 = '))
choice=input('Enter your choice + - * / // % ** = ')

if choice == '+':
  print(f'Addition:{num_1+num_2}')

elif choice == '-':
  print(f'Subtraction:{num_1-num_2}')

elif choice == '*':
  print(f'Multiply:{num_1*num_2}')

elif choice == '/':
  print(f'Divison:{num_1/num_2}')  

elif choice == '//':
  print(f'Floor Division:{num_1//num_2}')  

elif choice == '%':
  print(f'Modulo:{num_1%num_2}') 

elif choice == '**':
  print(f'Exponentiation:{num_1**num_2}')   

else:
  print("Invalid Choice")  