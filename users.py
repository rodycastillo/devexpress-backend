from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id=1, name="John", surname="Doe", url="https://www.google.com", age=25),
              User(id=2, name="Rail", surname="Doe",
                   url="https://www.google.com", age=25),
              User(id=3, name="Pepe", surname="Doe", url="https://www.google.com", age=25)]


@app.get('/usersjson')
async def usersjson():
    return [{"name": "John", "surname": "Doe", "url": "https://www.google.com", "age": 25},
            {"name": "Jane", "surname": "Doe", "url": "https://www.google.com", "age": 25}]


@app.get('/users')
async def users():
    return users_list


@app.get('/user/{id}')
async def userById(id: int):
    users = filter(lambda user: user.id == id, users_list)
    print(users, 'users')
    try:
        return list(users)[0]
    except:
        return {"message": "User not found"}
