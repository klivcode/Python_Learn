
a=55
def globall():
    global a  # Declare 'a' as global to modify the global variable
    print(f"Global a: {a}")
    a=10
    print(f"Local a: {a}")

# global keyword allows to modify the global variable with local variable
globall()
print(f"Global a after function call: {a}")