# SpaceX Falcon 9 — First Stage Landing Prediction

**Author:** Piyu
**Course:** IBM Data Science Professional Certificate — Applied Data Science Capstone

## Project Overview

SpaceX advertises Falcon 9 launches at ~$62M — far cheaper than competitors (~$165M+) — largely
because it reuses the rocket's first stage instead of discarding it. This project builds a machine
learning classifier to predict whether the first stage will land successfully, which can be used to
estimate the cost of a given launch.

## Repository Structure

```
notebooks/
  1_Data_Wrangling.ipynb       Cleans the raw launch log, engineers the binary `Class` label
  2_EDA_Visualization.ipynb    Explores trends (flight number, payload, orbit, year) with matplotlib/seaborn
  3_EDA_SQL.ipynb              SQL queries (SQLite) answering specific business questions
  4_Folium_Map.ipynb           Interactive map of launch sites with success/failure markers
  6_ML_Prediction.ipynb        Logistic Regression, SVM, Decision Tree, KNN — tuned via GridSearchCV

app.py                          Plotly Dash interactive dashboard (run: python app.py)
data/                           Source CSVs used across the notebooks
images/                         Exported chart images used in the presentation
SpaceX_Falcon9_Capstone_Piyu.pptx   Final presentation summarizing the project
```

## How to Run

```bash
pip install pandas numpy matplotlib seaborn scikit-learn folium plotly dash jupyter
jupyter notebook notebooks/
```

To launch the dashboard:

```bash
python app.py
```

## Key Results

- Overall first-stage landing success rate: **60.4%** across 101 launches (2010–2020)
- Success rate climbed from 0% (2010–2014) to ~90% (2019–2020)
- KSC LC-39A had the highest site-level success rate (77.3%)
- Decision Tree classifier generalized best in 5-fold cross-validation (87.3% CV accuracy)

## Data Source

Launch records compiled from publicly available SpaceX launch history, standard to the IBM Data
Science Capstone assignment. All analysis, code, and write-up in this repository are original.
