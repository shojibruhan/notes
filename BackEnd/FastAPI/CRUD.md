# Create/ post

```python

@app.post("/users/")
def create_user(user: UserSchema, db: Session = Depends(get_db)):

    # db_user = User(
    #     name=user.name,
    #     age=user.age
    # )
    db_user= models.UserModel(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)  # get the generated id

    return db_user
```

# Read/ get

```python
@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):

    all_user = db.query(User).filter(User.id == user_id).all()

    single_user = db.query(User).filter(User.id == user_id).first()

    if single_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "user": single_user,
        "all_users": all_user
    }
```

# Update/ put

```python
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User, db: Session = Depends(get_db)):

    db_response = db.query(models.User).filter(models.User.id == user_id)
    user= db_response.first()

    if db_response is None:
        raise HTTPException(status_code=404, detail="User not found")


    user.model_dump(user)

    db.commit()
    db.refresh(db_user)
    return db_user
```

# Delete/ delete

```python
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}
```
