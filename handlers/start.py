from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)

async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>

🔥I am  Music Bot, that lets you play music in your Telegram groups voice chat.
🔥if you need any help ask here @patricia_support.


Use the buttons below to know more about me.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒ COMMANDS", url="https://telegra.ph/patricia-05-17"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔥Owner🔥", url="https://t.me/piroXpower"
                    ),
                    InlineKeyboardButton(
                        "⚜️Channel⚜️", url="https://t.me/patricia_updates"
                    ),
                    InlineKeyboardButton(
                        "⚡Support⚡", url="https://t.me/patricia_support" )
                ],
                [
                    InlineKeyboardButton(
                        "🔥ADD🔥", url="http://t.me/patriciaXmusic_bot?startgroup=true"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
