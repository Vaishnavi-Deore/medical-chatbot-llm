# AI Medical Chatbot using LLM

## Overview

This project is an AI-powered Medical Chatbot that provides basic health guidance based on user symptoms. It uses a locally running Large Language Model (LLM) via Ollama to generate intelligent responses.

**Note:** This chatbot does not provide medical diagnosis. It only offers general guidance. Users should consult a medical professional for serious conditions.

---

## Features

* LLM-based chatbot using Ollama
* Symptom-based medical guidance
* Emergency detection system
* Interactive chat interface
* Works offline with local model

---

## Tech Stack

* Backend: Python, Flask
* Frontend: HTML, CSS, JavaScript
* LLM: Ollama (Phi3 model)
* Libraries: Requests

---

## Project Structure

```
medical-chatbot/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```

---

## Installation and Setup

### Step 1: Clone the repository

```
git clone https://github.com/YOUR_USERNAME/medical-chatbot-llm.git
cd medical-chatbot-llm
```

### Step 2: Install dependencies

```
pip install flask requests
```

### Step 3: Run the local LLM (Ollama)

```
ollama run phi3
```

### Step 4: Start the application

```
python app.py
```

### Step 5: Open in browser

```
http://127.0.0.1:5000
```

---

## Usage

1. Open the chatbot in your browser
2. Enter your symptoms
3. Receive AI-generated guidance
4. Follow recommendations or consult a doctor if needed

---

## Example Inputs

* I have fever and headache
* I have cold and cough
* I am experiencing chest pain

---

## Safety Features

* Detects emergency-related keywords
* Avoids providing final medical diagnosis
* Encourages professional consultation

---

## Future Enhancements

* Voice-based interaction
* Medical report generation
* Chat history storage
* Cloud deployment
* Enhanced UI/UX

---
