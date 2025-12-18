from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Secure Login System Running!"

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)

