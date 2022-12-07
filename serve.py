from typing import Union
from src import printcolors as pc
from fastapi import FastAPI, Form, Request
from multiprocessing import Process
import time
import subprocess

from app import AlocomBotArmy

app = FastAPI()


def main():
    alocom_bot = AlocomBotArmy()

    @app.get("/")
    def read_root():
        return {"Hello": "World"}

    @app.post("/run")
    async def start_process(link: Request):
        pc.printout("ARMY is calling up ...!\n", pc.YELLOW)
        start_time = time.time()
        params = await link.json()
        link, guests = params.values()
        # alocom_bot = AlocomBotArmy()
        # process = alocom_bot(guests, link)
        process = Process(name="massooti", target=alocom_bot(guests, link),
                          args=(guests, link))
        # process.daemon = True
        # return {'pid': process.name, 'id': process.pid}
        return {'message':  'procees completed', "duration": f'{time.time() - start_time} sec'}

    @app.get('/kill')
    async def stop_process(pid=int):
        # subprocess.call(['pkill', 'chrome'])
        alocom_bot.quit()
        return {'message': 'process terminated'}


if __name__ == 'serve':
    main()
