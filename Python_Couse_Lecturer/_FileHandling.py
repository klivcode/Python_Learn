# File Handling
#w  write
#r  read
# a  append
# x  exclusive creation
# b  binary
# t  text
# +  read and write
# with open('file.txt', 'w') as file:


# reading a file from the file folder
f=open("files/file1.txt") # path relative to the current working directory
re=f.read()
print(re)
f.close()

# witing to a file
f=open("files/file2.txt","w") # path relative to the current working directory
f.write("This is a new file created by Python")
print("File created successfully")
f.close()

