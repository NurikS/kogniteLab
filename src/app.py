from flask import Flask, request, render_template
from Model import Model

app = Flask(__name__)

@app.route("/api", methods=["GET", "POST"])
def AddLayer():
    print(request.json)
    return "OK", 200


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("../templates/index.html")



if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)