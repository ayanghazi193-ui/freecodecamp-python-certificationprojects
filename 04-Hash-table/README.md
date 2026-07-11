# Build a Hash Table

A Python implementation of a **Hash Table** created as part of the **freeCodeCamp Python Certification**.

## 📖 Overview

This project demonstrates how a hash table works by implementing one from scratch without using Python's built-in dictionary hashing mechanism.

The hash function calculates the hash value by summing the Unicode (ASCII) values of every character in a string. The resulting hash value is then used as the index for storing key-value pairs.

To handle hash collisions, each hash value stores a nested dictionary containing all key-value pairs that share the same hash.

## ✨ Features

* Custom hash function using Unicode values
* Add key-value pairs
* Look up values by key
* Remove key-value pairs
* Collision handling with nested dictionaries
* Graceful handling of missing keys

## 🛠️ Technologies Used

* Python 3

## 📂 Project Structure

```
.
├── main.py
└── README.md
```

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/build-a-hash-table.git
```

2. Navigate to the project folder:

```bash
cd build-a-hash-table
```

3. Run the program:

```bash
python main.py
```

## 💻 Example

```python
table = HashTable()

table.add("golf", "sport")
table.add("dear", "friend")
table.add("read", "book")

print(table.lookup("golf"))
# sport

table.remove("golf")

print(table.lookup("golf"))
# None
```

## 🎯 Learning Objectives

* Understand hash tables and hashing
* Implement a custom hash function
* Handle hash collisions
* Work with nested dictionaries
* Practice object-oriented programming (OOP) in Python

## 📜 License

This project is for educational purposes as part of the freeCodeCamp Python Certification.
