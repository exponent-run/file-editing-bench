from fastapi import APIRouter, Depends
from typing import Optional
from pydantic import BaseModel

router = APIRouter()

class ProductCreate(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    category: str

@router.post("/products/")
def create_product(product: ProductCreate):
    return {"message": "Product created", "data": product}

@router.put("/products/{product_id}")
def update_product(product_id: int, product: ProductCreate):
    return {"message": "Product updated", "id": product_id, "data": product}

@router.get("/products/")
def list_products(category: Optional[str] = None, sort_by: str = "name"):
    return {"message": "Products retrieved", "category": category, "sort_by": sort_by}