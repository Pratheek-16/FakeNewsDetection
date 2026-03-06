# 📰 Fake News Detection using Machine Learning

## 📌 Project Description
This project detects whether a news article is Fake or Real using a Machine Learning model. The system uses Natural Language Processing (NLP) techniques to analyze the textual content of news articles and classify them.

The model is trained using a dataset of real and fake news articles and uses TF-IDF vectorization and a Support Vector Machine (SVM) classifier for prediction.

## 🎯 Project Objective
The objective of this project is to build a system that can automatically detect fake news and help reduce the spread of misinformation on the internet.

## 🛠 Technologies Used
- Python
- Machine Learning
- Natural Language Processing (NLP)
- Scikit-learn
- Pandas
- NumPy
- Pickle

## 📂 Project Structure

FakeNewsDetection

│
├── app.py                     # Main application file
├── fake_news_svm_model.pkl    # Trained SVM machine learning model
├── tfidf_vectorizer.pkl       # TF-IDF vectorizer used for text processing
├── requirements.txt           # Required Python libraries
└── README.md                  # Project documentation


## ⚙️ How the System Works

1. The user inputs a news article or text.
2. The text is preprocessed and converted into numerical features using TF-IDF Vectorization.
3. The trained SVM model analyzes the features.
4. The model predicts whether the news is Fake or Real.

## 🚀 How to Run the Project

1. Clone the repository

git clone https://github.com/Pratheek-16/FakeNewsDetection.git

2. Navigate to the project folder

cd FakeNewsDetection

3. Install the required libraries

pip install -r requirements.txt

4. Run the application

python app.py

## 📊 Features
- Detects fake news using machine learning
- Uses TF-IDF for text feature extraction
- Uses Support Vector Machine (SVM) for classification
- Simple and efficient model for text analysis

## 🔮 Future Improvements
- Improve model accuracy using deep learning models
- Build a web interface for user interaction
- Deploy the project as a web application

## 👨‍💻 Author
Sree Pratheek
