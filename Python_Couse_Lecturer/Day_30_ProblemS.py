# n=int(input("Enter a number: "))
# product = 1
# for i in range(1,n+1):
#     product=product*i
# print("The PRODUCT OF ALL NUMBERS FROM 1 TO",n,"IS",product)


#Print stars in a pyramid pattern

n=int(input("Enter the number of rows for the pyramid: "))
for i in range(1,n+1):
    print(" "*(n-i) + "*"*(2*i-1))

#inverse pyramid pattern
for i in range(n,0,-1):
    print(" "*(n-i) + "*"*(2*i-1))