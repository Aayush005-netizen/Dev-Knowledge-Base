# Seaborn Notes

---

## 1. What is Seaborn?

Seaborn is a Python data visualization library built on top of Matplotlib that provides high-level, attractive statistical graphics.

### Why Seaborn is used
- Better looking plots
- Statistical visualizations
- Works easily with pandas DataFrames
- Less code than Matplotlib

---

## 2. Installing Seaborn

```python
pip install seaborn
```

---

## 3. Importing Libraries

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
```

| Alias | Library |
|-------|---------|
| `sns` | seaborn |
| `plt` | matplotlib.pyplot |

---

## 4. Loading Dataset

Seaborn provides built-in datasets.

```python
df = sns.load_dataset("tips")
print(df.head())
```

### Dataset Columns (`tips`)

| Column | Meaning |
|--------|---------|
| `total_bill` | Bill amount |
| `tip` | Tip amount |
| `sex` | Male/Female |
| `smoker` | Yes/No |
| `day` | Day of week |
| `time` | Lunch/Dinner |
| `size` | Number of people |

---

## 5. Distribution Plots

Used to understand data distribution.

### Histogram
Shows frequency distribution.

```python
sns.histplot(df["total_bill"])
plt.show()
```

**What it shows:**
- Data distribution
- Spread of values

### KDE Plot (Kernel Density Estimate)
Shows smooth distribution curve.

```python
sns.kdeplot(df["total_bill"])
```

### Combined Histogram + KDE

```python
sns.histplot(df["total_bill"], kde=True)
```

---

## 6. Relational Plots

Used to show relationships between variables.

### Scatter Plot
Shows relationship between two numerical variables.

```python
sns.scatterplot(x="total_bill", y="tip", data=df)
```

- X → total bill
- Y → tip

### Line Plot
Used for time-series data.

```python
sns.lineplot(x="size", y="total_bill", data=df)
```

---

## 7. Categorical Plots

Used for categorical variables.

### Bar Plot
Shows average values of categories.

```python
sns.barplot(x="day", y="total_bill", data=df)
```

> **Insight:** Which day has the highest average bill?

### Count Plot
Shows number of observations in each category.

```python
sns.countplot(x="sex", data=df)
```

> **Output:** Male count vs Female count

### Box Plot
Shows data distribution and outliers.

```python
sns.boxplot(x="day", y="total_bill", data=df)
```

#### Boxplot Components

| Part | Meaning |
|------|---------|
| Box | Interquartile range (IQR) |
| Line inside box | Median |
| Whiskers | Range |
| Dots | Outliers |

### Violin Plot
Combination of box plot + KDE distribution.

```python
sns.violinplot(x="day", y="total_bill", data=df)
```

**Shows:**
- Distribution shape
- Density

---

## 8. Pair Plot

Shows relationships between all numerical variables.

```python
sns.pairplot(df)
```

- Multiple scatter plots
- Histograms on the diagonal

> Very useful for machine learning exploration.

---

## 9. Heatmap

Used to visualize correlation matrix.

```python
corr = df.corr()
sns.heatmap(corr, annot=True)
```

| Color | Meaning |
|-------|---------|
| Dark | Strong correlation |
| Light | Weak correlation |

---

## 10. Styling Seaborn

Seaborn supports different themes.

```python
sns.set_style("darkgrid")
```

**Available styles:**
- `darkgrid`
- `whitegrid`
- `dark`
- `white`
- `ticks`

---

## 11. Changing Plot Colors

```python
# Single color
sns.barplot(x="day", y="total_bill", data=df, color="red")

# Palette
sns.barplot(x="day", y="total_bill", data=df, palette="viridis")
```

---

## 12. Adding Titles and Labels

```python
plt.title("Total Bill vs Tips")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
```

---

## 13. Figure Size

```python
plt.figure(figsize=(10, 6))
```

**Example:**

```python
plt.figure(figsize=(8, 5))
sns.barplot(x="day", y="total_bill", data=df)
```

---

## 14. Facet Grid

Used for multiple plots by category.

```python
g = sns.FacetGrid(df, col="sex")
g.map(sns.scatterplot, "total_bill", "tip")
```

> Generates separate plots for Male and Female.

---

## 15. Seaborn Workflow (Typical Data Science Flow)

| Step | Action |
|------|--------|
| Step 1 | Load dataset |
| Step 2 | Explore dataset |
| Step 3 | Check distributions |
| Step 4 | Check relationships |
| Step 5 | Visualize correlations |

---

## Quick Revision Summary

| Plot | Purpose |
|------|---------|
| `histplot` | Distribution |
| `kdeplot` | Density curve |
| `scatterplot` | Relation between variables |
| `lineplot` | Time series |
| `barplot` | Average of categories |
| `countplot` | Category frequency |
| `boxplot` | Outliers & distribution |
| `violinplot` | Density + distribution |
| `pairplot` | Relationship between all variables |
| `heatmap` | Correlation visualization |