# 🔐 Signup & Signin Web Application

<p align="center">
  <b>A simple full-stack authentication project built with FastAPI and HTML/CSS/JavaScript</b><br>
  <i>Designed as a beginner-friendly project for learning API development and frontend/backend communication.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/HTML5-Frontend-orange?logo=html5" alt="HTML5">
  <img src="https://img.shields.io/badge/JavaScript-Frontend-yellow?logo=javascript" alt="JavaScript">
  <img src="https://img.shields.io/badge/CSS3-Styling-blue?logo=css3" alt="CSS3">
</p>

---

## 📌 Project Overview

This project is a simple **Signup and Signin web application**.

The backend is built with **FastAPI**, while the frontend is a single HTML page containing the Signup and Signin forms.

The FastAPI application serves the HTML page and provides two API endpoints:

```text
POST /signup
POST /signin
```

The backend currently stores registered users in an **in-memory Python list**, so the data is temporary and will be lost when the application restarts. The project code defines this as `users_db = []`. fileciteturn0file0L19-L23

---

## 🖼️ Application Flow

```text
                 🌐 Browser
                     │
                     ▼
            ┌─────────────────┐
            │    index.html   │
            │                 │
            │  🔐 Sign Up     │
            │  🔑 Sign In     │
            └────────┬────────┘
                     │
                     │ HTTP / JSON
                     ▼
            ┌─────────────────┐
            │    FastAPI      │
            │     main.py     │
            └────────┬────────┘
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
      POST /signup          POST /signin
          │                     │
          ▼                     ▼
     Validate data         Find user
          │                     │
          ▼                     ▼
      users_db[]           Check password
          │                     │
          └──────────┬──────────┘
                     ▼
                  Response
                     │
                     ▼
                 🌐 Browser
```

---

## ✨ Features

| Feature | Description |
|---|---|
| 📝 Signup | Create a new account |
| 📧 Email | Email validation through Pydantic's `EmailStr` |
| 👤 Username | Register a username |
| 🔑 Password | Enter and confirm a password |
| 🔐 Signin | Login using email or username |
| 🔄 Form Switching | Switch between Signup and Signin |
| ⚠️ Validation | Displays validation and authentication errors |
| 🌐 REST API | Frontend communicates with FastAPI using JSON |
| 🧠 In-Memory Storage | Users are stored temporarily in a Python list |
| 🎨 Simple UI | Centered card-based interface |

The frontend contains separate Signup and Signin forms and allows the user to switch between them. fileciteturn0file1L18-L35

---

## 🏗️ Technology Stack

```text
Frontend
├── HTML5
├── CSS3
└── JavaScript

Backend
├── Python
├── FastAPI
├── Pydantic
└── Jinja2 Templates

Storage
└── Python in-memory list
```

### Technologies Used

- 🐍 **Python**
- ⚡ **FastAPI**
- 📦 **Pydantic**
- 🎨 **HTML5 / CSS3**
- ⚙️ **JavaScript**
- 🧩 **Jinja2Templates**
- 🌐 **Fetch API**

The backend imports FastAPI, CORS middleware, HTML responses, Jinja2 templates, and Pydantic models. fileciteturn0file0L1-L6

---

## 📁 Project Structure

Recommended project structure:

```text
signup-signin/
│
├── main.py
│
├── templates/
│   └── index.html
│
└── README.md
```

The FastAPI application is configured to load templates from a directory named `templates`. fileciteturn0file0L19-L20

> Make sure `index.html` is inside the `templates` folder if you are using the current `main.py`.

---

## 🔌 API Endpoints

### 📝 Signup

```http
POST /signup
```

Example JSON:

```json
{
  "email": "user@example.com",
  "username": "user123",
  "password": "123456",
  "re_password": "123456"
}
```

The backend checks whether the two passwords match and whether the email or username already exists. fileciteturn0file0L41-L50

Successful response:

```json
{
  "message": "Signup successful"
}
```

---

### 🔐 Signin

```http
POST /signin
```

Example JSON:

```json
{
  "identifier": "user123",
  "password": "123456"
}
```

The `identifier` can contain either the user's **email or username**. fileciteturn0file0L58-L64

Successful response:

```json
{
  "message": "Signin successful"
}
```

---

## 🧾 Request Models

### SignupRequest

The backend expects:

```python
class SignupRequest(BaseModel):
    email: EmailStr
    username: str
    password: str
    re_password: str
```

This means Signup requires:

```text
📧 Email
👤 Username
🔑 Password
🔁 Re-enter Password
```

The model is defined directly in `main.py`. fileciteturn0file0L25-L30

### SigninRequest

Signin requires:

```python
class SigninRequest(BaseModel):
    identifier: str
    password: str
```

fileciteturn0file0L32-L34

---

## 🎨 Frontend

The frontend provides a simple centered authentication card.

```text
┌──────────────────────────────────┐
│          🔐 Sign Up              │
│                                  │
│  📧 Email                        │
│  👤 Username                     │
│  🔑 Password                     │
│  🔁 Re-enter Password            │
│                                  │
│       [     Sign Up     ]        │
│                                  │
│ Already have an account? Sign In │
└──────────────────────────────────┘
```

The page uses CSS for the centered layout, form styling, buttons, error messages, and form switching. fileciteturn0file1L7-L15

---

## 🔄 Signup Process

```text
User enters:
    │
    ├── Email
    ├── Username
    ├── Password
    └── Re-enter Password
            │
            ▼
      JavaScript creates JSON
            │
            ▼
       POST /signup
            │
            ▼
       FastAPI validates
            │
       ┌────┴────┐
       ▼         ▼
   Valid       Invalid
       │         │
       ▼         ▼
 Store user   Show error
       │
       ▼
"Signup successful!"
       │
       ▼
 Switch to Signin
```

The frontend sends Signup data as JSON to `/signup` using JavaScript's `fetch()` API. fileciteturn0file1L40-L55

---

## 🔑 Signin Process

```text
User enters:
    │
    ├── Email / Username
    └── Password
            │
            ▼
      POST /signin
            │
            ▼
      Find user in users_db
            │
       ┌────┴────┐
       ▼         ▼
    Found      Not Found
       │         │
       ▼         ▼
Check password  404 Error
       │
   ┌───┴────┐
   ▼        ▼
Correct   Wrong
   │        │
   ▼        ▼
Success   401 Error
```

The backend searches for a user by either email or username and then checks the supplied password. fileciteturn0file0L58-L67

---

## ⚠️ Error Handling

The application currently handles several situations.

### Signup

If passwords do not match:

```text
Passwords do not match
```

If the email or username already exists:

```text
User already exists
```

These checks are implemented in the Signup endpoint. fileciteturn0file0L41-L50

### Signin

If the user does not exist:

```text
User does not exist
```

If the password is incorrect:

```text
Invalid email/username or password
```

fileciteturn0file0L60-L65

The frontend displays API errors in the appropriate error areas. fileciteturn0file1L94-L103

---

## 🌐 CORS

The backend enables CORS and currently allows all origins, methods, and headers:

```python
allow_origins=["*"]
allow_methods=["*"]
allow_headers=["*"]
```

fileciteturn0file0L10-L16

This is convenient for local development, but for a production application it should be restricted to trusted frontend origins.

---

## 🚀 Installation

### 1. Install Python

Check that Python is installed:

```bash
python --version
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn jinja2 pydantic[email]
```

---

## ▶️ Run the Application

From the project directory:

```bash
uvicorn main:app --reload
```

The application will normally be available at:

```text
http://127.0.0.1:8000
```

The frontend JavaScript is already configured to send API requests to:

```text
http://127.0.0.1:8000
```

fileciteturn0file1L37-L38

Open the application in your browser:

```text
http://127.0.0.1:8000
```

The `/` route serves the HTML template. fileciteturn0file0L36-L39

---

## 🧪 Testing the Application

### Test Signup

Try:

```text
Email: test@example.com
Username: testuser
Password: 123456
Re-enter Password: 123456
```

Expected:

```text
Signup successful! Please sign in.
```

### Test Wrong Password

After creating the user, try signing in with an incorrect password.

Expected:

```text
Invalid email/username or password
```

### Test Unknown User

Try an email or username that was not registered.

Expected:

```text
User does not exist
```

---

## 💾 Current Data Storage

This version does **not** use a database.

Users are stored here:

```python
users_db = []
```

A new user is appended to this list after successful Signup. fileciteturn0file0L22-L23

Example internal structure:

```python
{
    "email": "test@example.com",
    "username": "testuser",
    "password": "123456"
}
```

### Important

Because this is an in-memory list:

```text
Application starts
       ↓
users_db = []
       ↓
User signs up
       ↓
User stored in memory
       ↓
Application restarts
       ↓
users_db = []
       ↓
User data is gone
```

---

## 🔒 Security Notice

This project is suitable for **learning and local development**, but it is **not production-ready authentication**.

The current implementation stores passwords directly in the in-memory user dictionary. fileciteturn0file0L50-L53

For a production version, consider adding:

- 🔐 Password hashing
- 🗄️ SQLite/PostgreSQL database
- 🎟️ JWT authentication
- 🔑 Secure sessions
- 🛡️ HTTPS
- 🚫 Restricted CORS origins
- ⏳ Account/session expiration
- 🔒 Strong password rules
- 🧹 Input sanitization
- 📋 Authentication logging

---

## 🔮 Future Improvements

### Version 2 — Database

Replace:

```text
users_db = []
```

with:

```text
SQLite
```

Possible structure:

```text
users
├── id
├── email
├── username
├── password_hash
└── created_at
```

### Version 3 — Secure Authentication

Add:

```text
Password Hashing
      ↓
JWT Tokens
      ↓
Protected Routes
      ↓
User Sessions
```

### Version 4 — User Dashboard

After successful login:

```text
┌─────────────────────────────┐
│       👤 Dashboard          │
├─────────────────────────────┤
│ Welcome, Username!          │
│                             │
│ Profile                     │
│ Settings                    │
│ Change Password             │
│ Logout                      │
└─────────────────────────────┘
```

### Version 5 — Admin Panel

Possible future features:

- 👨‍💼 Admin login
- 👥 User management
- 🔍 Search users
- 🗑️ Delete users
- 🔒 Disable accounts
- 📊 User statistics

---

## 📚 Learning Objectives

This project demonstrates how a frontend and backend communicate.

You can learn:

- FastAPI basics
- API routes
- HTTP POST requests
- JSON requests/responses
- Pydantic models
- Request validation
- HTML forms
- CSS styling
- JavaScript `fetch()`
- Async JavaScript
- Error handling
- CORS
- Jinja2 templates
- Basic authentication concepts

---

## 📄 Files

### `main.py`

Contains:

```text
FastAPI application
       │
       ├── CORS configuration
       ├── Template configuration
       ├── User storage
       ├── Signup model
       ├── Signin model
       ├── Home route
       ├── Signup API
       └── Signin API
```

### `templates/index.html`

Contains:

```text
HTML
 ├── Signup form
 ├── Signin form
 ├── CSS
 ├── JavaScript
 ├── Signup request
 ├── Signin request
 └── Form switching
```

The uploaded frontend defines the complete Signup/Signin interface and its JavaScript API calls. fileciteturn0file1L18-L38

---

## 👨‍💻 Author

**Muhammad Furqan**

Python / FastAPI Authentication Project

---

## 📜 License

This project is intended for **educational and personal development purposes**.

You may modify and extend it for learning.

---

<p align="center">
  🔐 <b>Signup & Signin Application</b> 🔐<br>
  <i>Built with Python + FastAPI + HTML + CSS + JavaScript</i>
</p>
