from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Dummy training data
sample_texts = [
    "HDL: 60, LDL: 100",
    "Take 1 tablet daily after meal",
    "Patient was discharged with instructions",
    "MRI shows lesion in brain"
]
labels = ["Lab Report", "Prescription", "Discharge Summary", "Scan Report"]

# Train model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(sample_texts)
model = MultinomialNB().fit(X, labels)

def classify_text(text):
    return model.predict(vectorizer.transform([text]))[0]
