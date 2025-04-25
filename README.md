# 🩺 Visual Symptom Checker

A multimodal AI-powered health assistant that helps users analyze visible symptoms (e.g., rashes, swelling, redness) using both uploaded images and self-reported symptoms. Built with **Chainlit** for the frontend and **MongoDB** for persistent case tracking.

---

## 🚀 Features

- 🖼 Upload images of visible symptoms (e.g., skin rash)
- 📝 Describe additional symptoms (e.g., itching, pain)
- 🧠 Uses GPT-4 Vision (or LLaVA) to analyze both
- 🩹 Suggests likely conditions, severity, and treatment advice
- 🗃 Saves all cases to MongoDB for traceability

---

## 🧱 Tech Stack

- **Frontend**: [Chainlit](https://docs.chainlit.io) (LLM-native UI)
- **LLM Backend**: [OpenAI GPT-4V](https://openai.com/) or [LLaVA](https://llava-vl.github.io/)
- **Database**: [MongoDB](https://www.mongodb.com/) (for storing records)
- **Image Handling**: Pillow + Base64 encoding

---

## 🖼 Sample Use Case

Upload a photo of a rash and type:

> "It’s been itchy and red for 3 days with some swelling."

The assistant replies with:
- 🦠 Possible diagnosis: Contact dermatitis, Eczema...
- 🚨 Severity: Moderate
- 💊 Recommendations: Apply hydrocortisone, avoid irritants...

---

## 🎨 Diagram

![Diagram](https://github.com/patla001/multimodal-rag-chatbot/blob/main/Multimodal-Diagram.png)

---


## 🧪 Run Locally

### 1. Clone this repo

```
git clone https://github.com/patla001/multimodal-rag-chatbot.git
```
### 2. Install the requirements

```
python -m pip install -r requirements.txt
```

### 3. Add your ChatGPT under .env or enviroment.txt

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 4. Run Chainlit
```
python -m chainlit run app.py
```
