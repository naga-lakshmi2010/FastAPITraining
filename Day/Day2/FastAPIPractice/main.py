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

# Post request
@app.post("/create")
def create_something():
    return{"message":"Created"}

# Path Parameters
@app.get("/student/{usn}")
def get_result(usn):
    return{"Result":"Distinction","usn":usn}

# Path Parameters with type hint
@app.get("/candidate/{rollNo}")
def get_candidate(rollNo:int):
    return{"Result":"Distinction","roll no":rollNo,"type":str(type(rollNo))}