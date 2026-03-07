# 🔢 NumPy Notes

NumPy (Numerical Python) is a Python library used for numerical computations, working with arrays, linear algebra, scientific computing, and machine learning data processing. Its main feature is the **N-dimensional array (ndarray)** — much faster than Python lists because it's implemented in C.

---

## 🆚 NumPy vs Python Lists

At first glance, a NumPy array and a Python list look similar — both store collections of items. But under the hood, they are very different.

### 🔬 Key Differences

| Feature | Python List | NumPy Array |
|---|---|---|
| Data types | Mixed (int, str, float together) | Homogeneous (all same type) |
| Memory | More — each element is a Python object | Less — raw C-style contiguous block |
| Speed | Slow — interpreted one by one | Fast — vectorized C operations |
| Math operations | No built-in math; need loops | Element-wise math built-in |
| Multi-dimensional | Nested lists (messy) | Native N-dimensional support |
| Syntax | Verbose loops needed | Concise and expressive |

### 🐢 Why Python Lists are Slow

In Python, everything is an object. A list stores **pointers** to individual Python objects scattered in memory. When you loop over a list and do math, Python must:

1. Fetch the pointer to the element
2. Unbox the Python object
3. Perform the math operation
4. Re-box the result into a new Python object
5. Repeat for every single element

This is slow and memory-heavy, especially for large datasets.

### ⚡ Why NumPy is Fast

NumPy arrays store data as a **single contiguous block of raw bytes in memory** (like C arrays). Operations run in pre-compiled C/Fortran code, not interpreted Python. This means:

- No boxing/unboxing of Python objects
- CPU cache is used efficiently (data sits next to each other in RAM)
- Operations run at near-native C speed
- Supports **SIMD** (Single Instruction, Multiple Data) — one CPU instruction can process multiple values simultaneously

### 💻 Proof — Speed Comparison

```python
import numpy as np
import time

# Python List
py_list = list(range(1_000_000))
start = time.time()
result = [x * 2 for x in py_list]
print(f"List:  {time.time() - start:.4f}s")

# NumPy Array
np_array = np.arange(1_000_000)
start = time.time()
result = np_array * 2
print(f"NumPy: {time.time() - start:.4f}s")

# NumPy is typically 10x–100x faster
```

### 🧠 Memory Comparison

```python
import sys
import numpy as np

py_list  = list(range(1000))
np_array = np.arange(1000)

print(sys.getsizeof(py_list))   # ~8056 bytes
print(np_array.nbytes)          # 8000 bytes

# Python list stores pointers + per-object overhead
# NumPy stores just the raw values — much leaner
```

### ✍️ Syntax Difference

```python
# Multiply every element by 2

# Python List — need a loop or list comprehension
py_list = [1, 2, 3, 4, 5]
result  = [x * 2 for x in py_list]   # [2, 4, 6, 8, 10]

# NumPy — direct, readable, fast
np_array = np.array([1, 2, 3, 4, 5])
result   = np_array * 2               # [2 4 6 8 10]
```

> 💡 **When to use a Python list:** When you need mixed data types or dynamic appending of heterogeneous items (e.g. a list of names and numbers). For any numerical computation — always prefer NumPy.

---

## ⚙️ Setup

**Install NumPy**

```bash
pip install numpy
```

**Import NumPy**

```python
import numpy as np
```

> 💡 `np` is just an alias to make code shorter.

---

## 🏗️ Creating NumPy Arrays

**From a Python List**

```python
import numpy as np

a = np.array([1, 2, 3, 4])
print(a)
# Output: [1 2 3 4]
```

**Check Type**

```python
type(a)
# Output: numpy.ndarray
```

**Multi-Dimensional Array**

```python
b = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(b)
# Output:
# [[1 2 3]
#  [4 5 6]]
```

---

## 📐 Array Dimensions

**1D Array**

```python
a = np.array([1, 2, 3])
# Shape: (3,)
```

**2D Array**

```python
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
# Shape: (2, 3)  →  Rows = 2, Columns = 3
```

**Check Shape & Dimensions**

```python
print(a.shape)   # (2, 3)
print(a.ndim)    # 2
```

---

## ✨ Special NumPy Arrays

**Zeros Array**

```python
np.zeros((3, 3))
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]
```

**Ones Array**

```python
np.ones((2, 4))
```

**Identity Matrix**

```python
np.identity(3)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
```

**Range Array**

```python
np.arange(0, 10)
# [0 1 2 3 4 5 6 7 8 9]
```

**Range with Step**

```python
np.arange(0, 10, 2)
# [0 2 4 6 8]
```

**Linspace** — creates evenly spaced numbers

```python
np.linspace(0, 10, 5)
# [ 0.   2.5  5.   7.5 10. ]
```

---

## 🎯 Array Indexing

**1D Indexing**

```python
a = np.array([10, 20, 30, 40])
print(a[0])   # 10
print(a[2])   # 30
```

**2D Indexing**

```python
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(a[0, 1])  # 2
```

---

## ✂️ Array Slicing

**1D Slicing**

```python
a = np.array([1, 2, 3, 4, 5])
print(a[1:4])   # [2 3 4]
```

**Step Slicing**

```python
print(a[::2])   # [1 3 5]
```

**2D Slicing — Column Selection**

```python
a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(a[:, 1])   # [2 5 8]  ← all rows, column 1
```

**Row Selection**

```python
print(a[1, :])   # [4 5 6]  ← row 1, all columns
```

---

## ➕ Array Arithmetic

NumPy allows **vectorized operations** — element-wise by default.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)    # [5 7 9]
print(a - b)    # [-3 -3 -3]
print(a * b)    # [ 4 10 18]
print(a / b)    # [0.25 0.4  0.5]
print(a ** 2)   # [1 4 9]
```

---

## 📡 Broadcasting

Broadcasting allows operations between arrays of **different shapes**.

**Scalar Broadcasting**

```python
a = np.array([1, 2, 3])
b = 5
print(a + b)   # [6 7 8]  ← 5 is broadcast to every element
```

**Array Broadcasting**

```python
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
b = np.array([10, 20, 30])
print(a + b)
# [[11 22 33]
#  [14 25 36]]
```

---

## 📊 Aggregation Functions

Used for statistical operations.

```python
a = np.array([1, 2, 3, 4])

np.sum(a)    # 10
np.mean(a)   # 2.5
np.max(a)    # 4
np.min(a)    # 1
np.std(a)    # standard deviation
```

**Axis Aggregation**

```python
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

np.sum(a, axis=0)   # [5 7 9]  ← sum along columns
np.sum(a, axis=1)   # [6 15]   ← sum along rows
```

---

## 🔍 Filtering Arrays

Filtering means selecting elements using **boolean conditions**.

**Single Condition**

```python
a = np.array([1, 2, 3, 4, 5])
print(a[a > 3])   # [4 5]
```

**Multiple Conditions**

```python
a[(a > 2) & (a < 5)]   # [3 4]
```

---

## 🎲 Random Numbers

NumPy has a built-in `random` module. The modern approach uses **`np.random.default_rng()`** (RNG — Random Number Generator), which is more reproducible and recommended over the legacy `np.random.*` functions.

**Create an RNG instance**

```python
rng = np.random.default_rng(seed=42)  # seed makes results reproducible
```

> 💡 Always use `default_rng()` for new code. The `seed` parameter ensures you get the same random numbers every run — essential for reproducible ML experiments.

**Random Float (0 to 1)**

```python
rng.random()        # single float
rng.random(3)       # array of 3 floats
# Example output: [0.77 0.43 0.02]
```

**Random Matrix**

```python
rng.random((3, 3))  # 3×3 matrix of floats
```

**Random Integers**

```python
rng.integers(1, 10, size=5)  # 5 integers between 1–9
# Example output: [2 7 1 9 5]
```

**Random Choice**

```python
rng.choice([1, 2, 3, 4])          # pick 1 element
rng.choice([1, 2, 3, 4], size=2)  # pick 2 elements
```

**Random Normal Distribution**

```python
rng.normal(loc=0, scale=1, size=5)  # mean=0, std=1
```

**Shuffle an Array**

```python
a = np.array([1, 2, 3, 4, 5])
rng.shuffle(a)
print(a)  # shuffled in-place
```

> ⚠️ **Legacy API** (still works but not recommended for new code):
> ```python
> np.random.rand()             # float [0, 1)
> np.random.randint(1, 10, 5)  # integers
> np.random.seed(42)           # set seed globally
> ```

---

## 🤖 Why NumPy is Used in ML

NumPy is the **foundation** of most data science libraries:

| Library | Purpose |
|---|---|
| **Pandas** | Data manipulation |
| **Scikit-learn** | Machine learning |
| **TensorFlow** | Deep learning |
| **PyTorch** | Deep learning |
| **Matplotlib** | Data visualization |

NumPy helps with:

- Matrix operations
- Linear algebra
- Data preprocessing
- Feature transformations