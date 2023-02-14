import uuid


def _generate_uuid() -> str:
    """Simple function to create a string UUID using Python's UUID library.

    Placing the uuid.uuid4() function call inside this function allows SQLAlchemy to use UUIDs in string form as a default value for primary keys, as used by the models in this library.

    Returns:
        str: UUID cast as a string, used as primary keys for tables.
    """
    return str(uuid.uuid4())
