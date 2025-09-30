from pydantic import BaseModel

class AddInputModel(BaseModel):
    a: float
    b: float