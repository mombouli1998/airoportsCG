### Configuration for the database connection
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

SQLITE_DATABASE_URL = "sqlite:///airportsCongo.db"
engine = create_engine(SQLITE_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

##TESTING
if __name__ == "__main__":
    # Test the database connection
    try:
        with engine.connect() as session:
            print("Database connection successful.")
    except Exception as e:
        print(f"Database connection failed: {e}")