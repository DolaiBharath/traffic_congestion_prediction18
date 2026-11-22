# 🚦 Traffic Congestion Prediction Dashboard

An interactive, machine-learning-based web application that predicts traffic congestion and provides traffic-related insights through a user-friendly Streamlit dashboard.

The project combines machine learning, data visualization, live GPS location detection, and TomTom Traffic API integration to help users understand traffic conditions and explore congestion patterns.

---

## 📌 Project Overview

Traffic congestion is a major problem in urban areas. It leads to longer travel times, fuel consumption, and delays.

This project aims to analyze traffic-related data and predict congestion levels using machine learning models. It also provides an interactive dashboard where users can explore data, view model performance, and check traffic conditions based on their current GPS location or a searched location.

## 🎯 Objectives

- Predict traffic congestion using machine learning techniques.
- Analyze traffic patterns using historical traffic data.
- Compare machine learning model performance.
- Display traffic insights through interactive visualizations.
- Detect the user's current location using GPS.
- Search for locations and view their traffic conditions.
- Integrate real-time traffic information using the TomTom API.

## ✨ Key Features

### 1. Home Dashboard
- Project overview and introduction.
- Summary of traffic prediction features.
- Easy navigation between application modules.

### 2. Traffic Congestion Prediction
- Predict traffic conditions using trained machine learning models.
- Accept relevant input features.
- Display prediction results through the dashboard.

### 3. Data Explorer
- Explore the traffic dataset.
- View data summaries and traffic patterns.
- Analyze data using interactive charts.

### 4. Model Performance
- Evaluate and compare machine learning models.
- Display model performance metrics.
- Visualize model comparison results.

### 5. Traffic Insights
- Understand traffic trends and patterns.
- Explore important observations from the dataset.
- View graphical representations of traffic information.

### 6. Live GPS Traffic
- Detect the user's current location through browser geolocation.
- Retrieve the selected location's traffic information.
- Display current speed and free-flow speed.
- Show estimated traffic congestion conditions.

### 7. Location-Based Traffic Search
- Search for a location by name.
- Select a location directly on an interactive map.
- Retrieve traffic information for the selected coordinates.
- Display current speed, free-flow speed, and congestion classification.

## 🤖 Machine Learning Approach

The project uses five machine learning models to analyze traffic-related data and generate congestion predictions.

The trained models are used to learn patterns from the dataset and predict traffic conditions based on input features.

**Purpose of machine learning:**
- Learn traffic patterns from historical data.
- Identify relationships between traffic features.
- Predict traffic conditions.
- Compare model performance.

*Note: Add the exact names of your five models and their verified accuracy values here so viewers can understand the model comparison.*

## 🗺️ Live Traffic API Integration

This project integrates the **TomTom API** for location search and live traffic information.

| API / Technology | Purpose |
|---|---|
| TomTom Places Search API | Search for locations |
| TomTom Traffic API | Retrieve traffic flow information |
| Browser Geolocation | Detect current user location |
| Folium | Display interactive maps |
| Streamlit-Folium | Integrate maps into Streamlit |

**Important:** Machine learning predictions and TomTom live traffic information are separate features. TomTom provides traffic flow data, while the trained ML models provide predictions based on the project's dataset and input features.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning |
| Streamlit | Web application development |
| Plotly | Interactive data visualization |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Folium | Interactive maps |
| Streamlit-Folium | Map integration |
| Requests | API communication |
| TomTom API | Location search and traffic information |
| Joblib | Saving and loading trained models |
| Git & GitHub | Version control and project hosting |

## 📂 Project Structure

```text
traffic-congestion-prediction/
│
├── app.py
├── gps_traffic.py
├── location_traffic.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── .streamlit/
│   └── secrets.toml
│
├── dataset/
│   └── traffic_dataset.csv
│
├── models/
│   └── trained model files
│
└── other project files
```

*The dataset and model folder names above are examples. Adjust this structure to match the actual files in your repository.*

## ⚙️ Installation and Setup

Follow these steps to run the project on your local computer.

### Step 1: Clone the Repository

```bash
git clone https://github.com/DolaiBharath/traffic_congestion_prediction18.git
```

### Step 2: Open the Project Folder

```bash
cd traffic_congestion_prediction18
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate the environment again.

### Step 5: Install Required Libraries

```bash
python -m pip install -r requirements.txt
```

### Step 6: Configure the TomTom API Key

Create a file named `secrets.toml` inside the `.streamlit` folder.

Folder location:

```text
.streamlit/secrets.toml
```

Add your own TomTom API key:

```toml
TOMTOM_API_KEY = "YOUR_TOMTOM_API_KEY"
```

Replace the placeholder with your own API key.

**Security:** Never upload your actual API key to GitHub. Keep `.streamlit/secrets.toml` in `.gitignore`.

### Step 7: Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

Local URL:

```text
http://localhost:8501
```

## 🔑 API Configuration

To use the live location search and traffic features:

1. Create an account on the TomTom Developer Portal.
2. Generate an API key.
3. Enable the required Places Search and Traffic API products for your key.
4. Configure the key in `.streamlit/secrets.toml`.
5. Restart the Streamlit application.

TomTom API access and usage are subject to the provider's account limits and terms.

## ☁️ Deployment

This application can be deployed using Streamlit Community Cloud.

### Deployment Steps

1. Push the project to a GitHub repository.
2. Visit https://share.streamlit.io/
3. Sign in using your GitHub account.
4. Select the project repository.
5. Choose `app.py` as the main application file.
6. Open the application settings and configure the required secrets.
7. Add your TomTom API key in the deployment secrets using TOML format:

```toml
TOMTOM_API_KEY = "YOUR_TOMTOM_API_KEY"
```

8. Deploy the application.

**Note:** Ensure that your dataset, trained model files, and other required project files are included in GitHub. Do not upload private API keys or secret configuration files.

## 📊 Expected Application Workflow

```text
        User
         |
         v
   Streamlit Dashboard
         |
         v
   Select a Feature
         |
    +----+-------------------+
    |                        |
    v                        v
ML Predictions          Live Traffic
    |                        |
    v                        v
Trained ML Models       GPS / Location Search
    |                        |
    v                        v
Prediction Results      TomTom Traffic API
    |                        |
    +-----------+------------+
                |
                v
        Dashboard Results
```

## 🔒 Security

- API keys are stored using Streamlit secrets.
- Secret configuration files should not be committed to GitHub.
- The `.gitignore` file excludes sensitive files and unnecessary development files.
- Never publish private credentials in source code, screenshots, or documentation.

## 🚀 Future Enhancements

- Improve traffic prediction using additional traffic datasets.
- Add more geographical coverage.
- Improve location detection accuracy.
- Enhance interactive traffic visualization.
- Integrate additional traffic-related features.
- Improve model performance through further experimentation.

## 👨‍💻 Author

**Bharath Dolai**

GitHub: https://github.com/DolaiBharath
# Deployed link :https://trafficcongestionprediction18git-g6sjr4kx8zukkflkmecfij.streamlit.app/

## 📄 License

This project is developed for educational and academic purposes.

A suitable open-source license can be added to the repository if you decide to distribute the project under specific reuse terms.

---

⭐ If you find this project useful, feel free to explore the repository and learn more about machine learning-based traffic congestion prediction.
