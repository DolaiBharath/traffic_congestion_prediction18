# Traffic Congestion Prediction Using ML

An end-to-end machine learning project that forecasts traffic volume and classifies urban road congestion levels using historical traffic, weather, and event data. The project features a modular Python pipeline built with **scikit-learn** and an interactive web dashboard powered by **Streamlit**.
# 🚦 Traffic Congestion Prediction

## 📌 Project Overview

Traffic Congestion Prediction is a machine learning-based web application designed to predict traffic conditions using historical traffic data and machine learning algorithms.

The application helps users understand traffic patterns and estimate congestion levels. It provides an interactive interface built with Python and Streamlit.

## 🎯 Project Objectives

- Predict traffic congestion using machine learning.
- Analyze historical traffic data.
- Compare different machine learning models.
- Provide an easy-to-use web interface.
- Display prediction results and model performance.

## ✨ Features

- Interactive Streamlit dashboard.
- Traffic congestion prediction.
- Machine learning model integration.
- Regression and classification models.
- Data visualization and analysis.
- Model performance comparison.
- CSV-based results and reports.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Web application interface |
| NumPy | Numerical operations |
| Pandas | Data processing |
| Scikit-learn | Machine learning |
| Joblib | Model serialization |
| TensorFlow | Deep learning |
| Keras | Neural network development |
| Matplotlib | Data visualization |

## 📂 Project Structure

```text
traffic-congestion-prediction/
│
├── app.py
├── dashboard_utils.py
├── requirements.txt
├── README.md
│
├── models/
│   ├── gb_regression.pkl
│   ├── gradient_boosting_reg.pkl
│   ├── lasso_regression_reg.pkl
│   ├── linear_regression_reg.pkl
│   ├── ridge_regression_reg.pkl
│   ├── random_forest_reg.pkl
│   ├── random_forest_clf.pkl
│   ├── logistic_regression_clf.pkl
│   ├── lr_classification.pkl
│   └── svm_clf.pkl
│
├── data/
│
├── uploads/
│
└── .gitignore
```

*Note: The folder structure above is illustrative. Adjust it to match your actual project files.*

## 💻 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-GITHUB-USERNAME/traffic-congestion-prediction.git
```

### 2. Open the Project Folder

```bash
cd traffic-congestion-prediction
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
.venv\Scripts\activate
```

### 5. Install Required Libraries

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

## 🤖 Machine Learning Models

The project includes regression and classification models.

### Regression Models

- Linear Regression
- Ridge Regression
- Lasso Regression
- Random Forest Regressor
- Gradient Boosting Regressor

### Classification Models

- Logistic Regression
- Random Forest Classifier
- Support Vector Machine (SVM)

*Actual model availability depends on the trained model files included in the repository.*

## 📊 Model Evaluation

The project includes result files for evaluating model performance.

Examples:

- Regression performance results.
- Classification performance results.
- Test dataset evaluation.

## 📁 Dataset

The application uses traffic-related datasets for data processing, analysis, and prediction.

Place the required dataset files in the appropriate project directory before running the application.

## 🚀 Future Enhancements

- Real-time traffic data integration.
- Interactive traffic visualization.
- Live traffic congestion monitoring.
- Improved prediction accuracy.
- Map-based traffic visualization.
- Cloud deployment.

## 🔐 Important Notes

- Do not upload virtual environments such as `.venv/`.
- Do not upload passwords, API keys, or secret credentials.
- Use Git LFS for large machine learning model files when required.
- Ensure actual model files are available before running predictions.
- Use compatible Python and scikit-learn versions for saved models.

## 👨‍💻 Author

**Dolai Bharath**

GitHub: https://github.com/YOUR-GITHUB-USERNAME

## 📜 License

This project is developed for educational and learning purposes.

You may add an open-source license if you intend to distribute the project under specific terms.

---

⭐ If you find this project useful, consider giving the repository a star on GitHub!
---

## Key Features

* **Dual Machine Learning Models:**
  * **Regression:** Predicts continuous numeric traffic volume (`R² ≈ 0.75`).
  * **Classification:** Categorizes road conditions into congestion severity levels (`~82% accuracy`).
* **End-to-End Modular Pipeline:** Clean separation of data collection, preprocessing, exploratory data analysis (EDA), model training, and evaluation inside `src/`.
* **Interactive Streamlit Dashboard:** Real-time congestion predictions, interactive controls, and visual analytics served via `app.py`.
* **Pre-Trained Models Included:** Ready-to-run `.pkl` model files stored in `models/` for instant inference without retraining.

---

## Project Structure

```text
traffic-congestion-prediction/
├── app.py                  # Interactive Streamlit web dashboard
├── dashboard_utils.py      # Model loading, feature engineering, and UI helpers
├── requirements.txt        # Python package dependencies
├── .streamlit/
│   └── config.toml         # Custom Streamlit theme and server configuration
├── src/                    # Modular ML pipeline scripts
│   ├── data_collection.py
│   ├── data_preprocessing.py
│   ├── exploratory_analysis.py
│   ├── model_training.py
│   ├── model_evaluation.py
│   └── utils.py
├── Datasets/               # Raw data, train/val/test splits, and dataset notes
├── data/processed/         # Cleaned and feature-engineered intermediate data
├── models/                 # Saved .pkl models and evaluation metrics CSVs
├── visualizations/         # Generated EDA and model performance charts (PNG)
├── REPORT_EXECUTIVE.md     # Executive summary of findings
├── REPORT.md               # Detailed technical documentation
└── README.md               # Project overview and setup guide
```

---

## Prerequisites

Ensure you have the following installed on your machine:
* **Python 3.9+**
* **Git**

---

## Installation & Quick Start

1. **Clone the Repository**
   ```bash
   git clone https://github.com
   cd traffic-congestion-prediction
   ```

2. **Create and Activate a Virtual Environment**
   * **Windows (PowerShell):**
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   * **macOS / Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies**
   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Launch the Streamlit Dashboard**
   ```bash
   streamlit run app.py
   ```
   Open your browser to `http://localhost:8501` to interact with the application.

---

## Re-Running the ML Pipeline (Optional)

If you update the raw datasets or modify feature engineering, run the pipeline scripts sequentially to regenerate processed files, charts, and trained models:

```bash
python src/data_collection.py
python src/data_preprocessing.py
python src/exploratory_analysis.py
python src/model_training.py
python src/model_evaluation.py
```

---

## Tech Stack

* **Language:** Python
* **Machine Learning:** scikit-learn, NumPy, pandas
* **Visualization:** Matplotlib, Seaborn, Plotly
* **Web Interface:** Streamlit
#� �t�r�a�f�f�i�c�-�c�o�n�g�e�s�t�i�o�n�-�p�r�e�d�i�c�t�i�o�n�
�
�
#   t r a f f i c _ c o n g e s t i o n _ p r e d i c t i o n 1 8  
 