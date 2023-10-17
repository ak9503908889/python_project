n=int(input("enter any no:"))

for i in range (1,n+1):  #loop for rows
    for j in range (1,i+1): #loop for columns
        print(j,end=" ")
    print()


    '''
    ans :
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 '''