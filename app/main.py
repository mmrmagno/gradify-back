from fastapi import FastAPI
from .database import engine, Base
from .routers import schools, users, classes, assignments, grades
import uvicorn

# Initialize database
Base.metadata.create_all(bind=engine)

# Create FastAPI instance
app = FastAPI()

# Include Routers
app.include_router(schools.router)
app.include_router(users.router)
app.include_router(classes.router)
app.include_router(assignments.router)
app.include_router(grades.router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
