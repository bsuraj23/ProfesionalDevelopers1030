**FEATURES OF PYTHON**

1. **Easy to Learn and Read**

- **simple syntax**

2.  **Interpreted Language**

- code is executed **line by line** by the interpreter.
- No need to compile before running.

3.  **Dynamically Typed**

- **don’t need to declare variable types**.

4.  **Object-Oriented**

- **classes, inheritance, and objects**,
- promoting **reusable and organized** code.

5.  **Extensive Standard Library**

- large collection of **built-in modules** for file handling, math, web services, etc.

6. **Cross-Platform**

- Python runs on **Windows, macOS, Linux**, and even **Raspberry Pi** without modification.

7. **High-Level Language**

- You don’t have to manage **memory** or **system details**
- Python handles it automatically.

8.  **Supports Multiple Paradigms**

- You can write code in **procedural**, **object-oriented**, or **functional** styles.

9.  **Large Community and Open Source**

- Python is **free and open-source**, with a vast global community providing support and libraries.

10. **Wide Applications**

- Used in:
  - Web Development (Django, Flask)
  - Data Science & AI (NumPy, pandas, TensorFlow)
  - Automation
  - Game Development
  - Cybersecurity, etc.

##---------------------------------------------------------------------------------------##

**HOW IS PORTABILITY ACHIEVED IN PYTHON?**

- Python is a portable language because the **same code can run on different operating systems** — like Windows, macOS, and Linux — **without any modification**.
- This is possible because Python programs are **executed by an interpreter**, which works the same way across all platforms.

- Also, Python’s standard library provides **cross-platform modules** that handle system differences, so developers don’t have to change the code for each OS.
- In addition, **Python’s bytecode and virtual machine make it platform-independent.**
- **As long as a computer has a Python interpreter installed**, the same .py file will run the same way everywhere.

- For example, if I write a Python program on Windows to read a file or connect to a database, I can run the same code on Linux or macOS without changing anything — that’s portability.

==================================================================================================

## **LIST, TUPLE, SET, DICTIONARY**

## 🧾 **1. List**

- A **list** is an **ordered**, **changeable (mutable)** collection of items.
- It can contain elements of **different data types**.
- **Duplicates are allowed.**

```python
# Example
fruits = ["apple", "banana", "cherry", "apple"]

# Access elements
print(fruits[1])       # Output: banana

# Modify elements
fruits[2] = "mango"

# Add or remove items
fruits.append("orange")
fruits.remove("apple")

print(fruits)          # Output: ['banana', 'mango', 'apple', 'orange']
```

✅ **Key Points:**

- Ordered
- Mutable
- Allows duplicates
- Defined using square brackets `[ ]`

---

---

## 🔹 **2. Tuple**

- A **tuple** is an **ordered**, **unchangeable (immutable)** collection.
- Once created, you **cannot modify** it.
- **Duplicates are allowed.**

```python
# Example
colors = ("red", "green", "blue", "red")

print(colors[0])       # Output: red

# colors[1] = "yellow"  ❌ This will cause an error (immutable)

print(colors.count("red"))  # Output: 2
```

✅ **Key Points:**

- Ordered
- Immutable
- Allows duplicates
- Defined using parentheses `( )`

---

---

## 🔸 **3. Set**

- A **set** is an **unordered**, **changeable** collection of **unique** elements.
- **Duplicates are not allowed.**

```python
# Example
numbers = {1, 2, 3, 3, 4, 5}

print(numbers)   # Output: {1, 2, 3, 4, 5} (duplicates removed)

numbers.add(6)
numbers.remove(2)

print(numbers)   # Output: {1, 3, 4, 5, 6}
```

✅ **Key Points:**

- Unordered
- Mutable
- No duplicates
- Defined using curly braces `{ }`

---

---

## 🧠 **4. Dictionary**

- A **dictionary** stores data as **key–value pairs**.
- Each key must be **unique**, and values can be **of any type**.
- Useful for representing structured data (like a record).

```python
# Example
student = {"name": "Sravya", "age": 20, "course": "Python"}

print(student["name"])      # Output: Sravya

# Add or modify items
student["age"] = 21
student["city"] = "Hyderabad"

print(student)
# Output: {'name': 'Sravya', 'age': 21, 'course': 'Python', 'city': 'Hyderabad'}
```

✅ **Key Points:**

- Stores data in **key–value** pairs
- **Keys are unique**
- **Values can be changed**
- Defined using curly braces `{key: value}`

---

### 📊 **Quick Comparison Table**

| Data Type      | Ordered                | Mutable | Allows Duplicates | Example Syntax |
| -------------- | ---------------------- | ------- | ----------------- | -------------- |
| **List**       | ✅ Yes                 | ✅ Yes  | ✅ Yes            | `[ ]`          |
| **Tuple**      | ✅ Yes                 | ❌ No   | ✅ Yes            | `( )`          |
| **Set**        | ❌ No                  | ✅ Yes  | ❌ No             | `{ }`          |
| **Dictionary** | ✅ (since Python 3.7+) | ✅ Yes  | ❌ Keys unique    | `{key: value}` |

---

==================================================================================
