from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter(
    prefix="/schools",
    tags=["schools"]
)

@router.post("/", response_model=schemas.SchoolCreate)
def create_school(school: schemas.SchoolCreate, db: Session = Depends(get_db)):
    return crud.create_school(db=db, school=school)
