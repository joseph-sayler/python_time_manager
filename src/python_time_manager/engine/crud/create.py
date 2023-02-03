from sqlalchemy.orm import sessionmaker
from . import TABLE_STRUCT, User, Project, Event  # pylint: disable=E0611


def create(table: str, record: dict[str, str], session: sessionmaker):
    try:
        entry: User | Project | Event = TABLE_STRUCT[table](**record)
        session.add(entry)  # type: ignore
        session.commit()  # type: ignore
        return True
    except Exception as e:  # pylint: disable=W0703, C0103
        print(f"ran into issue adding to database: {e}")
        return False
