from sqlalchemy import create_engine
from sqlalchemy.orm  import sessionmaker,declarative_base

DATABASE_URL="sqlite:///./users.db"
engine=create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
session=sessionmaker(bind=engine,autoflush=False,autocommit=False)
Base=declarative_base()

#Dependency injection
def get_db():  #depends
    db=session()
    try:
        yield db
    except Exception as ex:
        print("Exception occured in get_db()",ex)
    finally:
        db.close()
        
