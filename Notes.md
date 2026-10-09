"Fastapi is faster than any other framework 
1. fastapi easy to learn 
2. asyn programing it means simultensly handle multiple request
3. it is build top on starlet and pydantic 

Fastapi is the framework which is used to build backend apis .."


For checking Python in cmd & pip 
Python --version 
pip --version 

For Installing Fastapi --
  1. Create Virtual Environment 
       python -m venv env 
  2. For activating venv 
       windows - ./env/Scripts/activate
                  \env\Scripts\activate.bat
       linux - source env/bin/activate

## For run Fastapi as server
    fastpi dev main.py

     🌐 Server started at http://127.0.0.1:8000
    Documentation at http://127.0.0.1:8000/docs

from fastapi import FastAPI

<!-- # print(fastapi.__version__) -->

app = FastAPI()  # server 

# endpoint  url 
particular data show krna hai 

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


