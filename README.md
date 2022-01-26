# Data Analysis Task
Data analysis task with fully data science lifecyle

Author: Davain Edwards

<img width="450" alt="data_science_cycle" src="https://user-images.githubusercontent.com/2211088/117272062-173c0b00-ae5b-11eb-947e-6e8c41855ce8.png">

Please do all the notebooks in order. The only exception is notebook 2, which can be skipped.

Using datasets known.csv and unknown.csv, [notebooks](
 
    1_business_understanding.ipynb,
    2_data_mining.ipynb, <-- Can be skipped!
    3_data_cleaning.ipynb,
    4_data_exploration.ipynb,
    5_feature_engineering.ipynb,
    6_predictive_modelling_with_pycaret.ipynb, <-- Final model training, test evaluation and model saving!
    6_predictive_modelling_with_sklearn.ipynb, <!-- Testing and error analysis
    7_data_visualization.ipynb) 

Shows a walk through all the steps of the Data Science Life Cycle. 
It thus contains:
- 1. Business Understanding
- 2. Data Mining
- 3. Data Cleaning
- 4. Exploratory Data Analysis
- 5. Feature Engineering
- 6. Predictive Modeling with Hyperparameter Tuning (Small Error Analysis)
- 7. Data Visualization

## Requirements

* pyenv
* python==3.8.5

## Setup

For this purpose you use following commands:

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
## Clean Notebooks

```bash
jupyter nbconvert --clear-output --inplace [NOTEBOOK.ipynb]
```



