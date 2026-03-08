# 🐼 Pandas Notes

---

## 1. What is Pandas?

**pandas** is a Python library used for **data analysis** and **data manipulation**. It helps work with structured data such as tables, spreadsheets, and datasets.

### Why Pandas is Used

- Handling datasets
- Data cleaning
- Data analysis
- Data transformation
- Data visualization preparation

> It works very closely with **NumPy**, which provides fast numerical operations.

---

## 2. Installing Pandas

```bash
pip install pandas
```

Or inside Jupyter Notebook:

```bash
!pip install pandas
```

---

## 3. Importing Pandas

Standard convention:

```python
import pandas as pd
```

Here, `pd` is an alias for pandas.

---

## 4. Pandas Data Structures

There are two main data structures:

| Structure | Description |
|-----------|-------------|
| Series | 1-D labeled array |
| DataFrame | 2-D table (rows and columns) |

---

## 5. Pandas Series

A **Series** is a one-dimensional labeled array.

### Example

```python
import pandas as pd

data = [10, 20, 30, 40]
s = pd.Series(data)
print(s)
```

**Output:**

```
0    10
1    20
2    30
3    40
```

> Left side → index | Right side → values

### Series with Custom Index

```python
data = [10, 20, 30]
s = pd.Series(data, index=["a", "b", "c"])
print(s)
```

**Output:**

```
a    10
b    20
c    30
```

### Series from Dictionary

```python
data = {
    "a": 10,
    "b": 20,
    "c": 30
}
s = pd.Series(data)
print(s)
```

---

## 6. Pandas DataFrame

A **DataFrame** is a 2D table-like structure.

| Name | Age |
|------|-----|
| A | 21 |
| B | 22 |
| C | 23 |

### Creating DataFrame — From Dictionary

```python
import pandas as pd

data = {
    "Name": ["A", "B", "C"],
    "Age": [21, 22, 23]
}

df = pd.DataFrame(data)
print(df)
```

**Output:**

```
  Name  Age
0    A   21
1    B   22
2    C   23
```

---

## 7. Reading Data Files

Pandas can read many file types.

**CSV**

```python
df = pd.read_csv("data.csv")
```

**Excel**

```python
df = pd.read_excel("data.xlsx")
```

**JSON**

```python
df = pd.read_json("data.json")
```

---

## 8. Viewing Data

**First rows:**

```python
df.head()
df.head(10)
```

**Last rows:**

```python
df.tail()
```

---

## 9. Data Information

**Dataset information:**

```python
df.info()
```

Shows: columns, data types, non-null values

**Statistical Summary:**

```python
df.describe()
```

Shows: mean, median, std, min, max

---

## 10. Selecting Columns

**Single column:**

```python
df["Age"]
```

**Multiple columns:**

```python
df[["Name", "Age"]]
```

> **Note:** Double brackets because we pass a list.

---

## 11. Selecting Rows

**Using label:**

```python
df.loc[0]
```

**Using integer index:**

```python
df.iloc[0]
```

| Method | Uses |
|--------|------|
| `loc` | label based |
| `iloc` | index based |

---

## 12. Filtering Data

```python
df[df["Age"] > 21]
```

**Output:**

```
  Name  Age
1    B   22
2    C   23
```

---

## 13. Adding New Column

```python
df["Salary"] = [30000, 40000, 50000]
```

---

## 14. Dropping Columns

```python
df.drop("Age", axis=1)
```

| Axis | Meaning |
|------|---------|
| 0 | rows |
| 1 | columns |

---

## 15. Handling Missing Values

**Check null values:**

```python
df.isnull()
```

**Fill missing values:**

```python
df.fillna(0)
```

---

## 16. Sorting Data

**Ascending (default):**

```python
df.sort_values("Age")
```

**Descending:**

```python
df.sort_values("Age", ascending=False)
```

---

## 17. GroupBy Operation

Used for **data aggregation**.

**Example dataset:**

| Department | Salary |
|------------|--------|
| IT | 50000 |
| HR | 40000 |
| IT | 60000 |

```python
df.groupby("Department").mean()
```

---

## 18. Applying Functions

```python
df["Age"].apply(lambda x: x + 1)
```

---

## 19. Pandas + NumPy Operations

```python
import numpy as np

df["Age"] = np.sqrt(df["Age"])
```

---

## 20. Broadcasting in Pandas

```python
df["Age"] + 5
```

> Every element in the column gets +5 automatically.

---

## 21. Exporting Data

**Save CSV:**

```python
df.to_csv("output.csv")
```

**Save Excel:**

```python
df.to_excel("output.xlsx")
```

---

## 📋 Quick Revision Summary

| Topic | Meaning |
|-------|---------|
| `Series` | 1D labeled array |
| `DataFrame` | 2D data table |
| `read_csv()` | load dataset |
| `head()` | first rows |
| `loc` / `iloc` | row selection |
| `groupby()` | aggregation |
| `fillna()` | handle missing values |
| `sort_values()` | sorting |