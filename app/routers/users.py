from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db
from ..keycloak import create_keycloak_user

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/", response_model=schemas.UserCreate)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Create the user in Keycloak
    create_keycloak_user(user.name, user.email, "defaultpassword")
    # Then create the user in the database
    return crud.create_user(db=db, user=user)

@router.get("/{user_id}", response_model=schemas.UserCreate)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
