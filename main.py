from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return{
        "message": "Hello My Dear Customer"
    }

@app.get("/products/categories/food")
def get_products():
    return {
        "product1": {
            "name": "sandwich",
            "price" : 10,
            "product_left" : 10
        }
        
    }