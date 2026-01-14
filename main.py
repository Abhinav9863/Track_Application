from fastapi import FastAPI
from models import Product

app = FastAPI()

products = [
    Product(id = 1, name ="phone",description ="budget smartphone",price =99.0, quantity=10),
    Product(id = 2, name ="laptop",description ="Budget Laptops",price =990.0, quantity=18)

]

@app.get("/")

def greet():
    return "Hello, Abhinavs world of programming!"

@app.get("/products")

def get_all_products():
    return products


