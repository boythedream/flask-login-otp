📌 Flask Login System with MySQL + OTP Password Reset

A beginner-friendly authentication system built using Flask, MySQL, and Email-based OTP.
Users can register, login, reset password using a one-time password, and securely manage their account.

🚀 Features
🔐 Authentication

User Registration

User Login

Secure Password Hashing

Logout System

📩 OTP Password Reset

Enter email

Receive OTP via email

Verify OTP

Set new password

🗄️ Database (MySQL)

Stores user records

Stores OTP logs

Works smoothly with MySQL Workbench

🔒 Environment Variables

Database Credentials

Secret Key

Email Credentials
All stored safely in .env file.

🧱 Project Structure
project/
│── app.py
│── config.py
│── requirements.txt
│── README.md
│── .env
│── .gitignore
│
├── templates/
│    ├── login.html
│    ├── register.html
│    ├── forgot.html
│    └── reset.html
│
└── static/
     └── style.css

⚙️ Installation Guide
1️⃣ Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux

3️⃣ Install Requirements
pip install -r requirements.txt

🔑 Environment Setup (.env File)

Create a .env file:

SECRET_KEY=your_secret_key

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=flask_auth

EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password

🗄️ MySQL Setup

Run the following in MySQL Workbench:

CREATE DATABASE flask_auth;

USE flask_auth;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255)
);

CREATE TABLE otps (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100),
    otp VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

▶️ Run the App
python app.py


Then open:

http://127.0.0.1:5000

🧹 .gitignore Included
venv/
.env
__pycache__/
instance/

✨ Future Improvements

User email verification at signup

OTP expiry time

Admin panel

JWT API version

Beautiful UI redesign

🤝 Contributing

Pull requests are welcome.
For major changes, open an issue first.

📄 License

This project is free to use for learning and practice.