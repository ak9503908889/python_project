'''A factorial number, often denoted as "n!" (pronounced as "n factorial"), is a mathematical concept
 used to represent the product of all positive integers from 1 to a given positive integer "n."
 In other words, the factorial of a non-negative integer "n" is calculated by multiplying all the
 integers from 1 to "n" together.

The factorial of "n" is defined as:

n! = 1 × 2 × 3 × 4 × ... × (n-1) × n'''

# find factorial of given number
i=int(input("Enter any no: "))
fac=1
while(i>0):
    fac=fac*i
    i=i-1
print("factorial of no is: ",fac)
