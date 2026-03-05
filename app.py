import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("fake_news_svm_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Page configuration
st.set_page_config(
    page_title="Fake News Detection System",
    page_icon="📰",
    layout="centered"
)

# Title
st.title("📰 Fake News Detection System")
st.markdown("Detect whether a news article is **Fake** or **Real** using Machine Learning.")

st.divider()

# Text input
news_text = st.text_area(
    "📝 Enter News Article Text:",
    height=200,
    placeholder="Paste the news content here..."
)

# Predict button
if st.button("🔍 Check News"):
    if news_text.strip() == "":
        st.warning("⚠️ Please enter some news text.")
    else:
        # Vectorize input
        transformed_text = vectorizer.transform([news_text])

        # Prediction
        prediction = model.predict(transformed_text)[0]
        print("prediction:",prediction)
        # Output
        if prediction == 1:
            st.success("✅ This news is **REAL**")
            
        else:
            st.error("❌ This news is **FAKE**")
           

st.divider()

# Footer
st.caption("Developed using Python, TF-IDF Vectorization & SVM Model")