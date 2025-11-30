
from fastapi import FastAPI
from app.api.routes.user_routes import router as user_router
from app.api.routes.chat_routes import router as chat_router

app = FastAPI(
    title="LLM Agent CRUD API",
    description="A simple CRUD API for LLM Agent management",
    version="1.0.0"
)

app.include_router(user_router)
app.include_router(chat_router)

@app.get("/")
async def root():
    return {"message": "LLM Agent CRUD API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
