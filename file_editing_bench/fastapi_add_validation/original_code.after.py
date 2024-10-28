from fastapi import APIRouter, Depends, Query, Path
from typing import Optional, List
from pydantic import BaseModel, Field, constr, confloat
from enum import Enum

router = APIRouter()


class CategoryEnum(str, Enum):
    ELECTRONICS = "electronics"
    CLOTHING = "clothing"
    BOOKS = "books"
    OTHER = "other"


class SortFieldEnum(str, Enum):
    NAME = "name"
    PRICE = "price"
    CATEGORY = "category"


class ProductCreate(BaseModel):
    name: constr(min_length=1, max_length=100) = Field(..., example="Laptop")
    price: confloat(gt=0, lt=1000000) = Field(..., example=999.99)
    description: Optional[str] = Field(
        None, max_length=1000, example="High-performance laptop"
    )
    category: CategoryEnum = Field(..., example=CategoryEnum.ELECTRONICS)


@router.post("/products/")
def create_product(product: ProductCreate):
    return {"message": "Product created", "data": product}


@router.put("/products/{product_id}")
def update_product(
    product_id: int = Path(..., gt=0, example=1),
    product: ProductCreate = Field(
        ..., example={"name": "Laptop", "price": 999.99, "category": "electronics"}
    ),
):
    return {"message": "Product updated", "id": product_id, "data": product}


@router.get("/products/")
def list_products(
    category: Optional[CategoryEnum] = Query(None, example=CategoryEnum.ELECTRONICS),
    sort_by: SortFieldEnum = Query(SortFieldEnum.NAME, example=SortFieldEnum.PRICE),
    limit: int = Query(50, ge=1, le=100, example=10),
    offset: int = Query(0, ge=0, example=0),
):
    return {
        "message": "Products retrieved",
        "category": category,
        "sort_by": sort_by,
        "limit": limit,
        "offset": offset,
    }
