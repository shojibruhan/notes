# Hash password

```bash
!pip install "pwdlib[argon2]"
```

```python
from pwdlib import passwordHash

password_hash= passwordHash.recomended()

# create a hashed password
def hash_password(password: str) -> str:
    return password_hash.hash(password)

# verify a password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)
```

# JWT Authentication

```bash
!pip install "python-jose[cryptography]"
!pip install pyjwt
```

Let's say we are going to an amusement park. We need a ticket to enter. The ticket is like a JWT token. It contains information about us (like our name, age, etc.) and is signed by the amusement park (the server). When we show our ticket at the entrance, the amusement park checks if the ticket is valid (not expired, not tampered with) and then allows us to enter.

Also it ensures that age is matched with a ride's age requirement. If the ticket is valid and the age is appropriate, we can enjoy the ride!

```python
import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
```

# Password request form

```python
from fastapi.security import OAuth2PasswordRequestForm

def login(user_credential: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_credential.username).first()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    if not verify_password(user_credential.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    return {
        "access_token": access_token, "token_type": "bearer"
        }
```

# Environment Variables

```python
from pydantic import BaseSettings

class settings(BaseSettings):
    database_hostname: str
    database_port: int
    database_password: str
    database_name: str
    database_username: str

```
