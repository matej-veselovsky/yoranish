from flask import Flask, render_template, request
from yoranish import translate

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    output=""
    if request.method=="POST":
        word = request.form.get("inputword")
        direction = int(request.form.get("direction"))
        output=translate(word, direction)

    return render_template("index.html", output=output)


@app.route("/about")
def about():
    with open("about.txt", "r", encoding="UTF-8") as file:
        return render_template("about.html", content=file.readlines())


if __name__ == "__main__":
    app.run()
