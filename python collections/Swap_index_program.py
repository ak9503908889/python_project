n=int(input("enter size of list:"))

list=[]
for _ in range(n):
    num=int(input())
    list.append(num)
index1=int(input("enter index1:"))
index2=int(input("enter index2:"))
print(list)

#Swapping values of index1 and index2
temp=list[index1]
list[index1]=list[index2]
list[index2]=temp
print(list)
