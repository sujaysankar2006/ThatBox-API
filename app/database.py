from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

#create db url
DATABASE_URL = "sqlite:///./thatbox.db"

#create engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)

#create session
SessionLocal = sessionmaker(
    bind = engine,
    autoflush= False,
    expire_on_commit= False
)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
       yield  db
    finally:
        db.close()



""" 
which is the engine of db use of sqlalchemy 
sqlalchemy.orm means object relation method which accpet the object then it turn into query for db 
essential things in db:
                   1. import sqlalchemy module and orm 
                   2. create a db url 
                   3. create or establish engine use of db url 
                   3. create session which means dedicated period of time that bind the engine
                   4.create a db object and pass arg as decalrative base
                   5. start db 



"""