from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter(
    prefix="/grades",
    tags=["grades"]
)

@router.post("/", response_model=schemas.GradeCreate)
def create_grade(grade: schemas.GradeCreate, db: Session = Depends(get_db)):
    return crud.create_grade(db=db, grade=grade)

@router.get("/{grade_id}", response_model=schemas.GradeCreate)
def get_grade(grade_id: int, db: Session = Depends(get_db)):
    db_grade = crud.get_grade(db, grade_id=grade_id)
    if not db_grade:
        raise HTTPException(status_code=404, detail="Grade not found")
    return db_grade
