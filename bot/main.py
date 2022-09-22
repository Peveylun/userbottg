from time import sleep
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.raw.types import Message

from misc.env import TgKeys

app = Client('my_account', api_id=TgKeys.API_ID, api_hash=TgKeys.API_HASH, plugins=dict(root="plugins"))


@app.on_message(filters.command('type', prefixes='.') & filters.me)
async def type(_, msg: Message):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = ''
    typing_symbol = '▉'
    while tbp != orig_text:
        try:
            await msg.edit(tbp + typing_symbol)
            sleep(0.05)
            tbp += text[0]
            text = text[1:]
            await msg.edit(tbp)
            sleep(0.05)
        except FloodWait as e:
            print(e)


@app.on_message(filters.command('heart', prefixes='.') & filters.me)
async def heart(_, msg: Message):
    try:
        counter = 0
        hearts = ['❤❤❤', '🧡🧡🧡', '💛💛💛', '💚💚💚', '💙💙💙', '💜💜💜', '🖤🖤🖤', '🤍🤍🤍', '🤎🤎🤎']
        while counter != 5:
            for i in hearts:
                await msg.edit(i)
                sleep(1)
            counter += 1
    except FloodWait as e:
        print(e)


@app.on_message(filters.command('gch', prefixes='.') & filters.me)
async def get_chat(_, msg: Message):
    users_id = []
    async for i in app.get_chat_members(msg.chat.id):
        users_id.append(i.user.id)
    print(await app.get_users(users_id))


def start_bot() -> None:
    print("started")


app.run(start_bot())
