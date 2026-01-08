#even numbers

for i in range (1,11):
  if i%2==0:
    print('even',i)
  else:
    print('odd',i)  

#
start=int(input('Enter Start='))
stop=int(input('Enter Stop= ')) 
skip=int(input('Number you want to skip = '))

if start<stop:
  for i in range(start,stop+1):
     if i==skip:
       continue
     print(i)
    
else:
  print("Enter a valid range ofvalues")