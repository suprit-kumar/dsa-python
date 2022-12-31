# Problem - Rotated Lists
from jovian.pythondsa import evaluate_test_cases, evaluate_test_case

"""
## Problem - Rotated Lists

We'll solve the following problem step-by-step:

> You are given list of numbers, obtained by rotating a sorted list an unknown number of times.
Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list.
Your function should have the worst-case complexity of `O(log N)`, where N is the length of the list.
You can assume that all the numbers in the list are unique.
>
> Example: The list `[5, 6, 9, 0, 2, 3, 4]` was obtained by rotating the sorted list `[0, 2, 3, 4, 5, 6, 9]` 3 times.
>
> We define "rotating a list" as removing the last element of the list and adding it before the first element.
E.g. rotating the list `[3, 2, 4, 1]` produces `[1, 3, 2, 4]`.
>
>"Sorted list" refers to a list where the elements are arranged in the increasing order  e.g. `[1, 3, 5, 7]`.
>
"""

"""
## Solution


### 1. State the problem clearly. Identify the input & output formats.

While this problem is stated clearly enough, it's always useful to try and express in your own words, 
in a way that makes it most clear for you. 
It's perfectly OK if your description overlaps with the original problem statement to a large extent.

_**Q: Express the problem in your own words below .**_

**Problem**

- The problem stated that , given a rotated sorted list that was rotated some unknown number of times, we need to find
the minimum number of times it was rotated


_**Q: The function you write will take one input called `nums`. What does it represent? Give an example.**_

**Input**

1. `nums`: [5,6,3, 2, 4, 1]



_**Q: The function you write will return a single output called `rotations`. What does it represent? Give an example.**_

**Output**

3. `rotations`: This is the number of times the sorted list was rotated. e.g:  2 for above list


Based on the above, we can now create a signature of our function:
"""

"""
### 2. Come up with some example inputs & outputs. Try to cover all edge cases.

Our function should be able to handle any set of valid inputs we pass into it. Here's a list of some possible variations we might encounter:

1. A list of size 10 rotated 3 times.
2. A list of size 8 rotated 5 times.
3. A list that wasn't rotated at all.
4. A list that was rotated just once. 
5. A list that was rotated `n-1` times, where `n` is the size of the list.
6. A list that was rotated `n` times (do you get back the original list here?)
7. An empty list.
8. A list containing just one element.
9. (can you think of any more?)

We'll express our test cases as dictionaries, to test them easily. Each dictionary will contain 2 keys: `input` (a dictionary itself containing one key for each argument to the function and `output` (the expected result from the function). Here's an example.
"""

tests = [
    {'input': {'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]}, 'output': 3},  # A list of size 10 rotated 3 times.
    {'input': {'nums': [4, 5, 6, 7, 8, 1, 2, 3]}, 'output': 5},  # A list of size 8 rotated 5 times.
    {'input': {'nums': [7, 3, 5]}, 'output': 1},  # A list that was rotated just once.
    {'input': {'nums': [10, 11, 13, 9]}, 'output': 3},
    # A list that was rotated n-1 times, where n is the size of the list.
    {'input': {'nums': [3, 5, 7, 8, 9, 10]}, 'output': 0},
    # A list that was rotated n times (do you get back the original list here?)
    {'input': {'nums': []}, 'output': 0},  # An empty list.
    {'input': {'nums': [1]}, 'output': 0},  # A list containing just one element.

]

# {'input': {'nums': [4]}, 'output': 0},
# {'input': {'nums': []}, 'output': 0},
# {'input': {'nums': [1]}, 'output': 0},


# Linear Search
"""
1. Create a variable with rotation_count = 0
2. Run while loop if rotation count < length of list
3. Run while loop to iterate through list if current number is smaller than it's previous number then return the rotation count.
4. increase rotation count on each iteration

"""


def count_rotation_linear(nums):
    rotation_count = 0
    if nums:
        while rotation_count < len(nums):
            if rotation_count > 0 and (nums[rotation_count] < nums[rotation_count - 1]):
                return rotation_count
            rotation_count += 1
    return 0


linear_search_complexity = "O(n)"


# print(count_rotation_linear([4, 5, 6, 7, 8, 1, 2, 3]))

# evaluate_test_cases(count_rotation_linear, tests)


def count_rotation_binary(nums):
    if nums:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid_index = (low + high) // 2
            number = nums[mid_index]
            if mid_index > 0 and number < nums[mid_index-1]:
                return mid_index
            elif number < nums[len(nums) - 1]:  # to left
                high = mid_index - 1
            elif number > nums[len(nums) - 1]:  # to right
                low = mid_index + 1
            else:
                return 0
    return 0


# print(count_rotation_binary([19, 25, 29, 3, 5, 6, 7, 9, 11, 14]))
evaluate_test_cases(count_rotation_binary,tests)
