from fastapi import FastAPI

# print(fastapi.__version__)

app = FastAPI()
# print(app)

#creating endpint 

@app.get("/")         
def home():
    return "WELCOME TO FASTAPI SERIES"


@app.get("/home")
def home2():
    return "Welcome to fastapi series"

#get -- http method 
#path -- http://127.0.0.1:8000/
# @app -- decorator 
# # app -- server  

@app.get("/contact")
def contact():
    return "YOu can connect us any time"