# 1.square shape * pattern:
rows=int(input("enter no.of rows:"))         # * * * *
columns=int(input("enter no.of columns:"))   # * * * *
for r in range (rows):                       # * * * *
    for c in range(columns):                 # * * * *
        print("*",end=" ")
    print()
    
#string reputation:
n=4
for i in range(n):
    print("*"*n)

# 2.* * * *
#   *     *      HALLOW SQUARE:
#   *     *
#   * * * *

for r in range(4):
    for c in range (4):
        if r==0 or r==3 or c==0 or c==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#3. X diagonal pattern
for r in range(5):
    for c in range(5):              #    *       *
        if r==c or r+c==4:          #      *   *       
            print("*",end=" ")      #        *
        else:                       #      *   *
            print(" ",end=" ")      #    *       *
    print()

#4.
n=4                                 #1 1 1 1
for r in range(1,n+1):              #2 2 2 2
    for c in range(1,n+1):          #3 3 3 3
        print(r,end=" ")            #4 4 4 4
    print()
#5.
n=4
for r in range(1,n+1):              #1 2 3 4
    for c in range(1,n+1):          #1 2 3 4
        print(c,end=" ")            #1 2 3 4
    print()                         #1 2 3 4



#
for r in range(4):                        #2  4  6  8
    for c in range(4):                    #1  3  5  7
        if r%2==0:                        #10 12 14 16
            print(r*4+(c+1)*2,end=" ")    #9  11 13 15
        else:
            print(r*4+(c*2)-3,end=" ")
    print()

even=2
odd=1
for i in range(4):
    for j in range(4):
        if i%2==0:
            print(odd,end=" ")
            odd+=2
        else:
            print(even,end=" ")
            even+=2
    print()
    
#6.right angle triangle:
#a.
for i in range(1,5):
    for j in range(i):
        print("*",end=" ")
    print()                            # *
#b.                                    # * *      
for i in range(1,5):                   # * * *
    for j in range(1,5):               # * * * *
        if i>=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#7. 
n=1                                   #1
for i in range(1,5):                  #2 3
    for j in range(i):                #4 5 6
        print(n,end=" ")              #7 8 9 10
        n+=1
    print()
#8.
for i in range(1,5):               #0
    for j in range(i):             #0 1
        print(j,end=" ")           #0 1 2
    print()                        #0 1 2 3 
#9.
for i in range(1,5):               #1
    for j in range(i):             #2 2
        print(i,end=" ")           #3 3 3
    print()                        #4 4 4 4

#10.
#a.
n=4
for i in range(4):                # * * * *
    for j in range(n-i):          # * * *
        print("*",end=" ")        # * *
    print()                       # *
#b.
n=4
for i in range(1,5):
    for j in range(1,5):
        if i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#11.
n=3
for i in range(n):
    #space:                         
    for j in range(n-i-1):    #        *
        print(" ",end=" ")    #     *  *  *
 #stars                       #  *  *  *  *  *
    for j in range(2*i+1):
        print("*",end=" ")
    print()
#12.
n=5
for i in range(n):                    # *  *  *  *  *  
    for j in range(i):                #    *  *  *
        print(" ",end=" ")            #       *
    for j in range(2*n-(2*i+1)):
            print("*",end=" ")
    print()

n=5
for i in range(n):
    #space:                         
    for j in range(n-i-1):    #            *
        print(" ",end=" ")    #         *  *  *
 #stars                       #      *  *  *  *  *
    for j in range(2*i+1):    #   *  *  *  *  *  *  *
        print("*",end=" ")    #      *  *  *  *  * 
    print()                   #         *  *  *
n=4                           #            *
for i in range(n):
    
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(2*n-(2*i+1)):
            print("*",end=" ")
    print()