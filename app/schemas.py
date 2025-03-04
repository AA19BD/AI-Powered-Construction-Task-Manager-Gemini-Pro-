from pydantic import BaseModel
from typing import List


class ProjectCreate(BaseModel):
    project_name: str
    location: str


class TaskSchema(BaseModel):
    name: str
    status: str


class ProjectResponse(BaseModel):
    id: int
    project_name: str
    location: str
    status: str
    tasks: List[TaskSchema]
