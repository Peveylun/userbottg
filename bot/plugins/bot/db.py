from pyrogram import Client, filters
from pyrogram.types import Message

from bot.misc.todo_db import DB


db = DB('database.db')


@Client.on_message(filters.command('add', prefixes='.') & filters.me)
async def add(_, msg: Message):
    temp = ' '.join(msg.text.split(' ')[1:])
    db.create(temp)
    await msg.edit(f'Added to DB: {temp}')


@Client.on_message(filters.command('get', prefixes='.') & filters.me)
async def get(_, msg: Message):
    try:
        await msg.edit(db.get())
    except Exception as _:
        await msg.edit("Empty.")


@Client.on_message(filters.command('delete', prefixes='.') & filters.me)
async def delete(_, msg: Message):
    db.delete(' '.join(msg.text.split(' ')[1:]))
