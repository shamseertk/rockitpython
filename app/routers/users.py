from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.database import get_session
from app.models import User, UserCreate

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[User])
def get_users(session: Session = Depends(get_session)):
    """List all users from the database."""
    users = session.exec(select(User)).all()
    return users

@router.post("/", response_model=User)
def create_user(user_in: UserCreate, session: Session = Depends(get_session)):
    """Create a new user in the database."""
    # Check if a user with that email already exists
    existing_user = session.exec(select(User).where(User.email == user_in.email)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Convert validated input schema (UserCreate) to database model (User)
    db_user = User.model_validate(user_in)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user
