from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///./bank.db", connect_args={"check_same_thread": False})
sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()