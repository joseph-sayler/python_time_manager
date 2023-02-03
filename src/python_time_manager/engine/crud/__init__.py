from src.python_time_manager.models import User, Project, Event


TABLE_STRUCT: dict[str, User | Project | Event] = {
    "user": User,
    "project": Project,
    "event": Event,
}
