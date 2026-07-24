# Import required modules
import random
import time
import sys

# Increase Python's recursion limit so deterministic Quicksort
# can handle larger worst-case inputs.
sys.setrecursionlimit(20000)


# DETERMINISTIC QUICKSORT
def divide_array(numbers, left, right):
    """
    Rearranges the elements in the array around the pivot.

    Elements smaller than the pivot are moved to the left.
    Elements greater than the pivot are moved to the right.

    Parameters:
        numbers : List of numbers
        left : Starting index
        right : Ending index

    Returns:
        The final position of the pivot.
    """

    # Select the last element as the pivot
    pivot_value = numbers[right]

    # boundary keeps track of the position for smaller elements
    boundary = left - 1

    # Traverse through the array
    current = left

    while current < right:

        # If current element is smaller than or equal to pivot
        if numbers[current] <= pivot_value:

            # Move the boundary of smaller elements
            boundary += 1

            # Swap current element into the smaller section
            numbers[boundary], numbers[current] = (
                numbers[current],
                numbers[boundary]
            )

        current += 1

    # Place the pivot in its correct sorted position
    numbers[boundary + 1], numbers[right] = (
        numbers[right],
        numbers[boundary + 1]
    )

    # Return the pivot index
    return boundary + 1


def fixed_pivot_quicksort(numbers, left, right):
    """
    Sorts an array using Deterministic Quicksort.
    """

    # Continue only if there is more than one element
    if left < right:

        # Partition the array and get pivot position
        pivot_position = divide_array(numbers, left, right)

        # Recursively sort the left partition
        fixed_pivot_quicksort(numbers, left, pivot_position - 1)

        # Recursively sort the right partition
        fixed_pivot_quicksort(numbers, pivot_position + 1, right)


# RANDOMIZED QUICKSORT
def random_divide(numbers, left, right):
    """
    Randomly selects a pivot before partitioning.

    Choosing a random pivot reduces the probability
    of worst-case performance.
    """

    # Generate a random pivot index
    random_position = random.randint(left, right)

    # Move the random pivot to the end
    numbers[random_position], numbers[right] = (
        numbers[right],
        numbers[random_position]
    )

    # Perform the normal partition operation
    return divide_array(numbers, left, right)


def random_pivot_quicksort(numbers, left, right):
    """
    Sorts an array using Randomized Quicksort.
    """

    # Continue recursion only if the sub-array has multiple elements
    if left < right:

        # Partition using a randomly selected pivot
        pivot_position = random_divide(numbers, left, right)

        # Sort the left partition
        random_pivot_quicksort(numbers, left, pivot_position - 1)

        # Sort the right partition
        random_pivot_quicksort(numbers, pivot_position + 1, right)


# DATASET GENERATION
def create_random_numbers(length):
    """
    Creates an array containing random integers.
    """

    values = []

    for _ in range(length):
        values.append(random.randint(1, 100000))

    return values


def create_sorted_numbers(length):
    """
    Creates an already sorted array.
    """

    values = []

    number = 0

    while number < length:
        values.append(number)
        number += 1

    return values


def create_reverse_numbers(length):
    """
    Creates a reverse sorted array.
    """

    values = []

    number = length

    while number > 0:
        values.append(number)
        number -= 1

    return values


# PERFORMANCE MEASUREMENT
def calculate_execution_time(sort_method, numbers):
    """
    Measures the execution time of a sorting algorithm.

    Parameters:
        sort_method : Sorting function
        numbers : Array to sort

    Returns:
        Execution time in seconds or a Recursion Error message.
    """

    # Record the start time
    begin_time = time.perf_counter()

    try:
        # Execute the sorting algorithm
        sort_method(numbers, 0, len(numbers) - 1)

    except RecursionError:
        return "Recursion Error"

    # Record the end time
    finish_time = time.perf_counter()

    # Return the elapsed time
    return finish_time - begin_time


# MAIN PROGRAM
if __name__ == "__main__":

    # Different input sizes for testing
    input_sizes = [1000, 5000, 10000]

    # Different dataset types
    test_sets = {
        "Random": create_random_numbers,
        "Sorted": create_sorted_numbers,
        "Reverse Sorted": create_reverse_numbers
    }

    # Display the program title
    print("=" * 75)
    print("Deterministic vs Randomized Quicksort Performance")
    print("=" * 75)

    # Test each input size
    for current_size in input_sizes:

        print("\nArray Size: {}".format(current_size))

        # Test each dataset type
        for set_name, create_data in test_sets.items():

            # Generate the original dataset
            source_data = create_data(current_size)

            # Make separate copies for each algorithm
            first_copy = source_data.copy()
            second_copy = list(source_data)

            # Measure execution times
            fixed_time = calculate_execution_time(
                fixed_pivot_quicksort,
                first_copy
            )

            random_time = calculate_execution_time(
                random_pivot_quicksort,
                second_copy
            )

            # Format deterministic result
            if isinstance(fixed_time, str):
                fixed_result = fixed_time
            else:
                fixed_result = "{:.6f}s".format(fixed_time)

            # Format randomized result
            if isinstance(random_time, str):
                random_result = random_time
            else:
                random_result = "{:.6f}s".format(random_time)

            # Display results
            print(
                "{:<18}Deterministic: {:<18}Randomized: {}".format(
                    set_name,
                    fixed_result,
                    random_result
                )
            )