from fastapi import APIRouter
from datetime import datetime, UTC

router = APIRouter(prefix="/api")

@router.get("/")
def server_up():
    return "server is up!"

@router.get("/utc-datetime")
def get_utc_datetime():
    current_utc_datetime = datetime.now(UTC).isoformat() + "Z"
    return {"utc_datetime": current_utc_datetime}