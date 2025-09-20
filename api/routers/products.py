from fastapi import APIRouter
from services.fake_data import products  # nur die Liste

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/")
def get_all_products():
    return products  # liefert die gesamte Kundenliste
