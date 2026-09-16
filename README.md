# IBM-SpaceX-Applied-Data-Science-Capstone
SpaceX project

## 📌 Project Overview

This project is my final capstone project for the **IBM Data Science Professional Certificate**.

The project focuses on analyzing **SpaceX Falcon 9 launch data** and predicting whether the Falcon 9 first-stage booster will successfully land.

The analysis follows an end-to-end data science workflow:

**Data Collection → Data Wrangling → Exploratory Data Analysis → Visualization → Interactive Analytics → Machine Learning → Business Insights**

The goal is to understand the factors that influence Falcon 9 first-stage landing success and build machine learning models capable of predicting landing outcomes.

---

## 🎯 Business Problem

SpaceX significantly reduces launch costs by reusing the first stage of its Falcon 9 rockets.

For a competing aerospace company, understanding the probability of a successful first-stage landing can help with:

* Launch cost estimation
* Mission planning
* Competitive analysis
* Risk assessment
* Bid preparation

Therefore, this project investigates:

> **Can we predict whether the Falcon 9 first stage will successfully land based on historical launch information?**

---

## 🔍 Project Objectives

The main objectives of this project are:

1. Collect SpaceX launch data using APIs.
2. Collect additional launch information through web scraping.
3. Clean and transform the collected data.
4. Perform exploratory data analysis using Python and SQL.
5. Visualize launch and landing patterns.
6. Analyze launch locations using Folium.
7. Build an interactive dashboard using Plotly Dash.
8. Build classification machine learning models.
9. Compare model performance.
10. Identify important factors affecting landing success.
11. Present the findings using a final presentation.

---

# 🧰 Technologies Used

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn
* Plotly

### Database / SQL

* SQLite
* SQL

### Machine Learning

* Scikit-learn
* Logistic Regression
* Support Vector Machine
* Decision Tree
* K-Nearest Neighbors
* GridSearchCV

### Data Collection

* SpaceX REST API
* Requests
* BeautifulSoup
* Web Scraping

### Interactive Visualization

* Folium
* Plotly Dash

### Development Tools

* Jupyter Notebook
* JupyterLab
* VS Code
* Git
* GitHub

---

# 📂 Project Structure

```text
IBM-SpaceX-Applied-Data-Science-Capstone/
│
├── README.md
│
├── data/
│   ├── spacex_launch_data.csv
│   ├── spacex_launch_data_cleaned.csv
│   └── spacex_launch_dash.csv
│
├── notebooks/
│   ├── 01_data_collection_api.ipynb
│   ├── 02_web_scraping.ipynb
│   ├── 03_data_wrangling.ipynb
│   ├── 04_eda_sql.ipynb
│   ├── 05_eda_visualization.ipynb
│   ├── 06_folium_interactive_map.ipynb
│   └── 07_machine_learning_prediction.ipynb
│
├── dashboard/
│   ├── spacex_dash_app.py
│   └── requirements.txt
│
├── presentation/
│   ├── SpaceX_Capstone_Presentation.pptx
│   └── SpaceX_Capstone_Presentation.pdf
│
├── images/
│   ├── launch_sites.png
│   ├── landing_success.png
│   ├── payload_mass.png
│   ├── folium_map.png
│   ├── dashboard.png
│   ├── confusion_matrix.png
│   └── model_comparison.png
│
├── requirements.txt
│
└── LICENSE
```

---

# 📊 Project Workflow

## 1. Data Collection

SpaceX launch data was collected using the SpaceX REST API.

Additional historical launch information was obtained through web scraping.

Tools used:

* Requests
* SpaceX API
* BeautifulSoup
* Pandas

---

## 2. Data Wrangling

The collected datasets were cleaned and transformed.

The process included:

* Handling missing values
* Converting data types
* Extracting relevant variables
* Combining datasets
* Creating the landing outcome variable
* Encoding categorical variables
* Preparing the dataset for machine learning

---

## 3. Exploratory Data Analysis

Exploratory analysis was performed to understand relationships between:

* Launch site
* Payload mass
* Orbit
* Booster version
* Number of flights
* Landing outcome
* Reused boosters

Python visualization libraries were used to identify patterns and trends.

---

## 4. Exploratory Data Analysis Using SQL

SQL queries were used to investigate the SpaceX dataset.

Examples include:

* Finding unique launch sites
* Counting launch records
* Calculating average payload mass
* Filtering launch records
* Analyzing booster versions
* Grouping launch outcomes

SQLite was used for SQL analysis.

---

# 🗺️ 5. Interactive Map Using Folium

Folium was used to create an interactive map of SpaceX launch sites.

The map was used to analyze:

* Launch site locations
* Distance from the coastline
* Nearby infrastructure
* Launch outcomes
* Geographic relationships

The interactive map provides a geographic perspective of the launch data.

---

# 📈 6. Interactive Dashboard

A Plotly Dash dashboard was created to allow users to interactively explore SpaceX launch data.

The dashboard includes analysis of:

* Launch site
* Payload mass
* Booster landing success
* Launch records
* Landing outcomes

Users can select different launch sites and payload ranges to explore the data.

---

# 🤖 7. Machine Learning

The project uses supervised machine learning to predict first-stage landing success.

The target variable is:

```text
Landing Success

0 → Unsuccessful landing
1 → Successful landing
```

The dataset was divided into training and testing datasets.

Several classification algorithms were evaluated.

### Models

* Logistic Regression
* Support Vector Machine
* Decision Tree
* K-Nearest Neighbors

Hyperparameter tuning was performed using:

```python
GridSearchCV
```

---

# 📏 Model Evaluation

The models were evaluated using:

Accuracy

Precision

Recall

F1 Score

Confusion Matrix

Model Performance

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---|---|---|---|
| Logistic Regression | 83.33% | 80.00% | 100.00% | 88.89% |
| KNN | 77.78% | 75.00% | 100.00% | 85.71% |
| SVM | 77.78% | 78.57% | 91.67% | 84.62% |
| **Decision Tree** | **94.44%** | **92.31%** | **100.00%** | **96.00%** |


The confusion matrix provides the following information:

| Model | TN | FP | FN | TP |
|---|---|---|---|---|
| Logistic Regression | 3 | 3 | 0 | 12 |
| KNN | 2 | 4 | 0 | 12 |
| SVM | 3 | 3 | 1 | 11 |
| Decision Tree | 5 | 1 | 0 | 12 |

TN: True Negative

FP: False Positive

FN: False Negative

TP: True Positive


Model Selection


Based on the test-set results, the Decision Tree achieved:

Accuracy: 94.44%

Precision: 92.31%

Recall: 100.00%

F1 Score: 96.00%


The confusion matrix contained:

True Negatives: 5

False Positives: 1

False Negatives: 0

True Positives: 12

These results were obtained from the test dataset used in this project.

---

# 📊 Key Findings

The final findings are based on the exploratory analysis and machine learning results obtained from the project dataset.

Important areas investigated include:

* Launch site performance
* Payload characteristics
* Booster reuse
* Orbit type
* Historical landing trends
* Machine learning model performance

The final model comparison and numerical results are included in the machine learning notebook and presentation.

---

# 📁 Notebooks

| Notebook                               | Description                                |
| -------------------------------------- | ------------------------------------------ |
| `01_data_collection_api.ipynb`         | Collect SpaceX data using API              |
| `02_web_scraping.ipynb`                | Collect additional data using web scraping |
| `03_data_wrangling.ipynb`              | Clean and transform the data               |
| `04_eda_sql.ipynb`                     | Perform exploratory analysis using SQL     |
| `05_eda_visualization.ipynb`           | Analyze data using Python visualizations   |
| `06_folium_interactive_map.ipynb`      | Create interactive launch-site map         |
| `07_machine_learning_prediction.ipynb` | Build and evaluate classification models   |

---

# 📊 Dashboard

The interactive dashboard is available in:

```text
dashboard/spacex_dash_app.py
```

To run the dashboard:

```bash
cd dashboard
pip install -r requirements.txt
python spacex_dash_app.py
```

The dashboard will normally be available at:

```text
http://127.0.0.1:8050/
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/nivetha-engineer/IBM-SpaceX-Applied-Data-Science-Capstone.git
```

Move into the project directory:

```bash
cd IBM-SpaceX-Applied-Data-Science-Capstone
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

---

# 📦 Requirements

The main Python libraries used in this project include:

```text
pandas
numpy
matplotlib
seaborn
scikit-learn
requests
beautifulsoup4
folium
plotly
dash
```

---

# 📚 Data Sources

The project uses publicly available SpaceX launch information and datasets provided as part of the IBM Applied Data Science Capstone learning environment.

Data collection techniques include:

* SpaceX REST API
* Web scraping
* IBM-provided datasets

---

# 🎓 IBM Certification

This project was completed as part of the:

**IBM Data Science Professional Certificate**

Capstone:

**Applied Data Science Capstone**

The capstone integrates data collection, data wrangling, exploratory data analysis, visualization, interactive analytics, and machine learning into an end-to-end data science project.

---

# 💡 Skills Demonstrated

This project demonstrates practical experience with:

* Python
* Pandas
* NumPy
* Data Cleaning
* Exploratory Data Analysis
* SQL
* Data Visualization
* Web Scraping
* REST APIs
* Geospatial Analysis
* Folium
* Plotly Dash
* Machine Learning
* Classification
* Hyperparameter Tuning
* Model Evaluation
* Git
* GitHub
* Data Storytelling

---

# 👩‍💻 Author

**Nivetha**

Aspiring Data Analyst / Data Scientist

GitHub:

`https://github.com/nivetha-engineer`

---

# 📌 Disclaimer

This project was created for educational and portfolio purposes as part of the IBM Data Science Professional Certificate Capstone.

The analysis and machine learning results are based on the dataset used in this project.

---

