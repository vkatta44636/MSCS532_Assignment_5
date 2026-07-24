# Assignment 5 – Quicksort Algorithm

## Overview

This Assignment implements and compares two versions of the Quicksort algorithm:

- **Deterministic Quicksort** (last element as the pivot)
- **Randomized Quicksort** (randomly selected pivot)

The program also measures and compares the execution time of both algorithms using different input types:
- Random arrays
- Sorted arrays
- Reverse-sorted arrays

---

## Requirements

- Python 3.x
- No external libraries are required (uses only Python's built-in `random` and `time` modules).

---

## How to Run

1. Clone or download this repository.
2. Open a terminal in the Assignment folder.
3. Run the following command:

```bash
python quicksort.py
```

The program will execute both versions of Quicksort and display their execution times for different input sizes and datasets.

---

## Summary of Findings

- **Deterministic Quicksort** performs well on random input but can degrade to **O(n²)** on already sorted or reverse-sorted arrays because it always selects the last element as the pivot.
- **Randomized Quicksort** reduces the likelihood of encountering the worst-case scenario by selecting the pivot randomly, resulting in more consistent performance across different input distributions.
- In most cases, both algorithms achieve an average time complexity of **O(n log n)**, while the randomized version is generally more robust for varied datasets.
```