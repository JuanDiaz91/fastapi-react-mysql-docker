from pydantic import BaseModel


class UserData(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        from_attributes = True


class UserId(UserData):
    id: int


class TaskData(BaseModel):
    title: str
    user_id: int


class TaskId(TaskData):
    id: int
