def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Example usage with a list containing both integers and strings
data = [10, 20, '30', 40]
average = calculate_average(data)
print(f"The average is: {average}")

# Example usage with a list of integers
data2 = [10, 20, 30, 40]
average2 = calculate_average(data2)
print(f"The average is: {average2}")