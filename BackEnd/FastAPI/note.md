# `__init__.py` in FastAPI

`__init__.py` is a special file used to tell Python: "Hey, this directory should be treated as a package(part of the codebase)." It can be empty or contain initialization code for the package.

In FastAPI projects, it helps organize your code into modules and submodules, making it easier to manage and import components across your application.

Why it exists
Makes a directory importable as a module
Allows you to use imports like:

```python
from app.models import user
```

```
Need imports / structure → use __init__.py
Just normal folder → not needed
__init__.py makes a folder behave like a Python package so it can be imported properly.

```

# `Base.metadata.create_all(bind=engine)`

```python
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    Base.metadata.create_all(bind=engine)
```

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name VARCHAR
);
```

## Break It Down

1. Base:
   ```python
   Base = declarative_base()
   ```
   Base keeps track of all model classes.
   ```python
   class User(Base):
       # Now User is registered inside Base.
   ```
2. metadata: A collection of table blueprints.

   Metadata is like a catalog of all the tables and their structures that you have defined using Base. It knows about all your models and how they map to the database.

   It contains:
   - table names
   - columns
   - data types
   - constraints

3. create_all(): Create all tables in the database.

   SQLAlchemy checks:

   does table already exist?
   - YES → skip
   - NO → create it

   A method that creates tables in the database based on the models defined in Base.

   When you call `Base.metadata.create_all(bind=engine)`, SQLAlchemy looks at all the models you've defined (like User) and generates the corresponding SQL commands to create those tables in the database.

# `model_dump()`

model_dump() `converts` validated data (Pydantic model) → `dict`

`**` => “Unpack this dictionary into named arguments.”

basically means:

"Give me all model data as a dictionary."

“Unpack this dictionary into named arguments.”

```python
class UserCreate(BaseModel):
    email: str
    password: str

user = UserCreate(
    email="john@test.com",
    password="1234"
)

user.model_dump()

# output:
{
    "email": "john@test.com",
    "password": "1234"
}

# ** is called dictionary unpacking. It takes a dictionary and unpacks its key-value pairs into keyword arguments for a function or constructor.

data = {
    "email": "john@test.com",
    "password": "1234"
}

UserModel(**data)

UserModel(
    email="john@test.com",
    password="1234"
)
```

# Route

```python
from fastapi import APIRouter

router = APIRouter(
    prefix="/users", # all routes in this router will start with /users
    tags=["users"] # for documentation
)

@router.post("/users/")
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    # logic to create user
    return user
```

```python
from fastapi import FastAPI
from .routers import user # import the router from routers directory

app = FastAPI()

app.include_router(user.router)
```

# Query & Search

```python
from typing import Optional

@app.get("/")
def get_items(current_user: User= Depends(get_current_user), db= Session= Depends(get_db), limit: int= 10, skip: int =0, search: Optional[str] = ""):
    items= db.query(models.Item).filter(models.Item.user_id == current_user.id).filter(models.Item.name.contains(search)).offset(skip).limit(limit).all()



```

# Error Handling in FastAPI

```python
from fastapi import FastAPI, HTTPException, status


@app.get("/items/{item_id}", status_code=status.HTTP_200_OK)
def read_item(item_id: int):
    if item_id == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found")
    return {
        "item_id": item_id,
        "message": "Item retrieved successfully"
        }
```
