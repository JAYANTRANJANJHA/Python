# loops help to run a code multiple times
#1- While Loop
#2- For Loop

print("while loop")
i=1 
while i<=5:
  print(i)
  i+=1

print("for loop")

a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
  print(i)

#range
b=list(range(10,0,-1))
print(b)

#nested loops

for i in range(1,3):
  for j in range(3,6):
    print(i,j)

#break statement

for num in range(1,10,1):
  if num ==7:
    break
  print(num) 

#continue

for num in range(1,10,1):
  if num ==7:
    continue
  print(num) 

#pass 

for num in range(1,10,1):
  if num ==7:
    pass
  print(num) 
          