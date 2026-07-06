# SQLAlchemy library se database engine banane ka function import
from sqlalchemy import create_engine

# Base class banane ke liye import
# is Base ko use karke hum database tables/models banayenge
from sqlalchemy.ext.declarative import declarative_base

# Database sessions create karne ke liye import
from sqlalchemy.orm import sessionmaker


# DATABASE URL
# sqlite database use ho raha hai
# ids.db naam ki database file database folder me banegi

DATABASE_URL = "sqlite:///./database/ids.db"


# Engine create karna
# engine database aur Python ke beech connection banata hai

engine = create_engine(

    DATABASE_URL,

    # SQLite multi-thread issue avoid karne ke liye
    # FastAPI me multiple requests aa sakti hain
    connect_args={"check_same_thread": False}
)


# Session factory create karna
# SessionLocal se database session/object banega

SessionLocal = sessionmaker(

    # Automatically commit nahi karega
    # manually db.commit() karna padega
    autocommit=False,

    # Changes automatically flush nahi honge
    autoflush=False,

    # Kis database engine ko use karna hai
    bind=engine
)


# Base class create karna
# iske through hum database tables/models banayenge

Base = declarative_base()