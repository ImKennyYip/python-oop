# [Python Object Oriented Programming](https://www.youtube.com/playlist?list=PLnKe36F30Y4Ykmi2jE28BZahMgPAV3Dzv)
Python Object Oriented Programming Tutorials: https://www.youtube.com/playlist?list=PLnKe36F30Y4Ykmi2jE28BZahMgPAV3Dzv
Setup Python for Visual Studio Code: https://youtu.be/9o4gDQvVkLU

Welcome to Object Oriented Programming in Python. In this tutorial series, you will learn how to create classes, define data members (attributes) and member functions (methods), and create objects (instances of the classes). In addition, you will learn other concepts such as polymorphism, which includes operator overloading (dunder methods), and inheritance.

## The four pillars of OOP
* **Abstraction** - the most basic principle of a class is to provide behaviours as an interface. For instance, with a list, you can append, pop, sort, etc, but all the code is abstracted away. The code implementation and logic for how these methods work is irrelevant. We just care that it works, and we simply use the method name to call the function.

* **Polymorphism** - the word has greek origin - poly "many" and morph (form). 
Polymorphism refers to many forms, which can mean, one class, many same behaviors.
    * a list can be created using literals ```[]```, or with the constructor ```list()```, and with the constructor, you can pass in a string ```list("abc")```, which would create ```['a', 'b', 'c']```.
    * a list can append elements from another list using ```lst.extend(lst2)``` or ```lst += lst2```. The latter is implemented with a concept called operator overloading (dunder methods in python). ```+=``` is the operator

Polymorphism can also refer to many classes, one form, as in the case with duck typing. Multiple classes can have a function with the same name so that they could be called together.
    * a string, list, set, dict, etc, all have the ```len``` operator supported.

Polymorphism can refer to a class in a hierarchy (inheritance).


## Prerequisites
* Python
  * Input/Output
  * Variables
  * Primitive Data Types (```int, float, bool```)
  * Artithmetic Operators (```+, -, *, /, %, //, **```)
  * Logical Operators (```and, or, not```)
  * Comparitive Operators (```<, <=, >, >=, ==, !=```
  * Built-in Functions (```abs(), max(), min(), sum(), type()```)
  * Control Flow (```if, elif, else, while```)
  * For Loops
  * Collections (```str, lst, tuple, dict, set```)
  * Functions

## Topics
* **Abstraction (Classes, Data Members, Methods, Objects)**
    * Student Class [#1](https://youtu.be/ysiogYbQ_G8)
    * Credit Card Class [#2](https://youtu.be/m1s2xUiwsQw)
    * Vending Machine Class [#3](https://youtu.be/SyxapGNsFWk)

* **Polymorphism (Dunder Methods / Operator Overloading)**
    * Complex Number Class with add, sub, mul [#4](https://youtu.be/p5-D23sK_sU)
    * Fraction Class with add, sub, mul, truediv [#5]()
    * Multiply int × Fraction Class with mul, rmul [#6]()
    * Sorting Fraction Class with lt, gt, le, ge, eq, ne [#7]()

* **Abstraction**
    * Import Class Files [#8](https://youtu.be/F1SwUENsCgY)
      
* **Encapsulation (Data Hiding)**
    * Name Mangling [#9](https://youtu.be/6cvFzLB6hbA)

* **Abstraction**
    * Class Variables
  
* **Polymorphism (Inheritance)**
    * Duck Typing
    * Inheritance
    * Abstract Classes
    * Multiple Inheritance
    * super( ) Function
    * Inner/Nested Classes

