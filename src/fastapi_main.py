from fastapi import FastAPI

from apps.customers.infraestructure.fastapi import endpoints


app = FastAPI()

app.include_router(endpoints.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}