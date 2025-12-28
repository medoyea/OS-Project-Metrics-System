from flask import Flask, render_template, send_file
import subprocess

app = Flask(__name__, static_folder="/shared", static_url_path="/shared")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/report")
def get_report():
    return send_file(
        "/shared/report.pdf",
        as_attachment=False,
        mimetype="application/pdf"
    )

@app.route("/generate")
def generate():
    subprocess.run(["python3", "/shared/generatereport.py"])
    return "ok"

app.run(host="0.0.0.0", port=8000)