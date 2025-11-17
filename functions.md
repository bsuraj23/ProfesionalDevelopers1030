**FUNCTIONS**

## 🧠 **What is a Function?**

A **function** is a block of code that performs a **specific task** and can be **reused** whenever needed.

It helps to:

- Avoid repeating code
- Make programs **modular** and **organized**
- Improve **readability** and **maintainability**

---

## 🧩 **Types of Functions in Python**

1. **Built-in functions** – already provided by Python

   - Examples: `print()`, `len()`, `sum()`, `type()`, `input()`, etc.

2. **User-defined functions** – created by programmers using the `def` keyword.

   - Example:

     ```python
     def greet():
         print("Hello, welcome to Python!")
     ```

---

## 🧱 **Defining and Calling a Function**

### 🔹 **Syntax**

```python
def function_name(parameters):
    # block of code
    return result
```

### 🔹 **Example**

```python
def add(a, b):
    return a + b

result = add(10, 5)
print(result)
```

**Output:**

```
15
```

### 🔹 Explanation:

- `def` → keyword to define a function
- `add` → function name
- `(a, b)` → parameters (inputs)
- `return` → sends the output back to where the function was called

---

## 🔄 **Function Parameters and Arguments**

| Term          | Meaning                                                                      |
| ------------- | ---------------------------------------------------------------------------- |
| **Parameter** | Variable listed inside function definition (e.g., `a, b` in `def add(a, b)`) |
| **Argument**  | Actual value passed when calling the function (e.g., `add(10, 5)`)           |

---

## 🔹 **Types of Arguments**

1. **Positional Arguments**

   ```python
   def greet(name, age):
       print(f"Hello {name}, you are {age} years old.")

   greet("Sravya", 20)
   ```

2. **Keyword Arguments**

   ```python
   greet(age=20, name="Sravya")
   ```

3. **Default Arguments**

   ```python
   def greet(name, msg="Good morning"):
       print(f"{msg}, {name}")

   greet("Sravya")  # uses default msg
   greet("Ravi", "Hello")  # overrides default
   ```

4. **Variable-length Arguments**

   - `*args` → for multiple positional arguments
   - `**kwargs` → for multiple keyword arguments

   ```python
   def show(*args):
       print(args)

   show(1, 2, 3, 4)
   ```

---

## 🔁 **Return Statement**

- The `return` keyword **sends back** a result from the function.
- If no `return` is given, the function returns `None` by default.

Example:

```python
def square(n):
    return n * n

print(square(4))  # 16
```

---

## 🧮 **Lambda (Anonymous) Functions**

A **lambda function** is a small, one-line, anonymous function.

```python
square = lambda x: x * x
print(square(5))  # Output: 25
```

Useful for short tasks, especially with `map()`, `filter()`, and `reduce()`.

---

## 🧱 **Scope of Variables**

- **Local variable** → defined inside a function (accessible only there)
- **Global variable** → defined outside a function (accessible everywhere)

```python
x = 10  # global

def show():
    y = 5  # local
    print("Inside:", x + y)

show()
print("Outside:", x)
```

---

## ⚙️ **Advantages of Using Functions**

✅ Code reusability
✅ Easier debugging
✅ Better readability
✅ Modular structure
✅ Simplifies complex problems

---

## 💡 **In Simple Words**

> A **function** is like a **machine**:
> You give it some **input (arguments)**,
> it performs a **task**,
> and gives back an **output (return value)**.

Example:

```
input → [5, 3]
function → add()
output → 8
```

---

## 🧾 **Example Combining Everything**

```python
def calculate(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    else:
        return "Invalid operation"

print(calculate(10, 5))             # 15
print(calculate(10, 5, "multiply")) # 50
```

---

**Built-in VS Pre-defined functions**

| Term                     | Meaning                                                                                                                                  |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Built-in Functions**   | Functions that are **already available in Python by default**, and can be used **without importing any module**.                         |
| **Predefined Functions** | Functions that are **defined in standard or external libraries (modules)** — you can use them **after importing** the respective module. |

---

## 🧩 **1️⃣ Built-in Functions**

### 🔹 Definition:

These are **automatically loaded** when you start Python.
You can use them **directly**, no need to import anything.

### 🔹 Examples:

```python
print("Hello")     # prints text
len([1, 2, 3])     # gives length of list
max(4, 9, 2)       # returns maximum value
sum([1, 2, 3])     # returns sum of list elements
type(10)           # returns data type
input("Enter: ")   # takes input
```

### 🔹 Total:

Python has around **70+ built-in functions**.

### 🔹 Examples list:

`print()`, `len()`, `sum()`, `min()`, `max()`, `sorted()`, `range()`, `type()`, `int()`, `float()`, `str()`, `input()`, etc.

---

## 🧩 **2️⃣ Predefined Functions**

### 🔹 Definition:

These functions are **already written and stored** in **Python libraries or modules**,
but you must **import** the module before using them.

### 🔹 Examples:

```python
import math
print(math.sqrt(16))   # 4.0
print(math.factorial(5))  # 120

import random
print(random.randint(1, 10))  # random number between 1 and 10
```

Here:

- `sqrt()` and `factorial()` are **predefined functions** in the **math module**.
- `randint()` is a **predefined function** in the **random module**.

---

## 🧾 **Comparison Table**

| Feature           | Built-in Functions                         | Predefined Functions                                |
| ----------------- | ------------------------------------------ | --------------------------------------------------- |
| **Definition**    | Functions provided by Python core language | Functions provided by Python libraries/modules      |
| **Import Needed** | ❌ No                                      | ✅ Yes                                              |
| **Availability**  | Always available                           | Available after importing                           |
| **Examples**      | `print()`, `len()`, `sum()`, `type()`      | `math.sqrt()`, `random.randint()`, `datetime.now()` |
| **Where defined** | In Python core                             | In standard modules or external libraries           |

---

## 💡 **Simple Way to Remember**

> 🧩 **Built-in** → already built inside Python (use directly).
> 📦 **Predefined** → pre-written but stored in modules (import first).

---

### ✅ Example Summary:

```python
# Built-in function
print(len([1,2,3]))

# Predefined function (need import)
import math
print(math.sqrt(25))
```

---

## **Scope of global and local variables**

## 🧩 **1️⃣ What is “Scope”?**

👉 **Scope** means **the region of a program** where a variable can be **accessed or modified**.

In Python, there are **two main types of variable scope**:

- **Local Scope**
- **Global Scope**

---

## 🌐 **2️⃣ Global Variables**

### 🔹 Definition:

A **global variable** is one that is **declared outside of all functions**.
It can be **accessed from anywhere** in the program — both inside and outside functions.

### 🔹 Example:

```python
x = 10   # global variable

def show():
    print("Inside function:", x)  # can access global variable

show()
print("Outside function:", x)
```

### ✅ **Output:**

```
Inside function: 10
Outside function: 10
```

### 🔹 Explanation:

- `x` is declared outside the function → so it’s **global**.
- The function `show()` can **read** it directly.

---

## 🏠 **3️⃣ Local Variables**

### 🔹 Definition:

A **local variable** is **declared inside a function** and can only be **used within that function**.

### 🔹 Example:

```python
def display():
    y = 5   # local variable
    print("Inside function:", y)

display()
print("Outside function:", y)  # ❌ Error
```

### ❌ **Error:**

```
NameError: name 'y' is not defined
```

### 🔹 Explanation:

- `y` exists **only inside** the function.
- Once the function ends, `y` is **destroyed**.

---

## 🔄 **4️⃣ Using Global Variables Inside a Function (with modification)**

If you want to **modify** a global variable inside a function,
you must declare it using the **`global` keyword**.

### Example:

```python
count = 0

def increase():
    global count   # tells Python to use the global variable
    count += 1
    print("Inside function:", count)

increase()
print("Outside function:", count)
```

### ✅ **Output:**

```
Inside function: 1
Outside function: 1
```

---

## 🧾 **Summary Table**

| Type                | Declared Where        | Accessible Where          | Lifetime           | Example  |
| ------------------- | --------------------- | ------------------------- | ------------------ | -------- |
| **Global Variable** | Outside all functions | Anywhere in the program   | Till program ends  | `x = 10` |
| **Local Variable**  | Inside a function     | Only inside that function | Till function ends | `y = 5`  |

---

## 💡 **Simple Way to Remember**

> 🏠 **Local** = lives **inside** the function.
> 🌍 **Global** = lives **everywhere** in the program.

---
