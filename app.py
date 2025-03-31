from flask import Flask, request, url_for, redirect, render_template
import pickle
import numpy as np


app = Flask(__name__)
app.debug = False

reg = pickle.load(open("model.pkl", "rb"))




@app.route("/")
def main():
     return render_template("main.html")

@app.route("/about")
def about():
     return render_template("about.html")

@app.route("/choose")
def choose():
     return render_template("choose.html")

@app.route("/remedy")
def remedy():
     return render_template("sol.html")

@app.route("/test")
def test():
     return render_template("test.html")



@app.route("/predict", methods=["POST"])
def predict():
    data = [float(request.form[key]) for key in request.form.keys()]
    arr = np.array([data])
    pred = reg.predict(arr)
    print(pred)
    return render_template("index.html", data=pred)




if __name__ == "__main__":
    # Use a production WSGI server like Gunicorn
    # Use Gunicorn for production
    app.run(host='0.0.0.0', port=5000)
