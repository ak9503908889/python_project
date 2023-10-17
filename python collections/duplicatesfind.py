l1=[1,5,8,12,6]
l2=[4,5,10,8,9]
l3=[5,56,89,45,8]

#if u want to find the duplictes in the abov all list
#first need to converted into set by using type casting

s1=set(l1)
s2=set(l2)
s3=set(l3)
#join using intersection
s1s2=s1.intersection(s2)
final_set=s1s2.intersection(s3)

final_list=list(final_set)
print(final_list)

