f=open("files/file1.txt","a") # path relative to the current working directory
with f as file:
    print(file.write("Python is a programming language and it is used for web development, data science, machine learning, and many other fields.\n"))
    print(file.write("Python is a high-level, interpreted language that is known for its simplicity and readability.\n"))