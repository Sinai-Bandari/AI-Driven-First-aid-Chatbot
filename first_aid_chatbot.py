import google.generativeai as genai
from flask import Flask, render_template, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

API_KEY = "AIzaSyC3XECajJ6Qn2XD8uPoHnEIXxfTcAglR7M"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

TRANSLATE_URL = "https://libretranslate.com/translate"


def translate_text(text, target_lang):
    if target_lang == "en":
        return text
    try:
        response = requests.post(TRANSLATE_URL, data={
            "q": text,
            "source": "en",
            "target": target_lang,
            "format": "text"
        }, timeout=10)
        return response.json().get("translatedText", text)
    except Exception as e:
        print(f"Translation error: {e}")
        return text


def detect_language(text):
    try:
        response = requests.post("https://libretranslate.com/detect", data={"q": text})
        return response.json()[0]["language"]
    except:
        return "en"


def translate_to_english(text):
    src_lang = detect_language(text)
    if src_lang == "en":
        return text
    try:
        response = requests.post(TRANSLATE_URL, data={
            "q": text,
            "source": src_lang,
            "target": "en",
            "format": "text"
        }, timeout=10)
        return response.json().get("translatedText", text)
    except:
        return text


def get_first_aid_response(query):
    prompt = f"""
    You are a helpful first-aid assistant. Provide clear and concise first-aid instructions for the following situation.
    If you cannot provide information, say: "I cannot provide information on that, please seek medical help immediately."

    User Query: {query}
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Gemini error: {e}")
        return "Sorry, I encountered an error. Please try again."


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_response", methods=["POST"])
def get_chat_response():
    user_query = request.form["user_query"]
    lang = request.form.get("lang", "en")

    try:
        english_query = translate_to_english(user_query)
        english_response = get_first_aid_response(english_query)
        translated_response = translate_text(english_response, lang)
        return jsonify({"response": translated_response})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"response": "Sorry, an error occurred. Please try again."})


if __name__ == "__main__":
    app.run(debug=True)