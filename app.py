from flask import Flask, render_template, request
from models.text_generation_model import TextGenerationModel

app = Flask(__name__)
model = TextGenerationModel()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.form["prompt"]
    generated_text = model.generate_text(prompt)
    return render_template("result.html", generated_text=generated_text)

if __name__ == "__main__":
    app.run(debug=True)