
input_tuple=(1,2,3,4,5,6,7)
list=[]    #make empty list

 # adding reversed values in list
for x in reversed(input_tuple):
    list.append(x)
ouput_tuple =tuple(list)  # typcasting list into tuple
print(ouput_tuple)


