from fastapi import FastAPI

app = FastAPI()

@app.get("/sinal")
def obter_sinal():
    return {"status": "LIBERADO"}
