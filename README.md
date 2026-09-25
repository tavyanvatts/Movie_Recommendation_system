# 🎬 Movie Recommendation System

A content-based movie recommendation web application built with Python, Pandas, and Streamlit. This app suggests similar movies based on your selection using similarity metrics computed from movie metadata.

![App Screenshot](images/Screenshot%202026-09-24%20222842.png)

## ✨ Features
* **Interactive UI:** Clean, responsive user interface built using Streamlit.
* **Lightweight Repository:** Large model and dictionary pickle files are hosted externally and fetched automatically via Google Drive (`gdown`) on startup.
* **Data Science Pipeline:** Includes the Jupyter Notebook detailing data preprocessing, feature engineering, and model training.

## 🛠️ Tech Stack
* **Framework:** Streamlit
* **Data Handling:** Pandas, Pickle
* **Cloud Storage & Fetching:** Google Drive & `gdown`
* **Development Environment:** Python, Jupyter Notebook

## 📁 Project Structure
```text
Movie_recommender/
│
├── .gitignore                                  # Excludes virtual environments and local caches
├── app.py                                      # Main Streamlit application
├── Content_Based_Recommendation_System.ipynb   # Jupyter Notebook for model training
├── requirements.txt                            # Python dependencies
├── README.md                                   # Project documentation
└── images/
    └── Screenshot 2026-09-24 222842.png        # UI preview screenshot
```

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Movie_recommender.git
   cd Movie_recommender
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```
   *(Note: On first launch, the app will automatically download the necessary recommendation models from cloud storage).*

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check issues page or submit a pull request.
