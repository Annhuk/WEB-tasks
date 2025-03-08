from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, EmailStr
from typing import List, Dict, Optional

app = FastAPI()

# -------------------- MODELS --------------------
class Comment(BaseModel):
    text: str

class Post(BaseModel):
    title: str
    content: str
    comments: List[Comment] = []

class User(BaseModel):
    name: str
    email: EmailStr
    posts: List[Post] = []

# -------------------- FAKE DATABASE --------------------
users_db: Dict[int, User] = {}  # {1: User(...)}
user_id_counter = 1

# -------------------- CRUD OPERATIONS --------------------

## CREATE USER
@app.post("/users/", response_model=User)
def create_user(user: User):
    global user_id_counter
    users_db[user_id_counter] = user
    user_id_counter += 1
    return user

## GET USERS WITH PAGINATION & SORTING
@app.get("/users/", response_model=List[User])
def get_users(limit: int = 10, offset: int = 0, sort_by: Optional[str] = None):
    users_list = list(users_db.values())

    if sort_by and sort_by in ["name", "email"]:
        users_list.sort(key=lambda x: getattr(x, sort_by))

    return users_list[offset: offset + limit]

## UPDATE USER
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_id] = user
    return user

## DELETE USER
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]
    return {"message": "User deleted successfully"}

# -------------------- NESTED ENTITIES (Posts & Comments) --------------------

## CREATE POST FOR USER
@app.post("/users/{user_id}/posts/", response_model=Post)
def create_post(user_id: int, post: Post):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    users_db[user_id].posts.append(post)
    return post

## GET POSTS OF A USER
@app.get("/users/{user_id}/posts/", response_model=List[Post])
def get_user_posts(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id].posts

## ADD COMMENT TO A POST
@app.post("/users/{user_id}/posts/{post_index}/comments/", response_model=Comment)
def add_comment(user_id: int, post_index: int, comment: Comment):
    if user_id not in users_db or post_index >= len(users_db[user_id].posts):
        raise HTTPException(status_code=404, detail="User or Post not found")
    users_db[user_id].posts[post_index].comments.append(comment)
    return comment
