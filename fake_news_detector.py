import pickle

# Load trained model
with open("fake_news_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load vectorizer
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

def predict_news(text):

    text_vector = vectorizer.transform([text])

    prediction = model.predict(text_vector)[0]

    if prediction == 1:
        return "REAL"
    else:
        return "FAKE"
