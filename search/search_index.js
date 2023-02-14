var __index = {"config":{"lang":["en"],"separator":"[\\s\\-]+","pipeline":["stopWordFilter"]},"docs":[{"location":"index.html","title":"Time Manager Docs","text":"<p>This site contains project documentation for the Python Time Manager application.</p> <p>Its aim is to provide a basic application framework to track, edit, store, and print time spent working on projects. It will be able to use multiple front ends and operate in a multi-user environment.</p>"},{"location":"db_engine.html","title":"DatabaseEngine","text":""},{"location":"db_engine.html#src.python_time_manager.engine.database_engine.DatabaseEngine","title":"<code>DatabaseEngine</code>","text":"<p>The DatabaseEngine class is the driving force behind all database interactions. It allows for basic CRUD operations for interacting with database.</p> <p>Attributes:</p> Name Type Description <code>__TABLE_STRUCT</code> <code>dict[str, type[Table]]</code> <p>Data structure mapping string aliases to Table object they represents</p>"},{"location":"db_engine.html#src.python_time_manager.engine.database_engine.DatabaseEngine.__init__","title":"<code>__init__(session)</code>","text":"<p>Parameters:</p> Name Type Description Default <code>session</code> <code>Session</code> <p>SQLAlchemy session object, used to access the current working SQLAlchemy session. This enables all functionality of this class.</p> required"},{"location":"db_engine.html#src.python_time_manager.engine.database_engine.DatabaseEngine.__query_results","title":"<code>__query_results(table, ident)</code>","text":"<p>Common code to query results from database.</p> <p>Examples:</p> <pre><code>&gt;&gt;&gt; # TODO add example\n</code></pre> <p>Parameters:</p> Name Type Description Default <code>table</code> <code>str</code> <p>Name of table to search.</p> required <code>ident</code> <code>str</code> <p>The ID of record to find.</p> required <p>Returns:</p> Type Description <code>Query[Table]</code> <p>Query[Table]: SQLAlchemy object containing results.</p>"},{"location":"db_engine.html#src.python_time_manager.engine.database_engine.DatabaseEngine.asdict","title":"<code>asdict(obj)</code>  <code>staticmethod</code>","text":"<p>Uses inspect to grab columns, plus their data, and put in a dict.</p> <p>Examples:</p> <pre><code>&gt;&gt;&gt; # TODO add example\n</code></pre> <p>Parameters:</p> Name Type Description Default <code>obj</code> <code>Query[Table]</code> <p>The object to inspect.</p> required <p>Returns:</p> Type Description <code>dict[str, str]</code> <p>dict[str, str]: Data from obj returned as key:value pairs.</p>"},{"location":"db_engine.html#src.python_time_manager.engine.database_engine.DatabaseEngine.create","title":"<code>create(table, record)</code>","text":"<p>Create a new record in target table by passing a dict of column names as keys and their associated data as values.</p> <p>Examples:</p> <pre><code>&gt;&gt;&gt; # TODO add example\n</code></pre> <p>Parameters:</p> Name Type Description Default <code>table</code> <code>str</code> <p>The name of the table to add to.</p> required <code>record</code> <code>dict[str, str]</code> <p>A key/value pairing of field with data.</p> required <p>Returns:</p> Type Description <code>type[Table]</code> <p>type[Table]: SQLAlchemy table object containing the record added to table.</p>"},{"location":"db_engine.html#src.python_time_manager.engine.database_engine.DatabaseEngine.delete","title":"<code>delete(table, ident)</code>","text":"<p>Delete a record from target table.</p> <p>Examples:</p> <pre><code>&gt;&gt;&gt; # TODO add example\n</code></pre> <p>Parameters:</p> Name Type Description Default <code>table</code> <code>str</code> <p>Name of table to delete data from.</p> required <code>ident</code> <code>str</code> <p>ID number of the record to delete.</p> required <p>Returns:</p> Name Type Description <code>bool</code> <code>bool</code> <p>Indication of successful deletion.</p>"},{"location":"db_engine.html#src.python_time_manager.engine.database_engine.DatabaseEngine.read","title":"<code>read(table, ident)</code>","text":"<p>Return a single result by searching table with id.</p> <p>Examples:</p> <pre><code>&gt;&gt;&gt; # TODO add example\n</code></pre> <p>Parameters:</p> Name Type Description Default <code>table</code> <code>str</code> <p>Name of the table to search.</p> required <code>ident</code> <code>str</code> <p>The ID of the record to find.</p> required <p>Returns:</p> Type Description <code>dict[str, str]</code> <p>dict[str, str]: The found record containing all fields from table.</p>"},{"location":"db_engine.html#src.python_time_manager.engine.database_engine.DatabaseEngine.update","title":"<code>update(table, ident)</code>","text":"<p>Update a record in target table.</p> <p>Examples:</p> <pre><code>&gt;&gt;&gt; # TODO add example\n</code></pre> <p>Parameters:</p> Name Type Description Default <code>table</code> <code>str</code> <p>Name of the table to update information for.</p> required <code>ident</code> <code>str</code> <p>ID number of record to update.</p> required <p>Returns:</p> Name Type Description <code>bool</code> <code>bool</code> <p>Indication of success of update</p>"},{"location":"model_event.html","title":"Event","text":""},{"location":"model_event.html#src.python_time_manager.models.event.Event","title":"<code>Event</code>","text":"<p>         Bases: <code>Base</code></p> <p>A table that holds information about time entries (events) entered by user for a project. This table is related to the <code>User</code> table through a many-to-one relationship. This means that a single user may have multiple events, but each event is associated with only one user. This relationship is established through the <code>Project</code> table, as each event is linked with a single project, and by association, each project is linked with a single user.</p> <p>Attributes:</p> Name Type Description <code>__tablename__</code> <code>str</code> <p>Name of the table within the database.</p> <code>id</code> <code>Column[str]</code> <p>Primary key field, default value is uuid.uuid4().</p> <code>start_datetime</code> <code>Column[datetime]</code> <p>Event start time field.</p> <code>end_datetime</code> <code>Column[datetime]</code> <p>Event end time field.</p> <code>description</code> <code>Column[str]</code> <p>User specified description of event.</p> <code>created_at</code> <code>Column[datetime]</code> <p>Time the record was created.</p> <code>project_id</code> <code>Column[str]</code> <p>Project ID foreign key field; takes its value from project table id field primary key.</p> <code>project</code> <p>References project.id from Project table. Back populates Project table with event.id.</p>"},{"location":"model_event.html#src.python_time_manager.models.event.Event.__repr__","title":"<code>__repr__()</code>","text":"<p>Displays a string representation of the object. Only displays the id and created_at fields for reference.</p> <p>Returns:</p> Name Type Description <code>str</code> <code>str</code> <p>The id and created_at fields from the respective object attributes.</p>"},{"location":"model_project.html","title":"Project","text":""},{"location":"model_project.html#src.python_time_manager.models.project.Project","title":"<code>Project</code>","text":"<p>         Bases: <code>Base</code></p> <p>A table that holds information about projects.</p> <p>This table is related to the <code>Event</code> table through a one-to-many relationship. This means that a single project can be associated with multiple events, but each <code>Event</code> is associated with only one Project.</p> <p>It is also related to the <code>User</code> table through a many-to-many relationship. This means that a single project can be associated with multiple users. The relationship is established through a join table, <code>ProjectUsers</code>.</p> <p>Attributes:</p> Name Type Description <code>__tablename__</code> <code>str</code> <p>Name of the table within the database.</p> <code>id</code> <code>Column[str]</code> <p>Primary key field, default value is uuid.uuid4().</p> <code>name</code> <code>Column[str]</code> <p>Friendly name of the project.</p> <code>description</code> <code>Column[str]</code> <p>User specified description of project.</p> <code>start_date</code> <code>Column[date]</code> <p>Date project is expected to start.</p> <code>end_date</code> <code>Column[date]</code> <p>Date project is expected to end.</p> <code>status</code> <code>Column[str]</code> <p>Current status of the project.</p> <code>category</code> <code>Column[str]</code> <p>A user-specified value.</p> <code>manager_id</code> <code>Column[str]</code> <p>User ID foreign key field; indicates which user is a manager for project. Takes its value from user table id field primary key.</p> <code>created_at</code> <code>Column[datetime]</code> <p>Time the record was created.</p> <code>users</code> <p>References user.id from User table. Back populates User and ProjectUsers tables with project.id.</p> <code>events</code> <p>References event.id from Event table. Back populates Event table with project.id.</p>"},{"location":"model_project.html#src.python_time_manager.models.project.Project.__repr__","title":"<code>__repr__()</code>","text":"<p>Displays a string representation of the object. Only displays the id and created_at fields for reference.</p> <p>Returns:</p> Name Type Description <code>str</code> <code>str</code> <p>The id and created_at fields from the respective object attributes.</p>"},{"location":"model_project_users.html","title":"ProjectUsers","text":""},{"location":"model_project_users.html#src.python_time_manager.models.project_users.ProjectUsers","title":"<code>ProjectUsers</code>","text":"<p>         Bases: <code>Base</code></p> <p>A joining table that holds information about what users have access to what projects. This models a many-to-many relationship between the <code>User</code> and <code>Project</code> objects.</p> <p>Attributes:</p> Name Type Description <code>__tablename__</code> <code>str</code> <p>Name of the table within the database.</p> <code>user_id</code> <code>Column[str]</code> <p>User ID foreign key field; takes its value from user table id field primary key.</p> <code>project_id</code> <code>Column[str]</code> <p>Project ID foreign key field; takes its value from project table id field primary key.</p>"},{"location":"model_user.html","title":"User","text":""},{"location":"model_user.html#src.python_time_manager.models.user.User","title":"<code>User</code>","text":"<p>         Bases: <code>Base</code></p> <p>A model that represents information about the users table.</p> <p>This table is related to the <code>Project</code> table through a many-to-many relationship. This means that a single user can be associated with multiple projects. The relationship is established through a join table, <code>ProjectUsers</code>.</p> <p>Attributes:</p> Name Type Description <code>__tablename__</code> <code>str</code> <p>Name of the table within the database.</p> <code>id</code> <code>Column[str]</code> <p>Primary key field, default value is uuid.uuid4().</p> <code>username</code> <code>Column[str]</code> <p>Field to hold username.</p> <code>first_name</code> <code>Column[str]</code> <p>Field to hold user first name.</p> <code>last_name</code> <code>Column[str]</code> <p>Field to hold user last name.</p> <code>email</code> <code>Column[str]</code> <p>Field to hold user email.</p> <code>created_at</code> <code>Column[datetime]</code> <p>Time the record was created.</p> <code>projects</code> <p>References project.id from Project table. Back populates Project and ProjectUsers tables with user.id.</p>"},{"location":"model_user.html#src.python_time_manager.models.user.User.__repr__","title":"<code>__repr__()</code>","text":"<p>Displays a string representation of the object. Only displays the id and created_at fields for reference.</p> <p>Returns:</p> Name Type Description <code>str</code> <code>str</code> <p>The id and created_at fields from the respective object attributes.</p>"}]}