from pydantic import BaseModel

class SchoolCreate(BaseModel):
    name: str
    address: str
    phone: str
    email: str

class UserCreate(BaseModel):
    name: str
    email: str
    role: str
    is_admin: bool = False

class ClassCreate(BaseModel):
    name: str
    teacher_id: int

class SubjectCreate(BaseModel):
    name: str
    class_id: int
    teacher_id: int

class AssignmentCreate(BaseModel):
    title: str
    subject_id: int
    max_grade: int

class GradeCreate(BaseModel):
    student_id: int
    assignment_id: int
    grade: int
