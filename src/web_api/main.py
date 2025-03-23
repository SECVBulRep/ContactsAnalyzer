import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from web_api.routers.main_routes import router as main_router

app = FastAPI(title="Contact Analyzer Web API")

app.include_router(main_router, prefix="/llm", tags=["LLM"])

# Это точно отработает
@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)