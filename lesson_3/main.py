import uvicorn
from fastapi import FastAPI, HTTPException, Query
from typing import Optional, List

from models.models import Product

title = "Lesson 3"


app = FastAPI(title=title)

sample_product_1 = {
    "product_id": 123,
    "name": "Smartphone",
    "category": "Electronics",
    "price": 599.99,
}

sample_product_2 = {
    "product_id": 456,
    "name": "Phone Case",
    "category": "Accessories",
    "price": 19.99,
}

sample_product_3 = {
    "product_id": 789,
    "name": "Iphone",
    "category": "Electronics",
    "price": 1299.99,
}

sample_product_4 = {
    "product_id": 101,
    "name": "Headphones",
    "category": "Accessories",
    "price": 99.99,
}

sample_product_5 = {
    "product_id": 202,
    "name": "Smartwatch",
    "category": "Electronics",
    "price": 299.99,
}

sample_products = [
    sample_product_1,
    sample_product_2,
    sample_product_3,
    sample_product_4,
    sample_product_5,
]


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8066, reload=True, workers=3)


def get_product_by_id(product_id: int):
    for product in sample_products:
        if product["product_id"] == product_id:
            return product
    return None


@app.get("/product/{product_id}")
async def get_product(product_id: int):
    product = get_product_by_id(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


def filter_products(keyword: str, category: Optional[str], limit: Optional[int]):
    filtered_products = []
    for product in sample_products:
        if keyword.lower() in product["name"].lower():
            if category is None or product["category"] == category:
                filtered_products.append(product)
                if limit and len(filtered_products) >= limit:
                    break
    return filtered_products


@app.get("/products/search")
async def search_products(
    keyword: str = Query(..., min_length=1),
    category: Optional[str] = None,
    limit: int = 10,
):
    if limit < 1:
        raise HTTPException(status_code=400, detail="Limit must be at least 1")
    matched_products = filter_products(keyword, category, limit)
    return matched_products
