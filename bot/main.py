from pyrogram import Client, filters
from pyrogram.raw.types import Message

from misc.env import TgKeys

app = Client('my_account', api_id=TgKeys.API_ID, api_hash=TgKeys.API_HASH, plugins=dict(root="plugins"))


@app.on_message(filters.command('gch', prefixes='.') & filters.me)
async def get_chat(_, msg: Message):
    users_id = []
    async for i in app.get_chat_members(msg.chat.id):
        users_id.append(i.user.id)
    print(await app.get_users(users_id))


def start_bot() -> None:
    print("started")


app.run(start_bot())
