from config import API_ID, API_HASH, BOT_TOKEN

from pyrogram import Client, filters
from pyrogram.types import Message
from telegraph import upload_file
import os

teletips=Client(
    "bot",
   api_id = 10651048,
    api_hash = "37775aca7d11f450ecde375baac17fe7",
    bot_token = "5475804553:AAEomjFZJy7_NECHqe67rdp0qUSr_enBgmw"
)

@teletips.on_message(filters.command('start') & filters.private)
async def start(client, message):
    text = f"""
Heya {message.from_user.mention},
Created and powered by @Apex_legends_AG
I am here to generate Telegraph links for your media files.

Simply send a valid media file directly to this chat.
Valid file types are 'jpeg', 'jpg', 'png', 'mp4' and 'gif'.

To generate links in **group chats**, add me to your supergroup and send the command <code>/tl</code> as a reply to a valid media file.

🏠 | [Home](https://t.me/Apex_legends_AG) 😎 | [Creator](https://agunivers7.github.io/) 
            """
    await teletips.send_message(message.chat.id, text, disable_web_page_preview=True)
    
        

@teletips.on_message(filters.media & filters.private)
async def get_link_private(client, message):
    try:
        text = await message.reply("Processing...")
        async def progress(current, total):
            await text.edit_text(f"📥 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐 𝚖𝚎𝚍𝚒𝚊 𝚒𝚗 𝙰𝚙𝚎𝚡... {current * 100 / total:.1f}%")
        try:
            location = f"./media/private/"
            local_path = await message.download(location, progress=progress)
            await text.edit_text("📤 𝚄𝚙𝚕𝚘𝚊𝚍𝚒𝚗𝚐 𝚝𝚘 𝙰𝚙𝚎𝚡 𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚙𝚑...")
            upload_path = upload_file(local_path) 
            await text.edit_text(f"**🌐 | Telegraph Link**:\n\n<code>https://telegra.ph{upload_path[0]}</code>")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"**❌ | File upload failed**\n\n<i>**Reason**: {e}</i>")
            os.remove(local_path) 
            return                 
    except Exception:
        pass        

@teletips.on_message(filters.command('tl'))
async def get_link_group(client, message):
    try:
        text = await message.reply("Processing...")
        async def progress(current, total):
            await text.edit_text(f"📥 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐 𝚖𝚎𝚍𝚒𝚊 𝚒𝚗 𝙰𝚙𝚎𝚡... {current * 100 / total:.1f}%")
        try:
            location = f"./media/group/"
            local_path = await message.reply_to_message.download(location, progress=progress)
            await text.edit_text("📤 𝚄𝚙𝚕𝚘𝚊𝚍𝚒𝚗𝚐 𝚝𝚘 𝙰𝚙𝚎𝚡 𝚃𝚎𝚕𝚎𝚐𝚛𝚊𝚙𝚑...")
            upload_path = upload_file(local_path) 
            await text.edit_text(f"**🌐 | Telegraph Link**:\n\n<code>https://telegra.ph{upload_path[0]}</code>")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"**❌ | File upload failed**\n\n<i>**Reason**: {e}</i>")
            os.remove(local_path) 
            return         
    except Exception:
        pass                                           

print("Bot is alive!")
teletips.run()

#Copyright ©️ 2022 TeLe TiPs. All Rights Reserved
