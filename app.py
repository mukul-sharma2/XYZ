from flask import Flask, render_template

app = Flask(__name__, template_folder="frontend/html", static_folder="frontend")


@app.route("/")
def home():
    return render_template("index.html", name="Flask")

if __name__ == "__main__":
    app.run(debug=True)
