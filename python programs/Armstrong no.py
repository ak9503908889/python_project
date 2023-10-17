#To find given no is Armstrong no or not
#An Armstrong number (also known as a narcissistic number) is a number that is equal
# to the sum of its own digits each raised to the power of the number of digits. For example,
# 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.

n = int(input("Enter the number\n"))
sum = 0
order = len(str(n)) # given no ki order or power milate supose no is 121 then order is  3
copy_n = n
while(n>0):
    digit = n%10   # no ka conversion  single digit me kiya
    sum += digit**order       # yaha pe digit rest to power addition hotey
    n= n//10               # no ko ham decrese krate hai 
if(sum == copy_n):
    print(f"{copy_n} is Armstrong no")
else:
    print(f"{copy_n} is not an Armstrong no")


''' DRY RUN
Let's take an example number, say n = 153, and we want to check if it's an Armstrong number.

Initialization:

n is initially 153.
sum is initialized to 0.
order is the number of digits in n, which is 3.
First Iteration:

digit = n % 10 → digit = 153 % 10 → digit = 3
sum += digit ** order → sum = 0 + 3 ** 3 → sum = 27
n = n // 10 → n = 153 // 10 → n = 15
Second Iteration:

digit = n % 10 → digit = 15 % 10 → digit = 5
sum += digit ** order → sum = 27 + 5 ** 3 → sum = 152
n = n // 10 → n = 15 // 10 → n = 1
Third Iteration:

digit = n % 10 → digit = 1 % 10 → digit = 1
sum += digit ** order → sum = 152 + 1 ** 3 → sum = 153
n = n // 10 → n = 1 // 10 → n = 0
Termination:
The loop terminates because n is now 0.

After the loop finishes, sum is 153, which is the same as the original number n (153). 
This means that 153 is an Armstrong number, as 1^3 + 5^3 + 3^3 = 153.

The logic behind the code is that it extracts each digit from right to left,
raises it to the power of the total number of digits, and accumulates the result in the sum variable. 
If the final sum is equal to the original number n, then the number is an Armstrong number.
'''


