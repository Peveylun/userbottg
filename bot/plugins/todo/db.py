from pyrogram import Client, filters
from pyrogram.types import Message

from bot.misc.todo_db import DB
from bot.misc.parsers import parse_text, parse_tasks

db = DB('database.db')


@Client.on_message(filters.command('add', prefixes='.') & filters.me)
async def add(_, msg: Message) -> None:
    temp = parse_text(msg)
    db.create(temp)
    await msg.edit(f'Додано: {temp}')


@Client.on_message(filters.command('get', prefixes='.') & filters.me)
async def get(_, msg: Message) -> None:
    tasks = parse_tasks(db.get())

    if tasks:
        await msg.edit(tasks)
    else:
        await msg.edit("Відсутні.")


@Client.on_message(filters.command('delete', prefixes='.') & filters.me)
async def delete(_, msg: Message) -> None:
    db.delete(id=parse_text(msg))
