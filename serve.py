from typing import Union
from src import printcolors as pc
from fastapi import FastAPI, Form, Request
from main4 import selenium
from multiprocessing import Process
import subprocess

from app import AlocomBotArmy


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/run")
async def start_process(link: Request):
    params = await link.json()
    link, guests = params.values()
    alocom_bot = AlocomBotArmy()
    # process = alocom_bot(guests, link)
    process = Process(name="massooti", target=alocom_bot(guests, link),
                      args=(guests, link))
    # process.daemon = True
    return {'pid': process.name, 'id': process.pid}
    process.start()
    process.join()


@app.get('/kill')
async def stop_process(pid=int):
    subprocess.call(['pkill', 'chrome'])
    return {'message': 'process terminated'}


if __name__ == 'serve.py':
    pc.printout("ARMY is calling up ...!\n", pc.YELLOW)
