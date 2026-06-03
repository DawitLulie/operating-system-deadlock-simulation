
# ⚙️ Operating System Deadlock & Synchronization Simulation ⚙️

![Python](https://img.shields.io/badge/Python-3.x-blue)
![OS Project](https://img.shields.io/badge/OS-Deadlock%20%26%20Sync-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 🚀 Project Overview
This project demonstrates important **Operating System concepts**:

- 🏦 Banker’s Algorithm (Deadlock Avoidance)
- 🔁 Strict Alternation (Process Synchronization)

It simulates how an operating system manages **resources safely** and ensures **mutual exclusion** between processes.

---

## 📁 Project Files

📌 Banker's Algorithm:
- `Banker's_algo.py`

📌 Strict Alternation:
- `Strict_alte.py`

---

## 🏦 Banker’s Algorithm (Deadlock Avoidance)

✨ Features:
- Calculates Need Matrix
- Checks safe state of the system
- Finds safe sequence of execution
- Handles resource requests
- Rolls back if unsafe state is detected

⚙️ How it works:
- A process requests resources
- System checks if request is safe
- If safe → resources allocated ✅
- If unsafe → request denied ❌

---

## 🔁 Strict Alternation (Synchronization)

✨ Features:
- Demonstrates process synchronization
- Ensures mutual exclusion
- Uses shared variable `turn`
- Simulates two processes (P0 & P1)

⚙️ How it works:
- `turn = 0` → P0 enters critical section
- `turn = 1` → P1 enters critical section
- After execution, control switches to the other process

---

## ▶️ How to Run

### 🏦 Banker’s Algorithm
```bash
python Banker's_algo.py
```

### 🔁 Strict Alternation
```bash
python Strict_alte.py
```

---

## 🧠 Concepts Covered
- Deadlock Avoidance
- Safe State Algorithm
- Resource Allocation
- Process Synchronization
- Critical Section Problem
- Mutual Exclusion

---

## 💻 Technologies Used
- Python 3
- Threading Module
- Operating System Concepts

---

## 📌 Output Example

### Banker’s Algorithm
```
Request GRANTED
Safe sequence: ['P1', 'P3', 'P0', 'P2']
```

or
```
Request DENIED (would lead to unsafe state)
```

---

### Strict Alternation
```
P0 is in critical section
P1 is in critical section
P0 is in critical section
P1 is in critical section
finishing....
```

---

## 👨‍💻 Author
Operating System Group Project  
Deadlock & Synchronization Simulation

---

## 📌 Note
This project is for educational purposes to demonstrate:
- How deadlocks are avoided
- How processes synchronize
- How operating systems manage shared resources

---
