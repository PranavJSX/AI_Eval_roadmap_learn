"""
1. The Stats Extractor (Tuple Packing/Unpacking)
Goal: Write a function called get_stats(numbers) that takes a list of numbers.

Requirements:

Calculate the minimum, maximum, and average of the list.

Return all three values in a single tuple (min_val, max_val, average).

Call the function and unpack the returned tuple into three distinct variables, then print them.
"""


def get_stats(numbers):
    print(numbers)
    return max(numbers), min(numbers), sum(numbers) / len(numbers)


def main():
    max, min, avg = get_stats([i for i in range(2, 15)])
    print(f"Max:{max} , Min:{min}, Average:{avg}")


main()
