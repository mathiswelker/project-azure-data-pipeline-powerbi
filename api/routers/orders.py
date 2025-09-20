from fastapi import APIRouter
from services.fake_data import orders  # nur die Liste

router = APIRouter(prefix="/orders", tags=["orders"])

@router.get("/")
def get_all_orders():
    return orders  # liefert die gesamte Kundenliste
