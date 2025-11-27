from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DB_URL, DB_SSL_MODE, DEBUG

# Secure Database Connection
connect_args = {}
if 'postgresql' in DB_URL and not DEBUG:
    connect_args['sslmode'] = DB_SSL_MODE

engine = create_engine(DB_URL, connect_args=connect_args, echo=DEBUG)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind=engine)