from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


app = FastAPI(title="Fast API Blog",
    docs_url="/api-docs",
    version="0.0.1")

origins = ["http://localhost:3000",]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def main_response():
    return {
        'data': 'Hello World Alpha Mare'
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)