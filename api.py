from fastapi import FastAPI
from db import *
app = FastAPI()

@app.get("/")
def root():
    return{
        "message": "Hello My Dear Customer"
    }

@app.get("/products/categories/food")
def get_products():
    prod_names = {}
    for i in range(0,cursor.execute("")):
        prod_key = f"product{i}"
        