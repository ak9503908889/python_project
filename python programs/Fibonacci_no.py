'''The Fibonacci series is a sequence of numbers in which each number is the sum of the two
 preceding ones. It starts with two initial terms: 0 and 1. After these initial terms,
  each subsequent term is obtained by adding the two immediately preceding numbers in
  the sequence. The Fibonacci sequence is often denoted as "F(n)" and can be defined as follows:

F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) for n > 1

Here are the first few terms of the Fibonacci series:

F(0) = 0
F(1) = 1
F(2) = F(1) + F(0) = 1 + 0 = 1
F(3) = F(2) + F(1) = 1 + 1 = 2
F(4) = F(3) + F(2) = 2 + 1 = 3'''

'''# program to print fiboncci sequence

no=int(input("enter the no till what u want the series : "))
a=0
b=1
c=0  #here initialised by 0
print(a)
print(b)
i=1
while(i<no):
    c=a+b
    a=b   # swap the no
    b=c   #swap the no
    print(c)
    i=i+1
'''

#same program in another way
n=int(input("enter no :"))
x=0
y=1
z=0     #starting ko 0 se initilised kiya hai
while(z<=n):
    print(z, end=' ')    # by using end=' ' u can print result on same line
    x=y      # swap the value
    y=z
    z=x+y

