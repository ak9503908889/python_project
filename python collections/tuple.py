# creating a tuple
colours=("yellow","green","red")
#creating a tuple with one item
fruit=("apple",)
fruit=tuple(("apple"))

#chek the type of tuple
print(type(fruit))
#chek the length of the tuple
print(len(colours))
#Accessing items in tuple
print(colours[1]) #positive indexing
print(colours[-1]) #negative indexing
print(colours[1:3]) #range indexing
print(colours[-2:]) #negative range indexing

#chek if item exits in tuple
if"green" in colours:
    print("green is part of a tuple")

# traverse the tuple
for i in colours:
    print(i) #In Python, "traversing a tuple" typically means iterating or going
             # through each element in the tuple, one by one, in order to perform some
               # operation or access the elements within it. Tuples are ordered
               # collections of items, and you can access their elements using indexing
                   # or by using a loop to go through each element.

#cocatenate two tuple
more_colours = ("blue","pink")
colours= colours + more_colours
print(colours)

#unpacking a tuple
days=("sunday","monday","tuesday")
sunday,monday,tuesday=days
print(sunday,monday,tuesday)