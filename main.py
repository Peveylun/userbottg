from time import sleep
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

import todo_db
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

app = Client('my_account', api_id=config['user']['api_id'], api_hash=config['user']['api_hash'])

db = todo_db.DB('database.db')


@app.on_message(filters.command('type', prefixes='.') & filters.me)
async def type(_, msg):
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
async def heart(_, msg):
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


@app.on_message(filters.command('add', prefixes='.') & filters.me)
async def add(_, msg):
    temp = ' '.join(msg.text.split(' ')[1:])
    db.create(temp)
    await msg.edit(f'Added to DB: {temp}')


@app.on_message(filters.command('get', prefixes='.') & filters.me)
async def get(_, msg):
    try:
        await msg.edit(db.get())
    except Exception as _:
        await msg.edit("Empty.")


@app.on_message(filters.command('delete', prefixes='.') & filters.me)
async def delete(_, msg):
    db.delete(' '.join(msg.text.split(' ')[1:]))


@app.on_message(filters.command('gch', prefixes='.') & filters.me)
async def get_chat(_, msg):
    users_id = []
    async for i in app.get_chat_members(msg.chat.id):
        users_id.append(i.user.id)
    print(await app.get_users(users_id))


def main():
    print("started")


app.run(main())
