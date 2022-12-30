'''
QUESTION 1: Alice has some cards with numbers written on them.
She arranges the cards in decreasing order, and lays them out face down in a sequence on a table.
She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
Write a function to help Bob locate the card.
'''

'''
The problem can now be stated as follows:
#### Problem
> We need to write a program to find the position of a given number in a list of numbers arranged in decreasing order. We also need to minimize the number of times we access elements from the list.
#### Input
1. `cards`: A list of numbers sorted in decreasing order. E.g. `[13, 11, 10, 7, 4, 3, 1, 0]`
2. `query`: A number, whose position in the array is to be determined. E.g. `7` (to be find)
#### Output
3. `position`: The position of `query` in the list `cards`. E.g. `3rd index` in the above case (counting from `0`)

'''

test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

'''
Our function should be able to handle any set of valid inputs we pass into it. 
Here's a list of some possible variations we might encounter:
1. The number `query` occurs somewhere in the middle of the list `cards`.
2. `query` is the first element in `cards`.
3. `query` is the last element in `cards`.
4. The list `cards` contains just one element, which is `query`.
5. The list `cards` does not contain number `query`.
6. The list `cards` is empty.
7. The list `cards` contains repeating numbers.
8. The number `query` occurs at more than one position in `cards`.
9. (can you think of any more variations?)
'''

# Test Cases append in list:
tests = [
    {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
    {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
    {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
    {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
    {'input': {'cards': [6], 'query': 6}, 'output': 0},
    {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
    {'input': {'cards': [], 'query': 7}, 'output': -1},
    {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3}, 'output': 7},
    {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 6}, 'output': 2}
]

"""
### 3. Come up with a correct solution for the problem. State it in plain English.
Our first goal should always be to come up with a _correct_ solution to the problem, which may necessarily be the most _efficient_ solution. 
The simplest or most obvious solution to a problem, which generally involves checking all possible answers is called the _brute force_ solution.

In this problem, coming up with a correct solution is quite easy: Bob can simply turn over cards in order one by one, 
till he find a card with the given number on it. Here's how we might implement it:

1. Create a variable `position` with the value 0.
3. Check whether the number at index `position` in `card` equals `query`.
4. If it does, `position` is the answer and can be returned from the function
5. If not, increment the value of `position` by 1, and repeat steps 2 to 5 till we reach the last position.
6. If the number was not found, return `-1`.
> **Linear Search Algorithm**: Congratulations, we've just written our first _algorithm_! 
An algorithm is simply a list of statements which can be converted into code and executed by a computer on different sets of inputs. 

This particular algorithm is called linear search, since it involves searching through a list in a linear fashion i.e. element after element.

"""

from jovian.pythondsa import evaluate_test_cases, evaluate_test_case


# Brute force solution
def locate_card1(cards, query):
    position = 0
    while position <= len(cards):
        if cards[position] == query:
            return position
        position = position + 1
    return -1


first_case = {'input': {'cards': [13, 11, 10, 8, 7, 4, 3, 1, 0], 'query': 4}, 'output': 5}
# result = locate_card1(first_case['input']['cards'],first_case['input']['query'])
# print(result)
# evaluate_test_case(locate_card1,first_case)


# Applying Binary search

"""
### 7. Come up with a correct solution for the problem.

Here's how binary search can be applied to our problem:

1. Find the middle element of the list.
2. If it matches queried number, return the middle position as the answer.
3. If it is less than the queried number, then search the first half of the list
3. If it is greater than the queried number, then search the second half of the list
4. If no more elements remain, return -1.

"""


# Applying binary search Solution 1
def locate_card2(cards, query):
    # Set low and high search space
    low, high = 0, len(cards) - 1

    while low <= high:
        mid_index = (low + high) // 2
        mid_num = cards[mid_index]
        if mid_num == query:
            return mid_index
        elif mid_num < query:
            high = mid_index - 1
        elif mid_num > query:
            low = mid_index + 1

    return -1


# result1 = locate_card2(first_case['input']['cards'],first_case['input']['query'])
# print(first_case)
# print(result1)
# evaluate_test_case(locate_card2,first_case)
# evaluate_test_cases(locate_card2,tests)
# evaluate_test_case(locate_card2,tests[8])


def test_location(cards, query, mid):
    mid_number = cards[mid]  # mid number
    if mid_number == query:
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return 'left'
        return 'found'
    elif mid_number < query :
        return 'left'
    elif mid_number > query:
        return 'right'

# Solution 2
def locate_card3(cards,query):
    low, high = 0, len(cards) - 1

    while low <= high:
        mid_index = (low + high) // 2
        result = test_location(cards,query,mid_index)

        if result == 'found':
            return mid_index
        elif result == 'left':
            high = mid_index - 1
        elif result == 'right':
            low = mid_index + 1

    return -1

# evaluate_test_cases(locate_card3,tests)

large_test = {
    'input': {
        'cards': list(range(10000000, 0, -1)),
        'query': 2
    },
    'output': 9999998

}

# evaluate_test_case(locate_card2,large_test)

# Tested with large list (large_test):
    # Linear Search Execution time: 1261.545 ms
    # Binary Search Execution time: 0.014 ms



# Binary Search with ascending sorted list

"""
Question: Given an array of integers nums sorted in ascending order, 
find the starting and ending position of a given number.
"""

ascending_sorted = [
    {'input': {'cards': [5, 7, 7, 8, 8, 10], 'query': 7}, 'output': (1, 2)},
    {'input': {'cards': [0, 1, 3, 4, 7, 10, 10, 11, 13], 'query': 10}, 'output': (5, 6)},
    {'input': {'cards': [-1, 1, 2, 4], 'query': 4}, 'output': (3,3)},
    {'input': {'cards': [-127, -9, -1, 3], 'query': -127}, 'output': (0,0)},
    {'input': {'cards': [6], 'query': 6}, 'output': (0,0)},
    {'input': {'cards': [-9, 2, 5, 7, 9], 'query': 4}, 'output': (-1,-1)},
    {'input': {'cards': [], 'query': 7}, 'output': (-1,-1)},
    {'input': {'cards': [0, 0, 0, 2, 2, 2, 3, 6, 6, 6, 6, 6, 8, 8], 'query': 3}, 'output': (6,6)},
    {'input': {'cards': [0, 0, 0, 2, 2, 2, 3, 6, 6, 6, 6, 6, 6, 8, 8], 'query': 6}, 'output': (7,12)}
]
