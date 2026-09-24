# 🎬 Netflix Content-Based Movie Recommender System

A complete end-to-end machine learning project featuring a data training pipeline in Google Colab and an interactive web interface built with **Streamlit** and **PyCharm**.

---

## 📌 Project Overview
This system recommends 5 similar movies based on a user's selection. It utilizes **Content-Based Filtering** by analyzing movie metadata tags (such as directors, cast, country, and ratings) and computing structural similarities.

<p align="center">
  <img src="images/Screenshot 2026-09-24 222842.png" alt="Streamlit App Screenshot" width="750">
</p>


### 🧠 How It Works:
1. **Data Engineering:** Text features from the Netflix dataset are preprocessed, cleaned, and combined into comprehensive text tags.
2. **Vectorization:** Tags are converted into mathematical vectors using text vectorization techniques.
3. **Similarity Engine:** Calculates the **Cosine Similarity** between movie vectors to find the closest matches.
4. **Serialization:** The computed similarity matrix and datasets are exported via `pickle` to power the web app.

---

## 🛠️ Tech Stack & Architecture

| Component | Technologies Used |
| :--- | :--- |
| **Language** | Python 3.x |
| **Model Training** | Google Colab, Pandas, NumPy, Scikit-learn, Pickle |
| **Web Interface** | Streamlit |
| **IDE / Version Control** | PyCharm, Git & GitHub |

---

## 📁 Repository Structure
```text
├── .venv/                         # Virtual environment (ignored by git)
├── Content-Based_Recommendation_System.ipynb  # Data training & processing notebook
├── app.py                         # Streamlit application UI and logic
├── requirements.txt               # Project dependencies
├── .gitignore                     # Git exclusion rules (safeguards large .pkl files)
└── README.md                      # Project documentation
```

---

## 🚀 Getting Started Locally

### 1. Clone the Repository
```bash
git clone https://github.com
cd Movie-Recommender-System
```

### 2. Set Up a Virtual Environment & Install Dependencies
```bash
# Create environment
python -m venv .venv

# Activate environment (Windows)
.venv\Scripts\activate

# Activate environment (Mac/Linux)
source .venv/bin/activate

# Install required packages
pip install streamlit pandas scikit-learn
```

### 3. Generate the Model Files
Ensure your dataset (`netflix_titles.csv.zip`) is present, then run the blocks in `Content-Based_Recommendation_System.ipynb` to generate:
* `movies.pkl`
* `movies_dict.pkl`
* `similarity.pkl`

*Place these generated files into the root folder of the project.*

### 4. Run the Streamlit Application
```bash
streamlit run app.py
```

---

## 🔮 Future Enhancements
* 🌐 **Cloud Deployment:** Deploy the Streamlit interface live using Streamlit Community Cloud or Render.
* 🖼️ **TMDB API Integration:** Fetch and display live movie posters dynamically inside the UI instead of text listings.
* 📊 **Hybrid Logic:** Incorporate collaborative filtering using user-rating interactions.
