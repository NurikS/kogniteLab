from flask import Flask, request, render_template
from Model import Model
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)



@app.route("/addlayer", methods=["GET", "POST"])
def AddLayer():
    print(request.json)
    return "OK", 200

@app.route("/summary", methods=["GET", "POST"])
def Summary():
    print(request.json)
    return "OK", 200

@app.route("/save", methods=["GET", "POST"])
def SaveModel():
    print(request.json)
    return "OK", 200

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")



if __name__ == '__main__':
    model = Model(10)
    app.run(host="127.0.0.1", port=5000, debug=True)