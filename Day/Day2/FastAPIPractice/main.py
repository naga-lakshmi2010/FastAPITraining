from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"page":"home"}
@app.get("/about")
def about():
    return{"page":"About","author":"Charitha"}
@app.get("/health")
def health():
    return{"status":"ok"}