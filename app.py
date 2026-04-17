from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# -----------------------
# 🤖 OLLAMA MEDICAL AI
# -----------------------
def get_response(message):

    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "llama3",   # or "mistral"
        "prompt": f"""
You are a STRICT MEDICAL AI ASSISTANT.

IMPORTANT RULES:
- Do NOT give long paragraphs
- Do NOT ask extra questions
- Give only structured output

FORMAT MUST BE:

Condition:
Treatment:
Warning:

User symptom: {message}
""",
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        data = response.json()

        return data.get("response", "No response from model")

    except Exception as e:
        print("ERROR:", e)
        return "⚠ Ollama not running. Start it using: ollama run llama3"


# -----------------------
# 🏠 HOME PAGE
# -----------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------
# 💬 CHAT ROUTE
# -----------------------
@app.route("/chat", methods=["POST"])
def chat():

    message = request.form.get("message")

    if not message:
        return render_template("index.html")

    reply = get_response(message)

    return f"""
    <html>
    <head>
        <title>AI Medical Assistant</title>
    </head>

    <body style="font-family:Arial; background:#f2f6ff; padding:20px;">

        <h2>🩺 AI Medical Assistant (LOCAL LLM)</h2>

        <div style="background:#cfe2ff; padding:10px; border-radius:10px;">
            <b>You:</b> {message}
        </div>

        <br>

        <div style="background:#d4edda; padding:10px; border-radius:10px;">
            <b>Bot:</b><br>{reply}</div>

        <br><br>

        <a href="/" style="text-decoration:none; background:#2b6cb0; color:white; padding:10px; border-radius:8px;">
            ⬅ Back
        </a>

    </body>
    </html>
    """


# -----------------------
# 🚀 RUN APP
# -----------------------
if __name__ == "__main__":
    app.run(debug=True)