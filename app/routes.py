from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Project, Task
from app.schemas import ProjectCreate, ProjectResponse, TaskSchema
from app.services import generate_tasks

router = APIRouter()


@router.post("/projects/", response_model=ProjectResponse)
async def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    db_project = Project(project_name=project.project_name, location=project.location, status="processing")
    db.add(db_project)
    db.commit()
    db.refresh(db_project)

    tasks = await generate_tasks(project.project_name, project.location)
    for task in tasks:
        db_task = Task(name=task["name"], project_id=db_project.id)
        db.add(db_task)
    db.commit()
    return db_project


@router.get("/projects/{project_id}", response_model=ProjectResponse)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    return ProjectResponse(
        id=project.id,
        project_name=project.project_name,
        location=project.location,
        status=project.status,
        tasks=[TaskSchema(name=t.name, status=t.status) for t in project.tasks]
    )
