# Import required modules
import random
import time
import sys
# Increase Python's recursion limit so deterministic Quicksort
# can handle larger worst-case inputs.
sys.setrecursionlimit(20000)


# DETERMINISTIC QUICKSORT
def partition(arr, low, high):
    """
    Rearranges the elements in the array around the pivot.

    Elements smaller than the pivot are moved to the left.
    Elements greater than the pivot are moved to the right.

    Parameters:
        arr : List of numbers
        low : Starting index
        high : Ending index

    Returns:
        The final position of the pivot.
    """

    # Select the last element as the pivot
    pivot = arr[high]

    # i keeps track of the position for smaller elements
    i = low - 1

    # Traverse through the array
    for j in range(low, high):

        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:

            # Move the boundary of smaller elements
            i += 1

            # Swap current element into the smaller section
            arr[i], arr[j] = arr[j], arr[i]

    # Place the pivot in its correct sorted position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return the pivot index
    return i + 1

def deterministic_quicksort(arr, low, high):
    """
    Sorts an array using Deterministic Quicksort.
    """

    # Continue only if there is more than one element
    if low < high:

        # Partition the array and get pivot position
        pivot_index = partition(arr, low, high)

        # Recursively sort the left partition
        deterministic_quicksort(arr, low, pivot_index - 1)

        # Recursively sort the right partition
        deterministic_quicksort(arr, pivot_index + 1, high)


# RANDOMIZED QUICKSORT
def randomized_partition(arr, low, high):
    """
    Randomly selects a pivot before partitioning.

    Choosing a random pivot reduces the probability
    of worst-case performance.
    """

    # Generate a random pivot index
    random_index = random.randint(low, high)

    # Move the random pivot to the end
    arr[random_index], arr[high] = arr[high], arr[random_index]

    # Perform the normal partition operation
    return partition(arr, low, high)

def randomized_quicksort(arr, low, high):
    """
    Sorts an array using Randomized Quicksort.
    """

    # Continue recursion only if the sub-array has multiple elements
    if low < high:

        # Partition using a randomly selected pivot
        pivot_index = randomized_partition(arr, low, high)

        # Sort the left partition
        randomized_quicksort(arr, low, pivot_index - 1)

        # Sort the right partition
        randomized_quicksort(arr, pivot_index + 1, high)


# DATASET GENERATION
def generate_random_array(size):
    """
    Creates an array containing random integers.
    """
    return [random.randint(1, 100000) for _ in range(size)]

def generate_sorted_array(size):
    """
    Creates an already sorted array.
    """
    return list(range(size))

def generate_reverse_sorted_array(size):
    """
    Creates a reverse sorted array.
    """
    return list(range(size, 0, -1))



# PERFORMANCE MEASUREMENT
def measure_time(sort_function, arr):
    """
    Measures the execution time of a sorting algorithm.

    Parameters:
        sort_function : Sorting function
        arr : Array to sort

    Returns:
        Execution time in seconds or a Recursion Error message.
    """

    # Record the start time
    start = time.perf_counter()

    try:
        # Execute the sorting algorithm
        sort_function(arr, 0, len(arr) - 1)

    except RecursionError:
        return "Recursion Error"

    # Record the end time
    end = time.perf_counter()

    # Return the elapsed time
    return end - start


# MAIN PROGRAM
if __name__ == "__main__":

    # Different input sizes for testing
    sizes = [1000, 5000, 10000]

    # Different dataset types
    datasets = {
        "Random": generate_random_array,
        "Sorted": generate_sorted_array,
        "Reverse Sorted": generate_reverse_sorted_array
    }

    # Display the program title
    print("=" * 75)
    print("Deterministic vs Randomized Quicksort Performance")
    print("=" * 75)

    # Test each input size
    for size in sizes:

        print(f"\nArray Size: {size}")

        # Test each dataset type
        for dataset_name, generator in datasets.items():

            # Generate the original dataset
            original = generator(size)

            # Make separate copies for each algorithm
            deterministic_array = original.copy()
            randomized_array = original.copy()

            # Measure execution times
            deterministic_time = measure_time(
                deterministic_quicksort,
                deterministic_array
            )

            randomized_time = measure_time(
                randomized_quicksort,
                randomized_array
            )

            # Format deterministic result
            if isinstance(deterministic_time, str):
                deterministic_result = deterministic_time
            else:
                deterministic_result = f"{deterministic_time:.6f}s"

            # Format randomized result
            if isinstance(randomized_time, str):
                randomized_result = randomized_time
            else:
                randomized_result = f"{randomized_time:.6f}s"

            # Display results
            print(
                f"{dataset_name:<18}"
                f"Deterministic: {deterministic_result:<18}"
                f"Randomized: {randomized_result}"
            )