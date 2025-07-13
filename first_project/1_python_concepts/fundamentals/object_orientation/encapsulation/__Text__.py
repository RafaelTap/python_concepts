#encapsulation

"""
encapsulation is a very important concept, the aim is to protect internals datas using modifiers
exposing only the necessary.

__ -> make the data private. only methods inside the class can access the data.
Python has not a real private attribute, we still can access the privates attributes.
See the archive "Account.py".

_ -> indicate that the attribute can be manipulated only internally (inside class).

"""

#decorators

"""
using the decorator @property, we can protect the attributes and access only through decorated 
methods. See archive "Account_2.py".
@property: this decorator allows define methods of classes tha can be accessed as instance attributes
, offering a
"""