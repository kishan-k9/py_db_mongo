# from fastapi import FastAPI
# from routes.user import user
# app = FastAPI()
# app.include_router(user)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user import user

app = FastAPI()

# Include the user routes
app.include_router(user)

# Define the origins that are allowed to access the API (replace * with your frontend URL)
origins = [
    "http://localhost",
    "https://xsdq4k.csb.app/",  # Example frontend UR
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)



# run = uvicorn index:app --reload
