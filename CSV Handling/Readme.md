📌 Project Overview

This repository contains my personal notes and practice code for working with CSV files in Python.
It documents what I learned, the logic behind reading/writing CSV files, and example scripts I wrote while following a video tutorial on the topic.

The focus of this section is on understanding how to:

Read data from CSV files

Write data into CSV files

Manipulate and analyze CSV data

Handle CSVs with Python libraries

The goal is to help me revisit these concepts easily in the future and build a stronger foundation in data handling.

---
🧠 What I Did

In this project, I:

Learned the basics of the CSV file format

What CSV means and when to use it.

How CSV stores data in rows and columns separated by commas.

Explored Python CSV handling

Used built-in Python libraries like csv to read and write files.

Practiced reading rows from a CSV into lists/dictionaries.

Tried writing new rows to a CSV file.

Tested sample CSV files

Loaded different CSV files to experiment with functions.

Printed and verified data read from CSVs.

---
🧪 Code Snippets
✅ Reading a CSV file

import csv

with open('data1.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

✅ Writing to a CSV file

import csv

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'email', 'age'])
    writer.writerow(['Alice', 'alice@example.com', '24'])

---
🧩 Concepts Covered

CSV format & why it’s useful

Python csv.reader vs csv.writer

Opening and closing files properly

Iterating rows

Writing rows back to disk

---
📌 Future Improvements

In future, I may add:

✔ Handling CSV files with pandas
✔ Filtering, sorting, and aggregating CSV data
✔ Web scraping + saving data to CSV
✔ Examples with real datasets
