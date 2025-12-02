from flask import Flask, render_template, request, redirect, session
from passlib.hash import sha256_crypt
from db import get_db
from otp_service import generate_otp
from dotenv import load_dotenv
import os

load_dotenv()


app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = sha256_crypt.hash(request.form["password"])
        conn = get_db()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (username, email, password) VALUES (%s,%s,%s)",
                (username, email, password)
            )
            conn.commit()
            return redirect("/login")
        except:
            return "Username or Email already exists!"
    return render_template("register.html")

# Login
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE username=%s", (username,))
        record = cursor.fetchone()
        if record and sha256_crypt.verify(password, record[0]):
            session["username"] = username
            return f"Login Successful! Welcome {username}"
        else:
            return "Invalid Username or Password"
    return render_template("login.html")

# Forgot Password
@app.route("/forgot", methods=["GET","POST"])
def forgot():
    if request.method == "POST":
        email = request.form["email"]
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE email=%s", (email,))
        user = cursor.fetchone()
        if user:
            otp = generate_otp()
            print("OTP:", otp)
            cursor.execute("UPDATE users SET otp=%s WHERE email=%s", (otp, email))
            conn.commit()
            session["reset_email"] = email
            return redirect("/verify-otp")
        else:
            return "Email not found!"
    return render_template("forgot.html")

# Verify OTP
@app.route("/verify-otp", methods=["GET","POST"])
def verify_otp():
    if request.method == "POST":
        otp_input = request.form["otp"]
        email = session.get("reset_email")
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT otp FROM users WHERE email=%s", (email,))
        real_otp = cursor.fetchone()
        if real_otp and otp_input == real_otp[0]:
            return redirect("/reset-password")
        else:
            return "Invalid OTP!"
    return render_template("verify_otp.html")

# Reset Password
@app.route("/reset-password", methods=["GET","POST"])
def reset_password():
    if request.method == "POST":
        new_pass = sha256_crypt.hash(request.form["password"])
        email = session.get("reset_email")
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET password=%s, otp='' WHERE email=%s", (new_pass, email))
        conn.commit()
        return "Password Reset Successfully! <a href='/login'>Login</a>"
    return render_template("reset_password.html")

# Home
@app.route("/")
def home():
    return redirect("/login")

app.run(debug=True)

