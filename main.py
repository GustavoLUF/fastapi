from fastapi import FastAPI
import uvicorn

from contas.routers import contas_router


app = FastAPI()

@app.get("/")
def apresentacao():
    return "Olá, mundo! Eu sou o Gustavo."

app.include_router(contas_router.router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

