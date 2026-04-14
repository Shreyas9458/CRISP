from fastapi import FastAPI
from DataModel.UserModel import UserModel
from Database.DatabaseOperations import Database

app = FastAPI()
db = Database("C:/Users/shrshinde/personalRepos/MicroservicesBasic/Database/curd.db")

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.post("/create")
async def create_user(user: UserModel):
    try:
        query = "INSERT INTO users (name, lastName, address) VALUES (?, ?, ?)"
        db.conn.execute(query, (user.name, user.last_name, user.address))
        db.conn.commit()
        return {"message": "User created successfully"}
    except Exception as e:
        return {"error": str(e)}
