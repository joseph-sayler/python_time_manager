import uuid
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import Column, String, ForeignKey


"""
these models represent database tables. they are set up to have relationships between them. each relationship is defined by the relationship() function and a foreign key attribute. note that the main table here is the User table (aka 'users'). from here you can find all other data. but you can also do some complex queries based on what events or projects you want to look at.

note that the foreign keys listed in Project and Event are NULLABLE meaning you can have 0 of them. but you must have a user.

"""


Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()))
    name = Column(String)
    projects = relationship(
        "Project",
        back_populates="users",
        lazy="dynamic",
        cascade="all, delete-orphan",
        single_parent=True,
    )
    events = relationship(
        "Event",
        back_populates="user",
        lazy="dynamic",
        cascade="all, delete-orphan",
        single_parent=True,
    )

    def __repr__(self):
        return f"User: id={self.id}, name={self.name}"


class Project(Base):
    __tablename__ = "projects"
    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()))
    name = Column(String)
    user_id = Column(String(36), ForeignKey("users.id"))
    users = relationship("User", back_populates="projects")
    events = relationship("Event", back_populates="project")

    def __repr__(self):
        return f"Project: id={self.id}, user_id={self.user_id}, name={self.name}"


class Event(Base):
    __tablename__ = "events"
    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()))
    user_id = Column(String(36), ForeignKey("users.id"), nullable=True)
    project_id = Column(String(36), ForeignKey("projects.id"), nullable=True)
    user = relationship("User", back_populates="events")
    project = relationship("Project", back_populates="events")

    def __repr__(self):
        return (
            f"Event: id={self.id}, user_id={self.user_id}, project_id={self.project_id}"
        )
