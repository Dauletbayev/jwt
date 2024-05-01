from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str | None
    full_name: str | None

class UserInDb(BaseModel):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class RokenData(BaseModel):
    username: str | None = None
