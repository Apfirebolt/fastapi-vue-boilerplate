from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
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

app.mount("/client", StaticFiles(directory="client/dist"), name="static")

templates = Jinja2Templates(directory="client/dist")


@app.get('/api')
def main_response():
    return {
        'data': 'Hello World Alpha Mare'
    }


@app.get("/{full_path:path}")
async def serve_vue_app(request: Request, full_path: str):
    """Serve the vue app bootstrapped by Vite
    """
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)




    
