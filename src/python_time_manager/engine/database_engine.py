from sqlalchemy.orm import Query
from sqlalchemy.orm.session import Session
from sqlalchemy.schema import Table
from sqlalchemy import inspect
from src.python_time_manager.models import User, Project, Event


class DatabaseEngine:
    """The database engine (not to be confused with the SQLAlchemy engine).

    This class is the driving force behind all database interactions. It
    allows for basic CRUD operations for interacting with database
    """

    __TABLE_STRUCT: dict[str, type[Table]] = {
        "user": User,
        "project": Project,
        "event": Event,
    }

    def __init__(self, session: Session) -> None:
        self.__session = session

    def create(self, table: str, record: dict[str, str]) -> type[Table]:
        """create a new record in target table by passing a dict of column names
        as keys and their associated data as values

        :param table: name of the table to add to
        :type table: str
        :param record: key/value pairing of field with data
        :type record: dict[str, str]
        :return: SQLAlchemy table object containing the record added to table
        :rtype: User | Project | Event
        """
        entry: User | Project | Event = self.__TABLE_STRUCT[table.lower()](**record)  # type: ignore
        self.__session.add(entry)
        self.__session.commit()
        return entry

    def read(self, table: str, ident: str) -> dict[str, str]:
        """return a single result by searching table with id

        :param table: name of the table to search
        :type table: str
        :param ident: the ID of the record to find
        :type ident: str
        :return: the found record containing all fields from table
        :rtype: dict[str, str]
        """
        query = self.__query_results(table=table, ident=ident)
        if query:
            return self._asdict(next(iter(query)))
        return {}

    def update(self):
        pass

    def delete(self, table: str, ident: str):
        query = self.__query_results(table=table, ident=ident)
        if query:
            query.delete()
            self.__session.commit()
            return True
        return False

    def __query_results(self, table: str, ident: str) -> Query[Table]:
        return self.__session.query(self.__TABLE_STRUCT[table.lower()]).filter_by(
            id=ident
        )

    @staticmethod
    def _asdict(obj: Query[Table]) -> dict[str, str]:
        """uses inspect to grab columns + their data and put in a dict"""
        insp = inspect(obj).mapper.column_attrs # type: ignore
        return {c.key: getattr(obj, c.key) for c in insp}
