# try with else
# when the try is successful, the else block is executed
try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError as v:
    print(f"Invalid input: {v}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

else:
    print("Input was valid, no exceptions occurred.")
