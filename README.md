# [Python Object Oriented Programming](https://www.youtube.com/playlist?list=PLnKe36F30Y4Ykmi2jE28BZahMgPAV3Dzv)
Python Object Oriented Programming Tutorials: https://www.youtube.com/playlist?list=PLnKe36F30Y4Ykmi2jE28BZahMgPAV3Dzv
Setup Python for Visual Studio Code: https://youtu.be/9o4gDQvVkLU

Welcome to Object Oriented Programming in Python. In this tutorial series, you will learn how to create classes, define data members (attributes) and member functions (methods), and create objects (instances of the classes). In addition, you will learn concepts from the 4 pillars of object oriented programming: Abstraction, Polymorphism, Encapsulation, and Inheritance.

## Topics
* **Abstraction (Classes, Data Members, Methods, Objects)**
    * Student Class [#1](https://youtu.be/ysiogYbQ_G8)
    * Credit Card Class [#2](https://youtu.be/m1s2xUiwsQw)
    * Vending Machine Class [#3](https://youtu.be/SyxapGNsFWk)

* **Polymorphism (Dunder Methods / Operator Overloading)**
    * Complex Number Class with add, sub, mul [#4](https://youtu.be/p5-D23sK_sU)
    * Fraction Class with add, sub, mul, truediv [#5](https://youtu.be/gun6lwny3GE)
    * Multiply int × Fraction Class with mul, rmul [#6](https://youtu.be/nYNVoM6N2so)
    * Sorting Fraction Class with lt, gt, le, ge, eq, ne [#7](https://youtu.be/TT4SRUmrWNs)

* **Abstraction**
    * Import Class Files [#8](https://youtu.be/F1SwUENsCgY)
      
* **Encapsulation (Data Hiding)**
    * Name Mangling [#9](https://youtu.be/6cvFzLB6hbA)

* **Abstraction**
    * Class Variables
  
* **Inheritance**
    * Duck Typing (Polymorphism)
    * Inheritance
    * super( ) Function
    * Multilevel Inheritance (Polymorphism)
    * Abstract Classes
    * Multiple Inheritance (Polymorphism)
    * "Deadly Diamond of Death" Problem
    * Inner/Nested Classes (Abstraction)


## The 4 pillars of OOP
* **Abstraction** - the most basic principle of a class is to provide behaviours as an interface. For instance, with a list, you can append, pop, sort, etc, but all the code is abstracted away. The code implementation and logic for how these methods work is irrelevant. We just care that it works, and we simply use the method name to call the function. This is known as working with a "black box". (You know that it's a box but you can't see inside because it's black). A class has data members (also called fields or attributes) and member functions (also called methods).

* **Polymorphism** - the word has greek origin - poly "many" and morph (form). Polymorphism refers to many forms.
    * Polymorphism can refer to one class, many same behaviors.
        * a list can be created using literals ```[]```, or with the constructor ```list()```, and with the constructor, you can pass in a string ```list("abc")```, which would create ```['a', 'b', 'c']```.
        * a list can append elements from another list using ```lst.extend(lst2)``` or ```lst += lst2```. The latter is implemented with a concept called operator overloading (dunder methods in python). ```+=``` is the operator

    * Polymorphism can also refer to one form shared by many different classes, as in the case with duck typing. Multiple classes can have a function with the same name so that they could be called together.
        * a string, list, set, dict, etc, all have the ```len``` operator supported.

* **Encapsulation** - involves wrapping data members(fields, or attributes) and methods in a single unit (class) and restricting direct access using access modifiers.
  * Delegation
      * a list allows you to use the set and get operators with ```lst[i]```, instead of letting you directly access the array data. This is important because if you tried to access and modify the data in a list directly, you would be able to do things like access a memory address outside the index range of a list. Therefore, instead of directly access the underlying array data of a list, you access elements using the provided set/get operators. This is called delegation, which means redirecting responsibility.
   * Data Hiding
       *  With name mangling, we can create "private" data members in Python. This is not fully private because there is actually a workaround to access the data member/method. But with the idea of data hiding, we make it less accessible to touch sensitive data.

* **Inheritance** - the process of promoting code reuse by creating a new child class (also referred to as derived or sub/supra class) that inherits attributes and methods from an existing parent class (also referred to as base or super class). Multiple classes can inherit from one base class. With inheritance, classes exist in a hierarchy.

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
