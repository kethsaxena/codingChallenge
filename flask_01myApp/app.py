from flask import Flask, render_template, request

app = Flask(__name__)

# Route: Home page with the form
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        return render_template("thanks.html", name=name)
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
