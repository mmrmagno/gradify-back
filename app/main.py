from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from .database import engine, Base
from .routers import schools, users, classes, assignments, grades
from .keycloak import validate_token
from dotenv import load_dotenv
import uvicorn
import os

# Load environment variables from .env file
load_dotenv()

# Initialize database
Base.metadata.create_all(bind=engine)

# Create FastAPI instance
app = FastAPI()

# Include OAuth2PasswordBearer for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    user_info = validate_token(token)
    if not user_info:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user_info

# Include Routers
app.include_router(schools.router)
app.include_router(users.router)
app.include_router(classes.router)
app.include_router(assignments.router)
app.include_router(grades.router)

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = crud.get_user_by_email(form_data.username)
    if not user or not crud.verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
