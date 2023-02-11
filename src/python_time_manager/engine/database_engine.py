# pylint: skip-file

from sqlalchemy.orm import Query
from sqlalchemy.orm.session import Session
from sqlalchemy.schema import Table
from sqlalchemy import inspect
from src.python_time_manager.models import User, Project, Event


class DatabaseEngine:
    """The DatabaseEngine class is the driving force behind all database interactions. It
    allows for basic CRUD operations for interacting with database.

    Attributes:
        __TABLE_STRUCT: Data structure mapping string aliases to Table object they represents
    """

    __TABLE_STRUCT: dict[str, type[Table]] = {
        "user": User,
        "project": Project,
        "event": Event,
    }

    def __init__(self, session: Session) -> None:
        """
        Args:
            session (Session): SQLAlchemy session object, used to access the current working SQLAlchemy session. This enables all functionality of this class.
        """
        self.__session = session

    def create(self, table: str, record: dict[str, str]) -> type[Table]:
        """Create a new record in target table by passing a dict of column names
        as keys and their associated data as values.

        Examples:
            >>> # TODO add example

        Args:
            table (str): The name of the table to add to.
            record (dict[str, str]): A key/value pairing of field with data.

        Returns:
            type[Table]: SQLAlchemy table object containing the record added to table.
        """
        entry: User | Project | Event = self.__TABLE_STRUCT[table.lower()](**record)  # type: ignore
        self.__session.add(entry)
        self.__session.commit()
        return entry  # type: ignore

    def read(self, table: str, ident: str) -> dict[str, str]:
        """Return a single result by searching table with id.

        Examples:
            >>> # TODO add example

        Args:
            table (str): Name of the table to search.
            ident (str): The ID of the record to find.

        Returns:
            dict[str, str]: The found record containing all fields from table.
        """
        query: Query[Table] = self.__query_results(table=table, ident=ident)
        if query:
            return self.asdict(next(iter(query)))
        return {}

    def update(self, table: str, ident: str) -> bool:
        """Update a record in target table.

        Examples:
            >>> # TODO add example

        Args:
            table (str): Name of the table to update information for.
            ident (str): ID number of record to update.

        Returns:
            bool: Indication of success of update
        """
        query = self.__query_results(table=table, ident=ident)
        if query:
            # TODO do something # pylint
            return True
        return False

    def delete(self, table: str, ident: str) -> bool:
        """Delete a record from target table.

        Examples:
            >>> # TODO add example

        Args:
            table (str): Name of table to delete data from.
            ident (str): ID number of the record to delete.

        Returns:
            bool: Indication of successful deletion.
        """
        query = self.__query_results(table=table, ident=ident)
        if query:
            query.delete()
            self.__session.commit()
            return True
        return False

    def __query_results(self, table: str, ident: str) -> Query[Table]:
        """Common code to query results from database.

        Examples:
            >>> # TODO add example

        Args:
            table (str): Name of table to search.
            ident (str): The ID of record to find.

        Returns:
            Query[Table]: SQLAlchemy object containing results.
        """
        return self.__session.query(self.__TABLE_STRUCT[table.lower()]).filter_by(
            id=ident
        )

    @staticmethod
    def asdict(obj: Query[Table]) -> dict[str, str]:
        """Uses inspect to grab columns, plus their data, and put in a dict.

        Examples:
            >>> # TODO add example

        Args:
            obj (Query[Table]): The object to inspect.

        Returns:
            dict[str, str]: Data from obj returned as key:value pairs.
        """
        insp = inspect(obj).mapper.column_attrs  # type: ignore
        return {c.key: getattr(obj, c.key) for c in insp}
