from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/fakebook")
def fakebook():
    return render_template("fakebook.html")

@app.route("/salon")
def salon():
    return render_template("salon.html")


if __name__ == '__main__':
    app.run()