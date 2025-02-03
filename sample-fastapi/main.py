import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

# In-memory "database"
fake_db = {}

SECRET_KEY = "mysecret"

def hash_password(password: str) -> str:
    pass

def verify_password(password: str, hashed_password: str) -> bool:
    pass

def create_jwt(email: str) -> str:
    pass

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"

@strawberry.type
class Mutation:
    @strawberry.mutation
    def signup(self, user_data: UserInput) -> User:
        pass

    @strawberry.mutation
    def login(self, user_data: UserInput) -> AuthResponse:
        pass

schema = strawberry.Schema(mutation=Mutation, query=Query)
app = FastAPI()
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

