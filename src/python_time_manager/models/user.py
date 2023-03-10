# pylint: skip-file

from ..engine._gen_uuid import _generate_uuid

from . import (
    Base,
    Column,
    String,
    datetime,
    relationship,
    DateTime,
    func,
)


class User(Base):
    """A model that represents information about the users table.

    This table is related to the `Project` table through a many-to-many relationship. This means that a single user can be associated with multiple projects. The relationship is established through a join table, `ProjectUsers`.

    Attributes:
        __tablename__: Name of the table within the database.
        id: Primary key field, default value is uuid.uuid4().
        username: Field to hold username.
        first_name: Field to hold user first name.
        last_name: Field to hold user last name.
        email: Field to hold user email.
        created_at: Time the record was created.
        projects: References project.id from Project table. Back populates Project and ProjectUsers tables with user.id.
    """

    __tablename__: str = "user"

    id: Column[str] = Column(String(36), primary_key=True, default=_generate_uuid)
    username: Column[str] = Column(String)
    first_name: Column[str] = Column(String)
    last_name: Column[str] = Column(String)
    email: Column[str] = Column(String)
    created_at: Column[datetime] = Column(DateTime, default=func.now(), nullable=False)

    # setting the type annotation with a generic such as Any will result in
    # errors as SQLAlchemy can use the type annotation to learn more about
    # the relationship; to remedy, put name of table in square brackets
    # instead of Any; however, due to potential circular imports, I have
    # chosen to leave the annotation off entirely, which is perfectly valid
    # and causes no issues at all

    projects = relationship(
        "Project", secondary="project_users", back_populates="users"
    )
    events = relationship("Event", back_populates="user")

    def __repr__(self) -> str:
        """Displays a string representation of the object. Only displays the id and created_at fields for reference.

        Returns:
            str: The id and created_at fields from the respective object attributes.
        """
        return f"User: id={self.id}, created_at={self.created_at}"
