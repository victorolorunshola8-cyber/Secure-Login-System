from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
import bcrypt

# -----------------------------
# Flask App Configuration
# -----------------------------
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supersecretkey'

db = SQLAlchemy(app)

# -----------------------------
# Database Model
# -----------------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.LargeBinary(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    failed_attempts = db.Column(db.Integer, default=0)
    is_locked = db.Column(db.Boolean, default=False)

# -----------------------------
# Home Route
# -----------------------------
@app.route("/")
def home():
    return "Secure Login System Running!"

# -----------------------------
# Register Route
# -----------------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        role = request.form["role"]

        hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        new_user = User(
            username=username,
            email=email,
            password=hashed_pw,
            role=role
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful!", "success")
        return redirect(url_for("login"))

    return render_template("register.html")

# -----------------------------
# Login Route (SECURED)
# -----------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()

        if not user:
            flash("Invalid credentials", "error")
            return redirect(url_for("login"))

        # 🔒 Check if account is locked
        if user.is_locked:
            flash("Account locked due to multiple failed attempts", "error")
            return redirect(url_for("login"))

        # 🔐 Verify password
        if bcrypt.checkpw(password.encode("utf-8"), user.password):
            user.failed_attempts = 0
            db.session.commit()

            session["user_id"] = user.id
            session["username"] = user.username
            session["role"] = user.role

            if user.role == "Admin":
                return redirect(url_for("admin_dashboard"))
            return redirect(url_for("user_dashboard"))

        # ❌ Wrong password
        user.failed_attempts += 1

        if user.failed_attempts >= 3:
            user.is_locked = True
            flash("Account locked after 3 failed attempts", "error")
        else:
            flash("Invalid credentials", "error")

        db.session.commit()
        return redirect(url_for("login"))

    return render_template("login.html")

# -----------------------------
# Admin Dashboard
# -----------------------------
@app.route("/admin")
def admin_dashboard():
    if "user_id" not in session or session.get("role") != "Admin":
        flash("Access denied!", "error")
        return redirect(url_for("login"))

    return f"ADMIN DASHBOARD — Welcome {session['username']}"

# -----------------------------
# User Dashboard
# -----------------------------
@app.route("/user")
def user_dashboard():
    if "user_id" not in session:
        flash("Please login first", "error")
        return redirect(url_for("login"))

    return f"USER DASHBOARD — Welcome {session['username']}"

# -----------------------------
# Logout
# -----------------------------
@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully", "success")
    return redirect(url_for("login"))

# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
