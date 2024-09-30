from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, keycloak
from ..database import get_db
from ..utils import send_email

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

def get_current_user(token: str):
    token_info = keycloak.introspect_token(token)
    if not token_info.get('active'):
        raise HTTPException(status_code=401, detail="Invalid token")
    return token_info

@router.post("/", response_model=schemas.UserCreate)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db), token: str = Depends(get_current_user)):
    # Create the user in Keycloak
    keycloak.create_keycloak_user(user.name, user.email, "defaultpassword")
    
    # Then create the user in the database
    db_user = crud.create_user(db=db, user=user)

    # Send welcome email with login information
    send_email(
        to_address=user.email,
        subject="Welcome to Gradify",
        message=f"Hello {user.name},\n\nYour account has been created. You can log in with your username and password."
    )
    
    return db_user

@router.get("/{user_id}", response_model=schemas.UserCreate)
def get_user(user_id: int, db: Session = Depends(get_db), token: str = Depends(get_current_user)):
    db_user = crud.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
