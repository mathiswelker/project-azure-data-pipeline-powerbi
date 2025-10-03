from fastapi import APIRouter
from app.services.fake_data import customers

router = APIRouter(prefix="/customers", tags=["customers"])

@router.get("/")
def get_all_customers():
    return customers
