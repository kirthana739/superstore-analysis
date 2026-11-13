# Superstore Sales Analysis

A team project that cleans the Superstore sales data, finds what drives sales and profit using **Pandas**, and presents the results as charts. The project was built by three people using a proper **Git and GitHub workflow** (branches, Pull Requests, code review and releases).

## Project Overview

- **Dataset:** Superstore sales data from Kaggle (about 10,000 orders)
- **Goal:** Clean the data, find the factors behind sales and profit, and show them visually
- **Run the whole pipeline with one command:** `python main.py` (clean, analyse, then draw charts)

## Key Findings

| Finding | Detail |
|---|---|
| Technology has the highest sales | About $836K in sales with a healthy 17% profit margin |
| Furniture sells a lot but earns little | About $742K in sales but only a 2.5% profit margin |
| Discounts hurt profit | Discount and profit are negatively correlated (about -0.22), so higher discounts tend to reduce profit |
| Loss-making products | 301 products are loss-making overall |
| Best region | The West region performs best |

## Project Structure

```
superstore-sales-analysis/
├── data/
│   └── raw/                # Put the downloaded dataset here (not uploaded to GitHub)
├── outputs/
│   └── charts/             # Charts are saved here when main.py runs
├── cleaning.py             # Data cleaning
├── analysis.py             # Sales and profit analysis
├── visualization.py        # Chart creation
├── main.py                 # Runs the full pipeline
└── README.md
```

## Team and Roles

| Member | Role | Responsibility |
|---|---|---|
| Kirthana | Team lead | Repo setup, branch management, reviewing and merging Pull Requests, testing, release (`v1.0`), and data cleaning in `cleaning.py` |
| Ananya Puthran | Data analyst | Analysis functions in `analysis.py` |
| Poonam | Visualization | Charts in `visualization.py` and the pipeline in `main.py` |

## How to Run

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```
2. **Install the requirements**
   ```bash
   pip install pandas matplotlib
   ```
3. **Download the dataset** from Kaggle (search for "Superstore Sales Dataset") and place the CSV file inside `data/raw/`. The file is large, so it is not included in this repository.
4. **Run the project**
   ```bash
   python main.py
   ```
5. **See the results** in the terminal, and the charts in `outputs/charts/`.

## Git Workflow

We followed a branching workflow so that nobody's work clashed:

- `main` holds the final, stable code. It is protected, so changes need a Pull Request.
- `dev` is where everyone's work is combined and tested first.
- Each member worked on their own feature branch:
  - `feature/data-cleaning`
  - `feature/data-analysis`
  - `feature/visualization`
- Nobody pushed directly to `dev` or `main`. Each member opened a **Pull Request** into `dev`, and the team lead reviewed and merged it.
- Finally, `dev` was merged into `main` and tagged **`v1.0`**.

## What We Learned

- Branching, Pull Requests, code review and teamwork on GitHub
- Fixing real Git problems, such as a wrong repository name and `main` and `dev` going out of sync
- Finding business insights from raw data with Pandas

## Future Improvements

- Add more analysis, such as sales forecasting
- Add automated tests
