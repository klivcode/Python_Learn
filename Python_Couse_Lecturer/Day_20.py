#Problem 

marks=int(input("Enter the marks:"))

if marks<=100 and marks>=90:
    grade="A+"
elif marks<90 and marks>=80:
    grade="A"
elif marks<80 and marks>=70:
    grade="B"
elif marks<70 and marks>=60:
    grade="C"
elif marks<60 and marks>=40:
    grade="D"
else:
    grade="F"   
print("Your grade is:",grade)    