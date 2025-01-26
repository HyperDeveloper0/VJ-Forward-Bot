import os
from config import Config

class  Script(object):
  START_TXT = """<b>ʜɪ {}
  
ɪ'ᴍ ᴀ ᴀᴅᴠᴀɴᴄᴇᴅ ꜰᴏʀᴡᴀʀᴅ ʙᴏᴛ
ɪ ᴄᴀɴ ꜰᴏʀᴡᴀʀᴅ ᴀʟʟ ᴍᴇssᴀɢᴇ ꜰʀᴏᴍ ᴏɴᴇ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴀɴᴏᴛʜᴇʀ ᴄʜᴀɴɴᴇʟ</b>

**ᴄʟɪᴄᴋ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ**"""
  HELP_TXT = """<b><u>🔆 Hᴇʟᴘ </b></u>

<u>**📚 Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:**</u>
<b>⏣ __/start - check I'm alive__ 
⏣ __/forward - forward messages__
⏣ __/settings - configure your settings__
⏣ __ /unequify - delete duplicate media messages in chats__
⏣ __ /stop - stop your ongoing tasks__
⏣ __ /reset - reset your settings__</b>

<b><u>💢 Fᴇᴀᴛᴜʀᴇs:</b></u>
<b>► __ꜰᴏʀᴡᴀʀᴅ ᴍᴇssᴀɢᴇ ꜰʀᴏᴍ ᴘᴜʙʟɪᴄ ᴄʜᴀᴧɴɴᴇʟ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜᴏᴜᴛ ᴀᴅᴍɪɴ ᴘᴇʀᴍɪssɪᴏɴ. ɪꜰ ᴛʜᴇ ᴄʜᴀᴧɴɴᴇʟ ɪs ᴘʀɪᴠᴀᴛᴇ, ɴᴇᴇᴅ ᴀᴅᴍɪɴ ᴘᴇʀᴍɪssɪᴏɴ. ɪꜰ ʏᴏᴜ ᴄᴀɴ'ᴛ ɢɪᴠᴇ ᴀᴅᴍɪɴ ᴘᴇʀᴍɪssɪᴏɴ, ᴛʜᴇɴ ᴜsᴇ ᴜsᴇʀʙᴏᴛ, ʙᴜᴛ ɪɴ ᴜsᴇʀʙᴏᴛ ᴛʜᴇʀᴇ ɪs ᴀ ᴄʜᴀɴᴄᴇ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ ʙᴀɴ ᴛʜᴇʀᴇғᴏʀᴇ ᴜsᴇ ꜰᴀᴋᴇ ᴀᴄᴄᴏᴜɴᴛ__
► __custom caption__
► __custom button__
► __skip duplicate messages__
► __filter type of messages__</b>
"""
  
  HOW_USE_TXT = """<b><u>⚠️ Before Forwarding:</b></u>
<b>► __add a bot or userbot__
► __add atleast one to channel__ `(your bot/userbot must be admin in there)`
► __You can add chats or bots by using /settings__
► __if the **From Channel** is private your userbot must be member in there or your bot must need admin permission in there also__
► __Then use /forward to forward messages__

► ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ [ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ](https://youtu.be/wO1FE-lf35I)</b>"""
  
  ABOUT_TXT = """<b>
╔════❰ ʀᴀᴘɪᴅ ꜰᴏʀᴡᴀʀᴅᴇʀ ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼📃 Nᴀᴍᴇ : [Rᴀᴘɪᴅ ꜰᴏʀᴡᴀʀᴅᴇʀ ⚡](https://t.me/RapidForwarderBot)
║┣⪼👨‍💻 Cʀᴇᴀᴛᴏʀ :[Mʀ. ʀᴇᴄᴏɴɪᴄ 👑](https://t.me/MrReconic)
║┣⪼🤖 Bᴇʟᴏɴɢs ꜰʀᴏᴍ: [Rᴇᴄᴏɴɪᴄ ʙᴏᴛs ](https://t.me/Reconic_Bots)
║┣⪼📡 Hᴏsᴛᴇᴅ ᴏɴ : Sᴜᴘᴇʀ Fᴀsᴛ
║┣⪼🗣️ Lᴀɴɢᴜᴀɢᴇ : Pʏᴛʜᴏɴ3
║┣⪼📚 Lɪʙʀᴀʀʏ : Pʏʀᴏɢʀᴀᴍ Gᴀᴛʜᴇʀ 2.11.0 
║┣⪼🗒️ Vᴇʀsɪᴏɴ : 0.18.3
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁۪۪
</b>"""
  STATUS_TXT = """
╔════❰ ʙᴏᴛ sᴛᴀᴛᴜs  ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼**⏳ Bᴏᴛ ᴜᴘᴛɪᴍᴇ:**`{}`
║┃
║┣⪼**👱 Tᴏᴛᴀʟ Usᴇʀs:** `{}`
║┃
║┣⪼**🤖 Tᴏᴛᴀʟ Bᴏᴛ:** `{}`
║┃
║┣⪼**🔃 Fᴏʀᴡᴀʀᴅɪɴɢs:** `{}`
║┃
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁۪۪
"""
  FROM_MSG = "<b>❪ SET SOURCE CHAT ❫\n\nForward the last message or last message link of source chat.\n/cancel - cancel this process</b>"
  TO_MSG = "<b>❪ CHOOSE TARGET CHAT ❫\n\nChoose your target chat from the given buttons.\n/cancel - Cancel this process</b>"
  SKIP_MSG = "<b>❪ SET MESSAGE SKIPING NUMBER ❫</b>\n\n<b>Skip the message as much as you enter the number and the rest of the message will be forwarded\nDefault Skip Number =</b> <code>0</code>\n<code>eg: You enter 0 = 0 message skiped\n You enter 5 = 5 message skiped</code>\n/cancel <b>- cancel this process</b>"
  CANCEL = "<b>Process Cancelled Succefully !</b>"
  BOT_DETAILS = "<b><u>📄 BOT DETAILS</b></u>\n\n<b>➣ NAME:</b> <code>{}</code>\n<b>➣ BOT ID:</b> <code>{}</code>\n<b>➣ USERNAME:</b> @{}"
  USER_DETAILS = "<b><u>📄 USERBOT DETAILS</b></u>\n\n<b>➣ NAME:</b> <code>{}</code>\n<b>➣ USER ID:</b> <code>{}</code>\n<b>➣ USERNAME:</b> @{}"  
         
  TEXT = """
╔════❰ ꜰᴏʀᴡᴀʀᴅ sᴛᴀᴛᴜs  ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼<b>🕵 Fᴇᴄʜᴇᴅ ᴍsɢ :</b> <code>{}</code>
║┃
║┣⪼<b>✅ Sᴜᴄᴄᴇꜰᴜʟʟʏ ꜰᴡᴅ :</b> <code>{}</code>
║┃
║┣⪼<b>👥 Dᴜᴘʟɪᴄᴀᴛᴇ ᴍsɢ :</b> <code>{}</code>
║┃
║┣⪼<b>🗑 Dʟᴇᴛᴇᴅ ᴍsɢ :</b> <code>{}</code>
║┃
║┣⪼<b>🪆 Sᴋɪᴘᴘᴇᴅ ᴍsɢ :</b> <code>{}</code>
║┃
║┣⪼<b>🔁 Fɪʟᴛᴇʀᴇᴅ ᴍsɢ :</b> <code>{}</code>
║┃
║┣⪼<b>📊 Cᴜʀʀᴇɴᴛ sᴛᴀᴛᴜs:</b> <code>{}</code>
║┃
║┣⪼<b>𖨠 Pᴇʀᴄᴇɴᴛᴀɢᴇ:</b> <code>{}</code> %
║╰━━━━━━━━━━━━━━━➣ 
╚════❰ {} ❱══❍⊱❁۪۪
"""
  DUPLICATE_TEXT = """
╔════❰ ᴜɴᴇǫᴜɪғʏ sᴛᴀᴛᴜs ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼ <b>ꜰᴇᴛᴄʜᴇᴅ ғɪʟᴇs:</b> <code>{}</code>
║┃
║┣⪼ <b>ᴅᴜᴘʟɪᴄᴀᴛᴇ ᴅᴇʟᴇᴛᴇᴅ:</b> <code>{}</code> 
║╰━━━━━━━━━━━━━━━➣
╚════❰ {} ❱══❍⊱❁۪۪
"""
  DOUBLE_CHECK = """<b><u>⚠️ Dᴏᴜʙʟᴇ Cʜᴇᴄᴋɪɴɢ ⚠️</b></u>
<code>ʙᴇꜰᴏʀᴇ ꜰᴏʀᴡᴀʀᴅɪɴɢ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇꜱ, ᴄʟɪᴄᴋ ᴛʜᴇ ʏᴇꜱ ʙᴜᴛᴛᴏɴ ᴏɴʟʏ ᴀꜰᴛᴇʀ ᴄʜᴇᴄᴋɪɴɢ ᴛʜᴇ ꜰᴏʟʟᴏᴡɪɴɢ</code>

<b>★ Yᴏᴜʀ ʙᴏᴛ:</b> [{botname}](t.me/{botuname})
<b>★ Fʀᴏᴍ ᴄʜᴀɴɴᴇʟ:</b> `{from_chat}`
<b>★ Tᴏ ᴄʜᴀɴɴᴇʟ:</b> `{to_chat}`
<b>★ Sᴋɪᴘ ᴍᴇssᴀɢᴇs:</b> `{skip}`

<i>° [{botname}](t.me/{botuname}) ᴍᴜꜱᴛ ʙᴇ ᴀᴅᴍɪɴ ɪɴ **TARGET CHAT**</i> (`{to_chat}`)
<i>° If the **SOURCE CHAT** ɪꜱ ᴘʀɪᴠᴀᴛᴇ, ʏᴏᴜʀ ᴜꜱᴇʀʙᴏᴛ ᴍᴜꜱᴛ ʙᴇ ᴀ ᴍᴇᴍʙᴇʀ ᴏʀ ʏᴏᴜʀ ʙᴏᴛ ᴍᴜꜱᴛ ʙᴇ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇʀᴇ ᴀʟꜱᴏ</b></i>

<b>ɪꜰ ᴛʜᴇ ᴀʙᴏᴠᴇ ɪꜱ ᴄʜᴇᴄᴋᴇᴅ, ᴛʜᴇɴ ᴛʜᴇ ʏᴇꜱ ʙᴜᴛᴛᴏɴ ᴄᴀɴ ʙᴇ ᴄʟɪᴄᴋᴇᴅ</b>"""
  
SETTINGS_TXT = """<b>ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ꜱᴇᴛᴛɪɴɢꜱ ᴀꜱ ʏᴏᴜʀ ᴡɪꜱʜ.</b>"""
