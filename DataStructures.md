**DATA STRUCTURES**

A **data structure** organizes data in a particular way so it can be used efficiently.
Two common **linear data structures** are:

- **Stack** – follows _Last In, First Out (LIFO)_
- **Queue** – follows _First In, First Out (FIFO)_

---

## 🥞 Stack (LIFO – Last In, First Out)

### 🔹 **Meaning:**

The **last element** added is the **first one removed** — just like stacking plates in a pile.
You can only add/remove from the **top**.

### 🔹 **Real-life Example:**

Imagine a stack of plates:

- You **add** a new plate **on top**.
- You **remove** the top plate **first**.

### 🔹 **Operations:**

| Operation          | Meaning                                  | Example              |
| ------------------ | ---------------------------------------- | -------------------- |
| `push()`           | Add an element on top                    | `push(10)`           |
| `pop()`            | Remove the top element                   | `pop()` → removes 10 |
| `peek()` / `top()` | View the top element without removing it | Shows 10             |
| `isEmpty()`        | Check if the stack is empty              | returns True/False   |

---

### 🔹 **In Python:**

You can use a **list** as a stack easily.

```python
stack = []
stack.append(10)  # push
stack.append(20)
stack.append(30)
print(stack)      # [10, 20, 30]

stack.pop()       # removes 30
print(stack)      # [10, 20]
```

✅ **LIFO Order:** Last inserted → First removed

---

## 🚶 Queue (FIFO – First In, First Out)

### 🔹 **Meaning:**

The **first element** added is the **first one removed** — like people waiting in line.
You add from the **rear** and remove from the **front**.

### 🔹 **Real-life Example:**

Think of a ticket counter:

- The **first person** in line gets the ticket **first**.
- New people **join the end** of the line.

### 🔹 **Operations:**

| Operation   | Meaning                     | Example                  |
| ----------- | --------------------------- | ------------------------ |
| `enqueue()` | Add an element to the rear  | `enqueue(10)`            |
| `dequeue()` | Remove the front element    | `dequeue()` → removes 10 |
| `peek()`    | View the front element      | Shows 10                 |
| `isEmpty()` | Check if the queue is empty | returns True/False       |

---

### 🔹 **In Python:**

You can use `collections.deque` (double-ended queue) — efficient for both ends.

```python
from collections import deque

queue = deque()
queue.append(10)   # enqueue
queue.append(20)
queue.append(30)
print(queue)       # deque([10, 20, 30])

queue.popleft()    # dequeue (remove front)
print(queue)       # deque([20, 30])
```

✅ **FIFO Order:** First inserted → First removed

---

## 🧠 Quick Comparison

| Feature               | Stack                          | Queue                          |
| --------------------- | ------------------------------ | ------------------------------ |
| Order                 | LIFO (Last In, First Out)      | FIFO (First In, First Out)     |
| Insertion             | One end (Top)                  | Rear end                       |
| Deletion              | Same end (Top)                 | Front end                      |
| Python Implementation | `list.append()` / `list.pop()` | `collections.deque`            |
| Example               | Undo feature, call stack       | Task scheduling, printer queue |

---

---

## 💡 Where They’re Used

- **Stack:**

  - Function call management (call stack)
  - Undo/Redo functionality
  - Expression evaluation (postfix, prefix)

- **Queue:**

  - Scheduling (CPU, printer jobs)
  - Handling requests (e.g., customer support tickets)
  - Data streaming or buffering

---

---

# Linked List

A **linked list** is a **linear data structure** where elements (called **nodes**) are **linked** together using **pointers (references)**.

Unlike arrays:

- Elements are **not stored in continuous memory**.
- Each element points to the **next** one.

---

## 🧩 Structure of a Node

Each **node** in a linked list has two parts:

1. **Data** → stores the actual value.
2. **Next** → a pointer/reference to the next node.

```
[Data | Next] → [Data | Next] → [Data | Next] → None
```

The **last node** points to **None**, indicating the end of the list.

---

## 🪜 1. **Singly Linked List (SLL)**

### 🔹 Structure:

Each node points to **only the next node**.

```
Head → [10 | *] → [20 | *] → [30 | None]
```

### 🔹 Features:

- Traversal is **only forward**.
- Simple to implement.
- Uses **less memory** (since there’s only one link per node).

### 🔹 Example in Python:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()
```

**Output:**

```
10 → 20 → 30 → None
```

---

## 🔁 2. **Doubly Linked List (DLL)**

### 🔹 Structure:

Each node has **three parts**:

1. `prev` → pointer to the **previous** node
2. `data` → stores the value
3. `next` → pointer to the **next** node

```
None ← [10 | * | *] ⇄ [20 | * | *] ⇄ [30 | * | None]
```

### 🔹 Features:

- Can be traversed **both forward and backward**.
- Easier to **delete or insert** nodes (since we can go back too).
- Needs **more memory** (extra `prev` pointer).

### 🔹 Use Case:

- Browser forward/backward navigation
- Undo/Redo in text editors

---

## 🔄 3. **Circular Linked List (CLL)**

### 🔹 Structure:

In this list, the **last node** points **back to the first node**, forming a **circle**.

```
[10 | *] → [20 | *] → [30 | *] ↺
     ↑----------------------------↑
```

### 🔹 Features:

- No `None` at the end — it loops continuously.
- You can start at any node and eventually reach it again.
- Can be **singly or doubly circular**.

### 🔹 Use Case:

- Multiplayer games (round-robin turn order)
- CPU scheduling (Round Robin)
- Continuous data streaming

---

## 🧩 Summary (Easy to Remember)

| Concept         | Key Idea            | Analogy                                      |
| --------------- | ------------------- | -------------------------------------------- |
| **Singly LL**   | One-way links       | Train cars connected in one direction        |
| **Doubly LL**   | Two-way links       | Train with cars connected in both directions |
| **Circular LL** | Loops back to start | Ferris wheel (keeps rotating)                |

---
