def square_sum(numbers):
    return sum(num**2 for num in numbers)

# Example usage
numbers = [1, 2, 3, 4]
print(square_sum(numbers))  # Output: 30

# В этой функции Python мы используем выражение-генератор внутри функции sum, 
# чтобы возвести в квадрат каждое число в списке чисел, а затем просуммировать 
# все возведенные в квадрат значения.