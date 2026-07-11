# Budget App

A Python project built as part of the **freeCodeCamp Scientific Computing with Python Certification**.

## Overview

This application simulates a simple budgeting system. It allows users to create budget categories, record deposits and withdrawals, transfer funds between categories, calculate balances, and generate a text-based spending chart.

## Features

* Create multiple budget categories
* Record deposits with optional descriptions
* Record withdrawals with balance validation
* Transfer funds between categories
* Calculate category balances
* Display a formatted ledger for each category
* Generate a percentage spending chart for all categories

## Technologies Used

* Python 3

## Concepts Practiced

* Object-Oriented Programming (OOP)
* Classes and Objects
* Instance Attributes
* Methods
* Lists and Dictionaries
* String Formatting
* Loops
* Conditional Statements
* Functions

## Example

```python
food = Category("Food")
clothing = Category("Clothing")

food.deposit(1000, "Initial deposit")
food.withdraw(25.50, "Groceries")
food.transfer(100, clothing)

print(food)
print(create_spend_chart([food, clothing]))
```

## Learning Outcomes

Through this project, I practiced:

* Designing classes with multiple methods
* Managing and validating financial transactions
* Creating reusable functions
* Formatting console output
* Working with collections such as lists and dictionaries

## Project Status

✅ Completed as part of the freeCodeCamp Scientific Computing with Python Certification.

## License

This project is intended for educational purposes.
