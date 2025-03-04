import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.database import SessionLocal
from app.models import Task
from app.routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(complete_tasks())
    yield None
    task.cancel()


app = FastAPI(lifespan=lifespan)
app.include_router(router)


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"message": "An internal error occurred."}
    )


async def complete_tasks():
    while True:
        db = SessionLocal()
        tasks = db.query(Task).filter(Task.status == "pending").all()
        if tasks:
            task = tasks[0]
            task.status = "completed"
            db.commit()
        db.close()
        await asyncio.sleep(10)
