from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db import get_db
from database.models import Doctor, User
from utils.auth import get_current_user

router = APIRouter(prefix="/doctors", tags=["Doctors"])


def parse_available_days(available_days: str) -> dict:
    """
    Format stored: days | phone | hospital | address | city | photo
    Example: "Mon,Wed,Fri | +91 98261 45231 | Bombay Hospital | Bombay Hospital, Ring Road, Indore | Indore | https://..."
    """
    parts = [p.strip() for p in available_days.split("|")] if available_days else []

    days    = parts[0] if len(parts) > 0 else ""
    phone   = parts[1] if len(parts) > 1 else ""
    hospital= parts[2] if len(parts) > 2 else ""
    address = parts[3] if len(parts) > 3 else ""
    city    = parts[4] if len(parts) > 4 else "Indore"
    photo   = parts[5] if len(parts) > 5 else ""

    # Remove city name from address to avoid duplication
    # e.g. "Bombay Hospital, Ring Road, Indore, MP" → "Bombay Hospital, Ring Road"
    clean_address = address
    for suffix in [f", {city}, MP", f", {city},MP", f" {city}, MP", f", {city}"]:
        if clean_address.endswith(suffix):
            clean_address = clean_address[: -len(suffix)].strip()
            break

    return {
        "days": days,
        "phone": phone,
        "hospital": hospital,
        "address": clean_address,
        "city": city,
        "photo": photo,
    }


@router.get("/")
def get_all_doctors(specialization: str = None, db: Session = Depends(get_db)):
    query = db.query(Doctor, User).join(User, Doctor.user_id == User.id)
    if specialization:
        query = query.filter(Doctor.specialization.ilike(f"%{specialization}%"))
    results = query.all()

    result = []
    for doctor, user in results:
        parsed = parse_available_days(doctor.available_days)
        result.append({
            "id": doctor.id,
            "user_id": doctor.user_id,
            "name": user.name,
            "specialization": doctor.specialization,
            "experience": doctor.experience,
            "consultation_fee": float(doctor.consultation_fee) if doctor.consultation_fee else 500,
            # Parsed fields
            "available_days": parsed["days"],
            "phone": parsed["phone"],
            "hospital": parsed["hospital"],
            "address": parsed["address"],
            "city": parsed["city"],
            "photo": parsed["photo"],
        })
    return result


@router.get("/{doctor_id}")
def get_doctor_by_id(doctor_id: int, db: Session = Depends(get_db)):
    result = db.query(Doctor, User).join(User, Doctor.user_id == User.id).filter(Doctor.id == doctor_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Doctor not found")
    doctor, user = result
    parsed = parse_available_days(doctor.available_days)
    return {
        "id": doctor.id,
        "name": user.name,
        "specialization": doctor.specialization,
        "experience": doctor.experience,
        "consultation_fee": float(doctor.consultation_fee) if doctor.consultation_fee else 500,
        "available_days": parsed["days"],
        "phone": parsed["phone"],
        "hospital": parsed["hospital"],
        "address": parsed["address"],
        "city": parsed["city"],
        "photo": parsed["photo"],
    }


@router.put("/{doctor_id}")
def update_doctor_profile(
    doctor_id: int,
    specialization: str = None,
    experience: int = None,
    consultation_fee: float = None,
    available_days: str = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    if doctor.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    if specialization:    doctor.specialization = specialization
    if experience:        doctor.experience = experience
    if consultation_fee:  doctor.consultation_fee = consultation_fee
    if available_days:    doctor.available_days = available_days
    db.commit()
    db.refresh(doctor)
    return {"message": "Doctor profile updated"}
