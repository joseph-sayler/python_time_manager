# pylint: skip-file

from . import (
    Base,
    Column,
    String,
    datetime,
    Relationship,
    Any,
    relationship,
    ForeignKey,
    DateTime,
    uuid,
    func,
)

class Event(Base):
    """A table that holds information about time entries (events) entered by user for a project. This table is related to the `User` table through a many-to-one relationship. This means that a single user may have multiple events, but each event is associated with only one user. This relationship is established through the `Project` table, as each event is linked with a single project, and by association, each project is linked with a single user.

    Attributes:
        __tablename__: Name of the table within the database.
        id: Primary key field, default value is uuid.uuid4().
        start_datetime: Event start time field.
        end_datetime: Event end time field.
        description: User specified description of event.
        created_at: Time the record was created.
        project_id: Project ID foreign key field; takes its value from project table id field primary key.
        project: References project.id from Project table. Back populates Project table with event.id.
    """

    __tablename__: str = "event"

    id: Column[str] = Column(String(36), primary_key=True, default=str(uuid.uuid4()))
    start_datetime: Column[datetime] = Column(DateTime, nullable=True)
    end_datetime: Column[datetime] = Column(DateTime, nullable=True)
    description: Column[str] = Column(String(250), nullable=True)
    created_at: Column[datetime] = Column(DateTime, default=func.now(), nullable=False)
    project_id: Column[str] = Column(String(36), ForeignKey("project.id"))

    project: Relationship[Any] = relationship("Project", back_populates="events")

    def __repr__(self) -> str:
        """Displays a string representation of the object. Only displays the id and created_at fields for reference.

        Returns:
            str: The id and created_at fields from the respective object attributes.
        """
        return f"Event: id={self.id}, created_at={self.created_at}"
