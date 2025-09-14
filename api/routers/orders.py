from fastapi import APIRouter
from services.fake_data import generate_order

router = APIRouter(prefix="/orders", tags=["orders"])

@router.get("/{order_id}")
def get_order(order_id: int):
    return generate_order(order_id)
