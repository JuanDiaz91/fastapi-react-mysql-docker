from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud.user_crud import get_all_users, get_user_by_id, get_user_by_email, create_user
from db.schemas import UserData, UserId
from db.db_session import get_db
from helper.formatter import is_valid_email


router = APIRouter()


@router.get('/api/users', response_model=list[UserId])
async def get_users(db: Session = Depends(get_db)):
    users = get_all_users(db)
    if not users:
        raise HTTPException(status_code=404, detail="No users found")

    return users


@router.get('/users/{user_id:int}/', response_model=UserId)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail='The user is not registered!')

    return user


@router.post('/users/', response_model=UserId)
async def create_new_user(user: UserData, db: Session = Depends(get_db)):
    if not is_valid_email(user.email):
        raise HTTPException(status_code=422, detail='Invalid email format!')

    if get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail='The email already exists; you must enter another one.')
    new_user = create_user(db, user)

    return UserId(id=new_user.id, username=new_user.username, email=new_user.email, password=new_user.password)
