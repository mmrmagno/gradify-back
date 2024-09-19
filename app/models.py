from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class School(Base):
    __tablename__ = "schools"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    address = Column(String)
    phone = Column(String)
    email = Column(String)
    
    users = relationship("User", back_populates="school")
    classes = relationship("Class", back_populates="school")

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    role = Column(String, default="student")
    is_admin = Column(Boolean, default=False)
    school_id = Column(Integer, ForeignKey("schools.id"))
    
    school = relationship("School", back_populates="users")
    classes = relationship("Class", back_populates="teacher")

class Class(Base):
    __tablename__ = "classes"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey("users.id"))
    school_id = Column(Integer, ForeignKey("schools.id"))
    
    teacher = relationship("User", back_populates="classes")
    school = relationship("School", back_populates="classes")
    subjects = relationship("Subject", back_populates="class_")

class Subject(Base):
    __tablename__ = "subjects"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    class_id = Column(Integer, ForeignKey("classes.id"))
    teacher_id = Column(Integer, ForeignKey("users.id"))
    
    class_ = relationship("Class", back_populates="subjects")
    assignments = relationship("Assignment", back_populates="subject")

class Assignment(Base):
    __tablename__ = "assignments"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    max_grade = Column(Integer, nullable=False)
    
    subject = relationship("Subject", back_populates="assignments")
    grades = relationship("Grade", back_populates="assignment")

class Grade(Base):
    __tablename__ = "grades"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("users.id"))
    assignment_id = Column(Integer, ForeignKey("assignments.id"))
    grade = Column(Integer, nullable=False)
    
    assignment = relationship("Assignment", back_populates="grades")
