# Author: Caleb Moura

# Importing sys module.
import sys

# Function definition for sum_to using while loop.
def sum_to(n):
    """
    Calculate the sum of all values from 1 to n using a while loop.

    Parameters:
    - n (int): The upper limit for the summation.

    Returns:
    - int: The sum of values from 1 to n.
    """
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

# If then system exit
if __name__ == "__main__":
    # Check if  command-line argument is provided.
    if len(sys.argv) != 2:
        print("Usage: python lab_8-1.py <integer>")
        sys.exit(1)

    # Extract integer argument from command line.
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Error: Please provide a valid integer argument.")
        sys.exit(1)

    # Call sum_to function and print result.
    result = sum_to(n)
    print(f"The sum of values from 1 to {n} is: {result}")

    # Was slightly confused, but figured it out