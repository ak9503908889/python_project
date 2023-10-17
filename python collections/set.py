# creating a set
names={"amit","mohit","priyanka"}
print(names)

#chek length of set
print(len(names))

#chek datatype of set
print(type(names))

#Acessing the items in set
for x in names:
    print(x)
 # chek if item exist in set
if "amit" in names:
    print("amit is in the set")

    # add elements in the set
    names.add("megha")
    print(names)

# add another sequence in the set
names_list=["ria","kia"]
names.update(names_list)
print(names)

#removing elements from a set
names.remove("ria")
print(names)

names.discard("ria") # this function will not set error if value is not present in the set
print(names)

#joining of two sets
s1={'a','b','c'}
s2={'x','b','z'}
print(s1,s2)

s3=s1.union(s2)
print(s3)

s1.update(s2)
print(s1)

#keep only duplicate values while joining
s1.intersection_update(s2)
print(s1)

#keep all values except duplicates
s1.symmetric_difference_update(s2)
print(s1)