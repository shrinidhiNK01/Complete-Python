# Python and Machine Learning Roadmap and Code Cookbook

Date: 2026-07-09

This file is a compact companion to:

- `python-complete-notes.md`
- `machine-learning-complete-notes.md`

Use it for revision, practice, and project execution.

---

## 1. Setup Commands

Create environment:

```bash
python -m venv .venv
```

Activate on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install common ML stack:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn scipy joblib jupyter pytest
```

Save dependencies:

```bash
pip freeze > requirements.txt
```

---

## 2. Learning Roadmap

### Stage 1: Python Basics

Learn:

- print
- comments
- variables
- data types
- operators
- strings
- conditionals
- loops
- lists, tuples, sets, dictionaries
- functions

Practice:

- calculator
- number guessing game
- marks/grade calculator
- password generator

### Stage 2: Intermediate Python

Learn:

- files
- JSON
- exceptions
- modules
- pip
- virtual environments
- OOP
- dataclasses
- decorators
- generators
- type hints
- testing

Practice:

- expense tracker
- contact manager
- file organizer
- command-line todo app

### Stage 3: Data Python

Learn:

- NumPy arrays
- pandas DataFrames
- missing values
- grouping
- merging
- plotting
- CSV/Excel handling

Practice:

- sales analysis
- student marks analysis
- customer churn EDA
- missing-value cleaning project

### Stage 4: Machine Learning Basics

Learn:

- features and target
- train/test split
- preprocessing
- regression
- classification
- metrics
- pipelines

Practice:

- house price prediction
- Titanic survival classification
- customer churn prediction
- spam classifier

### Stage 5: Advanced ML

Learn:

- cross-validation
- hyperparameter tuning
- feature selection
- regularization
- SVM
- KNN
- decision trees
- random forests
- boosting
- clustering
- association rules
- model interpretation
- deployment

Practice:

- fraud detection
- market basket analysis
- customer segmentation
- model API with FastAPI

---

## 3. End-to-End ML Checklist

Before modeling:

- define problem
- define target
- check if ML is needed
- understand prediction-time data
- collect data
- inspect data
- check missing values
- check duplicates
- check data types
- check outliers
- check class balance

During modeling:

- create honest train/test split
- use pipeline
- fit preprocessing only on train
- train baseline
- evaluate with correct metric
- compare multiple models
- tune hyperparameters with cross-validation
- check overfitting
- inspect errors
- save final pipeline

After modeling:

- document model
- deploy safely
- monitor inputs and predictions
- watch for drift
- retrain when needed

---

## 4. EDA Starter Code

```python
import pandas as pd

df = pd.read_csv("data.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.describe(include="all"))
print(df.isna().sum())
print(df.duplicated().sum())
```

Line by line:

- import pandas.
- read CSV into DataFrame.
- view first rows.
- view row/column count.
- view column types.
- view summary statistics.
- count missing values.
- count duplicate rows.

---

## 5. Data Cleaning Starter Code

```python
import pandas as pd

df = pd.read_csv("data.csv")

df = df.drop_duplicates()

for column in df.select_dtypes(include="number").columns:
    df[column] = df[column].fillna(df[column].median())

for column in df.select_dtypes(exclude="number").columns:
    df[column] = df[column].fillna(df[column].mode()[0])

print(df.isna().sum())
```

Line by line:

- load data.
- remove duplicate rows.
- loop over numeric columns.
- fill numeric missing values with median.
- loop over categorical columns.
- fill categorical missing values with mode.
- confirm missing values are handled.

For serious ML, prefer scikit-learn pipelines over cleaning the full dataset before splitting.

---

## 6. Regression Project Skeleton

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import joblib

df = pd.read_csv("data.csv")

X = df.drop(columns="target")
y = df["target"]

numeric_features = X.select_dtypes(include="number").columns
categorical_features = X.select_dtypes(exclude="number").columns

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", numeric_pipeline, numeric_features),
    ("cat", categorical_pipeline, categorical_features)
])

model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(n_estimators=200, random_state=42))
])

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("RMSE:", rmse)
print("R2:", r2)

joblib.dump(model, "regression_model.joblib")
```

---

## 7. Classification Project Skeleton

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import joblib

df = pd.read_csv("data.csv")

X = df.drop(columns="target")
y = df["target"]

numeric_features = X.select_dtypes(include="number").columns
categorical_features = X.select_dtypes(exclude="number").columns

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", numeric_pipeline, numeric_features),
    ("cat", categorical_pipeline, categorical_features)
])

model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced"))
])

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

joblib.dump(model, "classification_model.joblib")
```

---

## 8. Hyperparameter Tuning Skeleton

```python
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

param_grid = {
    "classifier__n_estimators": [100, 200],
    "classifier__max_depth": [None, 5, 10],
    "classifier__min_samples_leaf": [1, 5, 10]
}

model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(random_state=42))
])

search = GridSearchCV(
    model,
    param_grid=param_grid,
    cv=5,
    scoring="f1",
    n_jobs=-1
)

search.fit(X_train, y_train)

print(search.best_params_)
print(search.best_score_)
```

---

## 9. Clustering Skeleton

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

df = pd.read_csv("customers.csv")
X = df[["age", "income", "spending_score"]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = KMeans(n_clusters=4, random_state=42, n_init="auto")
clusters = model.fit_predict(X_scaled)

df["cluster"] = clusters

score = silhouette_score(X_scaled, clusters)
print("Silhouette:", score)
print(df.groupby("cluster").mean(numeric_only=True))
```

---

## 10. Model Serving Skeleton

```python
from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI()
model = joblib.load("classification_model.joblib")

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/predict")
def predict(record: dict):
    row = pd.DataFrame([record])
    prediction = model.predict(row)[0]
    return {"prediction": str(prediction)}
```

Run:

```bash
uvicorn app:app --reload
```

---

## 11. Common Mistake Fixes

Problem:

```text
Model performs great in notebook but bad in production.
```

Likely causes:

- preprocessing not saved
- train/test leakage
- production data has different categories
- target leakage
- data drift

Fix:

- use full pipeline
- save pipeline with `joblib`
- use `OneHotEncoder(handle_unknown="ignore")`
- monitor production data

Problem:

```text
Accuracy is high but model is useless.
```

Likely cause:

- imbalanced classes

Fix:

- use precision, recall, F1, ROC-AUC, PR-AUC
- tune threshold
- use class weights

Problem:

```text
SVM/KNN performs badly.
```

Likely cause:

- features not scaled

Fix:

- use `StandardScaler` in pipeline

---

## 12. Final Study Advice

Best learning sequence:

1. Python basics.
2. pandas and NumPy.
3. data cleaning.
4. train/test split.
5. regression.
6. classification.
7. metrics.
8. pipelines.
9. cross-validation.
10. tuning.
11. ensembles.
12. unsupervised learning.
13. deployment.
14. monitoring.

Build projects while studying. Machine learning becomes clear when you repeatedly move from messy data to a working evaluated model.

