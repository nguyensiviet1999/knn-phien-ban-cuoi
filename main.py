from flask import Flask, redirect, url_for, render_template, request, session, flash
import os.path
from werkzeug.utils import secure_filename
import predict_1_file_or_folder as predict

UPLOAD_FOLDER = "E:/Python/TextClassifier/predict/"
# ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)
app.secret_key = "hello"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("test.html")

@app.route("/test", methods=["POST", "GET"])
def test():
    if request.method == "POST":
        text = request.files['file']
        # print("text", text)
        if text.filename:
            filename = secure_filename(text.filename)
            # print("filename", filename)
            text.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            text_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            # print("text", text_path)
            result = predict.predict_1_file(text_path)
            flash(result)
            return redirect(url_for("home"))
    else:
        return render_template("test.html")
        # flash("Predict: ", result)

if __name__ == '__main__':
    app.run(debug=True)