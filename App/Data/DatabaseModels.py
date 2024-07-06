from App.Data.Database import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class Zorgverlener(Base):
    __tablename__ = "Zorgverleners"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    name = Column(String(50), nullable=False)
    lastName = Column(String(50), nullable=False)
    email = Column(String(50), unique=False, nullable=False)
    phoneNumber = Column(Integer, nullable=False)
    password = Column(String(50), nullable=False)
    profession = Column(String(50), nullable=False)


class Resultaat(Base):
    __tablename__ = "Resultaten"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    name = Column(String(50), nullable=False)
    date = Column(String(50), nullable=False)
    discription = Column(String(100), unique=False, nullable=False)


class Spiersterkte(Base):
    __tablename__ = "Spiersterkten"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement="auto")
    resultaat_id = Column(ForeignKey("Resultaten.id"), nullable=False)
    spiernaam = Column(String(50), nullable=False)
    spiermyometrie = Column(String(100), unique=False, nullable=False)
