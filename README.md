# 🧠 Sentiment Analysis Web App

A modern web application that analyzes the sentiment of user input text using Natural Language Processing (NLP). This app classifies text as **Positive**, **Negative**, or **Neutral**, and displays confidence scores with a clean and interactive UI.

---

## 🌐 Live Demo

🚀 Try it here:
👉 https://sentiment-analysis-project-seven.vercel.app/

---

## 🚀 Features

* 🔍 Real-time sentiment analysis
* 😊 Emoji-based sentiment output
* 📊 Confidence score with class breakdown
* 🌙 Dark mode toggle
* 🎨 Clean, responsive UI
* ⚡ Fast backend using Flask

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **NLP:** TextBlob
* **Frontend:** HTML, CSS, JavaScript
* **Deployment:** Vercel
* **Version Control:** Git & GitHub

---

## 📸 Preview

Example input:

```
I love it
```

Output:

* Sentiment: **Positive 😊**
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
├── static/ (optional)
├── requirements.txt
├── Procfile
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/sophiavergese-yoi/sentiment-analysis-project.git
cd sentiment-analysis-project
```

### 2. Create virtual environment (optional)

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
python -m textblob.download_corpora
```

---

## ▶️ Run Locally

```
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

1. User enters text
2. Flask backend processes input
3. TextBlob analyzes sentiment polarity
4. Output is classified into:

   * Positive
   * Neutral
   * Negative
5. Results displayed with confidence and emojis

---

## 🌟 Future Improvements

* 🤖 Use advanced models (Hugging Face Transformers)
* 📱 Mobile optimization / PWA
* 🗣️ Voice input support
* 📊 Save and visualize past results
* 🔐 User authentication

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repository and submit a pull request.

---

## 📄 License

This project is open-source under the MIT License.

---

## 👤 Author

GitHub: https://github.com/sophiavergese-yoi

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
