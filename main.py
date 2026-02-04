# === main.py ===
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, EmailStr

app = FastAPI()

# CORS setup for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# templates folder
templates = Jinja2Templates(directory="templates")

# In-memory user database
users_db = []

# --- Request models ---
class SignupRequest(BaseModel):
    email: EmailStr
    username: str
    password: str
    re_password: str

class SigninRequest(BaseModel):
    identifier: str
    password: str

# --- Routes ---
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/signup")
def signup(data: SignupRequest):
    if data.password != data.re_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    for user in users_db:
        if user['email'] == data.email or user['username'] == data.username:
            raise HTTPException(status_code=400, detail="User already exists")

    users_db.append({
        "email": data.email,
        "username": data.username,
        "password": data.password
    })

    return {"message": "Signup successful"}

@app.post("/signin")
def signin(data: SigninRequest):
    user = next((u for u in users_db if u['email']==data.identifier or u['username']==data.identifier), None)

    if not user:
        raise HTTPException(status_code=404, detail="User does not exist")
    if user['password'] != data.password:
        raise HTTPException(status_code=401, detail="Invalid email/username or password")

    return {"message": "Signin successful"}

