"""

AROUND CONSTANT VARIABLE, IN PYTHON IT NOT EXIST. WHAT WE HAVE TO DO IS WRITE THE NAME OF CONSTANT VARIABLE
IN UPPER CASE, OR BEGIN WITH "c_".
EXEMPLES: C_PI, PI.

SINCE PYTHON 3.8 WE CAN CREATE CONSTANTS USING THE LIBRARY "constant" OR THE DECORATOR "@final" OF MODULE
 TYPING.

"""
from typing import final, Final

PI: Final[float] = 3.14
ray = 5
area = PI * (ray ** 2)
print("VALOR DE PI É ", PI)
print(area)

c_PI = 3.14
ray = 8
area = c_PI * (ray ** 2)
print(area)