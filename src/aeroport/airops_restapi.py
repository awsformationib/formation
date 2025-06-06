# main.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from database import VolMySql
from vols import Vol

app = FastAPI()

db = VolMySql(host="localhost", login="root", password="", database="formation")

def make_dict(record):
    v1 = Vol("", "", None)
    clefs = v1.__dict__.keys()
    return { clef:record[i] for i, clef in enumerate(clefs) }


@app.get("/")
async def root():
    return {"greeting":"AirOps"}


@app.get("/vol/{numero}")
async def unvol(numero:str):
    try:
        data = db.lire_vol(numero)
        return make_dict(data)
    except:
        return JSONResponse(
            status_code=404,
            content={"message": "Vol non trouvé"}
        )

@app.get("/vols")
async def listedesvols():
    records = db.lire_vols()
    return [ make_dict(r) for r in records]

@app.post("/vol")
async def addvol(body):
    vol = Vol(**body)
    db.ecrire_vol(vol)
    #alternative utiliser "pydantic" pour transformer json en objet python
    return {"message": "Vol ajouté", "vol": vol.numero}
