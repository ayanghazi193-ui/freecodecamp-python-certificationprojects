# Tower of Hanoi Algorithm

A Python implementation of the classic **Tower of Hanoi** puzzle, created as part of the **freeCodeCamp Python Certification**.

## 📖 Overview

The Tower of Hanoi is a mathematical puzzle consisting of three rods and a number of disks of different sizes. The objective is to move all disks from the first rod to the third rod while following these rules:

* Only one disk can be moved at a time.
* Only the top disk on a rod may be moved.
* A larger disk cannot be placed on top of a smaller disk.

This project uses a **recursive algorithm** to solve the puzzle and returns every step of the solution, including the initial arrangement.

## ✨ Features

* Solves the Tower of Hanoi for any positive number of disks.
* Uses recursion to generate the optimal solution.
* Displays the complete state of all three rods after every move.
* Returns the solution as a formatted string.

## 📂 Project Structure

```text
.
├── main.py
└── README.md
```

## 🚀 Getting Started

### Prerequisites

* Python 3.x

### Run the Program

1. Clone the repository:

```bash
git clone https://github.com/your-username/tower-of-hanoi.git
```

2. Navigate to the project folder:

```bash
cd tower-of-hanoi
```

3. Run Python and test the function:

```python
from main import hanoi_solver

print(hanoi_solver(3))
```

## 🖥️ Example Output

```text
[3, 2, 1] [] []
[3, 2] [] [1]
[3] [2] [1]
[3] [2, 1] []
[] [2, 1] [3]
[1] [2] [3]
[1] [] [3, 2]
[] [] [3, 2, 1]
```

## 🧠 Concepts Practiced

* Recursion
* Functions
* Lists
* Problem Solving
* Algorithm Design
* State Tracking

## 🎯 Learning Objectives

This project demonstrates how recursive algorithms can efficiently solve problems by breaking them into smaller subproblems while maintaining the rules of the puzzle.

## 📜 License

This project is open source and available under the MIT License.

## 🙌 Acknowledgements

Created as part of the **freeCodeCamp Python Certification**.
