from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

# Define Person model
class Person(BaseModel):
    id: int
    name: str
    age: int
    email: str

# Sample person data stored as JSON string
person_data = '''
{
    "id": 1,
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com"
}
'''

@app.get("/person", response_model=Person)
async def get_person():
    # Parse JSON string to dictionary
    person_dict = json.loads(person_data)
    # Convert dictionary to Person model
    return Person(**person_dict)