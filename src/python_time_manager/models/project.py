# pylint: skip-file

from ..engine._gen_uuid import _generate_uuid

from . import (
    Base,
    Column,
    String,
    Date,
    date,
    datetime,
    relationship,
    ForeignKey,
    DateTime,
    func,
)


class Project(Base):
    """A table that holds information about projects.

    This table is related to the `Event` table through a one-to-many relationship. This means that a single project can be associated with multiple events, but each `Event` is associated with only one Project.

    It is also related to the `User` table through a many-to-many relationship. This means that a single project can be associated with multiple users. The relationship is established through a join table, `ProjectUsers`.

    Attributes:
        __tablename__: Name of the table within the database.
        id: Primary key field, default value is uuid.uuid4().
        name: Friendly name of the project.
        description: User specified description of project.
        start_date: Date project is expected to start.
        end_date: Date project is expected to end.
        status: Current status of the project.
        category: A user-specified value.
        manager_id: User ID foreign key field; indicates which user is a manager for project. Takes its value from user table id field primary key.
        created_at: Time the record was created.
        users: References user.id from User table. Back populates User and ProjectUsers tables with project.id.
        events: References event.id from Event table. Back populates Event table with project.id.
    """

    __tablename__: str = "project"

    id: Column[str] = Column(String(36), primary_key=True, default=_generate_uuid)
    name: Column[str] = Column(String(250), nullable=False)
    description: Column[str] = Column(String(512), nullable=True)
    start_date: Column[date] = Column(Date, nullable=True)
    end_date: Column[date] = Column(Date, nullable=True)
    status: Column[str] = Column(String(250))
    category: Column[str] = Column(String(250))
    manager_id: Column[str] = Column(String(36), ForeignKey("user.id"), nullable=True)
    created_at: Column[datetime] = Column(DateTime, default=func.now(), nullable=False)

    # setting the type annotation with a generic such as Any will result in
    # errors as SQLAlchemy can use the type annotation to learn more about
    # the relationship; to remedy, put name of table in square brackets
    # instead of Any; however, due to potential circular imports, I have
    # chosen to leave the annotation off entirely, which is perfectly valid
    # and causes no issues at all

    users = relationship("User", secondary="project_users", back_populates="projects")
    events = relationship("Event", back_populates="project")

    def __repr__(self) -> str:
        """Displays a string representation of the object. Only displays the id and created_at fields for reference.

        Returns:
            str: The id and created_at fields from the respective object attributes.
        """
        return f"Project: id={self.id}, created_at={self.created_at}"
