from pydantic import BaseModel


class CreateUnknown(BaseModel):
    id: int
    name: str
    year: str
    color: str
    pantone_value: str