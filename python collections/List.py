fruits=["apple","banana","kiwi","cucumber"] #create a list

print(fruits)   # print a list

print(type(fruits)) # chek type of list

print(len(fruits)) #chek length of list

# cheking if an item is present in the list
if "apple" in fruits :
    print("apple is part of of the list")

 # checking if the item is not present in the list
    if "mango" not in fruits:
     print("mango is not part of the the list")

 #indexing in list
print(fruits[1]) # banana
print(fruits[-2]) # kiwi

print(fruits[0:2]) # apple,banana
print(fruits[1:3]) #banana,kiwi
print(fruits[-3:-1]) #banana,kiwi

#adding elements in the list
fruits.append("mango")
print(fruits)

fruits.insert(2,"cherry")
print(fruits)

more_fruits=["papya","santra"]
fruits.extend(more_fruits)
print(fruits)

#removing elements in the list
fruits.remove("apple") # specified name itam removed
fruits.pop(1) # at index 1 item will be removed
fruits.pop()# last index item will remove

#changing or updating the list item
fruits[1]="coconut"
print(fruits)
fruits[1:3]=["coconut2"]
print(fruits)

# Sorting in a list
fruits.sort()#by default ascending order
fruits.sort(reverse=True) # Descending order
print(fruits)
fruits.reverse()
print(fruits)

#list comprehension--when we want to make a new list from items of an existing list
new_fruit=[fruit for fruit in fruits if "a" in fruit]
print(new_fruit)

#copy a list
new_fruit=fruits.copy()
print(new_fruit)

#nested list
fruits.insert(2,["ak","bk"])
print(fruits)
print(fruits[2][1])# bk will get
print(fruits[2][0]) # ak will get

input=[[1,2],[3,4],[5,6],[7,8]]
#ans=[1,2,3,4,5,6,7,8]
#input=[item for sublist in input for item in sublist]
#print(input)
flat_list=[]
for i in input:
    for j in i:
          flat_list.append(j)
print(flat_list)
