from pydantic import (
    BaseModel, 
    ValidationError, 
    EmailStr, 
    HttpUrl, 
    SecretStr, 
    ConfigDict,
    Field, 
    field_validator, 
    model_validator,
)
from datetime import datetime, UTC
from functools import partial
from typing import Literal, Annotated
from uuid import UUID ,uuid4

class User(BaseModel):
    # id: Annotated[int, Field(gt=100)]
    id: UUID= Field(default_factory=uuid4)
    name: Annotated[str, Field(min_length=3, max_length=20)]
    email: EmailStr
    age: int
    password: SecretStr
    website: HttpUrl | None = None
    status: str= 'single'
    is_active: bool= True
    fullname: str | None = 'N/A'

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: str) -> str:
        if not v.replace("_", "").isalnum():
            raise ValueError("Name must be alphanumeric")
        return v.lower()

    @field_validator("website", mode="before")
    @classmethod
    def add_http(cls, v: str)-> str | None:
        if v and not v.startswith(("http://", "https://")):
            return f"https://{v}"
        return v

# user1= User(
#     name='X',
#     email= 'abc@g.com',
#     status='complecated'
# )
# user1.name= 'change'
# print(user1.model_dump_json(indent=1))

user = User(
    name="Shojib_Hossain",
    email="CoreyMSchafer@gmail.com",
    age=39,
    password="secret123",
    website="www.youtube.com"
)
# print(user.model_dump_json(indent=2))

class Comment(BaseModel):
    content: str
    author_email: EmailStr
    likes: int = 0

class BlogPost(BaseModel):
    title: str
    content: str
    # author_id: str | int
    author: User
    view_count: int= 0
    is_published: bool= False

    tags: list[str]= Field(default_factory=list)
    
    created_at: datetime= Field(default_factory=lambda: datetime.now(tz=UTC))
    created_at_2: datetime= Field(default_factory=partial(datetime.now, tz= UTC))
    
    status: Literal["draft", "published", "archived"]= "draft"

    slug: Annotated[str, Field(pattern=r"^[a-z0-9-]+$")]
    comment: list[Comment]= Field(default_factory=list)



post_data = {
    "title": "Understanding Pydantic Models",
    "content": "Pydantic makes data validation easy and intuitive...",
    "slug": "understanding-pydantic",
    "author": {
        "name": "coreyms",
        "email": "CoreyMSchafer@gmail.com",
        "age": 39,
        "password": "secret123",
    },
    "comments": [
        {
            "content": "I think I understand nested models now!",
            "author_email": "student@example.com",
            "likes": 25,
        },
        {
            "content": "Can you cover FastAPI next?",
            "author_email": "viewer@example.com",
            "likes": 15,
        },
    ],
}

post = BlogPost(**post_data)

print(post.model_dump_json(indent=2))

# post = BlogPost(
#     title="Getting Started with Python",
#     content="Here's how to begin...",
#     author_id="12345",
# )

# print(post.model_dump_json(indent=1))

class UserRegistration(BaseModel):
    name: str
    password: SecretStr
    confirm_password: SecretStr

    @model_validator(mode='after')
    def password_match(self) -> UserRegistration:
        if self.password != self.confirm_password:
            raise ValueError("Password do not match")
        return self
    
try:
    registration= UserRegistration(
        name='shojib',
        password="1234",
        confirm_password="1234"
    )
    print(registration.model_dump_json(indent=2))
except ValidationError as e:
    print(e)

