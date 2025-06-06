# main.py
from fastapi import FastAPI


app = FastAPI()

db = VolMySql(host="localhost", login="root", password="", database="formation")

@app.get("/")
async def root():
 return {"greeting":"Hello world"}


@app.get("/vols")
async def listevols():
  vols = db.lire_vols()
  payload = [ v.__dict__ for v in vols if v]
  return payload

