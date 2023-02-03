from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.python_time_manager.models import User, Project, Event


# create a SQLite database connection
# SQLITE_CONNECTION_STRING = "sqlite:///:memory:"
SQLITE_CONNECTION_STRING = "sqlite:///database/test/test.sqlite"

# this connects you to the database
engine = create_engine(SQLITE_CONNECTION_STRING, future=True)

# this required to create the database using metadata (ie the models)
# not needed if only accessing an existing one (for all CRUD operations)
# Base.metadata.create_all(engine) # remember to import Base from models file first

# handles session context or manager or something; makes it easier to handle adding and querying
Session = sessionmaker(bind=engine)
session = Session()

# main commands to add and query information
test_user: User = User(name="testUser", projects=[], events=[])  # type: ignore
session.add(test_user)
session.commit()
session.query(User).all()

test_project: Project = Project(name="project1", user_id="9a2dbf01-48fc-4037-bfd4-f58eedc28785")
session.add(test_project)
session.commit()
session.query(Project).all()

test_event: Event = Event(
    project_id="800ab79a-6125-49d7-b6a4-ee178e1f2cbf",
    user_id="9a2dbf01-48fc-4037-bfd4-f58eedc28785",
)
session.add(test_event)
session.commit()
session.query(Event).all()

###

test_user2: User = User(name="user2", projects=[], events=[])  # type: ignore
session.add(test_user2)
session.commit()
session.query(User).all()
