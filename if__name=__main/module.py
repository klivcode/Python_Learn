def myFunc():
    print("This is myFunc from module.py")

myFunc()

if __name__ == "__main__":
    #if this code is directly executed by running the file its present in
   myFunc()
   print(__name__)
