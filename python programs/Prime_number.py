'''A prime number is a natural number greater than 1 that has no positive divisors other than 1
and itself. In other words, a prime number is a whole number that cannot be evenly divided by
 any other whole number except 1 and itself.'''

# to find out given no is prime or not

n=int(input("Enter given no:"))
count=0                          #here we find total count of no  who divedes given no so initialies by 0
i=1                              # no starts from 1
while(i<=n):
    if(n%i==0):
        count=count+1      #here if n%10=0 hoga to ek se count increase hoga we need count 2 then condition true
    i=i+1
if(count==2):
    print("prime no")
else:
    print("composite no ")


