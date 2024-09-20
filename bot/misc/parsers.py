import string

from pyrogram.types import Message


def parse_text(msg: Message):
    return ' '.join(msg.text.split(' ')[1:])


def parse_tasks(tasks: list) -> string:
    tasks_string = ''
    for task in tasks:
        tasks_string += f"{task[0]} | {task[1]}"

    return tasks_string
