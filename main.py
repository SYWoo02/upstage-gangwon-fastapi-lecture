import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello FastAPI!"}

if __name__ == '__main__':
    print('Hi uv')
    uvicorn.run(app, host='0.0.0.0', port=8880)