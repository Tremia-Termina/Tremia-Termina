from fastapi import FastAPI
import uvicorn
from main import game
app = FastAPI()

@app.get("/test")
def read_root():
    game()

if __name__ == "__main__":
    uvicorn.run(app = app, host = "0.0.0.0", port = 8080, workers = 1)