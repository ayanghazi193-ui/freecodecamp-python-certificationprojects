# Polygon Area Calculator

A Python project built as part of the **freeCodeCamp Python Certification**. This project demonstrates the use of **Object-Oriented Programming (OOP)** by implementing `Rectangle` and `Square` classes with inheritance, encapsulation, and method overriding.

## Features

* Create rectangle objects with custom width and height.
* Create square objects that inherit from the `Rectangle` class.
* Calculate:

  * Area
  * Perimeter
  * Diagonal length
* Generate an ASCII representation of the shape.
* Determine how many times one shape can fit inside another without rotation.
* Update rectangle dimensions using setter methods.
* Keep square dimensions equal using overridden setter methods.

## Concepts Used

* Python Classes and Objects
* Inheritance
* Method Overriding
* Constructors (`__init__`)
* Special Methods (`__str__`)
* Mathematical Calculations
* String Manipulation

## Project Structure

```text
.
├── main.py      # Rectangle and Square class implementations
└── README.md    # Project documentation
```

## Example Usage

```python
from main import Rectangle, Square

rect = Rectangle(10, 5)

print(rect.get_area())
print(rect.get_perimeter())
print(rect.get_diagonal())

sq = Square(4)

print(sq.get_area())
print(sq.get_picture())

print(rect.get_amount_inside(sq))
```

## Example Output

```text
50
30
11.180339887498949

****
****
****
****

2
```

## Skills Demonstrated

* Object-Oriented Programming (OOP)
* Class Inheritance
* Method Overriding
* Python Special Methods
* Problem Solving
* Clean and Reusable Code

## Project Source

This project was completed as part of the **freeCodeCamp Python Certification** curriculum.

## License

This project is intended for educational purposes.
