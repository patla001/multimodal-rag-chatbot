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
- **LLM Backend**: OpenAI GPT-4V or LLaVA
- **Database**: MongoDB (for storing records)
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

## 🧪 Run Locally

### 1. Clone this repo

```bash
[git clone https://github.com/patla001/multimodal-rag-chatbot.git](https://github.com/patla001/multimodal-rag-chatbot.git)
cd multimodal-rag-chatbot

```
