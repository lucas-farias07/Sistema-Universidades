import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import psycopg2



engine = db.create_engine(
    "postgresql+psycopg2://postgres:controle34@localhost:5432/university",
    echo=False
)

Session = sessionmaker(engine)
session = Session()

StudentsRegistration = db.Table("StudentsRegistration", db.MetaData(), autoload_with=engine)
Courses = db.Table("Courses", db.MetaData(), autoload_with=engine)
Subjects = db.Table("Subjects", db.MetaData(), autoload_with=engine)
Teachers = db.Table("Teachers", db.MetaData(), autoload_with=engine)

#COLOR CODES
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"
