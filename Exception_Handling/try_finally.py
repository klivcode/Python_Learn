try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

else:
    print("Input was valid, no exceptions occurred.")

finally:
    print("This block always executes, regardless of exceptions.")

