from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from ZeMusic import app

hmses = {}

@app.on_message(filters.reply & filters.regex("همسه") & filters.group)
async def reply_with_link(client, message):
    user_id = message.reply_to_message.from_user.id
    my_id = message.from_user.id
    bar_id = message.chat.id
    to_url = f"tg://openmessage?user_id={user_id}"
    start_link = f"https://t.me/{(await app.get_me()).username}?start=hms{my_id}to{user_id}in{bar_id}"
    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("اهمس هنا", url=start_link)]
        ]
    )
    await message.reply_text(f"⋆ تم تحديد الهمسه لـ ↞ <a href={to_url}>{(await app.get_chat(user_id)).first_name}</a>\n⋆ اضغط الزر لكتابة الهمسة\n-", reply_markup=reply_markup)

waiting_for_hms = {}

@app.on_message(filters.command("start"), group=473)
async def hms_start(client, message):
    global waiting_for_hms
    if message.text.split(" ", 1)[-1].startswith("hms"):
        hms_ids = message.text.split(" ", 1)[-1]
        waiting_for_hms[message.from_user.id] = hms_ids
        await message.reply_text("• اكتب همستك √")

@app.on_message(filters.private & filters.text & ~filters.command("start"), group=921)
async def send_hms(client, message):
    global waiting_for_hms
    if message.from_user.id in waiting_for_hms:
        hms_ids = waiting_for_hms[message.from_user.id]
        to_id = int(hms_ids.split("to")[-1].split("in")[0])
        from_id = int(hms_ids.split("hms")[-1].split("to")[0])
        in_id = int(hms_ids.split("in")[-1])
        to_url = f"tg://openmessage?user_id={to_id}"
        from_url = f"tg://openmessage?user_id={from_id}"

        hmses[str(to_id)] = {"hms": message.text, "bar": in_id}

        await message.reply_text("• تم ارسال همستك بنجاح √")

        await app.send_message(
            chat_id=in_id,
            text=f"⋆ الهمسه لـ ↞ <a href={to_url}>{(await app.get_chat(to_id)).first_name}</a>\n⋆ من ↞ <a href={from_url}>{(await app.get_chat(from_id)).first_name}</a>\n-",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("• اضغط لرؤية الهمسه.", callback_data="hms_answer")]])
        )

        del waiting_for_hms[message.from_user.id]

@app.on_callback_query(filters.regex("hms_answer"))
async def display_hms(client, callback):
    in_id = callback.message.chat.id
    who_id = callback.from_user.id

    if str(who_id) in hmses:
        if hmses[str(who_id)]["bar"] == in_id:
            await callback.answer(hmses[str(who_id)]["hms"], show_alert=True)
        else:
            await callback.answer("• الهمسه لا تخصك.", show_alert=True)
    else:
        await callback.answer("• لا توجد همسه لك.", show_alert=True)
