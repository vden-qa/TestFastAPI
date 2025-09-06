from sqlalchemy.orm import Mapped, mapped_column
from app.base_model import Base


class User(Base):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(unique=False)
    first_name: Mapped[str] = mapped_column(unique=False)
    last_name: Mapped[str] = mapped_column(unique=False)
    avatar: Mapped[str] = mapped_column(unique=False)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
