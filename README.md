# Operating System Deadlock and Synchronization Simulation

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Project](https://img.shields.io/badge/Operating%20System-Concepts-orange)
![Status](https://img.shields.io/badge/Status-Completed-green)

---

## Project Overview

This project demonstrates core Operating System concepts:

- Banker’s Algorithm for Deadlock Avoidance
- Strict Alternation for Process Synchronization

It simulates how an operating system manages resources safely and handles process coordination in a controlled environment.

---

## Project Structure

```
OS_code Group_6/
│
├── OS_code/
│   ├── Banker's_algo.py
│   └── Strict_alte.py
│
└── README.md
```

---

## Banker’s Algorithm

This module demonstrates deadlock avoidance.

### Features:
- Computes Need Matrix
- Checks system safety state
- Generates safe sequence
- Handles resource requests
- Rolls back unsafe allocations

### Working Principle:
A process requests resources.  
The system checks if granting the request keeps the system in a safe state.  
If safe, allocation is done. Otherwise, the request is denied.

---

## Strict Alternation

This module demonstrates process synchronization.

### Features:
- Ensures mutual exclusion
- Uses shared variable `turn`
- Simulates two processes (P0 and P1)

### Working Principle:
If `turn = 0`, P0 enters the critical section.  
If `turn = 1`, P1 enters the critical section.  
After execution, the turn switches to the other process.

---

## How to Run

Banker’s Algorithm:
```bash
python Banker's_algo.py
```

Strict Alternation:
```bash
python Strict_alte.py
```

---

## Concepts Covered

- Deadlock Avoidance
- Safe State Checking
- Resource Allocation
- Process Synchronization
- Critical Section Problem
- Mutual Exclusion

---

## Output Example

Banker’s Algorithm:
```
Request GRANTED
Safe sequence: [P1, P3, P0, P2]
```

OR

```
Request DENIED (unsafe state detected)
```

Strict Alternation:
```
P0 is in critical section
P1 is in critical section
P0 is in critical section
P1 is in critical section
finishing....
```

---

## Technologies Used

- Python 3
- Threading Library
- Operating System Concepts

---

## Author

Operating System Group Project  
Deadlock and Synchronization Simulation

---

## Note

This project is for educational purposes and demonstrates how operating systems handle:

- Deadlock avoidance
- Resource allocation safety
- Process synchronization
```
