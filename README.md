# **📰 Fake News Detection Web App**
    This is a simple Fake News Detection Web Application built with Flask and Machine Learning (Naive Bayes).

    It allows users to enter a news article, and the app predicts whether it is Fake or Real.

# **🚀 Features**
       ✅ Web interface using Flask

       ✅ Pre-trained Naive Bayes model
       
       ✅ Uses TF-IDF for text vectorization
       
       ✅ Lightweight and easy to deploy

# **📂 Project Structure**

    ├── app.py             # Flask web app
    
    ├── model.py           # Machine learning model
    
    ├── requirements.txt   # Dependencies
    
    ├── data/              # Contains Fake.csv & True.csv
    
    ├── templates/         # HTML templates (index.html, result.html)
    
    ├── static/            # (Optional) CSS/JS files
    
⚙️ Installation
1️⃣ Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/fake-news-detector.git
cd fake-news-detector
2️⃣ Create & activate virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3️⃣ Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Ensure you have the dataset
Place Fake.csv and True.csv inside the data/ folder.

▶️ Usage
Run the Flask app:

bash
Copy
Edit
python app.py
Then open your browser and go to http://127.0.0.1:5000/

🧠 Model Details
Uses Multinomial Naive Bayes

Text preprocessing: lowercasing, removing punctuation

Feature extraction: CountVectorizer + TF-IDF Transformer

Dataset: Combination of Fake.csv & True.csv

