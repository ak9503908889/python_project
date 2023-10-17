n=int(input("enter any no:"))

for i in range (1,n+1):  #loop for rows
    #print spaces
    print(" "*(n-i),end=" ")

    #printing digits
    for j in range (1,2*i):
        print(j,end=" ")
    print()

'''
ans :
      1 
    1 2 3 
   1 2 3 4 5 
  1 2 3 4 5 6 7 
 1 2 3 4 5 6 7 8 9
'''