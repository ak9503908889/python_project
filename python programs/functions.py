#function is a block of reusable code that perform a specific task.
# to find the sum of nth number to given by user

n=int(input("enter given no "))
sum=0
for i in range (1,n+1):
    sum+=i
print("sum of all no till n is: ",sum)