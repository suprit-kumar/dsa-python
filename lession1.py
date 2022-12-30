# Binary Search, Linked Lists and Complexity Analysis
# ---------------------------------------------------

# https://jovian.ai/learn/data-structures-and-algorithms-in-python/lesson/lesson-1-binary-search-linked-lists-and-complexity


'''
QUESTION 1: Alice has some cards with numbers written on them.
She arranges the cards in decreasing order, and lays them out face down in a sequence on a table.
She challenges Bob to pick out the card containing a given number by turning over as few cards as possible.
Write a function to help Bob locate the card.
'''

# Solution
# State the problem clearly. Identify the input & output formats.

"""
## Solution


### 1. State the problem clearly. Identify the input & output formats.

You will often encounter detailed word problems in coding challenges and interviews. The first step is to state the problem clearly and precisely in abstract terms. 

In this case, for instance, we can represent the sequence of cards as a list of numbers. Turning over a specific card is equivalent to accessing the value of the number at the corresponding position the list. 


The problem can now be stated as follows:

#### Problem

> We need to write a program to find the position of a given number in a list of numbers arranged in decreasing order. We also need to minimize the number of times we access elements from the list.

#### Input

1. `cards`: A list of numbers sorted in decreasing order. E.g. `[13, 11, 10, 7, 4, 3, 1, 0]`
2. `query`: A number, whose position in the array is to be determined. E.g. `7` (to be find)

#### Output

3. `position`: The position of `query` in the list `cards`. E.g. `3rd index` in the above case (counting from `0`)



Based on the above, we can now create the signature of our function:

**Tips**:

* Name your function appropriately and think carefully about the signature
* Discuss the problem with the interviewer if you are unsure how to frame it in abstract terms
* Use descriptive variable names, otherwise you may forget what a variable represents


### 2. Come up with some example inputs & outputs. Try to cover all edge cases.

Before we start implementing our function, it would be useful to come up with some example inputs and outputs which we can use later to test out problem. We'll refer to them as *test cases*.

Here's the test case described in the example above.

cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3



We'll represent our test cases as dictionaries to make it easier to test them once we write implement our function. 
For example, the above test case can be represented as follows:


test = {
    'input': { 
        'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
        'query': 7
    },
    'output': 3
}


The function can now be tested as follows.

locate_card(**test['input']) == test['output']




Our function should be able to handle any set of valid inputs we pass into it. Here's a list of some possible variations we might encounter:

1. The number `query` occurs somewhere in the middle of the list `cards`.
2. `query` is the first element in `cards`.
3. `query` is the last element in `cards`.
4. The list `cards` contains just one element, which is `query`.
5. The list `cards` does not contain number `query`.
6. The list `cards` is empty.
7. The list `cards` contains repeating numbers.
8. The number `query` occurs at more than one position in `cards`.
9. (can you think of any more variations?)

> **Edge Cases**: It's likely that you didn't think of all of the above cases when you read the problem for the first time. 
Some of these (like the empty array or `query` not occurring in `cards`) are called *edge cases*, as they represent rare or extreme examples. 

While edge cases may not occur frequently, your programs should be able to handle all edge cases, otherwise they may fail in unexpected ways. 
Let's create some more test cases for the variations listed above. We'll store all our test cases in an list for easier testing.

"""

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
The problem statement does not specify what to do if the list `cards` does not contain the number `query`. 

1. Read the problem statement again, carefully.
2. Look through the examples provided with the problem.
3. Ask the interviewer/platform for a clarification.
4. Make a reasonable assumption, state it and move forward.

We will assume that our function will return `-1` in case `cards` does not contain `query`.

In the case where `query` occurs multiple times in `cards`, we'll expect our function to return the first occurrence of `query`. 

While it may also be acceptable for the function to return any position where `query` occurs within the list, 
it would be slightly more difficult to test the function, as the output is non-deterministic.


"""

# --------------------------------------------------------------------------------------------------------

"""
### 3. Come up with a correct solution for the problem. State it in plain English.

Our first goal should always be to come up with a _correct_ solution to the problem, which may necessarily be the most _efficient_ solution. The simplest or most obvious solution to a problem, which generally involves checking all possible answers is called the _brute force_ solution.

In this problem, coming up with a correct solution is quite easy: Bob can simply turn over cards in order one by one, till he find a card with the given number on it. Here's how we might implement it:

1. Create a variable `position` with the value 0.
3. Check whether the number at index `position` in `card` equals `query`.
4. If it does, `position` is the answer and can be returned from the function
5. If not, increment the value of `position` by 1, and repeat steps 2 to 5 till we reach the last position.
6. If the number was not found, return `-1`.

> **Linear Search Algorithm**: Congratulations, we've just written our first _algorithm_! An algorithm is simply a list of statements which can be converted into code and executed by a computer on different sets of inputs. 
This particular algorithm is called linear search, since it involves searching through a list in a linear fashion i.e. element after element.


**Tip:** Always try to express (speak or write) the algorithm in your own words before you start coding. 
It can be as brief or detailed as you require it to be. Writing is a great tool for thinking clearly. 
It's likely that you will find some parts of the solution difficult to express, which suggests that you are probably unable to think about it clearly. 
The more clearly you are able to express your thoughts, the easier it will be for you to turn into code.
"""

from jovian.pythondsa import evaluate_test_cases, evaluate_test_case
import time


# results = evaluate_test_cases(locate_card,tests)

# Brute force solution

# Linear Search
# Solution - 1
def locate_card(cards, query):
    start = time.time()
    position = 0
    while True:
        if cards:
            if cards[position] == query:
                print(f"Time taken for solution 1: {time.time() - start}")
                return position
            position = position + 1
            if position == len(cards):
                print(f"Time taken for solution 1: {time.time() - start}")
                return -1
        else:
            print(f"Time taken for solution 1: {time.time() - start}")
            return -1


# Solution -2

def _locate_card(cards, query):
    start = time.time()
    position = 0
    while position < len(cards):
        if cards[position] == query:
            print(f"Time taken for solution 2: {time.time() - start}")
            return position
        position = position + 1
    print(f"Time taken for solution 2: {time.time() - start}")
    return -1


# first_case = {'input': {'cards': [13, 11, 10, 8, 7, 4, 3, 1, 0], 'query': 4}, 'output': 5}

# result = locate_card(first_case['input']['cards'],first_case['input']['query'])
# print(result)
# evaluate_test_case(_locate_card,first_case) # For single case

# evaluate_test_cases(_locate_card,tests) # For multiple test cases


"""
### 5. Analyze the algorithm's complexity and identify inefficiencies, if any.

Recall this statement from  original question:
 _"Alice challenges Bob to pick out the card containing a given number by **turning over as few cards as possible**."
 _ We restated this requirement as: _"Minimize the number of times we access elements from the list `cards`"_


Before we can minimize the number, we need a way to measure it. Since we access a list element once in every iteration, 
for a list of size `N` we access the elements from the list up to `N` times. 
Thus, Bob may need to overturn up to `N` cards in the worst case, to find the required card. 

Suppose he is only allowed to overturn 1 card per minute, it may take him 30 minutes to find the required card if 30 cards are laid out on the table. 
Is this the best he can do? Is a way for Bob to arrive at the answer by turning over just 5 cards, instead of 30?

The field of study concerned with finding the amount of time, space or other resources required to complete the execution of computer programs is called _the analysis of algorithms_. 
And the process of figuring out the best algorithm to solve a given problem is called _algorithm design and optimization_.


### Complexity and Big O Notation

> **Complexity** of an algorithm is a measure of the amount of time and/or space required by an algorithm for an input of a given size e.g. `N`. 
Unless otherwise stated, the term _complexity_ always refers to the worst-case complexity (i.e. the highest possible time/space taken by the program/algorithm to process an input).

In the case of linear search:

1. The _time complexity_ of the algorithm is `cN` for some fixed constant `c` that depends on the number of operations we perform in each iteration and the time taken to execute a statement. 
Time complexity is sometimes also called the _running time_ of the algorithm.

2. The _space complexity_ is some constant `c'` (independent of `N`), since we just need a single variable `position` to iterate through the array, and it occupies a constant space in the computer's memory (RAM).


> **Big O Notation**: Worst-case complexity is often expressed using the Big O notation. In the Big O, we drop fixed constants and lower powers of variables to capture the trend of relationship between the size of the input and the complexity of the algorithm i.e. if the complexity of the algorithm is `cN^3 + dN^2 + eN + f`, in the Big O notation it is expressed as **O(N^3)**

Thus, the time complexity of linear search is **O(N)** and its space complexity is **O(1)**.




### 6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.

At the moment, we're simply going over cards one by one, and not even utilizing the face that they're sorted. 
This is called a *brute force* approach.

It would be great if Bob could somehow guess the card at the first attempt, but with all the cards turned over it's simply impossible to guess the right card. 


The next best idea would be to pick a random card, and use the fact that the list is sorted, 
to determine whether the query card lies to the left or right of it. In fact, if we pick the middle card, 
we can reduce the number of additional cards to be tested to half the size of the list. Then, 
we can simply repeat the process with each half. This technique is called binary search. 


### 7. Come up with a correct solution for the problem. State it in plain English.

Here's how binary search can be applied to our problem:

1. Find the middle element of the list.
2. If it matches queried number, return the middle position as the answer.
3. If it is less than the queried number, then search the first half of the list
3. If it is greater than the queried number, then search the second half of the list
4. If no more elements remain, return -1.


"""


# Binary Search
def _binary_locate_card(cards, query):
    start = time.time()
    low, high = 0, len(cards) - 1  # Define search space

    while low <= high:
        middle_index = (low + high) // 2  # Find the relative middle index using floor division
        middle_number = cards[middle_index]

        print(f"low: {low} | high: {high} | middle_index: {middle_index} | middle_number: {middle_number}")

        if middle_number == query:
            print(f"Time taken for solution 3: {time.time() - start}")
            return middle_index
        elif middle_number < query:
            high = middle_index - 1
        elif middle_number > query:
            low = middle_index + 1
    print(f"Time taken for solution 3: {time.time() - start}")
    return -1


# get_match_index = _binary_locate_card(first_case['input']['cards'],first_case['input']['query'])
# print(get_match_index)

# evaluate_test_cases(_binary_locate_card,tests) # TOTAL: 9, PASSED: 8, FAILED: 1
# Time taken for solution 3: 1.1444091796875e-05
# Time taken for solution 2: 5.7220458984375e-06
# Time taken for solution 1: 6.198883056640625e-06

# Error in test case - [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]

"""
Seems like we did locate a 6 in the array, it's just that it wasn't the first 6. 
As you can guess, this is because in binary search, we don't go over indices in a linear order.

So how do we fix it?

When we find that `cards[mid]` is equal to `query`, we need to check whether it is the first occurrence of `query` in the list 
i.e the number that comes before it.

`[8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]`

To make it easier, we'll define a helper function called `test_location`, 
which will take the list `cards`, the `query` and `mid` as inputs.

"""


# 9,8,7,6,5,4,3,2,1
#
# q = 5
# mid = 4
# Binary search with handled error case

def test_location(cards, query, middle_index):
    middle_number = cards[middle_index]
    if middle_number == query:
        # Check for the first occurrence if number are duplicate
        if middle_index - 1 >= 0 and cards[middle_index - 1] == query:
            return 'left'
        else:
            return 'found'
    elif middle_number < query:
        return "left"
    elif middle_number > query:
        return "right"


def _binary_locate_card2(cards, query):
    low, high = 0, len(cards) - 1
    while low <= high:
        middle_index = (low + high) // 2
        result = test_location(cards, query, middle_index)
        if result == 'found':
            return middle_index
        elif result == 'left':
            high = middle_index - 1
        elif result == "right":
            low = middle_index + 1
    return -1


# evaluate_test_case(_binary_locate_card2,first_case)
# evaluate_test_cases(_binary_locate_card2, tests)


"""
### 9. Analyze the algorithm's complexity and identify inefficiencies, if any.

Once again, let's try to count the number of iterations in the algorithm. 
If we start out with an array of N elements, then each time the size of the array reduces to half for the next iteration, 
until we are left with just 1 element.

Initial length - `N`

Iteration 1 - `N/2`

Iteration 2 - `N/4` i.e. `N/2^2`

Iteration 3 - `N/8` i.e. `N/2^3`

...

Iteration k - `N/2^k`


Since the final length of the array is 1, we can find the 

`N/2^k = 1`

Rearranging the terms, we get

`N = 2^k`

Taking the logarithm

`k = log N`

Where `log` refers to log to the base 2. Therefore, our algorithm has the time complexity **O(log N)**. 
This fact is often stated as: binary search _runs_ in logarithmic time. 
You can verify that the space complexity of binary search is **O(1)**.



## Generic Binary Search

Here is the general strategy behind binary search, which is applicable to a variety of problems:

1. Come up with a condition to determine whether the answer lies before, after or at a given position
1. Retrieve the midpoint and the middle element of the list.
2. If it is the answer, return the middle position as the answer.
3. If answer lies before it, repeat the search with the first half of the list
4. If the answer lies after it, repeat the search with the second half of the list.

"""


# Here is the generic algorithm for binary search, implemented in Python:
def binary_search3(low, high, condition):  # Passing condition function as an argument
    while low <= high:
        middle_index = (low + high) // 2
        result = condition(middle_index)
        if result == 'found':
            return middle_index
        elif result == 'left':
            high = middle_index - 1
        else:
            low = middle_index + 1
    return -1


def locate_card3(cards, query):
    low, high = 0, len(cards) - 1

    def condition(middle_index):
        if cards[middle_index] == query:
            if middle_index > 0 and cards[
                middle_index - 1] == query:  # Search in left array if that same element occurs at one less index
                return 'left'
            else:
                return 'found'
        elif cards[middle_index] < query:  # Number < query
            return 'left'
        else:
            return 'right'  # Number > query

    return binary_search3(low, high, condition)


# evaluate_test_case(locate_card3,first_case)
# evaluate_test_cases(locate_card3, tests)


"""
The `binary_search` function can now be used to solve other problems too. It is a tested piece of logic.


> **Question**: Given an array of integers cards sorted in ascending order, find the starting and ending position of a given number. 

This differs from the problem in only two significant ways:

1. The numbers are sorted in increasing order.
2. We are looking for both first position and last position.

Here's the full code for solving the question, obtained by making minor modifications to our previous function:

"""


def first_position(cards, query):
    low, high = 0, len(cards) - 1

    def condition(middle_index):
        if cards[middle_index] == query:
            if middle_index > 0 and cards[middle_index - 1] == query:
                return 'left'
            return 'found'
        elif cards[middle_index] < query:
            return 'right'
        else:
            return 'left'

    return binary_search3(low, high, condition)


def last_position(cards, query):
    low, high = 0, len(cards) - 1

    def condition(middle_index):
        if cards[middle_index] == query:
            if middle_index < len(cards) - 1 and cards[middle_index + 1] == query:
                return 'right'
            return 'found'
        elif cards[middle_index] < query:
            return 'right'
        else:
            return 'left'

    return binary_search3(low, high, condition)


def first_and_last_position(cards, query):
    return first_position(cards, query), last_position(cards, query)

# nums = [5, 7, 7, 8, 8, 10]
# target = 8
# ans = first_and_last_position(nums, target)
# print(ans)

asscending_sorted = [
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

# for itr in asscending_sorted:
#     cards = itr['input']['cards']
#     query = itr['input']['query']
#     ans = first_and_last_position(cards,query)
#     print(f"cards: {cards} | query: {query} | ans: {ans}")


"""
## The Method - Revisited

Here's a systematic strategy we've applied for solving the problem:

1. State the problem clearly. Identify the input & output formats.
2. Come up with some example inputs & outputs. Try to cover all edge cases.
3. Come up with a correct solution for the problem. State it in plain English.
4. Implement the solution and test it using example inputs. Fix bugs, if any.
5. Analyze the algorithm's complexity and identify inefficiencies, if any.
6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.

Use this template for solving problems using this method: https://jovian.ai/aakashns/python-problem-solving-template

This seemingly obvious strategy will help you solve almost any programming problem you will face in an interview or coding assessment. 

The objective of this course is to rewire your brain to think using this method, by applying it over and over to different types of problems. 
This is a course about thinking about problems systematically and turning those thoughts into code.
"""
