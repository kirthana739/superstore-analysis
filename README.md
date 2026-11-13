# Superstore Sales Analysis (Pandas)

Cleaning, analysing and visualising the Sample Superstore sales dataset using Python, Pandas, Matplotlib and Seaborn.

## Team and roles
| Member | Branch | File |
|---|---|---|
| Kirthana  | `feature/data-cleaning` | `src/cleaning.py` |
| Ananya | `feature/data-analysis` | `src/analysis.py` |
| Poonam | `feature/visualization` | `src/visualization.py`, `main.py` |

## Dataset
Sample Superstore (Kaggle). Place the CSV at `data/raw/superstore.csv`.

## Setup
```bash
pip install -r requirements.txt
python main.py
```

## Output
- `data/cleaned/superstore_clean.csv` - cleaned data
- `outputs/tables/` - analysis tables (CSV)
- `outputs/charts/` - charts (PNG)

## Git workflow
- `main`: stable code only, changes come through Pull Requests
- `dev`: integration branch
- `feature/*`: one branch per member, merged into `dev` by Pull Request after review

## Key insights
(Fill this in after running `main.py`, using the printed KEY INSIGHTS.)

## Screenshots
(Add the charts from `outputs/charts/` here.)
