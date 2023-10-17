input_string=input("enter string: ")
n  =  int(input("enter n: "))

#creating dictionary for mirror operation

alphabets="abcdefghijklmnopqrstuvwxyz"
reverse_alphabets= alphabets[::-1]
dict1=dict(zip(alphabets,reverse_alphabets)) # by using zip we create cob=mbination of two string

# finding the part of string on which we will do mirror operation
prefix=input_string  [0:n-1]
suffix=input_string [n-1:]

#finding the mirror string
mirror=" "
for i in range(0,len(suffix)):
    mirror=mirror+dict1[suffix[i]]

# creating the final string
result=prefix+mirror
print("the result is: ",result)
