from sqlalchemy.orm import Session
from . import models, schemas

# CRUD Operations

def create_school(db: Session, school: schemas.SchoolCreate):
    db_school = models.School(**school.dict())
    db.add(db_school)
    db.commit()
    db.refresh(db_school)
    return db_school

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_class(db: Session, class_: schemas.ClassCreate):
    db_class = models.Class(**class_.dict())
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class

def create_subject(db: Session, subject: schemas.SubjectCreate):
    db_subject = models.Subject(**subject.dict())
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject

def create_assignment(db: Session, assignment: schemas.AssignmentCreate):
    db_assignment = models.Assignment(**assignment.dict())
    db.add(db_assignment)
    db.commit()
    db.refresh(db_assignment)
    return db_assignment

def get_assignment(db: Session, assignment_id: int):
    return db.query(models.Assignment).filter(models.Assignment.id == assignment_id).first()

def create_class(db: Session, class_: schemas.ClassCreate):
    db_class = models.Class(**class_.dict())
    db.add(db_class)
    db.commit()
    db.refresh(db_class)
    return db_class

def get_class(db: Session, class_id: int):
    return db.query(models.Class).filter(models.Class.id == class_id).first()

def create_grade(db: Session, grade: schemas.GradeCreate):
    db_grade = models.Grade(**grade.dict())
    db.add(db_grade)
    db.commit()
    db.refresh(db_grade)
    return db_grade

def get_grade(db: Session, grade_id: int):
    return db.query(models.Grade).filter(models.Grade.id == grade_id).first()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()
