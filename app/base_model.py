from sqlalchemy.orm import MappedAsDataclass, DeclarativeBase, declared_attr, Mapped, mapped_column


class Base(MappedAsDataclass, DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, init=False)
