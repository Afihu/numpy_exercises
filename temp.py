import numpy as np

# Define two arrays for demonstration
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# Element-wise Addition
addition = a + b

# Element-wise Subtraction
subtraction = a - b

# Element-wise Multiplication
multiplication = a * b

# Element-wise Division
division = a / b

# Element-wise Floor Division
floor_division = a // b

# Element-wise Modulus
modulus = a % b

# Element-wise Power
power = a ** b

# Element-wise Logical AND (for demonstration, using boolean arrays)
c = np.array([True, False, True, False])
d = np.array([False, False, True, True])
logical_and = c & d

# Element-wise Logical OR
logical_or = c | d

# Element-wise Logical XOR
logical_xor = c ^ d

# Element-wise Logical NOT
logical_not = ~c

# Print results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Floor Division:", floor_division)
print("Modulus:", modulus)
print("Power:", power)
print("Logical AND:", logical_and)
print("Logical OR:", logical_or)
print("Logical XOR:", logical_xor)
print("Logical NOT:", logical_not)