from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from Model import Model
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="../templates")
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

model = Model(10)


@app.route("/addlayer", methods=["GET", "POST"])
@cross_origin()
def AddLayer():
    model.AddLayer(10)
    print("layer added")
    return "added layer", 200


@app.route("/summary", methods=["GET", "POST"])
@cross_origin()
def Summary():
    model.ModelDefinition()
    return "summary printed", 200

@app.route("/save", methods=["GET", "POST"])
@cross_origin()
def SaveModel():
    model.SaveModel()
    print("model saved")
    return "OK", 200





if __name__ == '__main__':
    app.run(host = "127.0.0.1", debug=True)