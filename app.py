from flask import Flask, redirect, url_for, render_template, request, session, flash, jsonify
import os.path
from werkzeug.utils import secure_filename
import predict_1_file_or_folder as predict

UPLOAD_FOLDER = "/home"

app = Flask(__name__)
app.secret_key = "hello"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("test.html")

@app.route("/file", methods=["POST", "GET"])
def file():
    if request.method == "POST":
        text = request.files['file']
        if text.filename:
            filename = secure_filename(text.filename)
            text.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            text_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            result = predict.predict_1_file(text_path)
            # flash(result)
            # return redirect(url_for("home"))
            return jsonify(result)
    else:
        return render_template("test.html")
        # flash("Predict: ", result)

@app.route("/text", methods=["POST", "GET"])
def text():
    if request.method == "POST":
        text = request.form['text']
        #text = request.json["text"]
        print(text)
        result = predict.predict_by_text(text)
        # flash(result)
        # return redirect(url_for("home"))
        return jsonify(result)
    else:
        return render_template("test.html")

@app.route("/textjson", methods=["POST"])
def textjson():
    if request.method == "POST":
        #text = request.form['text']
        text = request.json["text"]
        print(text)
        result = predict.predict_by_text(text)
        # flash(result)
        # return redirect(url_for("home"))

        return jsonify({"result": result})
    else:
        return render_template("test.html")

if __name__ == '__main__':
    app.run(debug=True)