from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

app = Flask(__name__)

# Small built-in training set for a simple demo model.
TRAIN_TEXTS = [
    "I love this, amazing and wonderful",
    "This is fantastic and excellent",
    "Great product, very happy",
    "I hate this, very bad and awful",
    "Terrible experience, worst ever",
    "This is disappointing and poor",
    "It is okay, nothing special",
    "Average result, not bad not great",
    "This is fine and acceptable",
]

TRAIN_LABELS = [
    "positive",
    "positive",
    "positive",
    "negative",
    "negative",
    "negative",
    "neutral",
    "neutral",
    "neutral",
]

model = Pipeline(
    [
        ("tfidf", TfidfVectorizer()),
        ("clf", MultinomialNB()),
    ]
)
model.fit(TRAIN_TEXTS, TRAIN_LABELS)


@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    confidence = None
    class_scores = []
    error = None
    text = ""

    if request.method == "POST":
        text = request.form.get("text", "").strip()
        if not text:
            error = "Please enter some text."
        else:
            probabilities = model.predict_proba([text])[0]
            labels = model.classes_
            best_idx = int(probabilities.argmax())

            sentiment = labels[best_idx]
            confidence = float(probabilities[best_idx])
            class_scores = [
                {"label": label, "score": float(score)}
                for label, score in zip(labels, probabilities)
            ]

    return render_template(
        "index.html",
        sentiment=sentiment,
        confidence=confidence,
        class_scores=class_scores,
        error=error,
        text=text,
    )


if __name__ == "__main__":
    app.run(debug=True)
