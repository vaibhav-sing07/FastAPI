from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

#uvicorn myapi:app --reload

app=FastAPI()

students={
    1:{
        "name":"john",
        "age":17,
        "class":"year 12"
    }
}

class Student(BaseModel):
    name:str
    age:int
    year:str

class UpdateStudent(BaseModel):
    name: Optional[str]=None
    age: Optional[str]=None
    year: Optional[str]=None


@app.get("/")
def index():
    return {"name": "First Data"}


#Path Parameters
@app.get("/get-student/{student_id}")
def get_student(student_id:int = Path( description="The ID of the student",gt=0,lt=3)):
    return students[student_id]


#gt=greater than,lt=less than,ge=greater than and equal to,le=less than and equal to

#Query Parameters
#google.com/results?search=Python
@app.get("/get-by-name/{student_id}")
def get_student(*, student_id:int,name: Optional[str]=None, test : int):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    return {"Data":"Not Found"}

#Combining Query and Path parameter
#if a parameter is only in function its a path parameter
#if its in app definition and function both then its aquery parameter


#Request Body and the Post method
@app.post("/create-student/{student_id")
def create_student(student_id:int, student:Student):
    if student_id in students:
        return {"Error":"Student_Exists"}

    students[student_id]=student
    return students[student_id]


#Put method
@app.put("/update-student/{student_id}")
def update_student(student_id:int, student:UpdateStudent):
    if student_id not in students:
        return {"Error":"Student does not exist"}
    if student.name!=None:
        students[student_id].name=student.name
    if student.age!=None:
        students[student_id].age=student.age
    if student.year!=None:
        students[student_id].year=student.year

    #students[student_id]=student , this will give error
    return students[student_id]


#delete method
@app.delete("/delete-student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        return {"Error": "Student does not exist"}

    del students[student_id]
    return {"Message": "Student deleted successfully"}
