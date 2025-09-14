from fastapi import APIRouter
from services.fake_data import generate_customer

router = APIRouter(prefix="/customers", tags=["customers"])

@router.get("/{customer_id}")
def get_customer(customer_id: int):
    return generate_customer(customer_id)
