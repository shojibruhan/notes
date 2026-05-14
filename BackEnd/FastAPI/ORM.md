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
