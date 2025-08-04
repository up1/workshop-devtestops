from typing import List

from db import models, schemas
from db.database import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/post", response_model=List[schemas.CreateUser])
def test_posts(db: Session = Depends(get_db)):
    posts = db.query(models.User).all()
    return posts


@router.post(
    "/create", status_code=status.HTTP_201_CREATED, response_model=schemas.CreateUser
)
def create_posts(post: schemas.CreateUser, db: Session = Depends(get_db)):
    new_post = models.User(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post


@router.get("/{user_id}", response_model=schemas.CreateUser)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    db.commit()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# Get first 10 users
@router.get("/", response_model=List[schemas.CreateUser])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).limit(10).all()
    db.commit()
    return users
