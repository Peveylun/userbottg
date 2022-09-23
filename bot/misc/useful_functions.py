from pyrogram.types import Message


def parse_text(msg: Message):
    return ' '.join(msg.text.split(' ')[1:])
