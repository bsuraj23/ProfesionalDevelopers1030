# 🔍 **SEARCHING**

Searching means **finding an element** in a collection (like a list or array).

There are mainly **two types**:

---

## 🧩 1. **Linear Search (Sequential Search)**

- Start from the **first element** and check each one **until** you find the target or reach the end.
- Works on **unsorted** data.

### 🔹 **Example:**

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # position found
    return -1  # not found

arr = [10, 30, 50, 70, 90]
print(linear_search(arr, 70))  # Output: 3
```

### 🔹 **Time Complexity:**

| Case    | Complexity                               |
| ------- | ---------------------------------------- |
| Best    | O(1) → if the element is first           |
| Worst   | O(n) → if the element is last or missing |
| Average | O(n)                                     |

### 🔹 **Space Complexity:** O(1)

---

## 🧮 2. **Binary Search**

- Works **only on sorted arrays**.
- Repeatedly **divide the array into halves** and check whether the target lies in the left or right half.

### 🔹 **Example:**

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [10, 20, 30, 40, 50]
print(binary_search(arr, 40))  # Output: 3
```

### 🔹 **Time Complexity:**

| Case    | Complexity |
| ------- | ---------- |
| Best    | O(1)       |
| Worst   | O(log n)   |
| Average | O(log n)   |

### 🔹 **Space Complexity:** O(1) (iterative), O(log n) (recursive)

---

# **SORTING**

Sorting means **arranging elements** in **ascending or descending order**.
Example: `[5, 1, 4, 2] → [1, 2, 4, 5]`

There are many algorithms — let’s look at the main ones:

---

## 1. **Bubble Sort**

- Repeatedly **swap adjacent elements** if they are in the wrong order.
- “Heaviest” element **bubbles up** to the end in each pass.

### 🔹 **Example:**

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([5, 1, 4, 2]))
```

**Output:** `[1, 2, 4, 5]`

### 🔹 **Complexity:**

| Case    | Time                       |
| ------- | -------------------------- |
| Best    | O(n) (when already sorted) |
| Worst   | O(n²)                      |
| Average | O(n²)                      |
| Space   | O(1)                       |

---

## 2. **Selection Sort**

- Select the **smallest element** and place it at the **beginning**.
- Continue for the rest of the array.

### 🔹 **Example:**

```python
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

### 🔹 **Complexity:**

| Case    | Time  |
| ------- | ----- |
| Best    | O(n²) |
| Worst   | O(n²) |
| Average | O(n²) |
| Space   | O(1)  |

---

## 3. **Insertion Sort**

- Take one element at a time and **insert it** into the **correct position** among the already sorted elements.

### 🔹 **Example:**

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

### 🔹 **Complexity:**

| Case    | Time  |
| ------- | ----- |
| Best    | O(n)  |
| Worst   | O(n²) |
| Average | O(n²) |
| Space   | O(1)  |

---

## 4. **Merge Sort**

- **Divide and conquer** method:

  - Split the array into halves.
  - Sort each half.
  - Merge them in sorted order.

### 🔹 **Example:**

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]; i += 1; k += 1
        while j < len(R):
            arr[k] = R[j]; j += 1; k += 1
```

### 🔹 **Complexity:**

| Case    | Time       |
| ------- | ---------- |
| Best    | O(n log n) |
| Worst   | O(n log n) |
| Average | O(n log n) |
| Space   | O(n)       |

---

## 5. **Quick Sort**

- Choose a **pivot** element.
- Place all smaller elements **left** of pivot and larger ones **right**.
- Recursively sort left and right parts.

### 🔹 **Example:**

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

### 🔹 **Complexity:**

| Case    | Time                                   |
| ------- | -------------------------------------- |
| Best    | O(n log n)                             |
| Worst   | O(n²) (rare, when pivot chosen poorly) |
| Average | O(n log n)                             |
| Space   | O(log n) (recursive calls)             |

---

## 🧾 Summary Table

| Algorithm          | Best       | Average    | Worst      | Space    | Type   |
| ------------------ | ---------- | ---------- | ---------- | -------- | ------ |
| **Linear Search**  | O(1)       | O(n)       | O(n)       | O(1)     | Search |
| **Binary Search**  | O(1)       | O(log n)   | O(log n)   | O(1)     | Search |
| **Bubble Sort**    | O(n)       | O(n²)      | O(n²)      | O(1)     | Sort   |
| **Selection Sort** | O(n²)      | O(n²)      | O(n²)      | O(1)     | Sort   |
| **Insertion Sort** | O(n)       | O(n²)      | O(n²)      | O(1)     | Sort   |
| **Merge Sort**     | O(n log n) | O(n log n) | O(n log n) | O(n)     | Sort   |
| **Quick Sort**     | O(n log n) | O(n log n) | O(n²)      | O(log n) | Sort   |

---
