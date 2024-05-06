from .. import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Card(Base):
    __tablename__ = "cards"
    number: Mapped[int] = mapped_column(unique=True)
    holder_name: Mapped[str]
    cvv: Mapped[int]
    expiration_month: Mapped[int]
    expiration_year: Mapped[int]