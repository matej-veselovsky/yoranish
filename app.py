from flask import Flask, render_template, request
from yoranish import translate

app = Flask(__name__)


@app.route("/")
def question():
    return render_template("index.html")


@app.route("/answer", methods=["GET", "POST"])
def answer():
    if request.method == "POST":
        word = request.form.get("inputword")
        direction = request.form.get("direction")
        output = translate(word, int(direction))
        return render_template("answer.html", output=output)


if __name__ == "__main__":
    app.run()
