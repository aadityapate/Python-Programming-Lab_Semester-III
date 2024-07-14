a=int(input('\nEnter Min No.: '))
b=int(input('Enter Max No.: '))
print('\n-------------------------------------------------------------')

print('\nThe No.s Divisible by 5 & are Multiple of 9 in the range are:')

for i in range(a,b+1):
  if(i%5==0 and i%9==0):
    print(i)

oddcount = 0
evencount = 0

for i in range(a,b+1):
  if not i%2:
    evencount+=1
  else:
      oddcount+=1

print('\n-----------------------------------------------')
print('\nEven No.s in range',a,'&',b,'are:',evencount)
print('\nOdd No.s in range',a,'&',b,'are:',oddcount)

print('\n-----------------------------------------------')
print("\nPrime numbers between",a, "and",b, "are:")

for n in range(a, b + 1):
  if n>1:
    for i in range(2,n):
      if (n%i)==0:
        break
    else:
      print(n)
      