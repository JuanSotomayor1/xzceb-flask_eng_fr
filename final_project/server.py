from flask import Flask, render_template, request
from machinetranslation import translator

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/englishToFrench", methods=["POST"])
def translate_english_to_french():
    english_text = request.form.get("english_text")
    french_text = translator.englishToFrench(english_text)
    return french_text

@app.route("/frenchToEnglish", methods=["POST"])
def translate_french_to_english():
    french_text = request.form.get("french_text")
    english_text = translator.frenchToEnglish(french_text)
    return english_text

if __name__ == "__main__":
    app.run()

