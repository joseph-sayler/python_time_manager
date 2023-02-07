# pylint: skip-file

import uuid
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import Column, String, ForeignKey, DateTime, Date, func


Base = declarative_base()

"""

these classes demonstrate the relationship between tables:

    The User table is related to the Project table through a many-to-many relationship. This means that a single User can be associated with multiple Projects, and a single Project can be associated with multiple Users. This relationship is established through a join table, ProjectUsers.

    The Project table is related to the Event table through a one-to-many relationship. This means that a single Project can be associated with multiple Events, but each Event is associated with only one Project.

    The Event table is related to the User table through a many-to-one relationship. This means that multiple Events can be associated with a single User, but each Event is associated with only one User. This relationship is established through the Project table, as each Event is associated with a single Project, and each Project is associated with a single User.

"""


class User(Base):
    __tablename__ = "user"

    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()))
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    created_at = Column(DateTime, default=func.now(), nullable=False)

    projects = relationship(
        "Project", secondary="project_users", back_populates="users"
    )

    def __repr__(self):
        return f"User: id={self.id}, created_at={self.created_at}"


class Project(Base):
    __tablename__ = "project"

    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()))
    name = Column(String(250), nullable=False)
    description = Column(String(512), nullable=True)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    status = Column(String(250))
    category = Column(String(250))
    manager_id = Column(String(36), ForeignKey("user.id"), nullable=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)

    users = relationship("User", secondary="project_users", back_populates="projects")
    events = relationship("Event", back_populates="project")

    def __repr__(self):
        return f"Project: id={self.id}, created_at={self.created_at}"


# to have data added to this table automatically, you must add the project to a user or a user to a project
# do NOT add a user or project directly to the other table
class ProjectUsers(Base):
    __tablename__ = "project_users"

    user_id = Column(String(36), ForeignKey("user.id"), primary_key=True)
    project_id = Column(String(36), ForeignKey("project.id"), primary_key=True)


class Event(Base):
    __tablename__ = "event"

    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()))
    start_datetime = Column(DateTime, nullable=True)
    end_datetime = Column(DateTime, nullable=True)
    description = Column(String(250), nullable=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    project_id = Column(String(36), ForeignKey("project.id"))

    project = relationship("Project", back_populates="events")

    def __repr__(self):
        return f"Event: id={self.id}, created_at={self.created_at}"
