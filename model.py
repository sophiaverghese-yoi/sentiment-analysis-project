import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
data = pd.read_csv("data.csv")

# Separate input and output
X = data["text"]
y = data["label"]

# Convert text into numbers
vectorizer = TfidfVectorizer()
X_vector = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression()
model.fit(X_vector, y)

# Test with a sample
sample = ["I really love this!"]
sample_vector = vectorizer.transform(sample)

prediction = model.predict(sample_vector)

print("Prediction:", prediction[0])
