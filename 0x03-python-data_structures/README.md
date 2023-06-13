Data Structures in Python
Built-in data structures in Python can be divided into two broad categories: mutable and immutable. Mutable (from Latin mutabilis, changeable) data structures are those which we can modify -- for example, by adding, removing, or changing their elements. Python has three mutable data structures: lists, dictionaries, and sets. Immutable data structures, on the other hand, are those that we cannot modify after their creation. The only basic built-in immutable data structure in Python is a tuple.

Python also has some advanced data structures, such as stacks or queues, which can be implemented with basic data structures. However, these are rarely used in data science and are more common in the field of software engineering and implementation of complex algorithms, so we won't discuss them in this tutorial.

Different Python third-party packages implement their own data structures, like DataFrames and Series in pandas or arrays in NumPy. However, we will not talk about them here, either, because these are the topics of more specific tutorials (such as How to Create and Use a Pandas DataFrame or NumPy Tutorial: Data Analysis with Python).

Let's start with the mutable data structures: lists, dictionaries, and sets.

Lists
Lists in Python are implemented as dynamic mutable arrays which hold an ordered collection of items.

First, in many programming languages, arrays are data structures that contain a collection of elements of the same data types (for instance, all elements are integers). However, in Python, lists can contain heterogeneous data types and objects. For instance, integers, strings, and even functions can be stored within the same list. Different elements of a list can be accessed by integer indices where the first element of a list has the index of 0. This property derives from the fact that in Python, lists are ordered, which means they retain the order in which you insert the elements into the list.
