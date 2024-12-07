def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0  # Handle empty list after filtering
    return sum(numeric_numbers) / len(numeric_numbers)

# Example usage with a list containing both integers and strings
data = [10, 20, '30', 40]
average = calculate_average(data)
print(f"The average is: {average}")

# Example usage with a list of integers
data2 = [10, 20, 30, 40]
average2 = calculate_average(data2)
print(f"The average is: {average2}")

# Example usage with an empty list
data3 = []
average3 = calculate_average(data3)
print(f"The average is: {average3}") 