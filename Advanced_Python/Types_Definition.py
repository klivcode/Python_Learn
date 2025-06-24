# Types of Variables in Python

from typing import List, Tuple, Dict, Any, Union

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Tuple of integers
coordinates: Tuple[int, int] = (10, 20)
# Dictionary with string keys and integer values
person: Dict[str, int] = {"age": 30, "height": 175, "weight": 70}
# Union type that can be either an integer or a string
ValueType = Union[int, str]
# Example usage of the defined types
value: ValueType = 42  # This can also be a string, e.g., "Hello"

n: int = 10

name : str = "Klivcode"

def sum (a:int, b:int) -> int:
    return a + b
a = sum(5, 10)
print(a)
