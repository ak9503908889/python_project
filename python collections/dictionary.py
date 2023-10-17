#crating the dictionry
phones={ "amit":95039088,
         "priya":9523658,
         "amruta":45258
       }
#printing the dictionary
'''print(phones)

# checking the the type of the dictionary
print(type(phones))

#chek the length og dictionry
print(len(phones))

# access the itms of dictionsry
print(phones["amit"])
print(phones.get("amit"))

#print all keys in the given dictionary
print(phones.keys())

# update value in dict
phones["amit"]=858585
print(phones)

# add elements in dict
phones["bk"]=757575
print(phones)

# if u want to add more sequence in dict
more_phones={
    "sham":1111
}
phones.update(more_phones)
print(phones)

# remove element in dic
phones.pop("bk")
print(phones)

phones.popitem() # this will remove last added item
print(phones)

phones.clear() # if we want to make empty the dictionary
print(phones)

# printing values of dictionary
for x in phones:
    print(x) # it will give keys all
    print(phones[x]) # it will give all values in dictionry'''

 # if you want all keys and values in seperte form
for x in phones.items():
    print(x)

 # nested dictionary means one or more dic in one dictinary added .
phones={
     "area1":{
         "x":1,
         "y":2,
         "z":3
     },
     "area2":{
         "a":5,
         "b":12,
         "c":20
     }
 }
print(phones["area1"]["y"])