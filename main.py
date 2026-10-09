from fastapi import FastAPI, Request
from mockData import products



app = FastAPI()


@app.get("/")         
def home():
    return "WELCOME TO FASTAPI SERIES"


@app.get("/products")
def get_products():
    return products


#path params
@app.get("/product/{product_id}")
def get_one_product(product_id:int):
     ## if product available with id, return product else error message
     
     for one_prodct in products:
         if one_prodct.get("id") == product_id:
             return one_prodct
         
     return {
        "error":"There is no prodct belongs to this id "
         }

## query params

@app.get("/greet")
def greet(name:str,age:int):
    return {"greet ": f"hello {name}, your age is {age}"}


# when we have to send multiple querys 

# we use request 
# requset :- path , query , body params


@app.get("/greet_1")
def greet_user(request:Request):
       query_param =  dict(request.query_params)
       print(query_param)
       return {"greet ": f"hello {query_param.get("name")}, your age {query_param.get("age")} is "}