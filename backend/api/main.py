from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import auth, documents, people, projects
from api.routers.entity_facts import router as entity_facts_router
from api.routers.user_preferences import router as user_preferences_router
from api.database import Base, engine, SessionLocal
from api.models import Role

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(people.router)
app.include_router(projects.router)
app.include_router(documents.router)
app.include_router(entity_facts_router)
app.include_router(user_preferences_router)


def seed_default_roles() -> None:
    db = SessionLocal()
    try:
        for role_name in ("User", "Admin"):
            existing_role = db.query(Role).filter(Role.role_name == role_name).first()
            if not existing_role:
                db.add(Role(role_name=role_name))
        db.commit()
    finally:
        db.close()


seed_default_roles()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return "Health check complete"