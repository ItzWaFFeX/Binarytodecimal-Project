def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def decimal_to_binary(decimal_num):
    return bin(decimal_num)[2:]

def binary_operations(bin1, bin2):
    num1 = binary_to_decimal(bin1)
    num2 = binary_to_decimal(bin2)
    
    addition = decimal_to_binary(num1 + num2)
    subtraction = decimal_to_binary(num1 - num2)
    multiplication = decimal_to_binary(num1 * num2)
    division = decimal_to_binary(num1 // num2)
    
    return addition, subtraction, multiplication, division

# Example usage
binary1 = "1011"  # 11 in decimal
binary2 = "1101"  # 13 in decimal

addition, subtraction, multiplication, division = binary_operations(binary1, binary2)

# Print results
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
