#writing a program to calculate sum of 1 to n

def sumof_oneto_n(n):
    sum=0
    for i in range (1,n+1):
        sum+=i
    return sum

n=int(input("enter no: "))

#call the function
output=sumof_oneto_n(n)
print("sum of all no till n is: ", output)
