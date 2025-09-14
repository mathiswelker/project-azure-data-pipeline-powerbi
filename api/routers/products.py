from fastapi import APIRouter
from services.fake_data import generate_product

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/{product_id}")
def get_product(product_id: int):
    return generate_product(product_id)
