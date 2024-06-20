from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLAlchemy_DATABASE_URL = 'mariadb+mariadbconnector://Yurr:YurrPassword@163.123.183.82:10025/B2C6'

engine = create_engine(SQLAlchemy_DATABASE_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()