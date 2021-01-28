0x0A. Python - Inheritance
==========================

Foundations - Higher-level programming ― Python

_By Guillaume, CTO at Holberton School_

_Weight: 1_

Project over - took place from 01-19-2021 to 01-20-2021 - you're done with 150% of tasks.

QA review fully automated.

#### In a nutshell…

* **Auto QA review:** 170.0/170 mandatory & 10.65/21 optional
* **Altogether:**  **150.71%**
    * Mandatory: 100.0%
    * Optional: 50.71%
    * Calculation:  100.0% + (100.0% * 50.71%)  == **150.71%**

Resources
---------

**Read or watch**:

* [Inheritance](/rltoken/E2Bs3bxX8GuSEKuWqswU7g "Inheritance")
* [Multiple inheritance](/rltoken/auwnZOKkBZ97JaLtrMryuA "Multiple inheritance")
* [Inheritance in Python](/rltoken/ycewwwPmDpXqRp2R1FW51w "Inheritance in Python")
* [Learn to Program 10 : Inheritance Magic Methods](/rltoken/F8LUzmvPI4yur1Z37ZM1fQ "Learn to Program 10 : Inheritance Magic Methods")

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/Q_ghM0TZb99Dr6cesCoy3g "explain to anyone"), **without the help of Google**:

### General

* Why Python programming is awesome
* What is a superclass, baseclass or parentclass
* What is a subclass
* How to list all attributes and methods of a class or instance
* When can an instance have new attributes
* How to inherit class from another
* How to define a class with multiple base classes
* What is the default class every class inherit from
* How to override a method or attribute inherited from the base class
* Which attributes or methods are available by heritage to subclasses
* What is the purpose of inheritance
* What are, when and how to use `isinstance`, `issubclass`, `type` and `super` built-in functions

Requirements
------------

### Python Scripts

* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the `PEP 8` style (version `1.7.*`)
* All your files must be executable
* The length of your files will be tested using `wc`

### Python Test Cases

* Allowed editors: `vi`, `vim`, `emacs`
* All your files should end with a new line
* All your test files should be inside a folder `tests`
* All your test files should be text files (extension: `.txt`)
* All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case

* * *

Quiz questions
--------------

Show

#### Question #0

What do these lines print?

    class Base():
        """ My base class """
    
        __nb_instances = 0
    
        def __init__(self):
            Base.__nb_instances += 1
            self.id = Base.__nb_instances
    
    b = Base()
    print(b.id)
    

* [ ] 
    
    None
    
* [ ] 
    
    0
    
* [x] 
    
    1
    

#### Question #1

What do these lines print?

    class Base():
        """ My base class """
    
        __nb_instances = 0
    
        def __init__(self):
            Base.__nb_instances += 1
            self.id = Base.__nb_instances
    
    for i in range(3):
        b = Base()
    print(b.id)
    

* [ ] 
    
    None
    
* [x] 
    
    3
    
* [ ] 
    
    4
    
* [ ] 
    
    2
    

#### Question #2

What do these lines print?

    class Base():
        """ My base class """
    
        __nb_instances = 0
    
        def __init__(self):
            Base.__nb_instances += 1
            self.id = Base.__nb_instances
    
    class User(Base):
        """ My User class """
        pass
    
    u = User()
    print(u.id)
    

* [ ] 
    
    None
    
* [ ] 
    
    0
    
* [x] 
    
    1
    
* [ ] 
    
    2
    

#### Question #3

What do these lines print?

    class Base():
        """ My base class """
    
        __nb_instances = 0
    
        def __init__(self):
            Base.__nb_instances += 1
            self.id = Base.__nb_instances
    
    class User(Base):
        """ My User class """
        pass
    
    for i in range(4):
        u = User()
    print(u.id)
    

* [x] 
    
    4
    
* [ ] 
    
    3
    
* [ ] 
    
    5
    
* [ ] 
    
    None
    

#### Question #4

What do these lines print?

    class Base():
        """ My base class """
    
        __nb_instances = 0
    
        def __init__(self):
            Base.__nb_instances += 1
            self.id = Base.__nb_instances
    
    class User(Base):
        """ My User class """
        pass
    
    b = Base()
    u = User()
    print(u.id)
    

* [ ] 
    
    0
    
* [ ] 
    
    1
    
* [x] 
    
    2
    
* [ ] 
    
    3
    

#### Question #5

What do these lines print?

    class Base():
        """ My base class """
    
        __nb_instances = 0
    
        def __init__(self):
            Base.__nb_instances += 1
            self.id = Base.__nb_instances
    
    class User(Base):
        """ My User class """
    
        def __init__(self):
            self.id = 89
    
    u = User()
    print(u.id)
    

* [x] 
    
    89
    
* [ ] 
    
    90
    
* [ ] 
    
    1
    

#### Question #6

What do these lines print?

    class Base():
        """ My base class """
    
        __nb_instances = 0
    
        def __init__(self):
            Base.__nb_instances += 1
            self.id = Base.__nb_instances
    
    class User(Base):
        """ My User class """
    
        def __init__(self):
            super().__init__()
    
    u = User()
    print(u.id)
    

* [ ] 
    
    None
    
* [ ] 
    
    0
    
* [x] 
    
    1
    
* [ ] 
    
    2
    

#### Question #7

What do these lines print?

    class Base():
        """ My base class """
    
        __nb_instances = 0
    
        def __init__(self):
            Base.__nb_instances += 1
            self.id = Base.__nb_instances
    
    class User(Base):
        """ My User class """
    
        def __init__(self):
            self.id = 89
            super().__init__()
    
    u = User()
    print(u.id)
    

* [ ] 
    
    89
    
* [ ] 
    
    90
    
* [x] 
    
    1
    

#### Question #8

What do these lines print?

    class Base():
        """ My base class """
    
        __nb_instances = 0
    
        def __init__(self):
            Base.__nb_instances += 1
            self.id = Base.__nb_instances
    
    class User(Base):
        """ My User class """
    
        def __init__(self):
            super().__init__()
            self.id = 89
    
    u = User()
    print(u.id)
    

* [x] 
    
    89
    
* [ ] 
    
    90
    
* [ ] 
    
    1
    

#### Question #9

What do these lines print?

    class Base():
        """ My base class """
    
        __nb_instances = 0
    
        def __init__(self):
            Base.__nb_instances += 1
            self.id = Base.__nb_instances
    
    class User(Base):
        """ My User class """
    
        def __init__(self):
            super().__init__()
            self.id += 99
    
    u = User()
    print(u.id)
    

* [ ] 
    
    99
    
* [x] 
    
    100
    
* [ ] 
    
    1
    

* * *

Tasks
-----

Done?!  
Help

×

#### Students who are done with "0. Lookup"

#### 0\. Lookup mandatory

Score: 100.00% (Checks completed: 100.00%)

Write a function that returns the list of available attributes and methods of an object:

* Prototype: `def lookup(obj):`
* Returns a `list` object
* You are not allowed to import any module

    guillaume@ubuntu:~/0x0A$ cat 0-main.py
    #!/usr/bin/python3
    lookup = __import__('0-lookup').lookup
    
    class MyClass1(object):
        pass
    
    class MyClass2(object):
        my_attr1 = 3
        def my_meth(self):
            pass
    
    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))
    
    guillaume@ubuntu:~/0x0A$ ./0-main.py
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'my_attr1', 'my_meth']
    ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
    guillaume@ubuntu:~/0x0A$ 
    

**No test cases needed**

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0A-python-inheritance`
* File: `0-lookup.py`

Check your code?

×

#### Correction of "0. Lookup"

Start a new test

* * *

#### Result:

Commit ID used: `4ed23c5830ce65160957da25ddb7ffbb3384c5fb`

Check 0

Check 1

Check 2

Check 3

Check 4

Check 5

Check 6

Check 7

Check 8

Check 9

Check 10

Check 11

Check 12

Check 13

Check 14

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

QA Review

×

#### 0\. Lookup

Done?!  
Help

×

#### Students who are done with "1. My list"

#### 1\. My list mandatory

Score: 100.00% (Checks completed: 100.00%)

Write a class `MyList` that inherits from `list`:

* Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
* You can assume that all the elements of the list will be of type `int`
* You are not allowed to import any module

    guillaume@ubuntu:~/0x0A$ cat 1-main.py
    #!/usr/bin/python3
    MyList = __import__('1-my_list').MyList
    
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)
    
    guillaume@ubuntu:~/0x0A$ ./1-main.py
    [1, 4, 2, 3, 5]
    [1, 2, 3, 4, 5]
    [1, 4, 2, 3, 5]
    guillaume@ubuntu:~/0x0A$ 
    

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0A-python-inheritance`
* File: `1-my_list.py, tests/1-my_list.txt`

Check your code?

×

#### Correction of "1. My list"

Start a new test

* * *

#### Result:

Commit ID used: `d524eaf5aa2c8b0ace2707d29a5f45ace708e75f`

Check 0

Check 1

Check 2

Check 3

Check 4

Check 5

Check 6

Check 7

Check 8

Check 9

Check 10

Check 11

Check 12

Check 13

Check 14

Check 15

Check 16

Check 17

Check 18

Check 19

Check 20

Check 21

Check 22

Check 23

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

QA Review

×

#### 1\. My list

Done?!  
Help

×

#### Students who are done with "2. Exact same object"

#### 2\. Exact same object mandatory

Score: 100.00% (Checks completed: 100.00%)

Write a function that returns `True` if the object is _exactly_ an instance of the specified class ; otherwise `False`.

* Prototype: `def is_same_class(obj, a_class):`
* You are not allowed to import any module

    guillaume@ubuntu:~/0x0A$ cat 2-main.py
    #!/usr/bin/python3
    is_same_class = __import__('2-is_same_class').is_same_class
    
    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
    
    guillaume@ubuntu:~/0x0A$ ./2-main.py
    1 is an instance of the class int
    guillaume@ubuntu:~/0x0A$ 
    

**No test cases needed**

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0A-python-inheritance`
* File: `2-is_same_class.py`

Check your code?

×

#### Correction of "2. Exact same object"

Start a new test

* * *

#### Result:

Commit ID used: `4ed23c5830ce65160957da25ddb7ffbb3384c5fb`

Check 0

Check 1

Check 2

Check 3

Check 4

Check 5

Check 6

Check 7

Check 8

Check 9

Check 10

Check 11

Check 12

Check 13

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

QA Review

×

#### 2\. Exact same object

Done?!  
Help

×

#### Students who are done with "3. Same class or inherit from"

#### 3\. Same class or inherit from mandatory

Score: 100.00% (Checks completed: 100.00%)

Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`.

* Prototype: `def is_kind_of_class(obj, a_class):`
* You are not allowed to import any module

    guillaume@ubuntu:~/0x0A$ cat 3-main.py
    #!/usr/bin/python3
    is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class
    
    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))
    
    guillaume@ubuntu:~/0x0A$ ./3-main.py
    1 comes from int
    1 comes from object
    guillaume@ubuntu:~/0x0A$ 
    

**No test cases needed**

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0A-python-inheritance`
* File: `3-is_kind_of_class.py`

Check your code?

×

#### Correction of "3. Same class or inherit from"

Start a new test

* * *

#### Result:

Commit ID used: `4ed23c5830ce65160957da25ddb7ffbb3384c5fb`

Check 0

Check 1

Check 2

Check 3

Check 4

Check 5

Check 6

Check 7

Check 8

Check 9

Check 10

Check 11

Check 12

Check 13

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

QA Review

×

#### 3\. Same class or inherit from

Done?!  
Help

×

#### Students who are done with "4. Only sub class of"

#### 4\. Only sub class of mandatory

Score: 100.00% (Checks completed: 100.00%)

Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`.

* Prototype: `def inherits_from(obj, a_class):`
* You are not allowed to import any module

    guillaume@ubuntu:~/0x0A$ cat 4-main.py
    #!/usr/bin/python3
    inherits_from = __import__('4-inherits_from').inherits_from
    
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
    
    guillaume@ubuntu:~/0x0A$ ./4-main.py
    True inherited from class int
    True inherited from class object
    guillaume@ubuntu:~/0x0A$ 
    

**No test cases needed**

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0A-python-inheritance`
* File: `4-inherits_from.py`

Check your code?

×

#### Correction of "4. Only sub class of"

Start a new test

* * *

#### Result:

Commit ID used: `9c11f16ac389dc3781a1f9455990ace493cec7f3`

Check 0

Check 1

Check 2

Check 3

Check 4

Check 5

Check 6

Check 7

Check 8

Check 9

Check 10

Check 11

Check 12

Check 13

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

QA Review

×

#### 4\. Only sub class of

Done?!  
Help

×

#### Students who are done with "5. Geometry module"

#### 5\. Geometry module mandatory

Score: 100.00% (Checks completed: 100.00%)

Write an empty class `BaseGeometry`.

* You are not allowed to import any module

    guillaume@ubuntu:~/0x0A$ cat 5-main.py
    #!/usr/bin/python3
    BaseGeometry = __import__('5-base_geometry').BaseGeometry
    
    bg = BaseGeometry()
    
    print(bg)
    print(dir(bg))
    print(dir(BaseGeometry))
    
    guillaume@ubuntu:~/0x0A$ ./5-main.py
    <5-base_geometry.BaseGeometry object at 0x7f2050c69208>
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
    guillaume@ubuntu:~/0x0A$ 
    

**No test cases needed**

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0A-python-inheritance`
* File: `5-base_geometry.py`

Check your code?

×

#### Correction of "5. Geometry module"

Start a new test

* * *

#### Result:

Commit ID used: `71ae922e6fb3b5df09ff98631e131f69e2855327`

Check 0

Check 1

Check 2

Check 3

Check 4

Check 5

Check 6

Check 7

Check 8

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

QA Review

×

#### 5\. Geometry module

Done?!  
Help

×

#### Students who are done with "6. Improve Geometry"

#### 6\. Improve Geometry mandatory

Score: 100.00% (Checks completed: 100.00%)

Write a class `BaseGeometry` (based on `5-base_geometry.py`).

* Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
* You are not allowed to import any module

    guillaume@ubuntu:~/0x0A$ cat 6-main.py
    #!/usr/bin/python3
    BaseGeometry = __import__('6-base_geometry').BaseGeometry
    
    bg = BaseGeometry()
    
    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
    
    guillaume@ubuntu:~/0x0A$ ./6-main.py
    [Exception] area() is not implemented
    guillaume@ubuntu:~/0x0A$ 
    

**No test cases needed**

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0A-python-inheritance`
* File: `6-base_geometry.py`

Check your code?

×

#### Correction of "6. Improve Geometry"

Start a new test

* * *

#### Result:

Commit ID used: `71ae922e6fb3b5df09ff98631e131f69e2855327`

Check 0

Check 1

Check 2

Check 3

Check 4

Check 5

Check 6

Check 7

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

QA Review

×

#### 6\. Improve Geometry

Done?!  
Help

×

#### Students who are done with "7. Integer validator"

#### 7\. Integer validator mandatory

Score: 100.00% (Checks completed: 100.00%)

Write a class `BaseGeometry` (based on `6-base_geometry.py`).

* Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
* Public instance method: `def integer_validator(self, name, value):` that validates `value`:
    * you can assume `name` is always a string
    * if `value` is not an integer: raise a `TypeError` exception, with the message `<name> must be an integer`
    * if `value` is less or equal to 0: raise a `ValueError` exception with the message `<name> must be greater than 0`
* You are not allowed to import any module

    guillaume@ubuntu:~/0x0A$ cat 7-main.py
    #!/usr/bin/python3
    BaseGeometry = __import__('7-base_geometry').BaseGeometry
    
    bg = BaseGeometry()
    
    bg.integer_validator("my_int", 12)
    bg.integer_validator("width", 89)
    
    try:
        bg.integer_validator("name", "John")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
    
    try:
        bg.integer_validator("age", 0)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
    
    try:
        bg.integer_validator("distance", -4)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
    
    guillaume@ubuntu:~/0x0A$ ./7-main.py
    [TypeError] name must be an integer
    [ValueError] age must be greater than 0
    [ValueError] distance must be greater than 0
    guillaume@ubuntu:~/0x0A$ 
    

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0A-python-inheritance`
* File: `7-base_geometry.py, tests/7-base_geometry.txt`

Check your code?

×

#### Correction of "7. Integer validator"

Start a new test

* * *

#### Result:

Commit ID used: `6b2b4aa64c16dc28610d8086aa142bd2140334de`

Check 0

Check 1

Check 2

Check 3

Check 4

Check 5

Check 6

Check 7

Check 8

Check 9

Check 10

Check 11

Check 12

Check 13

Check 14

Check 15

Check 16

Check 17

Check 18

Check 19

Check 20

Check 21

Check 22

Check 23

Check 24

Check 25

Check 26

Check 27

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

QA Review

×

#### 7\. Integer validator

Done?!  
Help

×

#### Students who are done with "8. Rectangle"

#### 8\. Rectangle mandatory

Score: 100.00% (Checks completed: 100.00%)

Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`).

* Instantiation with `width` and `height`: `def __init__(self, width, height):`
    * `width` and `height` must be private. No getter or setter
    * `width` and `height` must be positive integers, validated by `integer_validator`

    guillaume@ubuntu:~/0x0A$ cat 8-main.py
    #!/usr/bin/python3
    Rectangle = __import__('8-rectangle').Rectangle
    
    r = Rectangle(3, 5)
    
    print(r)
    print(dir(r))
    
    try:
        print("Rectangle: {} - {}".format(r.width, r.height))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
    
    try:
        r2 = Rectangle(4, True)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
    
    guillaume@ubuntu:~/0x0A$ ./8-main.py
    <8-rectangle.Rectangle object at 0x7f6f488f7eb8>
    ['_Rectangle__height', '_Rectangle__width', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator']
    [AttributeError] 'Rectangle' object has no attribute 'width'
    [TypeError] height must be an integer
    guillaume@ubuntu:~/0x0A$ 
    

**No test cases needed**

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0A-python-inheritance`
* File: `8-rectangle.py`

Check your code?

×

#### Correction of "8. Rectangle"

Start a new test

* * *

#### Result:

Commit ID used: `08daff18a0fc31c96e7248d70bcf8c67bc66ea4a`

Check 0

Check 1

Check 2

Check 3

Check 4

Check 5

Check 6

Check 7

Check 8

Check 9

Check 10

Check 11

Check 12

Check 13

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

QA Review

×

#### 8\. Rectangle

Done?!  
Help

×

#### Students who are done with "9. Full rectangle"

#### 9\. Full rectangle mandatory

Score: 100.00% (Checks completed: 100.00%)

Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`). (task based on `8-rectangle.py`)

* Instantiation with `width` and `height`: `def __init__(self, width, height):`:
    * `width` and `height` must be private. No getter or setter
    * `width` and `height` must be positive integers validated by `integer_validator`
* the `area()` method must be implemented
* `print()` should print, and `str()` should return, the following rectangle description: `[Rectangle] <width>/<height>`

    guillaume@ubuntu:~/0x0A$ cat 9-main.py
    #!/usr/bin/python3
    Rectangle = __import__('9-rectangle').Rectangle
    
    r = Rectangle(3, 5)
    
    print(r)
    print(r.area())
    
    guillaume@ubuntu:~/0x0A$ ./9-main.py
    [Rectangle] 3/5
    15
    guillaume@ubuntu:~/0x0A$ 
    

**No test cases needed**

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0A-python-inheritance`
* File: `9-rectangle.py`

Check your code?

×

#### Correction of "9. Full rectangle"

Start a new test

* * *

#### Result:

Commit ID used: `ee4f8372d95969eaf4060a887318ed41a47c0844`

Check 0

Check 1

Check 2

Check 3

Check 4

Check 5

Check 6

Check 7

Check 8

Check 9

Check 10

Check 11

Check 12

Check 13

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

QA Review

×

#### 9\. Full rectangle

Done?!  
Help

×

#### Students who are done with "10. Square #1"

#### 10\. Square #1 mandatory

Score: 100.00% (Checks completed: 100.00%)

Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`):

* Instantiation with `size`: `def __init__(self, size):`:
    * `size` must be private. No getter or setter
    * `size` must be a positive integer, validated by `integer_validator`
* the `area()` method must be implemented

    guillaume@ubuntu:~/0x0A$ cat 10-main.py
    #!/usr/bin/python3
    Square = __import__('10-square').Square
    
    s = Square(13)
    
    print(s)
    print(s.area())
    
    guillaume@ubuntu:~/0x0A$ ./10-main.py
    [Rectangle] 13/13
    169
    guillaume@ubuntu:~/0x0A$ 
    

**No test cases needed**

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0A-python-inheritance`
* File: `10-square.py`

Check your code?

×

#### Correction of "10. Square #1"

Start a new test

* * *

#### Result:

Commit ID used: `e201f334af2c8706721a018a6f167217df7ac145`

Check 0

Check 1

Check 2

Check 3

Check 4

Check 5

Check 6

Check 7

Check 8

Check 9

Check 10

Check 11

Check 12

Check 13

Requirement success

Requirement fail

Code success

Code fail

Efficiency success

Efficiency fail

Text answer success

Text answer fail

QA Review

×

#### 10\. Square #1

Done?!  
Help

×

#### Students who are done with "11. Square #2"

#### 11\. Square #2 mandatory

Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`). (task based on `10-square.py`).

* Instantiation with `size`: `def __init__(self, size):`:
    * `size` must be private. No getter or setter
    * `size` must be a positive integer, validated by `integer_validator`
* the `area()` method must be implemented
* `print()` should print, and `str()` should return, the square description: `[Square] <width>/<height>`

    guillaume@ubuntu:~/0x0A$ cat 11-main.py
    #!/usr/bin/python3
    Square = __import__('11-square').Square
    
    s = Square(13)
    
    print(s)
    print(s.area())
    
    guillaume@ubuntu:~/0x0A$ ./11-main.py
    [Square] 13/13
    169
    guillaume@ubuntu:~/0x0A$ 
    

**No test cases needed**

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0A-python-inheritance`
* File: `11-square.py`

#### 12\. My integer #advanced

Write a class `MyInt` that inherits from `int`:

* `MyInt` is a rebel. `MyInt` has `==` and `!=` operators inverted
* You are not allowed to import any module

    guillaume@ubuntu:~/0x0A$ cat 100-main.py
    #!/usr/bin/python3
    MyInt = __import__('100-my_int').MyInt
    
    my_i = MyInt(3)
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)
    
    guillaume@ubuntu:~/0x0A$ ./100-main.py
    3
    False
    True
    guillaume@ubuntu:~/0x0A$ 
    

**No test cases needed**

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0A-python-inheritance`
* File: `100-my_int.py`

#### 13\. Can I? #advanced

Write a function that adds a new attribute to an object if it’s possible:

* Raise a `TypeError` exception, with the message `can't add new attribute` if the object can’t have new attribute
* You are not allowed to use `try/catch`
* You are not allowed to import any module

    guillaume@ubuntu:~/0x0A$ cat 101-main.py
    #!/usr/bin/python3
    add_attribute = __import__('101-add_attribute').add_attribute
    
    class MyClass():
        pass
    
    mc = MyClass()
    add_attribute(mc, "name", "John")
    print(mc.name)
    
    try:
        a = "My String"
        add_attribute(a, "name", "Bob")
        print(a.name)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
    
    guillaume@ubuntu:~/0x0A$ ./101-main.py
    John
    [TypeError] can't add new attribute
    guillaume@ubuntu:~/0x0A$ 
    

**No test cases needed**

**Repo:**

* GitHub repository: `holbertonschool-higher_level_programming`
* Directory: `0x0A-python-inheritance`
* File: `101-add_attribute.py`

#### 13\. Can I?
