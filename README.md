# 🧠 Sentiment Analysis Web App

A simple and interactive web application that analyzes the sentiment of user input text using Natural Language Processing (NLP). Built with Python and Flask, this app classifies text as **Positive**, **Negative**, or **Neutral** and provides a confidence score.

---

## 🚀 Features

* 🔍 Analyze sentiment of any text input
* 😊 Emoji-based sentiment display
* 📊 Confidence score with breakdown (Positive, Neutral, Negative)
* 🌙 Dark mode toggle
* ⚡ Fast and lightweight Flask backend
* 🎨 Clean and responsive UI

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **NLP Library:** TextBlob
* **Frontend:** HTML, CSS, JavaScript
* **Version Control:** Git & GitHub

---

## 📸 Preview

> Example input:
> `I love it`

**Output:**

* Sentiment: Positive 😊
* Confidence: ~36%
* Breakdown:

  * Positive: 36.9%
  * Neutral: 35.9%
  * Negative: 27.2%

---

## 📂 Project Structure

```
sentiment-analysis-app/
│
├── app.py
├── templates/
│   └── index.html
├── static/ (optional for CSS/JS)
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/sentiment-analysis-app.git
cd sentiment-analysis-app
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
```

### 3. Install dependencies

```bash
pip install flask textblob
python -m textblob.download_corpora
```

---

## ▶️ Run the App

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

1. User enters text in the input box
2. Flask backend receives the input
3. TextBlob processes sentiment polarity
4. Sentiment is classified into:

   * Positive
   * Negative
   * Neutral
5. Results are displayed with confidence scores and emojis

---

## 🌟 Future Improvements

* 🔥 Use advanced models (Hugging Face Transformers)
* 📱 Convert to mobile-friendly PWA
* 🗣️ Add voice input
* 📊 Store and visualize past results
* 🌐 Deploy online (Render / Vercel)

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a pull request.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👤 Author

Your Name
GitHub: https://github.com/your-username

---

## ⭐ Show your support

If you like this project, give it a ⭐ on GitHub!
