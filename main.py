import os
from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from starlette.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from controler.person import router as PersonRouter

app = FastAPI(root_path="/api", title="API de Personas", description="API para el manejo de personas", version="0.0.1")

app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*"])

app.include_router(PersonRouter, tags=["person"], prefix="/person")

app.mount("/public", StaticFiles(directory="public"), name="public")

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    file_name = "favicon.png"
    file_path = os.path.join(os.getcwd(), "public", file_name)
    return FileResponse(path=file_path, media_type="image/png")

@app.get("/", include_in_schema=False) 
def version():
  return {"v": "0.0.1"}