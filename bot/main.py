from pyrogram import Client

from misc.env import TgKeys

plugins = dict(root="plugins",
               include=["fun.some_fun heart who type",
                        "todo.db add get delete"])

app = Client('my_account', api_id=TgKeys.API_ID, api_hash=TgKeys.API_HASH, plugins=plugins)


def start_bot() -> None:
    print("started")


app.run(start_bot())
