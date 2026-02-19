
# list_operations.py

numbers = []

# Accept 5 integers
for i in range(5):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)

# Largest and smallest
largest = max(numbers)
smallest = min(numbers)

# Sum and average
total = sum(numbers)
average = total / len(numbers)

# Reverse order
reversed_list = numbers[::-1]

print("Largest number:", largest)
print("Smallest number:", smallest)
print("Sum of numbers:", total)
print("Average of numbers:", average)
print("List in reverse order:", reversed_list)