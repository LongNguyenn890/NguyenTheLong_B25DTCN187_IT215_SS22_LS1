from fastapi import FastAPI

from database import Base, engine
from models.user_model import UserModel

Base.metadata.create_all(bind=engine)

app = FastAPI()