# Algorithmic Sorting and Performance Analysis

This project was developed as part of the BBM103: Introduction to Programming Laboratory course. It focuses on implementing fundamental sorting algorithms and analyzing their efficiency through a simulated logistics scenario.

## 📌 Project Overview

The goal of this project is to optimize a logistics network by sorting warehouse data based on multiple criteria. The system handles a synthetic dataset containing Warehouse IDs, Priority Levels, and Package Counts.

The analysis involves a two-level sorting strategy:
1. Primary Sort: Sorting by Priority Level (Ascending).
2. Secondary Sort: Sorting by Package Count (Ascending) within the same priority level.

## 🛠️ Implemented Algorithms

Three different sorting methodologies are implemented and compared:
- **Bubble Sort:** An iterative approach used as a baseline for comparison.
- **Merge Sort:** A divide-and-conquer algorithm focused on recursive efficiency.
- **Quick Sort:** A highly efficient recursive sorting algorithm using a partitioning strategy.

## 📊 Key Features

- **Custom PRNG:** Includes a custom Linear Congruential Generator (LCG) for reproducible synthetic data generation.
- **Performance Metrics:** Tracks iteration counts for Bubble Sort and recursive step counts for Merge and Quick Sort to compare algorithmic complexity.
- **Stability & Correctness:** Ensures that all three algorithms produce identical sorted results despite their different internal logic.

## 📁 File Structure

- `hw_05.py`: The main Python script containing algorithm implementations and the execution logic.
- `hw05_input.csv`: The generated synthetic dataset of warehouses.
- `hw05_output.txt`: Detailed output showing sorted results and performance metrics for each algorithm.

## 🚀 How to Run

1. Ensure you have Python 3.x installed.
2. Clone this repository:
   git clone https://github.com/yourusername/logistics-sorting-analysis.git
3. Run the script:
   python hw_05.py
4. Check `hw05_output.txt` for the analysis results.

## 📈 Complexity Analysis
The implementation compares the efficiency of each algorithm:
- Bubble Sort: O(n²) average and worst-case complexity.
- Merge Sort: O(n log n) stable sorting.
- Quick Sort: O(n log n) average complexity.

---
*Developed as a Computer Engineering student at Hacettepe University.*