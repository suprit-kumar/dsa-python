# Binary Search Trees, Traversals and Balancing in Python

# https://jovian.ai/learn/data-structures-and-algorithms-in-python/lesson/lesson-2-binary-search-trees-traversals-and-balancing


"""
## Problem


In this notebook, we'll focus on solving the following problem:

> **QUESTION 1**: As a senior backend engineer at Jovian,
you are tasked with developing a fast in-memory data structure to manage profile information (username, name and email)
for 100 million users. It should allow the following operations to be performed efficiently:
>
> 1. **Insert** the profile information for a new user.
> 2. **Find** the profile information of a user, given their username
> 3. **Update** the profile information of a user, given their usrname
> 5. **List** all the users of the platform, sorted by username
>
> You can assume that usernames are unique.

Along the way, we will also solve several other questions related to binary trees and binary search trees that are often asked in coding interviews and assessments.

"""

"""
## The Method


Here's a systematic strategy we'll apply for solving problems:

1. State the problem clearly. Identify the input & output formats.
2. Come up with some example inputs & outputs. Try to cover all edge cases.
3. Come up with a correct solution for the problem. State it in plain English.
4. Implement the solution and test it using example inputs. Fix bugs, if any.
5. Analyze the algorithm's complexity and identify inefficiencies, if any.
6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.

"""

"""
## 1. State the problem clearly. Identify the input & output formats.

#### Problem

> We need to create a data structure which can store 100 million records and perform insertion, search, update and list operations efficiently.

#### Input

The key inputs to our data structure are user profiles, which contain the username, name and email of a user. 

A Python _class_ would be a great way to represent the information for a user. 
A class is a blueprint for creating _objects_. 
Everything in Python is an _object_ belonging to some _class_. Here's the simples possible class in Python, with nothing in it:



## 2. Come up with some example inputs & outputs. 

Let's create some sample user profiles that we can use to test our functions once we implement them.



## 3. Come up with a correct solution. State it in plain English.

Here's a simple and easy solution to the problem: we store the `User` objects in a list sorted by usernames. 

The various functions can be implemented as follows:

1. **Insert**: Loop through the list and add the new user at a position that keeps the list sorted.
2. **Find**: Loop through the list and find the user object with the username matching the query.
3. **Update**: Loop through the list, find the user object matching the query and update the details
4. **List**: Return the list of user objects.

We can use the fact usernames, which are are strings can be compared using the `<`, `>` and `==` operators in Python.





"""


class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User(username={self.username},name={self.name},email={self.email})"

    def __str__(self):
        return self.__repr__()


# 'biraj' < 'aakash' - False (Lexico graphic comparison)
# 'biraj' < 'hemanth' - True (Lexico graphic comparison)


class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if (user.username.lower() != self.users[i].username.lower()):
                if user.username < self.users[i].username:
                    break
                i += 1
            else:
                return
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if username == user.username:
                return user

    def update(self, user):
        target_user = self.find(user.username)
        target_user.name, target_user.email = user.name, user.email

    def remove(self, user):
        self.users.remove(self.find(user.username))

    def list_all(self):
        return self.users


aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

# database = UserDatabase()
# database.insert(hemanth)
# database.insert(aakash)
# database.insert(siddhant)
# database.insert(vishal)
# print(database.list_all())
# database.insert(biraj)
# print(database.list_all())
#
# user = database.find('siddhant')
# print(user)
# database.update(User('siddhant', 'Siddhant U', 'siddhant@example.com'))
# user = database.find('siddhant')
# # print(user)
# database.remove(User('siddhant', 'Siddhant U', 'siddhant@example.com'))
# print(database.list_all())


"""
## 5. Analyze the algorithm's complexity and identify inefficiencies for the above solution

The operations `insert`, `find`, `update` involves iterating over a list of users, in the worst case, they may take up to `N` iterations to return a result, where `N` is the total number of users. `list_all` however, simply returns the existing internal list of users. 

Thus, the time complexities of the various operations are:

1. Insert: **O(N)**
2. Find: **O(N)**
3. Update: **O(N)**
4. List: **O(1)**

**Exercise:** Verify that the space complexity of each operation is **O(1)**.

Is this good enough? To get a sense how long each function might take if there are 100 million users on the platform, 
we can simply run an `for` or `while` loop on 10 million numbers.


for i in range(100000000):
    j = i*i
    
    
It takes almost 10 seconds to execute all the iterations in the above cell. 

* A 10-second delay for fetching user profiles will lead to a suboptimal users experience and may cause many users to stop using the platform altogether. 
* The 10-second processing time for each profile request will also significantly limit the number of users that can access the platform at a time or increase the cloud infrastructure costs for the company by millions of dollars.

As a senior backend engineer, you must come up with a more efficient data structure! Choosing the right data structure for the requirements at hand is an important skill. It's apparent that a sorted list of users might not be the best data structure to organize profile information for millions of users. 

"""

"""
## 6. Apply the right technique to overcome the inefficiency

We can limit the number of iterations required for common operations like find, insert and update by organizing our data in the following structure, called a **binary tree**:

<img src="https://i.imgur.com/lVqP63n.png" width="520">



It's called a tree because it vaguely like an inverted tree trunk with branches. 
* The word "binary" indicates that each "node" in the tree can have at most 2 children (left or right). 
* Nodes can have 0, 1 or 2 children. Nodes that do not have any children are sometimes also called "leaves".
* The single node at the top is called the "root" node, and it typically where operations like search, insertion etc. begin.

<img src="https://i.imgur.com/TZHMKJr.png" width="400">


## Balanced Binary Search Trees

<img src="https://i.imgur.com/Mqef5b3.png" width="520">

For our use case, we require the binary tree to have some additional properties:

1. **Keys and Values**: Each node of the tree stores a key (a username) and a value (a `User` object). 
Only keys are shown in the picture above for brevity. 
A binary tree where nodes have both a key and a value is often referred to as a **map** or **treemap** (because it maps keys to values).

2. **Binary Search Tree**: The *left subtree* of any node only contains nodes with keys that are lexicographically 
smaller than the node's key, and the *right subtree* of any node only contains nodes with keys that lexicographically 
larger than the node's key. A tree that satisfies this property is called a **binary search trees**, 
and it's easy to locate a specific key by traversing a single path down from the root note.


3. **Balanced Tree**: The tree is **balanced** i.e. it does not skew too heavily to one side or the other. 
The left and right subtrees of any node shouldn't differ in height/depth by more than 1 level.


### Height of a Binary Tree

The number of levels in a tree is called its height. As you can tell from the picture above, 
each level of a tree contains twice as many nodes as the previous level. 

For a tree of height `k`, here's a list of the number of nodes at each level:

Level 0: `1`

Level 1: `2`

Level 2: `4` i.e. `2^2`

Level 3: `8` i.e. `2^3`

...

Level k-1: `2^(k-1)`

If the total number of nodes in the tree is `N`, then it follows that

```
N = 1 + 2^1 + 2^2 + 2^3 + ... + 2^(k-1)
```


We can simplify this equation by adding `1` on each side:

```
N + 1 = 1 + 1 + 2^1 + 2^2 + 2^3 + ... + 2^(k-1) 

N + 1 = 2^1 + 2^1 + 2^2+ 2^3 + ... + 2^(k-1) 

N + 1 = = 2^2 + 2^2 + 2^3 + ... + 2^(k-1)

N + 1 = = 2^3 + 2^3 + ... + 2^(k-1)

...

N + 1 = 2^(k-1) + 2^(k-1)

N + 1 = 2^k

k = log(N + 1) <= log(N) + 1 

```

Thus, to store `N` records we require a balanced binary search tree (BST) of height no larger than `log(N) + 1`. 
This is a very useful property, in combination with the fact that nodes are arranged in a way that makes it easy to find a specific key by 
following a single path down from the root. 

As we'll see soon, the `insert`, `find` and `update` operations in a balanced BST have time complexity `O(log N)` 
since they all involve traversing a single path down from the root of the tree.



"""

"""
## Binary Tree

> **QUESTION 2**: Implement a binary tree using Python, and show its usage with some examples.

To begin, we'll create simple binary tree (without any of the additional properties) containing numbers as keys within nodes. Here's an example:

<img src="https://i.imgur.com/hg2ZG5h.png" width="240">

Here's a simple class representing a node within a binary tree.

"""


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __repr__(self):
        return f"(left: {self.left} | key: {self.key} | right:{self.right})"

    def __str__(self):
        return self.__repr__()


# node0 = TreeNode(3)
# node1 = TreeNode(4)
# node2 = TreeNode(5)


# print(node0)
# print(node0.key)
# print(node0.left)

# node0.left = node1
# node0.right = node2
#
# tree = node0
# print(tree.key)
# print(tree.left.key)
# print(tree.right.key)


tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))


# Helper function to create Tree

def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node


tree2 = parse_tuple(tree_tuple)
#
# print(tree2.key)
# print(tree2.left.key, tree2.right.key)
# print(tree2.left.left.key, tree2.left.right, tree2.right.left.key, tree2.right.right.key)
# print(tree2.right.left.right.key, tree2.right.right.left.key, tree2.right.right.right.key)


"""
**Exercise:** 
Define a function `tree_to_tuple` that converts a binary tree into a tuple representing the same tree. 
E.g. `tree_to_tuple` converts the tree created above to the tuple `((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))`. 
*Hint*: Use recursion.
"""


def tree_to_tuple(node):
    if isinstance(node, TreeNode):
        # check if left and right node are equal to None if so, then it means it has no child nodes
        # and simply just return key node
        if node.left is None and node.right is None:
            return node.key
        # use recursion to iterate through each subtree and get the left , key and right nodes
        return tree_to_tuple(node.left), node.key, tree_to_tuple(node.right)
    else:
        return node


# tree3 = parse_tuple(tree_tuple)
# print(tree_to_tuple(tree3))


# Let's create another helper function to display all the keys in a tree-like structure for easier visualization.

def display_keys(node, space='\t', level=0):
    # print(node.key if node else None, level)

    # If the node is empty
    if node is None:
        print(space * level + '∅')
        return

        # If the node is a leaf
    if node.left is None and node.right is None:
        print(space * level + str(node.key))
        return

    # If the node has children
    display_keys(node.right, space, level + 1)
    print(space * level + str(node.key))
    display_keys(node.left, space, level + 1)


# display_keys(tree3,space='  ')





# def traverse_in_order(node):
#     if node is None:
#         return []
#     return(traverse_in_order(node.left) +
#            [node.key] +
#            traverse_in_order(node.right))


# print(traverse_in_order(tree2))



def traverse_in_order(node):
    if node is None:
        return []
    left = traverse_in_order(node.left)
    root = [node.key]
    right = traverse_in_order(node.right)

    return left + root + right # concatenate the lists

print('In-order',traverse_in_order(tree2))


def traverse_pre_order(node):
    # if node is None:
    #     return
    # print(node.key,end=" ")
    # traverse_pre_order(node.left)
    # traverse_pre_order(node.right)

    if node is None:
        return []
    root = [node.key]
    left = traverse_pre_order(node.left)
    right = traverse_pre_order(node.right)

    return root + left + right

# traverse_pre_order(tree2)
print('Pre-order',traverse_pre_order(tree2))

def traverse_post_order(node):
    if node is None:
        return

    traverse_post_order(node.left)
    traverse_post_order(node.right)
    print(node.key, end=" ")

    # if node is None:
    #     return []
    #
    # left = traverse_post_order(node.left)
    # right = traverse_post_order(node.right)
    # root = [node.key]
    #
    # return  left + right + root


traverse_post_order(tree2)
# print(traverse_post_order(tree2))