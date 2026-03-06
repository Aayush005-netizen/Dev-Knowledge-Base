# 📊 Matplotlib Notes

Matplotlib is a **Python library used for data visualization**. It allows you to create different types of graphs and charts to visually represent data. It works seamlessly with NumPy, Pandas, SciPy, and Seaborn, and is one of the most widely used visualization libraries in Python.

> 💡 **What is Data Visualization?**
> Representing data in graphical form so humans can easily understand patterns, trends, and relationships — instead of reading raw tables, a line chart instantly shows the trend.

---

## 🔧 Setup & Installation

```bash
pip install matplotlib
```

```python
import matplotlib.pyplot as plt
import pandas as pd

x = [1, 2, 3]
y = [4, 5, 6]

plt.plot(x, y)  # plots points (1,4), (2,5), (3,6)
plt.grid()
plt.show()
```

---

## 🧬 Anatomy of a Figure

![Anatomy of a Matplotlib Figure](https://raw.githubusercontent.com/Aayush005-netizen/Dev-Knowledge-Base/main/Photos/anatomy_of_matplotlib_graph.webp)

A Matplotlib visualization is made of several nested components:

<details>
<summary>📖 Click to expand — Detailed Explanation of Every Component</summary>

### 🖼️ Figure — `plt.figure()`
The **Figure** is the outermost container — the entire window or canvas. Think of it as a blank sheet of paper that holds everything else. You can have multiple Axes (subplots) inside a single Figure.

```python
fig = plt.figure(figsize=(10, 6))  # width=10 inches, height=6 inches
```

### 📐 Axes — `fig.subplots()` / `fig.add_subplot()`
The **Axes** is the actual plotting area where data gets drawn. It contains the X axis, Y axis, title, and all plot elements. One Figure can hold multiple Axes. Don't confuse **Axes** (plot area) with **Axis** (the number line).

```python
fig, ax = plt.subplots()         # 1 plot
fig, axs = plt.subplots(1, 3)    # 3 plots side by side
```

### 📏 Axis — `ax.xaxis` / `ax.yaxis`
The **Axis** objects are the actual X and Y number lines. They control the scale range, tick positions, and tick labels.

```python
ax.xaxis  # horizontal number line
ax.yaxis  # vertical number line
```

### 🏷️ Title — `ax.set_title()`
The **Title** is the descriptive text label at the top of the Axes.

```python
ax.set_title("Age vs Salary")
plt.title("Age vs Salary")   # Pyplot shorthand
```

### 🔤 X & Y Labels — `ax.set_xlabel()` / `ax.set_ylabel()`
**Labels** describe what each axis represents. Always include them for clarity.

```python
ax.set_xlabel("Age (years)")
ax.set_ylabel("Salary (INR)")
```

### 📌 Legend — `ax.legend()`
The **Legend** identifies plotted elements with color-coded labels. Use `label=` when plotting, then call `legend()` to show it.

```python
plt.plot(x, y1, label="Sales")
plt.plot(x, y2, label="Profit")
plt.legend()
```

### 🔲 Grid — `ax.grid()`
The **Grid** adds reference lines in the background to make reading values easier.

```python
plt.grid()
ax.grid(axis='y', linestyle='--')  # horizontal dashes only
```

### 🦴 Spines — `ax.spines`
**Spines** are the four border lines that form the box around the plot (top, bottom, left, right). You can hide or style them for cleaner visuals.

```python
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
```

### ✏️ Major Ticks — `ax.yaxis.set_major_locator()`
**Major Ticks** are the primary, labeled scale markers on an axis (e.g., 0, 10000, 20000). They define the main intervals.

```python
from matplotlib.ticker import MultipleLocator
ax.yaxis.set_major_locator(MultipleLocator(10000))
ax.yaxis.set_major_formatter(...)  # format how labels look
```

### ✏️ Minor Ticks — `ax.yaxis.set_minor_locator()`
**Minor Ticks** are smaller, unlabeled markers between major ticks — they add finer granularity to the scale without cluttering labels.

```python
ax.yaxis.set_minor_locator(MultipleLocator(2500))
```

### ⚫ Markers — `marker=` in `plot()` / `scatter()`
**Markers** are shapes drawn at each individual data point. Common types: `'o'` circle, `'*'` star, `'^'` triangle, `'s'` square.

```python
plt.plot(x, y, marker='o')
plt.scatter(x, y, marker='^')
```

### 📉 Line — `ax.plot()`
The **Line** connects data points. Control color, style, and thickness.

```python
ax.plot(x, y, color='blue', linestyle='--', linewidth=2)
```

</details>

| Component | Description | API |
|-----------|-------------|-----|
| Figure | The entire canvas / outer container | `plt.figure()` |
| Axes | The actual plotting area (contains X & Y axis) | `fig.add_subplot()` / `fig.subplots()` |
| Axis | The number scales along the edges (X or Y) | `ax.xaxis` / `ax.yaxis` |
| Title | Describes the plot | `ax.set_title()` |
| Labels | Describe the axes | `ax.set_xlabel()` / `ax.set_ylabel()` |
| Legend | Identifies plotted elements | `ax.legend()` |
| Grid | Background reference lines | `ax.grid()` |
| Spines | The border lines of the axes | `ax.spines` |
| Major/Minor Ticks | Scale markers on axes | `ax.yaxis.set_major_locator()` |
| Markers | Data point shapes in scatter/line plots | `ax.scatter()` |

---

## 🖼️ Two APIs in Matplotlib

| API | Style | Best For |
|-----|-------|----------|
| **Pyplot API** | Functional / quick (`plt.plot()`) | Simple, quick plots |
| **Object-Oriented API** | Explicit (`fig, ax = plt.subplots()`) | Multiple plots, full customization |

---

## 📈 Pyplot API

### 1️⃣ Univariate – Numerical

> Analysis of a **single numerical variable** (e.g. distribution of Salary). Charts: Histogram, Boxplot, Line Plot.

**Line Plot** — trends over ordered data

```python
plt.plot(df["Salary"], color="red", marker="*", linestyle=":", linewidth="2")
plt.grid()
plt.show()
```

Customization options:

| Parameter | Meaning |
|-----------|---------|
| `color` | Line color |
| `linestyle` | `'-'` solid, `'--'` dashed, `':'` dotted |
| `marker` | Shape at data points (`'o'`, `'*'`, `'^'`) |
| `linewidth` | Thickness of the line |

**Histogram** — shows frequency distribution; bins divide data into intervals

```python
plt.hist(df["Salary"], bins=5, color="green")
plt.show()
```

**Boxplot** — shows median, Q1–Q3 (IQR), whiskers (range), and outlier points

```python
plt.boxplot(df["Salary"])
plt.show()

# Demo: add an outlier row to see it appear as a point
df.loc[20] = [0]
plt.boxplot(df["Salary"])
plt.show()
df.drop(index=20, inplace=True)
```

![Boxplot Anatomy](https://raw.githubusercontent.com/Aayush005-netizen/Dev-Knowledge-Base/main/Photos/boxplot.webp)

| Part | Meaning |
|------|---------|
| Median line | Middle value (Q2) |
| Box | Q1 to Q3 (interquartile range) |
| Whiskers | Extend to min/max within 1.5×IQR |
| Points beyond whiskers | Outliers |

---

### 2️⃣ Univariate – Categorical

> Analysis of a **single categorical variable** (e.g. Department counts). Charts: Pie, Bar/Count Plot.

**Pie Chart** — shows proportions of each category

```python
count = df["dept"].value_counts()
plt.pie(count, labels=count.index, autopct="%1.2f", explode=[0, 0.1, 0.2])
plt.axis("equal")   # keeps it circular
plt.show()
```

**Count/Bar Plot** — frequency of each category

```python
plt.bar(count.index, count, color=["green", "black", "red"])
plt.show()
```

---

### 3️⃣ Bivariate – Numerical vs Numerical

> Relationship between **two numerical variables** (e.g. Age vs Salary). Charts: Scatter, Line, Bar.

**Scatter Plot** — best for finding correlation and patterns

```python
plt.scatter(df["Age"], df["Salary"], color="orange")
plt.show()
```

**Line Plot (sorted)** — sort by x-axis first for a clean line

```python
sort_age = df.sort_values("Age")
plt.plot(sort_age["Age"], df["Salary"], color="red", marker="*", linewidth="2")
plt.grid()
plt.show()
```

**Bar Chart**

```python
plt.bar(sort_age["Age"], df["Salary"], color="green")
plt.show()
```

---

### 4️⃣ Bivariate – Numerical vs Categorical

> Comparing a **numerical value across categories** (e.g. Salary by Department).

**Grouped Boxplot** — compare spread & outliers across groups

```python
hr_sal = df[df["dept"] == "HR"]["Salary"]
it_sal = df[df["dept"] == "IT"]["Salary"]
fin_sal = df[df["dept"] == "Finance"]["Salary"]

plt.boxplot([hr_sal, it_sal, fin_sal], labels=["HR", "IT", "Finance"])
plt.show()
```

**Pie Chart (by group sum)**

```python
salary_by_dept = df.groupby("dept")["Salary"].sum()
plt.pie(salary_by_dept, labels=salary_by_dept.index, autopct="%1.2f", shadow=True, explode=[0.1, 0, 0.1])
plt.axis("equal")
plt.show()
```

**Bar Plot (mean salary per dept)**

```python
hr_mean = sum(hr_sal)/len(hr_sal)
it_mean = sum(it_sal)/len(it_sal)
fin_mean = sum(fin_sal)/len(fin_sal)

plt.bar(["HR", "IT", "Finance"], [hr_mean, it_mean, fin_mean], color=["green", "black", "red"])
plt.grid()
plt.show()
```

---

### 5️⃣ Multivariate – 3+ Variables

> Visualizing **more than two variables** simultaneously. Charts: Bubble Plot, Color-mapped Scatter, 3D Plots.

**Bubble Plot** — 3 numerical variables; size of bubble = 3rd variable

```python
plt.scatter(df["Age"], df["Salary"], s=df["experience"]*50, color="skyblue", edgecolors="black")
plt.title("Age vs Salary vs Experience")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()
```

| Parameter | Meaning |
|-----------|---------|
| `x`, `y` | Variable 1 & 2 (position) |
| `s` | Bubble size = 3rd variable |
| `c` | Color = categorical variable |

**Scatter with Color Mapping — 2 numerical + 1 categorical**

```python
# Method 1: Direct color map (no legend)
plt.scatter(df["Age"], df["Salary"], c=df["dept"].map({"HR": "yellow", "IT": "blue", "Finance": "orange"}))
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age vs Salary vs Dept")
plt.show()

# Method 2: Loop — gives proper legend per category
color = {"HR": "yellow", "IT": "blue", "Finance": "orange"}
for dept, col in color.items():
    df_dept = df[df["dept"] == dept]
    plt.scatter(df_dept["Age"], df_dept["Salary"], c=col, label=dept)
plt.legend()
plt.show()
```

---

## 🎛️ Object-Oriented API

> More control over layout. `fig` = the whole canvas, `axs` = individual plot areas. Preferred for professional and multi-plot visualizations.

```python
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Line Plot
axs[0].plot(sort_age["Age"], df["Salary"], color="red", marker="*", linewidth="2", markersize=2)
axs[0].grid()
axs[0].set_title("Line Plot")
axs[0].set_xlabel("Age")
axs[0].set_ylabel("Salary")

# Histogram
axs[1].hist(df["Salary"], bins=5, color="skyblue")
axs[1].set_title("Histogram")
axs[1].set_xlabel("Salary")
axs[1].set_ylabel("Frequency")

# Boxplot
axs[2].boxplot(df["Salary"])
axs[2].set_title("Boxplot")
axs[2].set_xlabel("Salary")

plt.savefig("multipleplots.png")   # save BEFORE show()
plt.show()
```

**Multi-line Plot with Legend**

```python
plt.plot(df2["Year"], df2["Sales"], label="Sales")
plt.plot(df2["Year"], df2["Profit"], label="Profit")
plt.plot(df2["Year"], df2["Expenses"], label="Expenses")

plt.title("Financial Analysis")
plt.xlabel("Year")
plt.ylabel("Amount")
plt.legend()
plt.show()
```

> 💡 `plt.subplots(rows, cols)` creates a grid of plots. Access each with `axs[row, col]` for 2D grids or `axs[i]` for a single row.

---

## 🌐 3D Plots

**Matplotlib 3D** (static)

```python
ax = plt.axes(projection="3d")
ax.scatter(df["Age"], df["Salary"], df["experience"])
ax.set_xlabel("Age")
ax.set_ylabel("Salary")
ax.set_zlabel("Experience")
plt.show()
```

**Plotly** (interactive — rotate, zoom, hover)

```python
import plotly.express as px
fig = px.scatter_3d(df, x="Age", y="Salary", z="experience", title="3D Scatter Plot")
fig.show()
```

> 💡 Use Plotly for interactive 3D exploration; use Matplotlib 3D for static figures in reports/papers.

---

## 🗂️ Quick Reference

| Plot Type | Analysis Type | Use Case | Function |
|-----------|--------------|----------|----------|
| Line | Univariate / Bivariate | Trends over time or order | `plt.plot()` |
| Histogram | Univariate Numerical | Distribution of data | `plt.hist()` |
| Boxplot | Univariate / Bivariate | Spread, IQR & outliers | `plt.boxplot()` |
| Pie | Univariate Categorical | Proportions of categories | `plt.pie()` |
| Bar | Univariate / Bivariate | Comparing categories | `plt.bar()` |
| Scatter | Bivariate Numerical | Correlation between 2 variables | `plt.scatter()` |
| Bubble | Multivariate | 3 numerical variables | `plt.scatter(s=...)` |
| 3D Scatter | Multivariate | 3D view of 3 variables | `plt.axes(projection="3d")` |