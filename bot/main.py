from pyrogram import Client

from misc.env import TgKeys

app = Client('my_account', api_id=TgKeys.API_ID, api_hash=TgKeys.API_HASH, plugins=dict(root="plugins"))


def start_bot() -> None:
    print("started")


app.run(start_bot())
