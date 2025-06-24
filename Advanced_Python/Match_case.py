#Match Case is just like a switch case in c and java, but it is more powerful and flexible.

def match_case_example(value):
    match value:
        case 1:
            return "You selected option 1"
        case 2:
            return "You selected option 2"
        case 3:
            return "You selected option 3"
        case _:
            return "Invalid option"
# Example usage
if __name__ == "__main__":
    user_input = int(input("Enter a number (1-3): "))
    result = match_case_example(user_input)
    print(result)