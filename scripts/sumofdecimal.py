

class DigitCalculator:
    def __init__(self, digit):
        self.digit = digit

    def validate_input(self):
        # Check if the input is a single digit and between 0 and 9
        if not isinstance(self.digit, dec):
            raise ValueError("Input must be a decimal digit .")

    def calculate_sum(self):
        self.validate_input()
        total_sum = 0
        
        # Calculate the values X, XX, XXX, XXXX
        for i in range(1, 5):
            number = int(str(self.digit) * i)  # Create the number by repeating the digit
            total_sum += number
        
        return total_sum

# Example usage:
try:
    digit = 3  # Example input
    calculator = DigitCalculator(digit)
    result = calculator.calculate_sum()
    print(f"The result for digit {digit} is: {result}")
except ValueError as e:
    print(e)