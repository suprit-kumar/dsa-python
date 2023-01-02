# Binary Search Trees, Traversals and Balancing in Python

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

database = UserDatabase()
database.insert(hemanth)
database.insert(aakash)
database.insert(siddhant)
database.insert(vishal)
print(database.list_all())
database.insert(biraj)
print(database.list_all())

user = database.find('siddhant')
print(user)
database.update(User('siddhant', 'Siddhant U', 'siddhant@example.com'))
user = database.find('siddhant')
# print(user)
database.remove(User('siddhant', 'Siddhant U', 'siddhant@example.com'))
print(database.list_all())



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