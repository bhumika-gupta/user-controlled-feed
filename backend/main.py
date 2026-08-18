from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
def get_health():
    return {"status": "healthy"}

@app.get("/feed")
def get_feed():
    feed_list = [
        {"id": 1, "creator": "randomcreator1", "topic": "technology", "content": "ai this ai that", "timestamp": "10:00 August 11 2026" },
        {"id": 2, "creator": "randomcreator2", "topic": "music", "content": "ep release coming to u this friday", "timestamp": "14:00 August 12 2026" },
        {"id": 3, "creator": "randomcreator3", "topic": "photography", "content": "sunset", "timestamp": "20:00 August 13 2026" }]

    return {
        "feed": feed_list
    }

