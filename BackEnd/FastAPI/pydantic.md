# BaeseModel

```python
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
    in_stock: bool

```

> A powerful data-validation class that turns raw input data into safe, structured Python objects.
>
> BaseModel is a smart blueprint for data. A smart form checker.
>
> In FastAPI/Pydantic, a class that inherits from Pydantic BaseModel is commonly called a schema/structure for data.

It checks:

- Is name text? ✅
- Is price float? ✅ (converted)
- Is in_stock boolean? ✅ (converted)
- Missing anything? ❌
- Invalid data? ❌

Then it gives clean validated data.  
When you create a class using BaseModel, Pydantic gives your class superpowers like:

- data validation
- type checking
- automatic conversion
- JSON conversion
- error handling

Normal Python Class

```python
class User:
    def __init__(self, age):
        self.age = age

class User(BaseModel):
    age: int
```

### 1. Type validation

```python
User(age="hello")

ValidationError

# Type ValidationError: value is not a valid integer (type=type_error.integer)
```

### 2. Automatic Conversion

```python
User(age="25")

age = 25 # "25" is automatically converted to 25
```

### 3. Required Fields

```python
class User(BaseModel):
    name: str
    age: int

User(name="Ruhan")

# Error: age field required
```

### 4. JSON Conversion

```python
user = User(name="Ruhan", age=25)
print(u.model_dump())

{
    'name': 'Ruhan',
    'age': 25
}
```

### 5. API Request Validation in FastAPI

```python
class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: User):
    return user

# client sends POST /users with JSON body

 {
    "name": "Ruhan",
    "age": "25"
}


```

Pydantic automatically:

- validates
- converts
- creates Python object

Pydantic automatically:

```python
class User(BaseModel):
    name: str
    age: int
```

Pydantic internally acts like:

```
Incoming data
      ↓
Check fields
      ↓
Check types
      ↓
Convert types if possible
      ↓
Raise error if invalid
      ↓
Create clean Python object

```

## Config Class:

configure/customize how Pydantic models behave. A special settings for this schema.  
Allow this schema to read data from object attributes (like SQLAlchemy models), not just dictionaries.

```python

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

        # old name for from_attributes
        # orm_mode = True
```

Usually Pydantic expects data like this: `dictionary-style data`

```python
{
    "id": 1,
    "email": "a@gmail.com"
}
```

But in SQLAlchemy or FastAPI, database rows are often objects like this: `attribute-style data`

```python
user.id
user.email
```

With `from_attributes = True`, Pydantic can also accept data like this: object-style data.  
So it can convert ORM/database objects into response schemas.

When, `from_attributes=True` Pydantic can work with both dictionary-style and attribute-style data.

So before: pydantic only accepted dictionary-style data, but now it can also accept attribute-style data.

**New style (Pydantic v2)**

```python
from pydantic import ConfigDict

model_config = ConfigDict(from_attributes=True)
```

# Best Practices for validation:

- Always return a value even you didn't modify it. Don't return None.

- raise ValueError for ValidationError. Pydantic will catch it and convert it into a proper error response(ValidationError).
