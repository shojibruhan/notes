```bash
pip install sqlalchemy
```

# Models:

models are Python `classes (Blueprints)` that represent database `tables`. They define the structure of the data you want to store in the database and how it should be organized.

> In a word, models are like blueprints for your database tables. They define the structure of the data you want to store and how it should be organized.

### Why called “model”?

Because it models/represents real-world data structure.

### Simple Mapping:

---

```
Model class  ↔  Database table
Object       ↔  Row
Attribute    ↔  Column
```

```python

# This is legacy version

import uuid
from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import UUID
from .database import Base

class User(Base):
    __tablename__= "users"
        id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    name= Column(String, nullable= False)
    age = Column(Integer, nullable= False)
    created_at= Column(
        TIMESTAMP(timezone=True),
        nullable= False,
        server_default=text('now()')
        )
```

```python

# Modern version

from __future__ import annotations
from datetime import datetime, UTC
from sqlalchemy import  Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from dbfile.database import Base


class User(Base):
    __tablename__= "users"

    id: Mapped[int] = mapped_column(Integer, primary_key= True, index= True)
    username: Mapped[str] = mapped_column(String(50), unique= True, nullable= False)
    email: Mapped[str] = mapped_column(String(150), unique= True, nullable= False)
    image_file: Mapped[str | None] = mapped_column(String(200), nullable= True, default= None)
    posts: Mapped[list[Post]]= relationship(back_populates="author")

    @property
    def image_path(self) -> str:
        if self.image_file:
            return f"media/profile_pics/{self.image_file}"
        return f"static/profile_pics/default.jpg"



```

- Mapped: Mapped for python type annotations [Python/type checkers]
- mapped_column: new version of `Column`

```python
name: Mapped[str] = mapped_column(String(50))

mapped_column(String(50)) # Create a VARCHAR(50) column in the database.
name: Mapped[str] # When access user.name, it will be a Python str. It’s about the Python object type.
```

