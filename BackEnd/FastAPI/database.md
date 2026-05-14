# PostgresSQL with FastAPI

```python

❌ # Method 1: Using psycopg2 (raw SQL queries)

pip install psycopg2-binary

import psycopg2
from psycopg2.extras import RealDictCursor

while True:
    try:
        db= psycopg2.connect(
            host= 'localhost',
            database= 'fastapi',
            user= 'postgres',
            password= '1234',
            cursor_factory=RealDictCursor
        )
        cursor= db.cursor()
        print("🟢 Successfully Connected to the Database!!!")
        break
    except Exception as error:
        print("❌ Error: Can't Connect to Database ❌")
        print("Error details:", error)

```

`RealDictCursor` makes PostgreSQL query results behave like dictionaries instead of tuples, so data is easier to use in APIs.

```python
cursor.execute("SELECT id, name FROM users")
print(cursor.fetchone())

# Output:
(1, 'Ruhan')

from psycopg2.extras import RealDictCursor

cursor = db.cursor(cursor_factory=RealDictCursor)
cursor.execute("SELECT id, name FROM users")

print(cursor.fetchone())

# Output:
{
    'id': 1,
    'name': 'Ruhan'
}

```

```python
cursor.execute("INSERT INTO users (name) VALUES ('Ruhan') RETURNING id, name")
new_user= cursor.fetchone()
db.commit()  # save changes to the database
return {
    "new User": new_user
}

```

Converts database rows into Python dictionaries instead of tuples.

# Object-Relational Mapping (ORM): sqlalchemy

```bash
!pip install sqlalchemy
```

```python

✅ # Method 2: Using SQLAlchemy (ORM)

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

SQLALCHEMY_DATABASE_URL= 'postgresql://postgres:1234@localhost/fastapi'

engine= create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal= sessionmaker(autocommit= False, autoflush=False, bind= engine)

Base= declarative_base()

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()

```

1. `create_engine`:

   This function creates a connection to the database. You provide a connection string that specifies the
   - database type
   - username
   - password
   - host
   - database name

   ```python
   DATABASE_URL = "postgresql://postgres:1234@localhost/database_name"

   engine = create_engine(DATABASE_URL)
   ```

2. `declarative_base`:

   ```python
   Base = declarative_base()

    # Any class inheriting from this Base is a database table.

    # without Base:
   class User:
    pass
    # A normal Python class that can’t talk to the database.


    class User(Base):
        __tablename__ = "users"

    # User → becomes a database model/table
   ```

   Now SQLAlchemy understands:
   - create table
   - map columns
   - query data
   - ORM features

   Think of Base like: a “database model stamp”. Any class stamped with it becomes a database table model.

   `declarative_base()` in SQLAlchemy creates a special parent class for all your database models.

   This function creates a base class for your database models. You will inherit from this base class to define your tables.

   ```python
   Base = declarative_base()

   # models.py file
   from .database import Base
   class User(Base):
       __tablename__= "users"
       id= Column(Integer, primary_key=True, index= True)
       name= Column(String, nullable= False)
       age= Column(Integer, nullable= False)
   ```

   `declarative_base()` creates the parent class that turns normal Python classes into SQLAlchemy database models.

3. `sessionmaker`:

   making database sessions whenever needed.

   This function creates a factory for database sessions. A session is used to interact with the database, allowing you to execute queries and manage transactions.
   - Factory = something that creates objects.

     Car factory → creates cars  
      Session factory → creates sessions

   ```python
   SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
   ```

   ## Simple Mental Model

   | Thing          | Real-life analogy    |
   | -------------- | -------------------- |
   | `sessionmaker` | coffee machine       |
   | `Session`      | actual cup of coffee |

- `bind=engine`: connect sessions to this database engine. Tells the sessionmaker which database to connect to. Without it, sessions wouldn’t know which database to use.

- `autocommit=False`: don’t save changes automatically. You have to call `db.commit()` to save changes. This gives you control over when to save data.

- `autoflush=False`: don’t send temporary changes to the database automatically. You have to call `db.flush()` to send changes. This can help with performance and control over when data is sent to the database.

  ## Sample Mental Model

  | Setting            | Meaning                                    |
  | ------------------ | ------------------------------------------ |
  | `bind=engine`      | which DB to connect                        |
  | `autocommit=False` | don’t save automatically                   |
  | `autoflush=False`  | don’t send temporary changes automatically |

4. Session: This is the class used to create a session instance. You will use this session to perform database operations.

   Session: A temporary conversation/workspace between your Python app and the database.

   Used for:
   - add data
   - update data
   - delete data
   - commit changes

   ```python
   def get_db():
       db = SessionLocal()
       try:
           yield db
       finally:
           db.close()
   ```

   In this example, `get_db` is a `dependency function` that creates a new database session for each request and ensures that the session is closed after the request is completed. You can use this function in your FastAPI routes to access the database.

   `db = SessionLocal()`. Now db is a session.

   Now anyone can use this session to talk to the database.

   ```python
   db.add(user)
   db.commit()
   db.query(User).all()
   ```

   Think of a session like: A waiter taking your orders to the database restaurant.

   | Setting            | Meaning                                    |
   | ------------------ | ------------------------------------------ |
   | `bind=engine`      | which DB to connect                        |
   | `autocommit=False` | don’t save automatically                   |
   | `autoflush=False`  | don’t send temporary changes automatically |

   ```python
   from fastapi import Depend


   @app.get("/users/{user_id}")
   def read_user(user_id: int, db: Session = Depends(get_db)):
       user = db.query(User).filter(User.id == user_id).first()

       if user is None:
           raise HTTPException(status_code=404, detail="User not found")

       return user
   ```

In this route, we use the get_db dependency to get a database session. We then query the User model to find a user with the specified user_id. If the user is not found, we raise an HTTPException with a 404 status code. If the user is found, we return the user object.

# Simple Mental Model

```
create_engine      → connects to DB
declarative_base   → creates model base
sessionmaker       → creates sessions
Session            → talks to DB
```

# Depends: Dependency Injection

FastAPI injects/provides required things automatically. Tells FastAPI to automatically run another function and inject its result into your route function.

Examples:

- DB session
- current user
- auth check
- permissions
- settings

> `Dependency Injection` means automatically providing required objects/functions instead of manually creating them inside the code.

```python
from fastapi import Depends

@app.post("/users")
def create_user(user: User, db: Session= Depends(get_db)):
    pass
# Depends means: “Before running this function(create_user), first run another function (get_db) and give me its result.”

# get_db() → creates a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

```

# MongoDB with FastAPI

source: [medium](https://medium.com/@ChanakaDev/mongodb-with-fastapi-1d5440880520)

```bash
# pip install pymongo
# Install Motor (the async driver for MongoDB)
!pip install motor

# Optional: Install Beanie (an ODM for easier model management)
!pip install beanie
```
