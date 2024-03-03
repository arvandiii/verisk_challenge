import sys
from decimal import Decimal, InvalidOperation

def validate_argument(arg, name):
    """Validate that an argument is within the specified range."""
    try:
        value = Decimal(arg)
    except InvalidOperation:
        sys.exit(f"Error: {name} must be a valid decimal number.")

    if not (Decimal('0.0') <= value <= Decimal('1_000_000_000.0')):
        sys.exit(f"Error: {name} must be between 0.0 and 1,000,000,000.0 inclusive.")
    return value

def process_input(threshold, limit, numbers):
    output_numbers = []
    cumulative_sum = Decimal('0.0')

    for number in numbers:
        # Transform the input number based on the threshold
        transformed_number = max(Decimal('0.0'), number - threshold)

        # Check if adding this number would exceed the limit
        if cumulative_sum + transformed_number > limit:
            transformed_number = max(Decimal('0.0'), limit - cumulative_sum)
        
        # Add the transformed number to the output list and update the cumulative sum
        output_numbers.append(transformed_number)
        cumulative_sum += transformed_number

    # Add the cumulative sum as the last output value
    output_numbers.append(cumulative_sum)

    return output_numbers

def main():
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 3:
        sys.exit("Usage: compute.py <threshold> <limit>")

    # Validate and convert command line arguments to Decimal within the specified range
    threshold = validate_argument(sys.argv[1], "Threshold")
    limit = validate_argument(sys.argv[2], "Limit")

    # Read input numbers from standard input and convert them to Decimal
    numbers = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            sys.exit(f"Error: All lines should be decimal number. Empty line found.")
        try:
            number = Decimal(line)
            if not (Decimal('0.0') <= number <= Decimal('1_000_000_000.0')):
                sys.exit(f"Error: Input {line} must be between 0.0 and 1,000,000,000.0 inclusive.")
            numbers.append(number)
            if len(numbers) > 100:
                sys.exit(f"Error: Input count must not exceed 100 numbers.")
        except InvalidOperation:
            sys.exit(f"Error: Input {line} must be a valid decimal number.")

    # Process the input numbers
    output_numbers = process_input(threshold, limit, numbers)

    # Print the output numbers with decimal precision
    for number in output_numbers:
        print(f"{number:.1f}")

if __name__ == "__main__":
    main()
