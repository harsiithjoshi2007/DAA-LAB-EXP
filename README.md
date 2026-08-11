# DAA-LAB-EXP

# CS5303 - Design and Analysis of Algorithms Lab Portfolio

This repository contains the implementation, performance analysis, and documentation for the first five core experiments of the Design and Analysis of Algorithms laboratory curriculum (Academic Year: 2026 – 2027).

## 🏫 Institutional Details
- **Institution:** Chennai Institute of Technology
- **Department:** Computer Science and Engineering
- **Course:** B.E. Computer Science and Engineering (III Semester)
- **Faculty:** Dr. J Venkatesh

---

## 🗂️ Portfolio Index

| Exp. No. | Title of Experiment | Paradigm / Technique | Analysis Document |
| :---: | :--- | :--- | :--- |
| 1 | Implementation and Performance Analysis of Interpolation Search | Searching / Decrease and Conquer | [Analysis Details](docs/exp1_analysis.md) |
| 2 | Comparative Analysis of Naive, Rabin-Karp, and KMP Algorithms | String Matching | [Analysis Details](docs/exp2_analysis.md) |
| 3 | Implementation of Kruskal's and Prim's Algorithms for Minimum Spanning Tree | Greedy Approach | [Analysis Details](docs/exp3_analysis.md) |
| 4 | Implementation of Single Source Shortest Path Algorithm (Dijkstra's) | Greedy Approach | [Analysis Details](docs/exp4_analysis.md) |
| 5 | To Find Min-Max Value by Applying Divide and Conquer Technique | Divide and Conquer | [Analysis Details](docs/exp5_analysis.md) |

---

## 🚀 Execution Guide

### Prerequisites
Make sure you have Python 3.8 or higher installed. No external third-party packages are required.

### Running Experiments
You can execute individual files directly from the terminal root directory:

```bash
python src/exp1_interpolation_search.py
python src/exp2_string_matching.py
python src/exp3_mst_algorithms.py
python src/exp4_dijkstra_shortest_path.py
python src/exp5_min_max_divide_conquer.py
```

---

## 📁 Repository Structure

```text
daa-lab-portfolio/
├── .gitignore
├── README.md
├── src/
│   ├── __init__.py
│   ├── exp1_interpolation_search.py
│   ├── exp2_string_matching.py
│   ├── exp3_mst_algorithms.py
│   ├── exp4_dijkstra_shortest_path.py
│   └── exp5_min_max_divide_conquer.py
└── docs/
    ├── exp1_analysis.md
    ├── exp2_analysis.md
    ├── exp3_analysis.md
    ├── exp4_analysis.md
    └── exp5_analysis.md
```

---

## 💡 Notes
- Each experiment is implemented as a standalone Python module under `src/`.
- Analysis documents in `docs/` summarize design, complexity, and interpretation.
- This structure is ideal for GitHub publication and academic portfolio presentation.
