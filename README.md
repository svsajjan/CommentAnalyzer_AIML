# 🧠 AIML Comment Analyzer

AIML Comment Analyzer is a Machine Learning–based web application that analyzes user comments and predicts whether the sentiment is **Positive**, **Negative**, or **Neutral**.  
The project uses **Python**, **Natural Language Processing (NLP)**, and **Streamlit** to provide an easy-to-use interface.

---

## 🚀 Features

- ✔️ Sentiment prediction using ML  
- ✔️ User-friendly Streamlit UI  
- ✔️ Real-time text analysis  
- ✔️ Lightweight and fast  
- ✔️ Easy to run locally  

---

## 📁 Project Structure
comment_analyzer/
- app.py # Main Streamlit application
- requirements.txt # Project dependencies
- README.md # Project documentation
- .streamlit/
  - config.toml # Theme settings
 
---

## ⚙️ Installation & Execution Guide

Follow these steps to run the project on your computer.

---

### 🔹 Step 1: Clone the Repository

*(If your repository name changed, replace `MyProject` with your updated name.)*

---

### 🔹 Step 2: Create a Virtual Environment (Recommended)

#### **Windows**
python -m venv venv
venv\Scripts\activate

#### **Mac / Linux**
python3 -m venv venv
source venv/bin/activate

---

### 🔹 Step 3: Install Required Libraries
pip install -r requirements.txt

---

### 🔹 Step 4: Run the Application

streamlit run app.py


After running the command, your browser will open automatically at:http://localhost:8501


---

## 🧪 How the Model Works

1. User enters a comment  
2. The text is cleaned using NLP preprocessing  
3. A Machine Learning model predicts the comment sentiment  
4. Output is displayed with color-coded labels  
5. User receives instant feedback  

---

## 📦 Requirements

All required libraries are already listed in **requirements.txt**, such as:
streamlit
pandas
numpy
scikit-learn
regex


---

## 🌱 Future Enhancements

- Add a larger sentiment dataset  
- Improve accuracy with deep learning models  
- Add emoji support in sentiment analysis  
- Deploy the system online using Streamlit Cloud  

---

## 🤝 How to Contribute

You can contribute to this project by:

1. **Forking** the repository  
2. Creating a **new branch**  
3. Making your changes  
4. Submitting a **Pull Request**  

---

## 📜 License

This project is free to use for learning and development purposes.

---

## ⭐ Thank You!

If you like this project, consider giving the repository a **⭐ star** on GitHub.
### New Feature: Emoji Sentiment Support (Coming Soon)
### 😀 Emoji Sentiment Support Coming Soon!
Our model will soon detect the sentiment of emojis like 😊😢😠










