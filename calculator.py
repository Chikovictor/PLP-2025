  
def calculator(nums, op):
    try:
        num1, num2 = map(float, nums.split())
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            if num2 == 0:
                return "Error: Division by zero"
            return num1 / num2
        else:
            return "Error: Invalid operator"
    except ValueError:
        return "Error: Invalid input"
    
# Example usage:
if __name__ == "__main__":
    nums = input("Enter two numbers separated by space: ")
    op = input("Enter an operator (+, -, *, /): ")
    result = calculator(nums, op)
    print("Result:", result)