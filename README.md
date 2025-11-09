# SentimentSense
A full-stack AI-powered sentiment analysis web app using Transformers (BERT) for emotion detection in text.

Perfect 👏 Here’s your **final professional `README.md`** for your full-stack AI project — **SentimentSense**.
This version is recruiter-ready and fits both **SDE** and **AI/ML** portfolios.



### 📘 Overview

**SentimentSense** is a **full-stack sentiment analysis application** that classifies user input text into *Positive*, *Negative*, or *Neutral* sentiments.
It integrates a **Flask backend** powered by **Hugging Face Transformers (BERT)** with a **React frontend**, offering real-time predictions through a clean and responsive UI.

---

### 🚀 Features

✅ Real-time sentiment prediction using fine-tuned BERT model
✅ RESTful Flask API for scalable text analysis
✅ Interactive React frontend with modern UI design
✅ Confidence scores and sentiment visualization
✅ Modular full-stack architecture for deployment readiness

---

### 🧩 Tech Stack

**Frontend:** React.js, Axios, Tailwind CSS
**Backend:** Flask (Python), Transformers, Torch
**Model:** `bert-base-uncased` (Hugging Face)
**Other Tools:**

* NLTK for text preprocessing
* REST API integration
* JSON communication between frontend & backend

---

### 🗂️ Project Structure

```
SentimentSense/
│
├── backend/
│   ├── app.py                # Flask API backend
│   ├── model.py              # Model loading and inference
│   ├── requirements.txt      # Python dependencies
│
├── frontend/
│   ├── src/
│   │   ├── App.js            # Main React component
│   │   ├── components/       # UI Components
│   │   └── services/api.js   # Axios API connection
│   ├── public/
│   │   └── index.html
│
├── data/
│   └── sample_inputs.txt
│
└── README.md
```

---

### ⚙️ Installation & Setup

#### 1️⃣ Clone the repository

```bash
git clone https://github.com/Dibyajyoti1511/SentimentSense.git
cd SentimentSense
```

#### 2️⃣ Backend setup

```bash
cd backend
pip install -r requirements.txt
python app.py
```

*(This will start the Flask server at `http://127.0.0.1:5000/`)*

#### 3️⃣ Frontend setup

Open a new terminal:

```bash
cd frontend
npm install
npm start
```

*(Frontend runs at `http://localhost:3000/`)*

---

### 🧠 Model Details

The backend uses **BERT (Bidirectional Encoder Representations from Transformers)** fine-tuned for sentiment classification.
It predicts the sentiment and returns confidence scores in JSON format:

```json
{
  "sentiment": "Positive",
  "confidence": 0.94
}
```

---

### 📊 Example Input/Output

**Input:**

> “The movie was absolutely fantastic and full of emotion!”

**Output:**

> Sentiment: **Positive**
> Confidence: **0.94**

---

### 🌐 Deployment

You can deploy this app using:

* **Frontend:** Netlify / Vercel
* **Backend:** Render / AWS / Flask on EC2

---

### 🏅 Author

👨‍💻 **Dibyajyoti Bhattacharjee**

* 🎓 B.Tech CSE (AI & ML), SRM Institute of Science and Technology
* 📧 Email: [db8364@srmist.edu.in](mailto:db8364@srmist.edu.in)
* 🔗 GitHub: [Dibyajyoti1511](https://github.com/Dibyajyoti1511)

---

### 📜 License

This project is licensed under the **MIT License** – free to use and modify with attribution.


