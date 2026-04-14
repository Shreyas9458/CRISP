from pydantic import BaseModel

class UserModel(BaseModel):
    name: str
    last_name: str
    address: str
