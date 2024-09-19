from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter(
    prefix="/assignments",
    tags=["assignments"]
)

@router.post("/", response_model=schemas.AssignmentCreate)
def create_assignment(assignment: schemas.AssignmentCreate, db: Session = Depends(get_db)):
    return crud.create_assignment(db=db, assignment=assignment)

@router.get("/{assignment_id}", response_model=schemas.AssignmentCreate)
def get_assignment(assignment_id: int, db: Session = Depends(get_db)):
    db_assignment = crud.get_assignment(db, assignment_id=assignment_id)
    if not db_assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")
    return db_assignment
