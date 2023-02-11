# pylint: skip-file

from . import (
    Base,
    Column,
    String,
    ForeignKey,
)


# to have data added to this table automatically, you must add the project to a user or a user to a project
# do NOT add a user or project directly to the other table
class ProjectUsers(Base):
    """A joining table that holds information about what users have access to what projects. This models a many-to-many relationship between the `User` and `Project` objects.

    Attributes:
        __tablename__: Name of the table within the database.
        user_id: User ID foreign key field; takes its value from user table id field primary key.
        project_id: Project ID foreign key field; takes its value from project table id field primary key.
    """

    __tablename__: str = "project_users"

    user_id: Column[str] = Column(String(36), ForeignKey("user.id"), primary_key=True)
    project_id: Column[str] = Column(
        String(36), ForeignKey("project.id"), primary_key=True
    )
