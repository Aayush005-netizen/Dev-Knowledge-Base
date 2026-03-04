# Machine Learning Notes

![ML Notes Page 1](https://raw.githubusercontent.com/Aayush005-netizen/Dev-Knowledge-Base/main/Photos/ML_Notes_1.jpg)
![ML Notes Page 1](https://raw.githubusercontent.com/Aayush005-netizen/Dev-Knowledge-Base/main/Photos/ML_Notes_2.jpg)
![ML Notes Page 1](https://raw.githubusercontent.com/Aayush005-netizen/Dev-Knowledge-Base/main/Photos/ML_Notes_3.jpg)
![ML Notes Page 1](https://raw.githubusercontent.com/Aayush005-netizen/Dev-Knowledge-Base/main/Photos/ML_Notes_4.jpg)
![ML Notes Page 1](https://raw.githubusercontent.com/Aayush005-netizen/Dev-Knowledge-Base/main/Photos/ML_Notes_5.jpg)
![ML Notes Page 1](https://raw.githubusercontent.com/Aayush005-netizen/Dev-Knowledge-Base/main/Photos/ML_Notes_6.jpg)
![ML Notes Page 1](https://raw.githubusercontent.com/Aayush005-netizen/Dev-Knowledge-Base/main/Photos/ML_Notes_7.jpg)
![ML Notes Page 1](https://raw.githubusercontent.com/Aayush005-netizen/Dev-Knowledge-Base/main/Photos/ML_Notes_8.jpg)
![ML Notes Page 1](https://raw.githubusercontent.com/Aayush005-netizen/Dev-Knowledge-Base/main/Photos/ML_Notes_9.jpg)
![ML Notes Page 1](https://raw.githubusercontent.com/Aayush005-netizen/Dev-Knowledge-Base/main/Photos/ML_Notes_10.jpg)
![ML Notes Page 1](https://raw.githubusercontent.com/Aayush005-netizen/Dev-Knowledge-Base/main/Photos/ML_Notes_11.jpg)
![ML Notes Page 1](https://raw.githubusercontent.com/Aayush005-netizen/Dev-Knowledge-Base/main/Photos/ML_Notes_12.jpg)
![ML Notes Page 1](https://raw.githubusercontent.com/Aayush005-netizen/Dev-Knowledge-Base/main/Photos/ML_Notes_13.jpg)
![ML Notes Page 1](https://raw.githubusercontent.com/Aayush005-netizen/Dev-Knowledge-Base/main/Photos/ML_Notes_14.jpeg)

# 📊 EDA Using Univariate Analysis

---

## 📌 Table of Contents

1. [What is EDA?](#1-what-is-eda)
2. [What is Univariate Analysis?](#2-what-is-univariate-analysis)
3. [Univariate Analysis for Numerical Data](#3-univariate-analysis-for-numerical-data)
4. [Histogram](#4-histogram)
5. [KDE Plot](#5-kde-plot-density-plot)
6. [Box Plot](#6-box-plot)
7. [Distribution Shape](#7-distribution-shape)
8. [Univariate Analysis for Categorical Data](#8-univariate-analysis-for-categorical-data)
9. [Value Counts](#9-value-counts)
10. [Bar Plot](#10-bar-plot)
11. [Pie Chart](#11-pie-chart)
12. [Typical EDA Workflow](#12-typical-eda-workflow)
13. [Full Code Example](#13-full-code-example)
14. [Key Interview Points](#14-key-interview-points)

---

## 1. What is EDA?

**Exploratory Data Analysis (EDA)** is the process of analyzing datasets to understand:

- 🗂️ Structure of the data
- 📈 Distribution of variables
- ❓ Missing values
- 🚨 Outliers
- 🔍 Patterns or anomalies

> EDA helps us **prepare data** before applying Machine Learning models.

### Why EDA is Important

| Purpose | Description |
|---|---|
| 🐛 Detect errors | Find issues in the dataset |
| 📊 Understand distribution | See how data is spread |
| 🔗 Feature relationships | Identify connections between variables |
| 🎯 Detect outliers | Spot unusual values |
| 🤖 Model selection | Choose proper ML models |

---

## 2. What is Univariate Analysis?

**Univariate Analysis** means analyzing **one variable at a time**.

It helps understand:
- Distribution
- Central tendency
- Spread of values
- Outliers

### Types of Variables

| Variable Type | Example |
|---|---|
| **Numerical** | Age, Salary, Height |
| **Categorical** | Gender, City, Color |

> Different techniques are used for each type.

---

## 3. Univariate Analysis for Numerical Data

### 3.1 Descriptive Statistics

We first analyze statistical summaries.

| Measure | Meaning |
|---|---|
| **Mean** | Average value |
| **Median** | Middle value |
| **Mode** | Most frequent value |
| **Std** | Spread of data |
| **Min** | Smallest value |
| **Max** | Largest value |

```python
import pandas as pd

df = pd.read_csv("data.csv")

df['age'].describe()
```

**Output:**

```
count    1000.000000
mean       35.520000
std        12.345678
min        18.000000
25%        26.000000
50%        34.000000
75%        44.000000
max        75.000000
```

---

## 4. Histogram

### What is a Histogram?

A **Histogram** shows the distribution of numerical data by dividing values into **bins**.

### Use Cases
- ✅ Detect skewness
- ✅ Understand distribution shape
- ✅ Detect concentration of values

```python
import matplotlib.pyplot as plt

plt.hist(df['age'], bins=20, color='steelblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
```

---

## 5. KDE Plot (Density Plot)

**KDE = Kernel Density Estimation**

Shows a smooth **probability distribution curve** — useful when you want a continuous view of the distribution.

```python
import seaborn as sns

sns.kdeplot(df['age'], fill=True)
plt.title('Age - KDE Plot')
plt.show()
```

---

## 6. Box Plot

### What is a Boxplot?

A **Boxplot** helps identify:
- 🎯 Outliers
- 📏 Data spread
- 📍 Median
- 📦 Quartiles

### Boxplot Structure

```
|----[  Q1 -------- Median -------- Q3  ]----|
Min                                          Max
     ← IQR (Interquartile Range) →
```

### IQR Formula

```
IQR = Q3 - Q1
```

### Outlier Detection

```
Upper Fence: Value > Q3 + 1.5 × IQR  ← Outlier
Lower Fence: Value < Q1 - 1.5 × IQR  ← Outlier
```

```python
import seaborn as sns

sns.boxplot(x=df['age'])
plt.title('Age - Box Plot')
plt.show()
```

---

## 7. Distribution Shape

Understanding distribution shape is critical for choosing ML models and preprocessing steps.

### 🔵 Normal Distribution
- Symmetrical bell curve
- **Mean ≈ Median ≈ Mode**

```
         ██
       ██████
     ██████████
   ██████████████
  ████████████████
```

### 🟠 Right Skewed (Positive Skew)
- Tail extends to the **right**
- **Mean > Median**
- e.g., Income distribution

```
  ███
  █████
  ████████____
```

### 🔴 Left Skewed (Negative Skew)
- Tail extends to the **left**
- **Mean < Median**
- e.g., Age at retirement

```
         ███
    _____█████
         ████████
```

---

## 8. Univariate Analysis for Categorical Data

For categorical variables we analyze:
- Frequency
- Count
- Distribution

### Example: Gender Column

| Category | Count |
|---|---|
| Male | 600 |
| Female | 400 |

---

## 9. Value Counts

The most common method for categorical analysis.

```python
df['gender'].value_counts()
```

**Output:**
```
Male      600
Female    400
Name: gender, dtype: int64
```

---

## 10. Bar Plot

Bar plots visualize categorical **frequencies** clearly.

```python
import seaborn as sns

sns.countplot(x='gender', data=df, palette='Set2')
plt.title('Gender Distribution')
plt.show()
```

---

## 11. Pie Chart

Shows **percentage distribution** of categories.

```python
df['gender'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=90,
    colors=['#66b3ff','#ff9999']
)
plt.title('Gender - Pie Chart')
plt.ylabel('')
plt.show()
```

---

## 12. Typical EDA Workflow

```
📂 Load Dataset
       ↓
🔍 Check Shape & Data Types
       ↓
❓ Handle Missing Values
       ↓
📊 Univariate Analysis       ← We are here (Day 20)
       ↓
🔗 Bivariate Analysis
       ↓
🔀 Multivariate Analysis
       ↓
⚙️ Feature Engineering
       ↓
🤖 Model Building
```

---

## 13. Full Code Example

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("train.csv")

# ── Numerical Analysis ──────────────────────────

# 1. Summary Statistics
print(df['Age'].describe())

# 2. Histogram
plt.figure(figsize=(8, 4))
plt.hist(df['Age'], bins=20, color='steelblue', edgecolor='black')
plt.title('Age Distribution - Histogram')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# 3. KDE Plot
plt.figure(figsize=(8, 4))
sns.kdeplot(df['Age'], fill=True, color='coral')
plt.title('Age Distribution - KDE Plot')
plt.show()

# 4. Box Plot
plt.figure(figsize=(8, 4))
sns.boxplot(x=df['Age'], color='lightgreen')
plt.title('Age Distribution - Box Plot')
plt.show()

# ── Categorical Analysis ────────────────────────

# 5. Value Counts
print(df['Sex'].value_counts())

# 6. Count Plot
plt.figure(figsize=(6, 4))
sns.countplot(x='Sex', data=df, palette='Set2')
plt.title('Gender Distribution')
plt.show()

# 7. Pie Chart
df['Sex'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Gender - Pie Chart')
plt.ylabel('')
plt.show()
```

---

## 14. Key Interview Points

### ❓ What is EDA?
> Process of **exploring a dataset** to understand its structure, patterns, and anomalies — before building ML models.

### ❓ What is Univariate Analysis?
> Analyzing **one variable at a time** to understand its distribution, spread, and central tendency.

### ❓ Difference between Univariate, Bivariate, Multivariate?

| Type | Variables | Example |
|---|---|---|
| **Univariate** | 1 | Histogram of Age |
| **Bivariate** | 2 | Age vs Salary scatter plot |
| **Multivariate** | > 2 | Heatmap of correlations |

### ❓ Methods for Numerical Data

| Method | Purpose |
|---|---|
| `describe()` | Summary statistics |
| Histogram | Distribution shape |
| KDE Plot | Smooth probability curve |
| Box Plot | Outlier detection + spread |

### ❓ Methods for Categorical Data

| Method | Purpose |
|---|---|
| `value_counts()` | Frequency of each category |
| Count Plot | Bar chart of frequencies |
| Pie Chart | Percentage distribution |
---

> 💡 **Tip:** Always perform EDA before jumping into model building. Clean, well-understood data leads to better models!

---
