from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    bad_websites = [
        {"rank": 1, "url": "https://indianairforce.nic.in/", "country": "India"},
        {"rank": 2, "url": "http://nationalarchives.nic.in/", "country": "India"},
        {"rank": 3, "url": "https://www.irctctourism.com/", "country": "India"},
        {"rank": 4, "url": "https://www.ugc.gov.in/#", "country": "India"},
        {"rank": 5, "url": "https://www.ugc.gov.in/#", "country": "India"},
    ]
    return render_template("home.html", bad_websites=bad_websites)
if __name__ == "__main__":
    app.run(debug=True)
